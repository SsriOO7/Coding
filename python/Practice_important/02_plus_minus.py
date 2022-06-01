# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with  places after the decimal.

def plusMinus(arr):
    pos=0
    neg=0
    zero=0
    for i in arr:
        if i>0:
            pos+=1
        elif i<0:
            neg+=1
        else:
            zero+=1
    print(round((pos/len(arr)),6))
    print(round((neg/len(arr)),6))
    print(round((zero/len(arr)),6))     
       
     # rounds off to the given number of digits and returns the floating-point number      
    
    
n=int(input())
# The Python strip() method removes any spaces or specified characters at the start and end of a string


arr=list(map(int, input().rstrip().split()))  #The split() method splits a string into a list

# The rstrip() method returns a copy of the string by removing the trailing characters specified as argument
# Python's map() is a built-in function that allows you to process and
# transform all the items in an iterable without using an explicit for loop


plusMinus(arr)