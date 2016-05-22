import random
import Robot

class Arena:

    ''' white=0, gray=1, black=2'''

    def __init__(self):
        global white, gray, black
        self.numOfRobots=0
        self.id = id
        self.X = 30
        self.Y = 30
        self.matrix=[[0 for x in range(self.X)]for y in range(self.Y)]
        self.movingRob = [[]]
        self.staticRob = [[]]

    def create_arena(self):
        global white, gray, black
        #create the boundaries of the :
        for x in range (self.X):
            self.matrix[x][self.Y-1]=2
            self.matrix[x][0]=2
        for y in range(self.Y):
            self.matrix[self.X-1][y] = 2
            self.matrix[0][y] = 2
        #create gray areas:
        for x in range(3):
            rand1 = (random.random() * (self.X - 1)) + 1
            rand2 = (random.random() * (self.X - 1)) + 1
            rand3 = (random.random() * (self.Y - 1)) + 1
            rand4 = (random.random() * (self.Y - 1)) + 1

            for x in range(int(min(rand1, rand2)), int(max(rand1, rand2))):
                for y in range(int(min(rand3, rand4)), int(max(rand3, rand4))):
                    self.matrix[x][y]=1

        # create black areas:
        for x in range(1):
            rand1 = (random.random() * (self.X - 1)) + 1
            rand2 = (random.random() * (self.X - 1)) + 1
            rand3 = (random.random() * (self.Y - 1)) + 1
            rand4 = (random.random() * (self.Y - 1)) + 1

            for x in range(int(min(rand1, rand2)),int(max(rand1, rand2))):
                for y in range(int(min(rand3, rand4)), int(max(rand3, rand4))):
                    self.matrix[x][y] = 2


    def print_arena(self):
        for x in range(self.X):
            print (self.matrix[x])

    def create_robots(self,num,isStatic):
        for x in range(num):
            self.numOfRobots=self.numOfRobots+1
            randX=0
            randY=0
            while(self.matrix[randX][randY]==2): #make sure we wont put any robot on a black spot
                randX = int((random.random() * (self.X - 1)) + 1)
                randY = int((random.random() * (self.Y - 1)) + 1)
            if(isStatic):
                r = Robot.Robot(self.numOfRobots+3,isStatic,self.matrix[randX][randY],randX,randY)
                self.staticRob.append([r,randX,randY])
            else:
                r = Robot.Robot(self.numOfRobots+3, isStatic, self.matrix[randX][randY], 0, 0)
                self.movingRob.append([r,randX,randY])
            self.matrix[randX][randY] = r.id

