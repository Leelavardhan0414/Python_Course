class A:
    def f1(self):
        print("Function 1")

    def f2(self):
        print("Function 2")

    def show():
        print("in A Show")


class B(A):
    def f3(self):
        print("Function 3")

    def f4(self):
        print("Function 4")

    def show(self):
        print("in B Show")


class C(B):
    def f5(self):
        print("Function 5")


# Multiple inheitence


# class C(A,B):
#     def f5(self):
#         print("Function 5")

#     def show(self):
#         print("in C Show")
obj1 = C()

B.show(obj1)
obj1.f5()
obj1.show()
