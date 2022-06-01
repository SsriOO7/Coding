a=1
b=0
total_marks=0
while a<=3:
   Stu_marks=int(input("Enter your marks\n"))
   if Stu_marks>33:
       print ("Pass in",a,"exam")
   else:
        print("Fail in ",a,"exam")
   a+=1

   total_marks+=Stu_marks
b=a-1
if total_marks/b>=40.0:
    print ("Student score 40% and passed the exam")
else:
    print ("Student score less than 40% and failed the exam")