s = input("Enter a String: ")

count = {}
print(count)

for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print("Character Occurrences:")
print(count)

for ch in count:
    print(ch, "=", count[ch])
print()

print("Occurrance of Single Charater")
print()
s1 = input("Enter a  String: ")
s2 = input("Enter a character: ")
countt=0
for i in range(len(s1)):
    if(s1[i]==s2):
        countt+=1
print(countt)


# s3 = s1.replace(s2,"")
# print(len(s1)-len(s3))