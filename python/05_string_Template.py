# To write template
a= input ("Enter name\n")
b=input("Enter date dd/mm/yy\n")
letter= ''' Dear Name
                 You are selected 
                 Date'''
letter=letter.replace("Name", a)
letter=letter.replace("Date", b)
print (letter)
