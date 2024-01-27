from abc import ABC,abstractmethod
class employee(ABC):
    def employee_info(self):
        print('login')
    @abstractmethod
    def empvalue(self):
        pass
class company(employee):
    def company_info(self):
        print('company login')
class suba(company):
    def empvalue(self):
        print('employee value')
a=suba()
a.employee_info()
a.company_info()
a.empvalue()
'''

class student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def value(self):
        print(f'id {self.id} and my name {self.name}')
class employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def value(self):
        print(f'employeeid is {self.id} and employeename is {self.name}')
a=student(1,'invigo')
b=employee(1,'vinitha')
for x in (a,b):
    a.value()
    b.value()  
'''

        



    
    
        

                                                                                                 