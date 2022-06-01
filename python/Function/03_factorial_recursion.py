print ("normal technique")
def factorial_iter(num):
    product=1
    for i in range(num):
        product*=(i+1)
    return product

num=int(input("Enter any number"))
print (factorial_iter(num))

# or
print ("Factorial recursive technique") #recursion is a function which call itself again and again, It is mostly use in mathematical equation
def factorial_recursive(num): #It is directly used in mathematical formula
    if num==1 or num==0 :
        return 1
    return num * factorial_recursive(num-1) 

print (factorial_recursive(num))