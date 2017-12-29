# Robots Arena
Robot class model
Move
1. If the robot is currently in the white zone (==charging), the direction is random.
2. If the robot is currently in a gray zone, the direction is calculated to it’s nearest neighbor that is in the white zone\ to the last location that this robot was in a white zone.

Send Message
If a robot is not “dead” (has battery), he can send a message if one of the following happens:
1. He is a static robot (==knows its location)
2. He is a moving robot- that knows its location with a guess based on at least 4 neighbors.

Update Guess
this method is activated every time the robot moves.
It is based on the RMS algorithm. 
The algorithm is used with the latest messages the robot received.

Arena class model
Create random arena
This method generates white, gray and black areas in the arena. 
The default size of the arena is 1000*1000 as defined in the Global Parameters class.

Create arena from file
This method creates the arena from a file (build in a template).
The method “reads” the limits of the black and gray areas, and then implements them unto the arena.

Create robots
This method receive argument: number of robots to create, and Boolean- isStatic.
For each robot it choose a random spot- make sure its not a black one, and place the new robot to the spot.
Then the method creates the robot in the gui.

Simulator class model
Move
1. The method moves all the moving robots on each iteration.
2. It calls to the send message method.
3. It calls the update guess for each robot- to update its location based on the messages that were just send.

Send Message
1. The method decides randomly which robots will send\ get the messages.
2. For each receiving robot- the method calculates which sending robot is the closest to him.
3. The receiving robot gets the message with the distance from the sender- uniformed by 20%.

Main
1. Creates the arena (from file or randomly)
2. Creates the robots.
3. Move the robots in the arena.

![](https://github.com/idonava/matala3/blob/master/img.png)
