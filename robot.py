'''
This program will emulate a robot moving around on a square table.

'''

def main():
    rob = Robot()
    print("test")
    print(rob)


class Robot(object):
    '''
    Represents a robot that can move around on a table.
    '''

    def __init__(self, x=0,y=0,f=0):
        self.x = x 
        self.y = y 
        self.f = f #0 = north, 1 = east, 2 = south, 3 = west

    def __str__(self):
        return "My position is ({0},{1}) and I am facing {2}".format(self.x,self.y,self.get_facing())

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
        if self.f == 0:
            self.f = 3
        else:
            self.f -= 1

    def turn_right(self):
        if self.f == 3:
            self.f = 0
        else:
            self.f += 1



if __name__ == '__main__':
    main()
