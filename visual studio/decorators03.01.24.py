def outer(x):
    def inner(y):
        return x+y
    return inner
x=outer(2)
y=x(2)
print(y)