from abc import ABC, abstractmethod
#Abstract Class

class Bank(ABC):
   def bank_info(self):
       print("Welcome to bank")
   @abstractmethod
   def interest(self):
       
       pass
#Sub class/ child class of abstract class
class SBI(Bank):
      def interest(self):
          print("5 percentage")

s= SBI()
s.bank_info ()
s.interest()




""" 
from abc import ABC, abstractmethod
#Abstract Class
class Bank(ABC):
   def bank_info(self):
       print("Welcome to bank")
   @abstractmethod
   def interest(self):
       pass
#Sub class/ child class of abstract class
class SBI(Bank):
   def interest(self):
       print("hi")
   def balance(self):
       print("Balance is 100")
s= SBI()
s.bank_info()
s.balance() """

""" 
from abc import ABC, abstractmethod
#Abstract Class
class Bank(ABC):
   def bank_info(self):
       print("Welcome to bank")
   @abstractmethod
   def interest(self):
       "Abstarct Method"
       pass
#Sub class/ child class of abstract class
class SBI(Bank):
   def balance(self):
       print("Balance is 100")
class Sub1(SBI):
   def interest(self):
       print("In sbi bank interest is 5 rupees")
s= Sub1()
s.bank_info ()
s.balance()
s.interest() """


""" 
from abc import ABC, abstractmethod
class One(ABC):
   @abstractmethod
   def calculate(self, a):
       pass
class Square(One):
   def calculate(self, a):
       print("square: ", (a*a))
class Cube(One):
   def calculate(self, a):
       print("cube: ", (a*a*a))
s = Square()
c = Cube()
s.calculate(2)
c.calculate(2) """

