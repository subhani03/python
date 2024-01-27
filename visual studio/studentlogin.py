'''
def login():
    username=input('enter username: ')
    password=input('enter your password: ')
    return username,password

username,password=login()

f=open('studentlogin.txt','a')
f.write('\n')
f.write(username)
f.write('\t')
f.write(password)
'''
f=open('studentlogin.txt','r')
r=f.read()
sn=r.split('\n')
for x in sn:
    st=x.split('\t')
    for std in st:
        if(std=='joe'):
            print(st)





