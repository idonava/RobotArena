import random
import Battery
import sys
from numpy import *
import GlobalParameters as GP


class Robot():


    def __init__(self, id, isStatic,color,X,Y, numOfRobots):
        self.id = id
        self.numOfRobots = numOfRobots                          #number of all the robots in the arena- need to know in order to recieve messages from them
        self.isStatic = isStatic
        self.X = X
        self.Y = Y
        self.color = color                                      #the color that the robot is currently on- wight\gray
        self.isDead = False                                     #did the robot ran out of battery?
        self.Battery = Battery.Battery()
        self.sendMessage = False                                #indicates if the robot is sending\getting a message in the current iteration
        self.message = [self.id, self.isStatic, self.color, self.X, self.Y]
        self.allMessages = [None]*(self.numOfRobots+3)
        self.indexOfNeighbors=[]                                #help list- in order not to look for the entire allMessage list- we look only for the index we got message from
        self.guess = GP.initialGuess                            #init guess
        self.MovingType = self.rationalMoving()                 #True if the robot have rational moving.
        self.closeRobot = -1
        self.isWhite= False
        self.lastStep=5
        self.direction = -1

    def rationalMoving(self):
        rand = int(random.random()*100)+1
        if (rand<=GP.percentOfRationalRobots):
            return True
        else:
            return False
    def send_message(self):                                     #this message activates the senMessage flag
        if not(self.isDead):                                    #make sure the robot has battery before he can send a message
            self.message = [self.id, self.isStatic, self.color, self.X, self.Y]
            if(self.isStatic):
                self.sendMessage = True
            elif(len(self.indexOfNeighbors)>3):                 # only if a moving robot already knows its location- it sends it to its neighbors
                self.sendMessage = True

    def get_message(self):                                      # this message disables the senMessage flag
        self.sendMessage = False

    def move(self):                                             #move method- return int- that represent the direction the robot is moving
        if not (self.isDead):
            self.update_bat()
            if(self.color == 0):                                #random move in the arena
                self.direction = -1
                self.isWhite=True
                if (self.MovingType):
                    self.lastStep=self.doRationalMove()
                    return self.lastStep
                else:
                    self.lastStep=int(random.random()*4)
                    return self.lastStep
            else:                                               # low battery, search for neighbors in the light and move towards them
                if(self.isWhite):
                    return self.outOfGray()
                else:
                    self.lastStep = self.doRationalMove()
                    return self.lastStep
    def outOfGray(self):
        if(self.lastStep==0):
            return 1
        elif(self.lastStep == 1):
            return 0
        elif (self.lastStep == 2):
            return 3
        elif (self.lastStep == 3):
            return 2
    def doRationalMove(self):                                   # Moving to the closet neighbor are in white area.
        minIndex = -1
        minDist = sys.maxsize
        for index in self.indexOfNeighbors:
            msg = self.allMessages[index]
            if (msg[0][2] == 0 and msg[1] < minDist):
                minDist = msg[1]
                minIndex = index

        if (minIndex == -1 ):                                    # if there are no neighbors in the light- move random
            rand = int(random.random() * 4)
            if(self.direction == -1):
                self.direction = rand
                return rand
            else:
                return self.direction

        else:
            neighbor = self.allMessages[minIndex]
            Xdiff = self.X - neighbor[0][3]
            Ydiff = self.Y - neighbor[0][4]
            self.closeRobot = neighbor
            if (Xdiff < 0):
                return 0
            elif (Xdiff > 0):
                return 1
            elif (Ydiff < 0):
                return 2
            elif (Ydiff > 0):
                    return 3

    def update_bat(self):                                       #update current battery state- activates every time the robot is moving\sends a message
        if(self.color==0):
            self.Battery.charge()
        else:
            self.Battery.unCharge()

    def updateGuess(self):                                      #this method updates the current guess of the robot's location
        self.radius = GP.radius
        self.guess =[self.X,self.Y]
        while (self.radius > 1):
            testGuess = self.generateGuess()                    #generate 4 new guesses around the current guess
            error = []
            for Gus in testGuess:
                error.append(self.RMS(Gus))
            i = error.index(min(error))                         #check which error is the lowest (==better)
            self.guess = testGuess[i]                           #update the current guess to be the best of this iteration
            self.X = abs(self.guess[0])
            self.Y = abs(self.guess[1])
            self.radius = self.radius / 2

    def RMS(self, guess):                                       #RMS algorithem
        E=[]
        for index in self.indexOfNeighbors:
            msg = self.allMessages[index]
            newDist = self.dist(msg[0][3], msg[0][4], guess[0], guess[1])
            realDist = msg[1]
            newDist = math.pow((newDist-realDist),2)
            E.append(newDist)
        return math.sqrt(sum(E)/len(E))

    def dist(self, x1, y1, x2, y2):                             #oklidi distance method
        return math.sqrt(math.pow(x1-x2,2)+ math.pow(y1-y2,2))

    def generateGuess(self):                                    #genarate 4 guesses around the current guess
        x = self.guess[0]
        y = self.guess[1]
        return [self.guess, [x + self.radius, y], [x, y + self.radius],
                [x - self.radius, y], [x, y - self.radius]]

