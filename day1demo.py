x,y=5,6
print(x,y)
x,y=(y,x)
print(x,y)
# s='ID:{id}\nName:{n}\nID{id}'
# # print(s.format(1,'diab',1))
# # print(s.format(2,'abdo',2))
# # print(s.format(3,3,'yasm.'))
# print(s.format(n='yasm.',id=3))
#
# # def fun(y,*x,**z):
# #     pass
# # fun(1,2,3,4,5)
# # fun(k1=1,)
# # varname,va2=val1,val2
# # t=1,2
# # print(type(t))
# # z,x,*y=(10,1,2,3,4)#unpacking
# # print(x,y)
# # name='aya ali ahmed'
# # print(name.replace('a','@',2))
# # # print(name[[start=0],end=lenght,[step=1]])
# # print(name[::-1])
# # print(name[-1])
# # #
# # # def mysum(**arg):
# # #     print(type(arg))
# # #     print(arg)
# # # d={'id':1,'name':'aya'}
# # # mysum(key1=1,key2=3,k3=3)#packing keys,values
# # # mysum(key=d)#{'key':d}
# # # print(mysum)
# # # def mysum():
# # #     pass
# # # print(mysum(d='d'))
# # #{'key1':1,'key2':2}
# # # t=(1,2,3)
# # # mysum(t)#((1,2,3),)
# # # mysum(t)#((1,2,3),)
# # # mysum(1,2)#(1,2) packing
# # # mysum([1,23])
# # # # mysum(1,2,3)
# #
# # # mysum(1,2)
# # # mysum(2)
# # # def mysum(x,y=10,z=20):
# # #     print(x,y,z)
# # # # def mysum(num1,num2):
# # # #         return num1+num2
# # # # print('hi')
# # # # var=mysum(1,2)
# # # # print(var)
# # # # var=mysum("aya",'ali')
# # # # var=mysum("aya",'ali')
# # # # var=mysum("aya",'ali')
# # # # var=mysum("aya",'ali')
# # # # var=mysum("aya",'ali')
# # # # var=mysum("aya",'ali')
# # # # var=mysum("aya",'ali')
# # # # var=mysum("aya",'ali')
# # # # var=mysum("aya",'ali')
# # # # var=mysum("aya",'ali')
# # # # var=mysum("aya",'ali')
# # # # var=mysum("aya",'ali')
# # # # print(var)
# # # # # x=eval(input('enter your age'))
# # # # # # if(x.isa)
# # # # # # x=int(x)
# # # # # print(type(x))
# # # # # # # from operator import index
# # # # # # #
# # # # # # name='''nada'''
# # # # # # # index=0
# # # # # # #convert string to collection of tuples
# # # # # # #[(index,value),(),,,,()]
# # # # # # for var in enumerate(name):
# # # # # #     print(f'Index:{var[0]},Item:{var[1]}')
# # # # # #     print('Index:',var[0],'Item:',var[1])
# # # # # # # if (True):
# # # # # #
# # # # # #     #sep=' '
# # # # # #     #end='\n'
# # # # # #     # index+=1
# # # # # #     # if(var=='a'):
# # # # # #     #     break
# # # # # #     # print(var,index,end=' ')
# # # # # # # # else:
# # # # # # #
# # # # # # # print('for ended sucessfuly')
# # # # # # #
# # # # # # #
# # # # # # # # r=range(1,13,1)
# # # # # # # # for month in r:
# # # # # # # #     print(month)
# # # # # # # # print(r)
# # # # # # # # range(1,13)
# # # # # # # # range(13)
# # # # # # # # #block level1
# # # # # # # # name='nada'
# # # # # # # # #block level1
# # # # # # # # if name=='alia':
# # # # # # # #     # block level2
# # # # # # # #     print('hi')
# # # # # # # #     if(True):
# # # # # # # #         # block level3
# # # # # # # #         print('hi nada')
# # # # # # # # # else:
# # # # # # # # #     print('not allowd')
# # # # # # # # # print(0 and 5 and 3)
# # # # # # # # # print(16/5)
# # # # # # # # # print(2**3)
# # # # # # # # # print(1=='1')
# # # # # # # # # print(1!='1')
# # # # # # # # # # print(1<>'1')
# # # # # # # # # # c1=2+2j
# # # # # # # # # # c2=3+5j
# # # # # # # # # # c3=c1+c2
# # # # # # # # # # print(type(c3))
# # # # # # # # # # num='one'#str
# # # # # # # # # # num=int(num)
# # # # # # # # # # print(type(num))
# # # # # # # # #
# # # # # # # # # # print('hi')
# # # # # # # # # # print('abdallah')
# # # # # # # # # # #var
# # # # # # # # # # #collection of values diff data types,not fixed size
# # # # # # # # # # #store as key==>str : value
# # # # # # # # # # student={
# # # # # # # # # #     'id':1,
# # # # # # # # # #     'name':'aya',
# # # # # # # # # #     'course':['python','java']
# # # # # # # # # # }
# # # # # # # # # # s={1,'1',True,[],()}
# # # # # # # # # # print(student)
# # # # # # # # # # # #collection of values diff data types,not fixed size
# # # # # # # # # # # #tuple is immutable list
# # # # # # # # # # # t=(1.1,[])
# # # # # # # # # # # # t[1]=100
# # # # # # # # # # # t[1].append(100)
# # # # # # # # # # # print(type (t),t)
# # # # # # # # # # #collection of values diff data types,not fixed size
# # # # # # # # # # # student=[1,'aya ali',3.9,['bash','python','java'],True]
# # # # # # # # # # # student[1]='omar'
# # # # # # # # # # # print(student[1])
# # # # # # # # # # # name=None
# # # # # # # # # # # print(type(name))
# # # # # # # # # # # name='hamdy'
# # # # # # # # # # # print(type(name))
# # # # # # # # # # # name=10
# # # # # # # # # # # print(type(name))
# # # # # # # # # # # name=2.2
# # # # # # # # # # # print(type(name))
# # # # # # # # # # # name=True
# # # # # # # # # # # print(type(name))
# # # # # # # # # # # import  sys
# # # # # # # # # # # print(sys.maxsize)
# # # # # # # # # # # x=sys.maxsize
# # # # # # # # # #
