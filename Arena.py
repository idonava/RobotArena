import random
import Robot
import matplotlib.pyplot as plt
import copy
import Tkinter as tk
import time


import numpy as np

class Arena:

    ''' white=0, gray=1, black=2'''

    def __init__(self):
        global white, gray, black
        self.numOfRobots=0
        self.id = id
        self.X = 1000
        self.Y = 1000
        self.matrix=[[0 for x in range(self.X)]for y in range(self.Y)]
        self.movingRob = []
        self.staticRob = []
        self.numOfStatics = 10
        self.numOfMoving=50
        self.matrixWithoutRobots=[]
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=1000, height=1000)
        self.canvas.pack()

    def create_arena_from_file(self,fileName):
        i=0
        with open (fileName,'r') as f:
            lines=f.readlines()
        self.X=int(lines[i].split('=',1)[1])
        i=i+1
        self.Y = int(lines[i].split('=', 1)[1])
        i=i+1
        self.create_boundaries()
        numOfBlack = int(lines[i].split(':', 1)[1])
        i=i+1
        rectangleList=[]
        for x in range(numOfBlack):
            list1=lines[i].split('->')
            i=i+1
            for num in list1:
                list2=num.split(',')
                rectangleList.append(int(list2[0]))
                rectangleList.append(int(list2[1]))
            for x in range(rectangleList[0],rectangleList[2]+1):
                for y in range(rectangleList[1],rectangleList[3]+1):
                    self.matrix[x][y] = 2
            rectangleList = []
        numOfGray = int(lines[i].split(':', 1)[1])
        i = i + 1
        rectangleList = []
        for x in range(numOfGray):
            list1 = lines[i].split('->')
            i = i + 1
            for num in list1:
                list2 = num.split(',')
                rectangleList.append(int(list2[0]))
                rectangleList.append(int(list2[1]))
            for x in range(rectangleList[0], rectangleList[2]+1):
                for y in range(rectangleList[1], rectangleList[3]+1):
                    self.matrix[x][y] = 1
            rectangleList = []
        self.numOfStatics = int(lines[i].split('=',1)[1])
        i=i+1
        self.numOfMoving = int(lines[i].split('=',1)[1])
        self.matrixWithoutRobots=copy.deepcopy(self.matrix)


    def create_boundaries(self):
        self.matrix = [[0 for x in range(self.X)] for y in range(self.Y)]
        for x in range(self.X):
            self.matrix[x][self.Y - 1] = 2
            self.matrix[x][0] = 2
        for y in range(self.Y):
            self.matrix[self.X - 1][y] = 2
            self.matrix[0][y] = 2
        self.canvas.create_rectangle(0,0,1000,1, fill='black')
        self.canvas.create_rectangle(0,0,1,1000, fill='black')


    def create_random_arena(self):
        self.create_boundaries()
        #create gray areas:
        for x in range(3):
            rand1 = (random.random() * (self.X - 1)) + 1
            rand2 = (random.random() * (self.X - 1)) + 1
            rand3 = (random.random() * (self.Y - 1)) + 1
            rand4 = (random.random() * (self.Y - 1)) + 1

            self.canvas.create_rectangle(int(min(rand1, rand2)), int(min(rand3, rand4)), int(max(rand1, rand2)),int(max(rand3, rand4)),fill='gray')
            for x in range(int(min(rand1, rand2)), int(max(rand1, rand2))):
                for y in range(int(min(rand3, rand4)), int(max(rand3, rand4))):
                    self.matrix[x][y] = 1


        # create black areas:
        for x in range(1):
            rand1 = (random.random() * (self.X - 1)) + 1
            rand2 = (random.random() * (self.X - 1)) + 1
            rand3 = (random.random() * (self.Y - 1)) + 1
            rand4 = (random.random() * (self.Y - 1)) + 1

            self.canvas.create_rectangle(int(min(rand1, rand2)), int(min(rand3, rand4)), int(max(rand1, rand2)),int(max(rand3, rand4)),fill='gray')
            for x in range(int(min(rand1, rand2)),int(max(rand1, rand2))):
                for y in range(int(min(rand3, rand4)), int(max(rand3, rand4))):
                    self.matrix[x][y] = 2
        self.matrixWithoutRobots=copy.deepcopy(self.matrix)

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
                r = Robot.Robot(self.numOfRobots+2,isStatic,self.matrix[randX][randY],randX,randY)
                self.staticRob.append([r,randX,randY])
            else:
                r = Robot.Robot(self.numOfRobots+2, isStatic, self.matrix[randX][randY], 0, 0)
                self.movingRob.append([r,randX,randY])
            self.matrix[randX][randY] = r.id

    def getColor(self,x,y):
        n= self.matrixWithoutRobots[x][y]
        print(n)
        if n==0:
            return 'white'
        else:
            return 'gray'

    def gui(self):
        Matrix = [[0 for x in range(self.X)] for y in range(self.Y)]

        fig, ax = plt.subplots(figsize=(10, 10))
        for rob in self.staticRob:
            plt.plot(rob[1], rob[2], color='green', linestyle='dashed', marker='o',
                     markerfacecolor='red', markersize=12)
        for rob in self.movingRob:
            plt.plot(rob[1], rob[2], color='green', linestyle='dashed', marker='o',
                     markerfacecolor='green', markersize=12)
       # ax.imshow(Matrix, cmap='RdGy', interpolation='nearest')
       # plt.plot(1, 2, 'o','g')

        ax.imshow(self.matrix, cmap='RdGy', interpolation='nearest')
        plt.show()

        # canvas.create_rectangle(x0, y0, x1, y1, option, ... )
        # x0, y0, x1, y1 are corner coordinates of ulc to lrc diagonal
        for rob in self.staticRob:
            self.canvas.create_rectangle(rob[1], rob[2],rob[1]+10,rob[2]+10, outline='white', fill='red')
        for rob in self.movingRob:
            self.canvas.create_rectangle(rob[1],rob[2],rob[1]+10, rob[2]+10, outline='white', fill='green')
        for x in range(50):
            y = x = 5
            time.sleep(0.025)
            #canvas.move(rc1, x, -y)
            #canvas.move(rc2, x, y)
            self.canvas.update()
        self.root.mainloop()
