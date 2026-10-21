# outer function
def fun1(msg):  
    # inner function
    def fun2():
         # access variable from outer scope
        print(msg) 
    fun2()
fun1("Hello")



def fun1(): 
    msg = "Geeks for geeks"
    def fun2(): 
        print(msg) 
    fun2()
fun1()