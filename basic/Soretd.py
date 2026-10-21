s = list(map(int, input("Enter numbers: ").split()))
for i in range (len(s)):
    for j in range(len(s)):
        if(s[i]>s[j]):
            t = s[i]
            s[i]=s[j]
            s[j]=t
print(s)