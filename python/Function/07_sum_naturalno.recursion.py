
def fun_recusrion(num):
    i=num
    if i==1 or i==0:
        return 1
    else:
        i=i+fun_recusrion(num-1)
        return i

num=int(input("Enter any natural number"))     
i=fun_recusrion(num)
print (i)