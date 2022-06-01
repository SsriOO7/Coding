i=1
t=[]
while i!=0:
    b=input("want to continue y/n\n")
    if b=="n":
        i=0
        break
    a=input("enter marks of student\n")
    t.append(a)              
t.sort()
print(t)