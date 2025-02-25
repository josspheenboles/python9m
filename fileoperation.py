#module==>containr varible,function,class drfination,
count=10
def readallfile(pathfile):
    with open(pathfile,'r') as f:
        return  f.read()
def readfilecountchar(pathfile,count):
    with open(pathfile,'r') as f:
        if(isinstance(count,int)):
            return  f.read(count)




