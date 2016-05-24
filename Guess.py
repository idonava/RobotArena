import math

class Guess:
    def __init__(self, allMSG):
        self.allMessage=allMSG
        self.guess=[500,500]
        self.radius=100

    def guessTest(self):
        while(self.radius>1):
            testGuess=self.generateGuess()
            #print(testGuess)
            error=[]
            for Gus in testGuess:
                error.append(self.create_table(Gus))
           # print(error)
            i = error.index(min(error))
            self.guess=testGuess[i]
            self.radius=self.radius/2

    def generateGuess(self):
        x=self.guess[0]
        y=self.guess[1]
        return [self.guess,[x+self.radius,y+self.radius],[x-self.radius,y+self.radius],
                [x+self.radius,y-self.radius],[x-self.radius,y-self.radius]]

    def create_table(self, guess):
        self.table=[]
        for msg in self.allMessage:
            #create table with columns: msg, dist, guessDist, dist-guessDist
            if(msg[1]==True):
                self.table.append([msg[0],msg[1],self.dist(msg[0][3],msg[0][4],guess[0],guess[1])])
        return self.ERR()

    def ERR(self):
        if(len(self.table)>0):
            E=[]
            for x in self.table:
                E.append(x[1] - x[2])
            return math.sqrt((sum(E)*sum(E)/len(E)))

    def dist(self, x1,y1,x2,y2):
        return math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))