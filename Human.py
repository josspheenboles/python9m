
class Human:
    #class variable
    count=0
    live=True
    def __init__(self,id,name,age=22,gender='M'):
        #instance var
        #private
        self.__id=id
        self.name=name
        self.age=age
        #protected
        self._gender=gender
        Human.count+=1
    def __str__(self):
        return f'iam human ,Id:str({self.__id})'
    def __len__(self):
        return self.age
    @property
    def ID(self):
        return self.__id
    @ID.setter
    def ID(self,newid):
        if (len(newid) == 14):
            self.__id=newid
    # def getid(self):
    #     return  self.__id
    # def setid(self,newid):
    #     if(len(newid)==14):
    #         self.__id=newid

    #instance method
    def speek(self):
        print(f'my id {self.__id} ,my name is {self.name},age:{self._gender}')
    def walk(self):
        print(f'iam walingin')
    @classmethod
    def getpopulation(cls):
        # print(cls)
        return cls.count
    @staticmethod
    def mesuretemp(temp):
        # temp=input('enter temp')
        if (temp>37):
            print('too hot')
        elif (temp<37):
            print('too cold')
        else:
            print('normal')
   #      print(self)
   #      print('hi iam human constr.')
   #
class Test:
    pass

def fun():
    pass

var=10