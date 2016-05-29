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
    while(arena.isMoving):
        for robot in arena.movingRob:
            direction = robot[0].move()
            if (direction == 0):  # step right
                if (arena.matrix[robot[1] + 1][robot[2]] == 0 or arena.matrix[robot[1] + 1][robot[2]] == 1):
                    arena.matrix[robot[1]][robot[2]] = robot[0].color
                    robot[0].color = arena.matrix[robot[1] + 1][robot[2]]
                    arena.matrix[robot[1] + 1][robot[2]] = robot[0].id
                    robot[1] = robot[1] + 1
                    robot[0].X+=1
                    arena.canvas.move(robot[3], 1, 0)
                    arena.canvas.update()
            elif (direction == 1):  # step left
                if (arena.matrix[robot[1] - 1][robot[2]] == 0 or arena.matrix[robot[1] - 1][robot[2]] == 1):
                    arena.matrix[robot[1]][robot[2]] = robot[0].color
                    robot[0].color = arena.matrix[robot[1] - 1][robot[2]]
                    arena.matrix[robot[1] - 1][robot[2]] = robot[0].id
                    robot[1] = robot[1] - 1
                    robot[0].X -= 1
                    arena.canvas.move(robot[3], -1, 0)
                    arena.canvas.update()
            elif (direction == 2):  # step up
                if (arena.matrix[robot[1]][robot[2] + 1] == 0 or arena.matrix[robot[1]][robot[2] + 1] == 1):
                    arena.matrix[robot[1]][robot[2]] = robot[0].color
                    robot[0].color = arena.matrix[robot[1]][robot[2] + 1]
                    arena.matrix[robot[1]][robot[2] + 1] = robot[0].id
                    robot[2] = robot[2] + 1
                    robot[0].Y += 1
                    arena.canvas.move(robot[3], 0, 1)
                    arena.canvas.update()
            elif (direction == 3):  # step down
                if (arena.matrix[robot[1]][robot[2] - 1] == 0 or arena.matrix[robot[1]][robot[2] - 1] == 1):
                    arena.matrix[robot[1]][robot[2]] = robot[0].color
                    robot[0].color = arena.matrix[robot[1]][robot[2] - 1]
                    arena.matrix[robot[1]][robot[2] - 1] = robot[0].id
                    robot[2] = robot[2] - 1
                    robot[0].Y -= 1
                    arena.canvas.move(robot[3], 0, -1)
                    arena.canvas.update()


            if int(robot[0].Battery.bat) == 20:
                arena.canvas.itemconfig(robot[3], fill="green")
            elif int(robot[0].Battery.bat) == 0:
                arena.canvas.itemconfig(robot[3], fill="black")
                robot[0].isDead = True
            elif int(robot[0].Battery.bat) < 20 and robot[0].Battery.bat > 0 :
                arena.canvas.itemconfig(robot[3], fill="orange")

        changeSend(arena)
        print(arena.movingRob[0][1],arena.movingRob[0][2])
        print(arena.movingRob[0][0].guess)
        for index in arena.movingRob[0][0].indexOfNeighbors:
            print(arena.movingRob[0][0].allMessages[index])


def changeSend(arena):
        #Need to add sleep time to robots
        for rob in arena.staticRob:
            rand =int(random.random()*2)
            if (rand ==0):
                rob[0].get_message()
            else:
                rob[0].send_message()
        for rob in arena.movingRob:
            rand =int(random.random()*2)
            if (rand ==0):
                rob[0].get_message()
            else:
                rob[0].send_message()
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
        minDis = getDistance(reciveRobot,minRobot)
        for sendRobot in sendRobots:
            dis = getDistance(reciveRobot,sendRobot)
            if dis<minDis:
                minRobot=sendRobot
                minDis = dis
        if (minDis<500):
            reciveRobot[0].allMessages[minRobot[0].id]=([minRobot[0].message,minDis])
            if(minRobot[0].id not in reciveRobot[0].indexOfNeighbors):
                reciveRobot[0].indexOfNeighbors.append(minRobot[0].id)
            reciveRobot[0].makeGuess()

def getDistance(reciveRobot,sendRobot):
    r1 = reciveRobot[1]
    r2 = sendRobot[1]
    r3 = reciveRobot[2]
    r4 = sendRobot[2]
    dis = math.sqrt(math.pow(r1-r2,2)+ math.pow(r3-r4,2))
    rand = random.uniform(0.8,1.2)
    return dis

if __name__ == "__main__":
    main()


