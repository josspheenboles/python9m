import  sys
try:
    open('asd.txt','r')
    int('aya')
    1/0
except PermissionError:
    print('filer permiis')
except ValueError:
    print('val')
except ZeroDivisionError:
    print('zer')
except FileNotFoundError:
    print('')
except:
    print('error',sys.exc_info()[1])
# import  os
# print(os.system('cd /;ls -l'))
# print(os.name)
# # # from myexperpckg.fileoperation import count as fcount
# # from myexperpckg.files import fileoperation
# # from myexperpckg.files.fileoperation import count
# # # from myexperpckg.files import  fileoperation.count
# # count=0
# # print(count)
# # print(fileoperation.count)
# # # import  fileoperation
# # # fileoperation.readallfile('demo2.py')
# # # #modes
# # # #r==>must be exsist,read only,must have permission
# # # #w===>clear contetnt,not exsists will create,write ony
# # # #a===>conti. add ,,not exsists will create,write only
# # # #r+--->must be exsist,read & append,must have permission
# # # #rb--->binary file
# # # #rb+--->bninary file ,read,write
# # # with open('asd.txt','a') as file:
# # #     # if(file.writable()):
# # #         file.write('hamdy\n')
# # #         file.seek(3)
# # #         file.write('''abdo
# # #         maha''')
# # #         l=['yasmen\n','mariam\n','abdallha\n']
# # #         file.writelines(l)
# # # #     if(file.readable()):
# # # #         file.read()
# # # # # with open('asd.txt','r') as file:
# # #
# # #     # print(type(file),file)
# # #     # print(file.readlines())
# # #     # for line in file:
# # #     #     print(line)
# # #     # print(file.read(3))
# # #     # print('===',file.read(),'===',sep='')
# # #
# # #
# # # def readallfile(pathfile):
# # #     #file must exssist
# # #     #file must have permission
# # #     with open(pathfile,'r') as f:
# # #         content=f.read()
# # #     return  content
# # # def readcountofchar(pathfile,count):
# # #     with open(pathfile,'r') as file:
# # #         if(isinstance(count,int)):
# # #             content=file.read(count)
# # #             return  content
# # #         else:
# # #             return 'count must be int'
# # # print(readcountofchar('asd.txt',1))
# # # # s={'aya','ali',3,4}
# # # # for it in enumerate(s):
# # # #     print(it)
# # # # print(type(s),s[0])
# # #
# # # # d1={'id':1}
# # # # d2={'name':'omr'}
# # # #
# # # # d2['name']='ahmed'
# # # # print(d1,d2,sep='\n')
# # # # # l1=[1,2]
# # # # # l2=[3,4]
# # # # # # l1=l2
# # # # # l1=l2.copy()
# # # # # l1[0]='abdo'
# # # # # print(l1,l2,sep='\n')
# # # # # # d={'id':1,'name':'omr','id':100}
# # # # # # d['intake']=45
# # # # # # for key,val in d.items():
# # # # # #     print(key,val)
# # # # # # print(d.items())
# # # # # # # print(d[key])
# # # # # # # d2={'intake':45,'name':'ghada'}
# # # # # # # print(d['id'])
# # # # # # # d2.update(d)
# # # # # # # print(d,d2,sep='\n')
# # # # # # # print(d+d2)
# # # # # # # print(d*3)
# # # # # # # l1=[3,4]
# # # # # # # l2=[5,6]
# # # # # # # l2=l1.copy()
# # # # # # # l2[0]='hamdy'
# # # # # # # print(l1,l2,sep='\n')
# # # # # # #
# # # # # # # # #data struct
# # # # # # #tuple
# # # # # # # t1='1',3
# # # # # # # print(t1)
# # # # # # # # t2=(3,4)
# # # # # # # t1=t1+t2
# # # # # # # t1+=t2
# # # # # # # print(t1,t2)
# # # # # # # print(t1*2)
# # # # # # # print(t1+t2)
# # # # # # # t=('aya',(),{})
# # # # # # # t[0].append(1)
# # # # # # # t[0]='A'
# # # # # # # t[0]=[]
# # # # # # # print(t)
# # # # # # # print(t[1:3])
# # # # # # # # index,value=(1,2)
# # # # # # # for index,value in enumerate(t):
# # # # # # #     # print(item,type(item))
# # # # # # #     print(index,value)
# # # # # # # print(type(t),t)
# # # # # # # # #list
# # # # # # # prog=['java','c','c++','php']
# # # # # # # admin=['admin1','bash','python']
# # # # # # # # print(prog+admin)
# # # # # # # # prog.extend(admin)
# # # # # # # # prog+=admin
# # # # # # # # prog.append(admin)
# # # # # # # name='aya'
# # # # # # # print(prog*3)
# # # # # # # print(prog,admin,sep='\n')
# # # # # # #
# # # # # # #
# # # # # # # # #collection of values diff data
# # # # # # # # l=[1,1.1,True,'one',[],(),{'id':1},{}]
# # # # # # # # l.append('abdallha')
# # # # # # # # l.insert(1,'mariam')
# # # # # # # # print(l.pop())
# # # # # # # # l.pop(1)
# # # # # # # # print(l.remove(True))
# # # # # # # # print(l.index(True))
# # # # # # # # # l[4].append(4)#[4]
# # # # # # # # # l[4].insert(0,5)#[5,4]
# # # # # # # # print(l)
# # # # # # # #
# # # # # # # #
