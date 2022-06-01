# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range (0,n):
    string = input()
    length = len(string)
    for j in range (length):
        if j%2==0:
            s=string[j]
            print (s,end="")
        else:
            if j!=length:
                s=string[j+1]
                print(s,end="")
                
        