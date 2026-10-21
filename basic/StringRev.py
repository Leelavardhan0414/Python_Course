str = input("Enter a String: ")
str = str.lower()
rev =""
if len(str)!=0:
    for i in range(len(str)-1,-1,-1):
        rev +=str[i]
    print(rev)
    # for i in reversed(str):
    #     print(i)
    # rev = "".join(reversed(str))
    # print(rev)
else:
    print("Not a valid string")
if str == rev:
    print("palindrome")
else:
    print("Not palindrome")