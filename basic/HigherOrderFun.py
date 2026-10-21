# def counter(start=0):  # higher order function
#     count = start

#     def increment():  # inner function
#         nonlocal count  # retains access to 'count' even after counter() ends
#         count += 1
#         return count

#     return increment  # returns the inner function

# counter1 = counter(5)  # closure retains count = 5
# print(counter1())
# print(counter1())

# counter2 = counter(10)  # new closure with count = 10
# print(counter2())


def squr(x):
    return x*x


def cube(x):
    return x*x*x


def operate(y, operation):
    for i in y:
        result = operation(i)
        print(result)


y = [1, 2, 3, 4, 5]
operate(y, squr)
