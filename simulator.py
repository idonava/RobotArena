import time
import math
import Arena
import random

def main():
    a = Arena.Arena()
    #a.create_random_arena()
    a.create_arena_from_file("arena1.txt")
    a.create_robots(a.numOfStatics, True)
    a.create_robots(a.numOfMoving, False)
    moveRobot(a)
    a.root.mainloop()


def moveRobot(arena):
    while(True):
        for robot in arena.movingRob:
            direction = robot[0].move()
            if (direction == 0):  # step right
                if (arena.matrix[robot[1] + 1][robot[2]] == 0 or arena.matrix[robot[1] + 1][robot[2]] == 1):
                    arena.matrix[robot[1]][robot[2]] = robot[0].color
                    arena.matrix[robot[1] + 1][robot[2]] = robot[0].id
                    robot[1] = robot[1] + 1
                    robot[0].X+=1
                    arena.canvas.move(robot[3], 1, 0)
                    arena.canvas.update()
            if (direction == 1):  # step left
                if (arena.matrix[robot[1] - 1][robot[2]] == 0 or arena.matrix[robot[1] - 1][robot[2]] == 1):
                    arena.matrix[robot[1]][robot[2]] = robot[0].color
                    arena.matrix[robot[1] - 1][robot[2]] = robot[0].id
                    robot[1] = robot[1] - 1
                    robot[0].X -= 1
                    arena.canvas.move(robot[3], -1, 0)
                    arena.canvas.update()
            if (direction == 2):  # step up
                if (arena.matrix[robot[1]][robot[2] + 1] == 0 or arena.matrix[robot[1]][robot[2] + 1] == 1):
                    arena.matrix[robot[1]][robot[2]] = robot[0].color
                    arena.matrix[robot[1]][robot[2] + 1] = robot[0].id
                    robot[2] = robot[2] + 1
                    robot[0].Y += 1
                    arena.canvas.move(robot[3], 0, 1)
                    arena.canvas.update()
            if (direction == 3):  # step down
                if (arena.matrix[robot[1]][robot[2] - 1] == 0 or arena.matrix[robot[1]][robot[2] - 1] == 1):
                    arena.matrix[robot[1]][robot[2]] = robot[0].color
                    arena.matrix[robot[1]][robot[2] - 1] = robot[0].id
                    robot[2] = robot[2] - 1
                    robot[0].Y -= 1
                    arena.canvas.move(robot[3], 0, -1)
                    arena.canvas.update()
        changeSend(arena)
        time.sleep(0.01)
        print(arena.movingRob[0][0].allMessages)
def changeSend(arena):
        #Need to add sleep time to robots
        for rob in arena.staticRob:
            rand =int(random.random()*2)
            if (rand ==0):
                rob[0].sendMessage=False
            else:
                rob[0].sendMessage = True
        for rob in arena.movingRob:
            rand =int(random.random()*2)
            if (rand ==0):
                rob[0].sendMessage=False
            else:
                rob[0].sendMessage = True
        checkMessages(arena)

def checkMessages(arena):
    sendRobots = []
    reciveRobots = []
    for rob in arena.staticRob:
        if rob[0].sendMessage:
            sendRobots.append(rob)
        else:
            reciveRobots.append(rob)

    for rob in arena.movingRob:
        if rob[0].sendMessage:
            sendRobots.append(rob)
        else:
            reciveRobots.append(rob)

    for reciveRobot in reciveRobots:
        minRobot = sendRobots[0]
        minDis = getDistance(reciveRobot[0],minRobot[0])
        for sendRobot in sendRobots:
            dis = getDistance(reciveRobot[0],sendRobot[0])
            if dis<minDis:
                minRobot=sendRobot
                minDis = dis
        if (dis<500):
            reciveRobot[0].allMessages.append([minRobot[0].message,dis])

def getDistance(reciveRobot,sendRobot):
    return math.sqrt(math.pow(reciveRobot.X-sendRobot.X,2)+ math.pow(reciveRobot.Y-sendRobot.Y,2))

if __name__ == "__main__":
    main()


