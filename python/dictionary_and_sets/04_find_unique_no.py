i=1
t=set()
while i!=0:
    b=input("want to continue y/n\n")
    if b=="n":
        i=0
        break
    a=int(input("enter number\n"))
    t.add(a)              

print(t)