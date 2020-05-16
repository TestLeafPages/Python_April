class testleaf:

    # constructor
    def __init__(self, name, exp):
        self.name = name
        self.exp = exp
        print('im the constructor from testleaf')
        print(f'from constructor {self}')

    def __str__(self):
        return "testleaf"

    def python(self):
        print(f'{self.name}----->{self.exp}')

    def selenium(self):
        print(f'{self.name}----->{self.exp}')



per1 = testleaf('dinesh', 3)
per1.python()
print(per1)

# print('*' * 25)
#
# per2 = testleaf('Rajesh', 7)
# per2.selenium()

a = 10
b = 15

print(a + b)
print(a.__add__(b))
