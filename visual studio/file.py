'''
import os
if(os.path.exists("file.txt")):
    os.remove("file.txt")
else:
    raise Exception("no file")


import os
if(os.path.exists('sfile.txt')):
    os.remove('sfile.txt')
else:
    raise Exception('file does not  exist')
'''
""" 
import os
if(os.path.exists('subhafile.txt')):
    os.remove('subhafile.txt')
else:
    print('file does not exist')
 """

class rules():
    a=5
    def func(self):
        print("this is function")

c=rules()
b=rules()
b.a=7
print(c.a)
c.func()
print(b.a)
b.func()
print(c.a)
