d = {'a':1,'b':2}
h = d.pop('a')
val = d.get('c',3)
print(val)
print(d)
print(h)




for k,v in d.items():
    print(k,":", v)

d1 = {"a": 1, "b": 2}
for k, v in d1.items():
    print(k,':',v*2)








aa = [1,2,3,4,5,6]
aa.pop()

print(aa)
aa.insert(2,4)
print(aa)
c=aa.copy()
aa.reverse()

print(c)
print(aa)

print(d.popitem())