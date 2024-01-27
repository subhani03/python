def a():
    n=1
    while n<10:
        val=n*n*n
        yield val
        n+=1
x=a()
for i in x:
    print(i)