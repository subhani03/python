def greet(name):
    def display_name():
        print('hello',name)
    display_name()
greet('ammu')

def greet():
    name='ammu'
    return lambda:'hello'+name
message=greet()
print(message())


