# rock paper scissor game

import random

def game_win(comp,you):
    if comp==you:
        return None # If both have same sign then it will be a tie
    elif comp=="r":
        if you=="p":
            return True
        elif you=="s":
            return False
            
    elif comp=="p":
        if you=="s":
            return True
        elif you=="r":
            return False
            
    elif comp=="s":
        if you=="r":
            return True
        elif you=="p":
            return False

print ("computer turn: Rock(s),Paper(p),Scissor(s)")
ran=random.randint(1,3)

if ran==1:
    comp="r"
elif ran==2:
    comp="p"
elif ran==3:
    comp="s"

you=input("Your turn: Rock(s),Paper(p),Scissor(s)\t")
a=game_win(comp,you)

print(f"Computer choose {comp}")
print(f"You choose {you}")

if a==None:
    print ("\nIt's a tie")
elif a:
    print ("\nYou win")
else:
    print ('\nyou loose')

            
