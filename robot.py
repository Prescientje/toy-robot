'''
This program will emulate a robot moving around on a square table.

'''

def main():
    rob = Robot(1,1,1)
    print(rob.report())
    rob.turn_left()
    print(rob.report())
    rob.move()
    rob.move()
    print(rob.report())
    rob.place(2,2,2)
    print(rob.report())
    


class Robot(object):
    '''
    Represents a robot that can move around on a table.
    '''

    def __init__(self, x=0,y=0,f=0):
        self.x = x 
        self.y = y 
        self.f = f #0 = north, 1 = east, 2 = south, 3 = west

    def __str__(self):
        return "My position is ({0},{1}) and I am facing {2}.".format(self.x,
                                                                      self.y,
                                                                      self.get_facing())

    def get_facing(self):
        if self.f == 0:
            return "North"
        elif self.f == 1:
            return "East"
        elif self.f == 2:
            return "South"
        else:
            return "West"

    def turn_left(self):
        self.f -= 1
        self.f %= 4

    def turn_right(self):
        self.f += 1
        self.f %= 4

    def report(self):
        return str(self)

    def move(self):
        if self.f == 0:
            self.y += 1
        elif self.f == 2:
            self.y -= 1
        elif self.f == 1:
            self.x += 1
        else:
            self.x -= 1

    def place(self, x, y, f):
        self.x = x
        self.y = y
        self.f = f


if __name__ == '__main__':
    main()
