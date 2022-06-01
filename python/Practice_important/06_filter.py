list_1=[1,2,3,6,5,1,5]
def is_greater(num):
    return num>5

greater_than=list(filter(is_greater,list_1))
print (greater_than)