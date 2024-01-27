import os
def login(username,password):
    if os.path.exists('studentlogin.txt'):
        with open('studentlogin.txt','r') as file:
            lines=file.readlines()
            for x in lines:
                username,password=x.split()
                if(username==username and password==password):
                    print('login successful')
                    return
                else:
                    print('invalid username or password')
login("joe","joe")