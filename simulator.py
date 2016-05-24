import time

import Arena

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
        time.sleep(0.25)



if __name__ == "__main__":
    main()


