import random
import threading
import time
import Battery

class Robot(threading.Thread):

    def __init__(self, id, isStatic,color,X,Y):
        threading.Thread.__init__(self)
        self.id = id
        self.isStatic = isStatic
        self.X=X
        self.Y=Y
        self.color=color
        self.Battery=Battery.Battery()

    def run(self):
        while(True):
            self.move()
            self.update_bat()
            time.sleep(1)

    def move(self):
        if(self.Battery.bat>0):
            return int(random.random()*4)

    def update_bat(self):
        if(self.color==0):
            self.Battery.charge()
        else:
            self.Battery.unCharge()





