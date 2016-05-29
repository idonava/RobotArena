import random
import Battery
import sys
from numpy import *


class Robot():

    def __init__(self, id, isStatic,color,X,Y, numOfRobots):
        self.id = id
        self.numOfRobots = numOfRobots
        self.isStatic = isStatic
        self.X = X
        self.Y = Y
        self.color = color
        self.isDead = False
        self.Battery = Battery.Battery()
        self.sendMessage = False
        self.message = [self.id, self.isStatic, self.color, self.X, self.Y]
        self.allMessages = [None]*(self.numOfRobots+3)
        self.indexOfNeighbors=[]
        self.guess = [500,500]

    def send_message(self):
        if not(self.isDead):
            self.message = [self.id, self.isStatic, self.color, self.X, self.Y]
            if(self.isStatic):
                self.sendMessage = True
            elif(len(self.indexOfNeighbors)>3): # only if a moving robot already knows its location- it sends it to its neighbors
                self.sendMessage = True

    def get_message(self):
        self.sendMessage = False

    def makeGuess(self):
        self.guessTest()

    def move(self):
        if not (self.isDead):
            self.update_bat()
            if(self.Battery.bat>50 or self.color == 0): #randome move in the arena
                return int(random.random()*4)
            elif(self.color!=0): # low battery, search for neighbors in the light and move towards them
                minIndex = -1
                minDist = sys.maxsize
                for index in self.indexOfNeighbors:
                    msg = self.allMessages[index]
                    if (msg[0][2]==0 and msg[1]<minDist):
                        minDist = msg[1]
                        minIndex = index
                if(minIndex == -1): # if there are no neighbors in the light
                    return int(random.random() * 4)
                else:
                    neighbor= self.allMessages[minIndex]
                    Xdiff=self.X-neighbor[0][3]
                    Ydiff=self.Y-neighbor[0][4]
                    if abs(Xdiff)>abs(Ydiff):
                        if (Xdiff < 0):
                            return 0
                        elif (Xdiff > 0):
                            return 1
                    else:
                        if (Ydiff < 0):
                            return 2
                        elif (Ydiff > 0):
                            return 3

    def update_bat(self):
        if(self.color==0):
            self.Battery.charge()
        else:
            self.Battery.unCharge()

    def guessTest(self):
        self.radius = 500
        while (self.radius > 1):
            testGuess = self.generateGuess()
            error = []
            for Gus in testGuess:
                error.append(self.create_table(Gus))
            i = error.index(min(error))
            self.guess = testGuess[i]
            self.X = self.guess[0]
            self.Y = self.guess[1]
            self.radius = self.radius / 2

    def create_table(self, guess):
        E=[]
        for index in self.indexOfNeighbors:
            msg = self.allMessages[index]
            newDist = self.dist(msg[0][3], msg[0][4], guess[0], guess[1])
            realDist = msg[1]
            newDist = math.pow((newDist-realDist),2)
            E.append(newDist)
        return math.sqrt(sum(E)/len(E))

    def dist(self, x1, y1, x2, y2):
        return math.sqrt(math.pow(x1-x2,2)+ math.pow(y1-y2,2))

    def generateGuess(self):
        x = self.guess[0]
        y = self.guess[1]
        return [self.guess, [x + self.radius, y], [x, y + self.radius],
                [x - self.radius, y], [x, y - self.radius]]

