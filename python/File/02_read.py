file=open("another.txt",'r') # OR you can write open("anothr.txt") because by default it takes 'r'
# data=file.read()  ############## we cannot use read method more than ones
data=file.read(3)
print(data)
file.close