import math
import Arena
import random
import GlobalParameters as GP


def main():
    a = Arena.Arena()
    #a.create_random_arena()
    a.create_arena_from_file("arena2.txt")
    a.create_robots(a.numOfStatics, True)
    a.create_robots(a.numOfMoving, False)
    moveRobot(a)
    a.root.mainloop()


def moveRobot(arena):                           #MoveRobot Function - Update the current location of the robot in the matrix and the canvas (UI)
    while(arena.isMoving):
        for robot in arena.movingRob:
            direction = robot[0].move()
            if (direction == GP.moveRight):  # step right
                if (arena.matrix[robot[1] + 1][robot[2]] == 0 or arena.matrix[robot[1] + 1][robot[2]] == 1):
                    arena.matrix[robot[1]][robot[2]] = robot[0].color
                    robot[0].color = arena.matrix[robot[1] + 1][robot[2]]
                    arena.matrix[robot[1] + 1][robot[2]] = robot[0].id
                    robot[1] = robot[1] + 1
                    robot[0].X+=1
                    arena.canvas.move(robot[3], 1, 0)
                    arena.canvas.update()
            elif (direction == GP.moveLeft):  # step left
                if (arena.matrix[robot[1] - 1][robot[2]] == 0 or arena.matrix[robot[1] - 1][robot[2]] == 1):
                    arena.matrix[robot[1]][robot[2]] = robot[0].color
                    robot[0].color = arena.matrix[robot[1] - 1][robot[2]]
                    arena.matrix[robot[1] - 1][robot[2]] = robot[0].id
                    robot[1] = robot[1] - 1
                    robot[0].X -= 1
                    arena.canvas.move(robot[3], -1, 0)
                    arena.canvas.update()
            elif (direction == GP.moveUp):  # step up
                if (arena.matrix[robot[1]][robot[2] + 1] == 0 or arena.matrix[robot[1]][robot[2] + 1] == 1):
                    arena.matrix[robot[1]][robot[2]] = robot[0].color
                    robot[0].color = arena.matrix[robot[1]][robot[2] + 1]
                    arena.matrix[robot[1]][robot[2] + 1] = robot[0].id
                    robot[2] = robot[2] + 1
                    robot[0].Y -= 1
                    arena.canvas.move(robot[3], 0, 1)
                    arena.canvas.update()
            elif (direction == GP.moveDown):  # step down
                if (arena.matrix[robot[1]][robot[2] - 1] == 0 or arena.matrix[robot[1]][robot[2] - 1] == 1):
                    arena.matrix[robot[1]][robot[2]] = robot[0].color
                    robot[0].color = arena.matrix[robot[1]][robot[2] - 1]
                    arena.matrix[robot[1]][robot[2] - 1] = robot[0].id
                    robot[2] = robot[2] - 1
                    robot[0].Y += 1
                    arena.canvas.move(robot[3], 0, -1)
                    arena.canvas.update()

            if int(robot[0].Battery.bat) == GP.BatteryLow:
                arena.canvas.itemconfig(robot[3], fill="green")
            elif int(robot[0].Battery.bat) == GP.BatteryEmpty:
                arena.canvas.itemconfig(robot[3], fill="black")
                robot[0].isDead = True
            elif int(robot[0].Battery.bat) < GP.BatteryLow and robot[0].Battery.bat > GP.BatteryEmpty :
                arena.canvas.itemconfig(robot[3], fill="orange")

        sendMSG(arena)


def sendMSG(arena):                         #Set if the robot is get or send mesage.
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

def checkMessages(arena):               #Checking all the robot recived messages.
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
        if (len(sendRobots)!=0):
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
                if not(reciveRobot[0].isStatic):
                    reciveRobot[0].updateGuess()

def getDistance(reciveRobot,sendRobot):             #Checking the distance between the robots.
    r1 = reciveRobot[1]
    r2 = sendRobot[1]
    r3 = reciveRobot[2]
    r4 = sendRobot[2]
    dis = math.sqrt(math.pow(r1-r2,2)+ math.pow(r3-r4,2))
    return dis * GP.rand


if __name__ == "__main__":
    main()


