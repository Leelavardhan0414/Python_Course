# def MagicalMirror(a):
#     n = a
#     e=0
#     trans=0
#     while(n>0):
#         r = a%10
#         a = n//10
#         if r %2==0:
#             tans = (2*2)%10
#             e = e*10+trans

#         else:
#             trans=9-r
#             e = e*10+trans
#     ee = reversed(e)
#     aa = ee-e
#     return aa
# nnn = 123
# print(MagicalMirror(nnn))
def MirrorMiagic(n):
    origiginal = n
    r = 0
    digit = 0
    while (n > 0):
        digit = n % 10

        if (digit % 2 == 0):
            temp = (2*2) % 10
        else:
            temp = 9 - digit
    return
