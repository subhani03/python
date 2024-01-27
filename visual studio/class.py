'''
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('function')
    def student1(self):
        print(self.name,self.age)  
c=student('subha',21)
c.student1()  
'''
class r():
    a=5
    def func(self):
        print('function')
c=r()
b=r()
print(b.a)
b.a=7
c.func()
print(b.a)
b.func()
print(c.a)





class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')

# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')

# Child class
class SportsCar(Car):
    def sports_car_info(self):
        print('Inside SportsCar class')

# Create object of SportsCar
s_car = SportsCar()

# access Vehicle's and Car info using SportsCar object
s_car.Vehicle_info()
s_car.car_info()
s_car.sports_car_info()

    

    
        
    