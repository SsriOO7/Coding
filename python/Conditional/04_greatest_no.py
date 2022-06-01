a=int(input("Enter any no\n"))
b=int(input("Enter any no\n"))
c=int(input("Enter any no\n"))
d=int(input("Enter any no\n"))
if a>b and a>c and a>d:
    print ("This is the greatest number\n ",a)
elif b>a and b>c and b>d:
    print ("This is the greatest number\n",b)
elif c>a and c>b and c>d:
    print ('This is the greatest number \n',c)
else:
    print ("This is the greatest no\n",d)