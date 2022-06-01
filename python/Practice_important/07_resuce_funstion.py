from functools import reduce

list1=[1,2,3,4]
num=reduce(lambda x,y:x+y,list1)
print(num)

a=0
for i in list1:
    a=a+i

print(a)


######################## Reduce function reduces our workload by using this we can save our time 
