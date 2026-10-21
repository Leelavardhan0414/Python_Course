from array import *
arr = array('i',[1,2,3,4,5])
arr1=('i',[6,7,8,9,10])
print(type(arr))
li=[2,4,6]
list1 = li.index(6)
print(li)
print(arr)
print(list1)

numbers = list(map(int, input("Enter numbers: ").split()))
# arr2 = array('i',numbers)
# print(type(arr2))
# print(numbers)
sum=0
for i in range(len(numbers)): 
    sum = sum+numbers[i]
print("SUM:",sum)

# array functions

print(max(numbers))
print(min(numbers))
numbers.append(20)
print(numbers)
print(numbers.count(3))

numbers.extend([74,75,79,89,90,80])
print(numbers)
numbers.insert(1,45)
print()
print(numbers)
numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)
