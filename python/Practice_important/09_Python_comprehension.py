# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.


n=int(input())
marksheet=[[input(),float(input())] for _ in range(n)]

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1] ########set element is used to convert any of the iterable to sequence of iterable elements with distinct elements,
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
# print('\n'.join([a----(--VAriable--) for a,b in sorted(marksheet)----(===For Statement===) if b == second_highest------(==Condition===)]))
# join function is use to join given object like '\n' 