my_dict = {
    "FAst" : "In a quick way",# Key : Value
    "tony" : "is a coder",
    "Marks" : [1,2,3], # List inside dictionary
    "Another_dict" : {"tony" : "Player"} #Another dictionary inside primary dictionary
}
print (my_dict['FAst'])
print (my_dict['tony'])
print (my_dict['Marks'])
print (my_dict['Another_dict']['tony'])
my_dict['Marks'] =  [2,3] #to change dictionary
print (my_dict['Marks'])
print (my_dict.keys()) #To print keys of the dictionary
print (my_dict.values()) #To print values of the dictionary
print (my_dict.items()) #To print (keys,values)of every content of the dictioanry of the dictionary
update_dict = {
    "Apple" : "Banana"
}
my_dict.update(update_dict) # To update or add content in dictionary
print (my_dict)
print (my_dict.get('tony2')) # it will not throw error if there is no value, it return none  #####################################
print (my_dict.get('tony')) # it will not throw error if there is no value, it return none  #####################################
print (my_dict['tony']) # it willthrow error if there is no value  #####################################
# print (my_dict('tony2')) # it willthrow error if there is no value  #####################################
# a={} #Empty dictionary