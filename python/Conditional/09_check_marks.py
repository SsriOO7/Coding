a=int(input("Enter your marks\n"))
i=1
while i==1:
    if a>100:
        print("Invalid number")
        i=0
        break
    if a>=90 :
        print ("your grade if O")
    elif a>=80:
        print ("Your grade is A")
    elif a>=70:
        print ("Your grade is B")
    elif a>=60:
        print ("Your grade is C")
    elif a>=50:
        print ("Your grade is D")
    else:
        print("You fail the exam")
    i=0