from Human import Human
from Employee import *
obj1=Human(10,'aya',10)
len(obj1)
# obj1.ID='10'
print(len(obj1))
emp1=Employee(10,'ahmed',23,'M',8000,'back')
print(len(emp1))
# from multipledispatch import dispatch
# @dispatch(int,int)
# def add(arg1,arg2):
#     (print(arg1,arg2)
# @dispatch(int, int,int)
# def add(arg1, arg2,arg3):
#         (print(arg1, arg2,arg3)
#
#          @dispatch(float,float))
# def add(arg1,arg2):
#     print(arg1,arg2)
#
# add(1.1,2.2)
# # def add(datatype,arg1,arg2):
# #     if(datatype=='int' or datatype=='float'):
# #         return  arg1+arg2
# #     elif(datatype=='str'):
# #         return  arg1+' '+arg2
# #     else:
# #         return  'invalid datat type'
# # print(add('int',1,2))
# # print(add('str','aya','ali'))
# # # class x(a,b)
# # from Human import Human
# # from Employee import Employee
# # # emp1=Employee(10,'aya',23,'F',8000,'back developer')#employee--->constr,human--->constr
# # # obj1=Human (10,'aya ali')
# # # print(emp1._gender)
# # # # print(emp1._age)
# # # emp1.mesuretemp(37)
# #
# # # obj1.speek()
# # #
# # # print(obj1.__id)
# # # obj1.speek()
# # # # def getpopulation():
# # # #     return  Human.count
# # # # id=10
# # # # print(id)
# # # from Human import  Human
# # # obj1=Human (10,'aya ali')
# # # Human.getpopulation()
# # # obj1.getpopulation()
# # # obj1.mesuretemp(10)
# # # Human.mesuretemp(10)
# # #
# # # #create object
# # # #parent object ()
# # # #is human class has constr access parent object
# # #
# # # # obj1.address='smart vil.'
# # # # print(obj1)
# # # # obj1.speek()
# # # # # #convert count to instance var
# # # # # print(obj1.id)
# # # # # obj1.count=10
# # # # # obj1.live=False
# # # # # obj2=Human (11,'ahmed ali')
# # # # # print(Human.count)
# # # # # print(obj1.count)
# # # # # print(obj2.count)
# # # # # obj1.id=100
# # # # # obj1.name='nada moataz'
# # # # # obj1.gender='Female'
# # # #
# # # # # print(obj1.id)