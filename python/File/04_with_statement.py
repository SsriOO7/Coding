with open("another.txt","r") as f:
    a=f.read()
print(a)

with open("another.txt",'w')as f:
    b=f.write("Moshimosh")
print(b)

with open("another.txt",'r') as f:
    c=f.read()
print(c)