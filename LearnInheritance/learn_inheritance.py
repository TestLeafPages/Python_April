class A:

    def __init__(self,a):
        print("from Class A __ init__")

    def first_class(self):
        print("i'm from Class A")


    def sec_class(self):
        print("i'm also from Class A")


class B(A):

    def __init__(self):
        print("from class B __init__")
        super().__init__()


    def thr_class(self):
        print("i'm from Class B")


b = B()
b.thr_class()
b.first_class()
b.sec_class()