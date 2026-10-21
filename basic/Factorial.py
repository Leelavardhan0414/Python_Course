# without function
# n=5
# fact = 1
# for i in range(1,n+1):
#     fact*=i
# print(fact)


# with function
def fact(x):
    f =1
    for i in range(1,x+1):
        f*=i
    return f
res= fact(5)
print(res)