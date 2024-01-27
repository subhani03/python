"""
from abc import ABC,abstractmethod
class login(ABC):
    def login_info(self):
        print('welcome your page')
    @abstractmethod
    def reg(self):
        pass
class student(login):
    def reg(self):
        print('subhani deeban')
a=student()
a.login_info()
a.reg()
"""
from abc import ABC,abstractmethod
class person(ABC):
    def person_info(self):
        print('welcome')
    @abstractmethod
    def details(self):
        pass
class details1(person):
    def details(self):
        print('hello world')

x=details1()
x.person_info()
x.details()


