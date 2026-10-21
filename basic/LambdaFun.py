



a = lambda x: x*x
print(a(5))


b = lambda str : str.upper()
print(b("leelavardhan"))

# use cases

check = lambda x: "positive" if x>0 else "negative" if x<0  else "Zero" 
print(check(10))
print(check(-1))
print(check(0))

#  List comparehesion

fun = [lambda arg: arg *10 for i in range(1,5)]
for i in fun:
    print(i())