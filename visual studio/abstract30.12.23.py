''' 
from abc import ABC,abstractmethod
class bank(ABC):
    def bank_details(self):
        print('welcome')
    @abstractmethod
    def interest(self):
        pass
class indian(bank):
    def customer(self):
        print('customer details')
class iob(indian):
    def interest(self):
        print('bank customer details')

a=iob()
a.bank_details()
a.interest()
'''



from abc import ABC, abstractmethod
class head(ABC):
    def head_details(self):
       print('head of our company')
    @abstractmethod
    def value(self):
       pass
class hr(head):
    def humanresource(self):
       print('hr of our company')
class tl(hr):
    def teamleader(self):
       print('tl of our company')
class worker(tl):
    def value(self):
       print('worker details')

x=worker()
x.head_details()
x.humanresource()
x.teamleader()
x.value()
   

  
 

