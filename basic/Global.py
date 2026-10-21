a=10    # global Variable
print('Outside: ',a)
def Var():

    global a
    a=16        # Local Variable
    print('inside: ',a)
Var()
print('Outside: ',a)



