import random
import time
import Battery
import Guess

class Robot():

    def __init__(self, id, isStatic,color,X,Y):
        self.id = id
        self.isStatic = isStatic
        self.X = X
        self.Y = Y
        self.color = color
        self.Battery = Battery.Battery()
        self.sendMessage = False
        self.message = [self.id, self.isStatic, self.color, self.X, self.Y]
        self.allMessages = []
        self.guess = Guess.Guess(self.allMessages)


    def send_message(self):
        self.sendMessage = True

    def get_message(self):
        self.sendMessage = False

        if(len(self.allMessages)>0):
            self.guess = Guess.Guess(self.allMessages)
            self.guess.guessTest()

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





