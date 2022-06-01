text = input("Enter your text\n")
if ("make a lot of money" in text):
    print ("It is is a spam message ")
elif ("buy now" in text):
    print ("it is a spam message ")
elif ("subscribe now" in text):
    print ("It is a spam message ")
else:
    print ("it is not a spam message ")


# OR

text =input("Enter your txt \n")
if "make a lot of money" in text:
    spam=True
elif "click this" in text:
    spam=True
elif "subscribe this" in text:
    spam =True
else:
    spam=False

if(spam):
    print ("This message is a spam")
else:
    print ("This message is not a spam")
