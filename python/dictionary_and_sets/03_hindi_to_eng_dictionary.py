my_dict = {
    "pankha" : "fan",
    "dabba" : "box",
    "vastu" : "item" 
}
print (my_dict.keys())
my_opt=input("write any above option to find english meaning\n ")
print ("The meaning of your word is-",my_dict.get(my_opt))