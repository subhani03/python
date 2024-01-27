def studentinput():
    registernumber=int(input('enter your register number: '))
    name=input('enter your name: ')
    age=int(input('enter your age: '))
    mark1=int(input('ebter your m1 mark: '))
    mark2=int(input('ebter your m2 mark: '))
    mark3=int(input('ebter your m3 mark: '))
    mark4=int(input('ebter your m4 mark: '))
    mark5=int(input('ebter your m5 mark: '))
    return registernumber,name,age,mark1,mark2,mark3,mark4,mark5
def cal(mark1,mark2,mark3,mark4,mark5):
    if(mark1>35 and mark2>35 and mark3>35 and mark4>35 and mark5>35):
        total=mark1+mark2+mark3+mark4+mark5
        average=total/5
        print('you are pass',total,average)
    else:
        print('you are fail')
    return total,average
def selection(average):
    if(average>80):
        print('you are eligible to choose bio maths')
    elif(average>70):
        print('you are eligible to choose computer science')
    else:
        print('choose other course')
registernumber,name,age,mark1,mark2,mark3,mark4,mark5=studentinput()
total,average=cal(mark1,mark2,mark3,mark4,mark5)
selection(average)
f=open('studentfile.txt','a')
f.write('\n')
f.write(str(registernumber))
f.write('\t')
f.write(name)
f.write('\t')
f.write(str(age))
f.write('\t')
f.write(str(mark1))
f.write('\t')
f.write(str(mark2))
f.write('\t')
f.write(str(mark3))
f.write('\t')
f.write(str(mark4))
f.write('\t')
f.write(str(mark5))
f.write('\t')
f.write(str(total))
f.write('\t')
f.write(str(average))

f=open('studentfile.txt','r')
r=f.read()
sn=r.split('\n')
for sn1 in sn:
    st=sn1.split('\t')
    for std in st:
        if std=='bio maths':
            print(st)




        
