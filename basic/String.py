# import re
# def Count(x):
#     count =0
#     x= x.lower()
#     h=re.findall(r'helloworld',x)
#     for i in h:
#         if(i=='helloworld'):
#             count=count+1
#     return count
# a = 'Helloworldhelloworldhellohdh'
# res= Count(a)
# print(res)


def count(x):
    x = x.lower()
    res=len(x.split('helloworld'))-1
    return res
a  = "Helloworldhelloworldhelloworldhekkuhshelloworld"
r = count(a)
print(r)