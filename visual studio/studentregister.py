import os
def studentregistration():
    studentid=int(input('enter student id: '))
    studentregisternumber=int(input('enter studentregisternumber: '))
    studentname=input('enter studentname: ')
    return studentid,studentregisternumber,studentname
def studentmarkdetail():
    tamil=int(input('tamil: '))
    english=int(input('english: '))
    maths=int(input('maths: '))
    science=int(input('science: '))
    socialscience=int(input('social science: '))
    if(tamil>35 and english>35 and maths>35 and science>35 and socialscience>35):
        print('pass')
        total=tamil+english+maths+science+socialscience
        average=total/5
        print(total,average)
        return tamil,english,maths,science,socialscience,total,average
    else:
        print('fail')
       
def check(average):
    if(average>85):
        print('you are eligible to select bio maths')
    elif(average>75):
        print('you are eligible to select computerscience')
    elif(average>60):
        print('you are eligible to select pure science')
    else:
        print('choose other')
def login():
    username=input('username: ')
    password=input('password: ')

    if os.path.exists("studentregistration.txt"):
        with open('studentregistration.txt','r') as file:
            lines=file.readlines()
            for x in lines:
                username1=x.split()[0]
                password1=x.split()[1]
                print(username,password,username1,password1)
                if(username1==username and password1==password):
                    print('login successful')
                    studentid=x.split()[0]
                    studentregisternumber=x.split()[1]
                    studentname=x.split()[2]
                    tamil=x.split()[3]
                    english=x.split()[4]
                    maths=x.split()[5]
                    science=x.split()[6]
                    socialscience=x.split()[7]
                    return
                
            else:
                print('give a valid username or password')  


def reg(studentid,studentregisternumber,studentname,tamil,english,maths,science,socialscience,total,average):
    f=open('studentregistration.txt','a')
    f.write('\n')
    f.write(str(studentid))
    f.write('\t')
    f.write(str(studentregisternumber))
    f.write('\t')
    f.write(studentname)
    f.write('\t')
    f.write(str(tamil))
    f.write('\t')
    f.write(str(english))
    f.write('\t')
    f.write(str(maths))
    f.write('\t')
    f.write(str(science))
    f.write('\t')
    f.write(str(socialscience))
    f.write('\t')
    f.write(str(total))
    f.write('\t')
    f.write(str(average))



c='d'
while(c=='d'):
   i=int(input('enter the value: '))
   if(i==1):
       a,b,c1=studentregistration()
       print('successfully registered')
       d,e,f,g,h,j,k=studentmarkdetail()
       check(k)
       reg(a,b,c1,d,e,f,g,h,j,k)
       print('your mark detail')
   elif(i==2):
       login()
      
   else:
       print('select a valid i value')
      
c=input('if you want to continue click d: ')


 

                    

                    
            
                    









