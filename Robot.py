import random
import threading
import time

class Robot(threading.Thread):

    def __init__(self, id, isStatic,color,X,Y):
        threading.Thread.__init__(self)
        self.id = id
        self.isStatic = isStatic
        self.X=X
        self.Y=Y
        self.color=color

    def run(self):
        while(True):
            self.move()
            time.sleep(0.1)

    def move(self):
            return int(random.random()*4)
            if (direction==0):    #step right
                self.X=self.X+1
            if (direction == 1):  # step left
                self.X = self.X - 1
            if (direction == 2):  # step up
                self.Y = self.Y + 1
            if (direction == 3):  # step down
                self.Y = self.Y - 1






