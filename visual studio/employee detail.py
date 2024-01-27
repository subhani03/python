import os
from datetime import date
def reg():
    employeeid=int(input('enter your employee id: '))
    employeename=input('enter your name: ')
    designation=input('enter your designation: ')
    username=input('enter your username: ')
    password=input('enter your password: ')

    

    if(designation=='python developer'):
        salary=40000
        print('your designation: ',designation,salary )
    elif(designation=="java developer"):
        salary=50000
        print('your designation: ',designation,salary)
    elif(designation=='fullstack developer'):
        salary=60000
        print('your designation: ',designation,salary)
    elif(designation=='manager'):
        salary=70000
        print('your designation: ',designation,salary)
    else:
        print('give a valid designation')

    f=open('empdetail.txt','a')
    f.write('\n')
    f.write(str(employeeid))
    f.write('\t')
    f.write(employeename)
    f.write('\t')
    f.write(designation)
    f.write('\t')
    f.write(str(salary))
    f.write('\t')
    f.write(username)
    f.write('\t')
    f.write(password)
    
            
def log():
    username=input('enter your username: ')
    password=input('enter your password: ')
    if os.path.exists('empdetail.txt'):
        with open('empdetail.txt','r') as file:
            lines=file.readlines()
            for x in lines:
                username1=x.split()[0]
                password1=x.split()[5]
                if(username1==username and password1==password):
                    print('login successful')
                    f=open('datetime.txt','a')
                    f.write('\n')
                    f.write(username)
                    f.write('\t')
                    f.write(str(date.today()))
                
                    employeeid=x.split()[0]
                    employeename=x.split()[1]
                    designation=x.split()[2]
                    salary=x.split()[3]
                    print(employeeid,employeename,designation,salary)
                    return
                print('invalid username or password')

    


c="y"
while(c=="y"):
    i=int(input('press 1 for Registration or press 2 for Login : '))
    if(i==1):
        reg()
        print('you are successfully registered')
    elif(i==2):
        print('login')
        log()
        print(date.today())
    else:
        print('select a correct value')
    c=input("Enter the Y to contiune...? ")

