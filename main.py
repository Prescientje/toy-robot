from sys import argv
from robot import *

def doLine(line):
    pass

def main():
    script, f_name = argv
    print("Reading from %s" % f_name)
    rob = Robot(1,1,1)
    print(rob.report())
    rob.turn_left()
    print(rob.report())
    rob.move()
    rob.move()
    print(rob.report())
    rob.place(2,2,2)
    print(rob.report())
    

if __name__ == '__main__':
    main()
