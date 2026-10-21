from functools import reduce

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
a = ['  apple  ', 'banana', 'orange', 'grapes']

even = list(filter(lambda x: x % 2 == 0, n))

double = list(map(lambda x: x*2, even))

red = reduce(lambda x, y: x+y, double)

max = list(filter(lambda x: len(x) > 5, a))

ma = list(map(lambda x: x*2, a))


def s(x, y): return (x+y, x*y)

res = reduce(lambda x,y :x+y,n)

numbers = [1, 2, 3, 4]

square = [(lambda x=i: x*10)(i) for i in n]


ss = list(map(lambda x : x**x,n))

sss = list(map(lambda x,y : x+y,n,numbers))

h = map(lambda x : x.upper(),a) # map(str.upper,a)

hh = map(lambda x :x.strip(),a)
print(list(hh))
print(list(h))
print(sss)

print(square)
print(ss)
print(res)

print(even)

print(double)

print(red)

print(max)

print(ma)

r = s(7, 4)
print(r)

re = sum(n)
print(re)
