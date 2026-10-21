# n = int(input("Enter a number: "))
# n1=n
# rev=0
# if n>0:
#     while n>0:
#         rev = rev*10+(n%10)
#         n=n//10
#     print(rev)
# else:
#     print("enter a valid number")
# if(rev==n1):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

n = int(input("Enter a number: "))
n1 =n
rev =0
if n<0:
    n = -n
while n>0:
    rev = rev*10+(n%10)
    n = n//10
print(rev)
if n1<0:
    rev = rev*-1
    print(rev)
else:
    print(rev)
if n1==rev:
    print("palindrome")
else:
    print("not palindrome")
