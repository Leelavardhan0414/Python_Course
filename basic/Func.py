def add(a, b):
    c = a+b
    # print(c)
    return c


res = add(10, 20)
print(res)


# def sub(a=10, b=9):   # default arguments
#     c = a-b
#     return c


# res = sub()
# print(res)


def Sum(a, *b):          # variable length arguments
    sum = a
    for i in b:
        sum += i
    return sum


res = Sum(2, 4, 7, 3, 8)
print(res)

print()


def details(name, age):          # keyword arguments
    print('name: ', name)
    print('age: ', age)


details(age=23, name='Leelavardhan')

print()


def detailss(name, **nvlarg):
    print('name: ', name)
    print(nvlarg)
    for i, j in nvlarg.items():
        print(i, ': ', j)


detailss(name='Leelavardhan', age=23, loc='B.Kothakota')
print()


def EvenOdd(x):
    # k=[]
    for i in range(len(x)):
        if x[i]%2==0:
            # k[i]="Even"
            print( "Even")
        else:
            # k[i]="Odd"
            print( "Odd")
n=[2,3,4,5,6,7]
h=[1,4,5,6,2,8]
EvenOdd(n)
EvenOdd(h)

