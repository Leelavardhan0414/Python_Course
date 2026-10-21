def fun(name,age):
    print(name,age)
fun(name='Leelavardhan',age=23)
fun(age=23,name='Leelavardhan')

def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    print(args)
    for arg in args:
        print(arg)

    print("Keyword Arguments (**kwargs):")
    print(kwargs)
    for key, value in kwargs.items():
        print(key, ":" ,value)

myFun('Hey', 'Welcome', first='Leelavardhan',  last='Thanakanti')