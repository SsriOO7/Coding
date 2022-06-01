i=1
t=[]
while i!=0:
    b=input("want to continue y/n\n")
    if b=="n":
        i=0
        break
    a=input("write any fruit name\n")
    t.append(a)
    tup=tuple(t)
            
print (tup)