num=int(input("Enter nay no\n"))
prime=True
for i in range(2,num):
    if num%i==0:
        prime = False
        break
if prime:
     print("This is a prime no")
else:
    print ("It is not a prime no")