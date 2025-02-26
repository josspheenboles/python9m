from Human import Human
class Employee(Human):
    def __init__(self,id,name,age,gender,salary,position):
        super().__init__(id,name,age,gender)
        self.salary=salary
        self.pos=position
    def speek(self):
        print(f'iam {self.name},gender:{self._gender}')
    def __str__(self):
        return super().__str__()+'iam empluyee'
    def __len__(self):
        return self.salary
