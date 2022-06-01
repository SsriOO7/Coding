def square(a):
    return a*a

def cube(b):
    return b*b*b

funct=[square,cube]
for i in range (5):
    value=list(map(lambda x:x(i),funct))
    print (value)