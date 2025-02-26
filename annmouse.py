def mydecroater(fun):
    def wrapper(*args,**kargs):
        # print(args,kargs)
        print('iam decroarto for fun function')
        res=fun(args[0])
        print('after exeuatiojn')
        return res
    return wrapper
@mydecroater
def fun(n):
    return (n+10)
fun(10)
# varlamda=lambda  n:n+3
# # def isodd(n):
# #     if(n%2!=0):
# #         return n
# l=[1,2,3,4,5,6,7]
# m=map(varlamda,l)
# # print(m)
# for x in m:
#     print(x)
# # # for n in l:
# #     print(isodd(n))
# #
#
# # l=[]
# #
# #
# # def gen(n):
# #     for n in range(1, 13):
# #         yield n
# # l.append(gen(5))
# # print(l)
# # # # # lambda  input:output
# # # # varname=l
# # ambda  x:x**2
# # # # print(varname(2))
# # # def fun(x):
# # #     print(x)
# # #     y=lambda n:n+x
# # #     return y
# # # print(fun(5)(3))