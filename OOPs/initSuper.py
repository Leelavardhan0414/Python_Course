class A:
    def __init__(self):
        print("In A init")

    def f1(self):
        print("Function 1")


class B(A):
    def __init__(self):
        super().__init__()
        print("In B init")

    def f2(self):
        print("Function 2")


obj1 = B()
obj1.f2()

