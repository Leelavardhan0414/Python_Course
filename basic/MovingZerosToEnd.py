n = list(map(int, input("Enter numbers: ").split()))

if len(n) != 0:
    count = 0
    for i in range(len(n)):
        if (n[i] != 0):
            n[count] = n[i]
            count += 1

    for i in range(count, len(n)):
        n[i] = 0
    print(n)
else:
    print("Enter numbers")
