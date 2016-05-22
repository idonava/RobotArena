import Arena
import thread

def main():
    a = Arena.Arena()
    a.create_arena()
    a.create_robots(3, True)
    a.create_robots(10, False)
    a.print_arena()

    print(a.movingRob[0].X, a.movingRob[0].Y)
    a.movingRob[0].start()
    print(a.movingRob[0].X, a.movingRob[0].Y)
    print(a.movingRob[0].X, a.movingRob[0].Y)
    print(a.movingRob[0].X, a.movingRob[0].Y)
    print(a.movingRob[0].X, a.movingRob[0].Y)

if __name__ == "__main__":
    main()