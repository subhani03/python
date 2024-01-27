'''
class employee:
    def __init__(self,empid,empname,empdesignation,empsalary):
        self.empid=empid
        self.empname=empname
        self.empdesignation=empdesignation
        self.empsalary=empsalary
    def value(self):
        print(f'employee id: '+self.empid)
        print('employee name: '+self.empname)
        print('employeedesignation: '+self.empdesignation)
        print('empsalary: '+self.empsalary)
a=employee('1','subhani','python developer','30000')
b=employee('2','subashini','fullstack developer','60000')
c=employee('3','deeban','sql developer','20000')
a.value()
b.value()
c.value()
'''
class hod:
    def __init__(self,department,college):
        self.department=department
        self.college=college
    def value(self):
        print('head of the department: '+self.department)
        print('head of the department: '+self.college)
class staff:
    def __init__(self,staffname):
        self.staffname=staffname
    def value1(self):
        print('staffname : '+self.staffname)
class student:
    def __init__(self,studentname):
        self.studentname=studentname
    def value2(self):
        print('staffname : '+self.studentname)

a=hod('computerscience','Daac')
a.value()
b=staff('vv')
b.value1()
c=student('subi')
c.value2()
  

        


