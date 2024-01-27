def management():
    employeeid=int(input('enter your employee id: '))
    employeename=input('enter your name: ')
    designation=input('enter your designation: ')
    return employeeid,employeename,designation



employeeid,employeename,designation=management()
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
elif(designation=='tester'):
     salary=40000

     print('your designation: ',designation,salary)
else:
      print('give a valid designation')

f=open('management.txt','a')
f.write('\n')
f.write(str(employeeid))
f.write('\t')
f.write(employeename)
f.write('\t')
f.write(designation)
f.write('\t')
f.write(str(salary))

'''

f=open('management.txt','r')
r=f.read()
sn=r.split('\n')
for x in sn:
    st=x.split('\t')
    for std in st:
        if(std=='java developer'):
            print(st)




    
    
    

    