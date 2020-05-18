class Rectangle:

    def __init__(self, len, brea):
        self.len = len
        self.brea = brea


    def getArea(self):
        print(self.len * self.brea,  is are of rectangle)


class square(Rectangle):

    def __init__(self, side):
        self.side = side
        Rectangle.__init__(self, side, side)

    def getArea(self):
        print(self.side * self.side, is area of square)