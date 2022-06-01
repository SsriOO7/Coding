numbers=[2,31,35,135,132,3,21]
number= list(map(int,numbers)) #Map function will change all the list value(String) to integer
print(number)


num=[21,51,654,1,23,5,11,3216]
square=list(map(lambda x: x*x,num)) #using lambda function we do not have to define a function
print(square)