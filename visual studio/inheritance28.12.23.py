'''
class person:
    def __init__(self,fname,lname,a,dob,eml):
        self.firstname=fname
        self.lastname=lname
        self.age=a
        self.dateofbirth=dob
        self.email=eml
    def value(self):
        print(self.firstname,self.lastname,self.age,self.dateofbirth,self.email)
class employee(person):
    def __init__(self,fname,lname,id,salary,dev,a,dob,eml):
        super().__init__(fname,lname,a,dob,eml)
        self.employeeid=id
        self.employeesalary=salary
        self.developer=dev
    def value1(self):
        print(self.firstname,self.lastname,self.employeeid,self.employeesalary,self.developer)
x=employee('subha','deeban','101','30000','python developer',12,"12/12/12","sdfjlk@g.com")
x.value()
x.value1()
'''
class person:
    def __init__(self,fname,lname,place):
        self.firstname=fname
        self.lastname=lname
        self.location=place
    def value(self):
        print(self.firstname,self.lastname,self.location)
class student(person):
    def __init__(self, fname, lname,id,cls,place):
        super().__init__(fname, lname,place)
        self.studentid=id
        self.course=cls
    def value1(self):
        print(self.studentid,self.course)
class college(student):
    def __init__(self,fname,lname,deg,id,cls,place):
        super().__init__(fname,lname,id,cls,place)
        self.degree=deg
    def value2(self):
        print(self.degree)

x=college('deeban','deeban','b.sc',101,'cs','myd')
x.value()

    
        
        

