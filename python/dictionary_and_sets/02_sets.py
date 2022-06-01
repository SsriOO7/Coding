a={1,2,3,1}
print (type(a))
print (a) 
# sets is not repretative item 
b= set() # Empty set
print (type(b))
# adding an value into a set
b.add(4)
b.add(5)
b.add(5)
print (b)
# can not add list in set 
# we can add tuple, because it is immutable datatype 
# we can not add dictionary
# set is not indexed and set can not contain duplicate values
b.add((4,5,6)) # Tuple in set
print (b)
print (len(b)) # find the length of the set
b.remove(4) #remove no from the set
print (b)
print (b.union({8,11})) #union value 
print (b.intersection({5})) #common value 
c = {18,"18"} # Both datatype are different 
print (c)