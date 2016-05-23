import time

import Arena

def main():
    a = Arena.Arena()
    #a.create_random_arena()
    a.create_arena_from_file("arena1.txt")
    a.create_robots(a.numOfStatics, True)
    a.create_robots(a.numOfMoving, False)
    moveRobot(a)
    rect=a.canvas.create_rectangle(500, 500, 500 + 10, 500 + 10, fill='blue')

    #OMG!! we can move a single robot!!
    while(True):
        a.canvas.move(rect,20,20)
        a.canvas.update()
        time.sleep(0.5)
    a.root.mainloop()


def moveRobot(arena):
    for robot in arena.movingRob:
        direction = robot[0].move()
        if (direction == 0):  # step right
            if (arena.matrix[robot[1] + 1][robot[2]] == 0 or arena.matrix[robot[1] + 1][robot[2]] == 1):
                arena.matrix[robot[1]][robot[2]] = robot[0].color
                arena.matrix[robot[1] + 1][robot[2]] = robot[0].id
                robot[1] = robot[1] + 1
                robot[0].X+=1
        if (direction == 1):  # step left
            if (arena.matrix[robot[1] - 1][robot[2]] == 0 or arena.matrix[robot[1] - 1][robot[2]] == 1):
                arena.matrix[robot[1]][robot[2]] = robot[0].color
                arena.matrix[robot[1] - 1][robot[2]] = robot[0].id
                robot[1] = robot[1] - 1
                robot[0].X -= 1
        if (direction == 2):  # step up
            if (arena.matrix[robot[1]][robot[2] + 1] == 0 or arena.matrix[robot[1]][robot[2] + 1] == 1):
                arena.matrix[robot[1]][robot[2]] = robot[0].color
                arena.matrix[robot[1]][robot[2] + 1] = robot[0].id
                robot[2] = robot[2] + 1
                robot[0].Y += 1
        if (direction == 3):  # step down
            if (arena.matrix[robot[1]][robot[2] - 1] == 0 or arena.matrix[robot[1]][robot[2] - 1] == 1):
                arena.matrix[robot[1]][robot[2]] = robot[0].color
                arena.matrix[robot[1]][robot[2] - 1] = robot[0].id
                robot[2] = robot[2] - 1
                robot[0].Y -= 1



if __name__ == "__main__":
    main()


