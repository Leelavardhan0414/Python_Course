list = [2,3,8,8,7,3,9,0]
list.sort()
print(list)
secMax=list[-2]
count=0
for i in list:
    if(secMax==i):
        count+=1
print(count)

print()
print()

print("-----------------Slicing------------------")
print(list[2:-1]) #slicing
print(list[0:3])
print(list[-1:3])
print(list[:])
print(list[2:])
print(list[:90])
print(list[0:90])
print(list[3:-1])  #slicing
print("-----------------Slicing------------------")

print()

# list = ["Leelavardhan","Ram","Ana"]
# list.sort(key=len)
# for i in range(len(list)):
#     print(list[i])


