

class person:
    def __init__(self, fname, lname, a, dob, eml):
        self.firstname = fname
        self.lastname = lname
        self.age = a
        self.dateofbirth = dob
        self.email = eml

    def value(self):
        print(self.firstname, self.lastname, self.age, self.dateofbirth, self.email)


class employee(person):
    def __init__(self, fname, lname, a, dob, eml, empid, empname, empsal, dev):
        super().__init__(fname, lname, a, dob, eml)
        self.employeeid = empid
        self.employeename = empname
        self.salary = empsal
        self.developer = dev

    def value(self):
        super().value()
        print(self.employeeid, self.employeename, self.salary, self.developer)


c = employee('subhani', 'panneer', '21', '03/01,2002', 'sg@gmail.com', '101', 'subha', '30000', 'python developer')
c.value()
        
