class learnoverloading:

    ls = []
    def __init__(self, *args):
        self.ls = args
        print(self.ls)


y = learnoverloading(10, 20, 30, 40, 50)
z = learnoverloading(1, 2, 3)


