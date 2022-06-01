def percentage(marks):
    p=(sum(marks)/i)
    return p

# a=1
# y=0
# while a>0:
#     x=list(input("Enter number"))
#     for i in x:
#         y=y+int(i) 
#     n=input("continue y/n\t")
#     if n=="n":
#         a=0
# print (y)

mark=0
i=1
y=1
for i in range (1,mark+1):
    a=input("you want to continue y/n\t")
    if a=="y":
        d=list(input(("Enter your marks \t")))
        for z in d:
            mark=mark+int(z)
            y+=1
            
    else:
        print ("You are done, Here is your result ")

b=percentage(mark)
print(b)
