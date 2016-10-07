'''
This program will emulate a robot moving around on a square table.

'''



class Robot(object):
    '''
    Represents a robot that can move around on a table.
    The table is default 5x5, so the southwest corner is (0,0)
    and the northeast corner is (4,4).
    '''

    def __init__(self, x=0,y=0,f=0,maxX=5,maxY=5):
        self.x = x-1
        self.y = y-1
        self.f = f #0 = north, 1 = east, 2 = south, 3 = west
        self.maxX = maxX-1
        self.maxY = maxY-1

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
        if self.f == 0 and self.y < self.maxY:
            self.y += 1
        elif self.f == 2 and self.y > 0:
            self.y -= 1
        elif self.f == 1 and self.x < self.maxX:
            self.x += 1
        elif self.f == 3 and self.x > 0:
            self.x -= 1

    def place(self, x, y, f):
        self.x = x-1
        self.y = y-1
        self.f = f

