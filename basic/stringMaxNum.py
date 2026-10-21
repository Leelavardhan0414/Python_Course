n = input("Enter a String Number: ")
if len(n)!=0:
    max = n[0]
    if n.isdigit():
        for i in range(len(n)):
            if (max < n[i]):
                max = n[i]
        print(max)
    else:
        print("Not a valid String")
else:
    print("Enter a valid String number")
# n1=int(max)
# print(max)
# print(type(n1))
