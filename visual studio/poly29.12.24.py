'''
class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def value(self):
        print(f'firstname of the person{self.fname}.last name of the person{self.lname}')
    def hobbie(self):
        print('book reading')
class employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def value(self):
        print(f'first name of the employee{self.fname}.last name of the employee{self.lname}')
    def hobbie(self):
        print('badmiton')
    
x=person('subha','deeban')
y=employee('subi','karthi')
for z in(x,y):
    z.value()
    z.hobbie()

class icecream:
    def __init__(self,flavour):
        self.flavour=flavour
    def value(self):
        print(f'flavour of the icecream  {self.flavour}')
    def company(self):
        print('ibaco')
class chocolate:
    def __init__(self,flavour):
        self.flavour=flavour
    def value(self):
        print(f'flavour of the chocolate  {self.flavour}')
    def company(self):
        print('kitkat')
a=icecream('vennila')
b=chocolate('strawberry')
for x in(a,b):
    x.value()
    x.company()
'''
class rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def value(self):
        print(f'this is a height {self.height} and width  {self.width}  of a circle')
class square:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def value(self):
        print(f'this is a height  {self.height}  and width {self.width} of a square')
class triangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def value(self):
        print(f'this is a height {self.height} and width {self.width} of a triangle')
class trapezium:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def value(self):
        print(f'this is a height {self.height} and width {self.width} of a trapezium')
class rhombus:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def value(self):
        print(f'this is a height {self.height} and width {self.width} of rhombus')


a=rectangle(30,15)
b=square(12,12)
c=triangle(9,13)
d=trapezium(25,40)
e=rhombus(35,50)

for z in (a,b,c,d,e):
    z.value()
            
        
