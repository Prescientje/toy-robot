from sys import argv
from robot import *

def doLine(line, rob):
    if rob == None and not line.startswith("place"):
        return None
    elif rob == None and line.startswith("place"):
        vals = line.strip("place ").split(",")
        return Robot(int(vals[0]),int(vals[1]),int(vals[2]))
    elif line.startswith("move"):
        rob.move()
    elif line.startswith("left"):
        rob.turn_left()
    elif line.startswith("right"):
        rob.turn_right()
    elif line.startswith("report"):
        print(str(rob))
    elif line.startswith("place"):
        vals = line.strip("place ").split(",")
        rob.place(int(vals[0]),int(vals[1]),int(vals[2]))

    return rob


def main():
    if len(argv) == 1:
        print("You need to call this file with a txt file of instructions for the robot to follow.")
        return

    script, f_name = argv
    s = "Reading from %s:" % f_name
    print(s)
    print("-"*len(s)+"\n")
    instrs = open(f_name, "r")
    rob = None
    for i in instrs:
        rob = doLine(i.lower(), rob)

    print("\n----------------------")
    print("Instructions complete.")

    '''
    rob = Robot(1,1,0)
    print(rob.report())
    rob.turn_left()
    print(rob.report())
    rob.move()
    rob.move()
    print(rob.report())
    rob.move()
    print(rob.report())
    rob.move()
    print(rob.report())
    rob.move()
    print(rob.report())
    rob.place(2,2,2)
    print(rob.report())
    '''
    

if __name__ == '__main__':
    main()
