def remove_and_strip(string,word):
    new_string=string.replace(word,"")
    return new_string.strip() #Strip function is used to remove spaces at the begining and at the end of the string 

word=("    Eat an apple a day     ")
print (word)
n=remove_and_strip(word,"Eat")
print(n)