def grea_num(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            return num1
        else:
            return num3
    elif num2>num1:
        if num2>num3:
            return num2 
        else:
            return num3

num1=int(input(f"enter first number"))
num2=int(input(f"enter second number"))
num3=int(input(f"enter third number"))
num=grea_num(num1,num2,num3)
print ("The greatest number is",num)
