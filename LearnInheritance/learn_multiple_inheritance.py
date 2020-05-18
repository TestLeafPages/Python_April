class A:

    def a(self):
        print('from A')

    def c(self):
        print('from C')


class B:

    def b(self):
        print('from B')


class C(A):
    pass



class D(C, B):                   # Multiple inheritance

    def d(self):
        print('from D')

z = D()
print(D.__mro__)
