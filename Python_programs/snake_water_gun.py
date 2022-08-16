# creating a function 
def Game():
    #making a list and taking a user input
    list1=["SNAKE","WATER","GUN"]
    k=int(input("YOU:"))
    user=list1[k]
    print("USER:",user)

    #taking a computer input       
    rad=random.choice(list1)
    print("comp:",rad)

    #declaring WINNER!
    if (user==rad):
        print("\t\t TIE")
    elif ((user=="SNAKE" and rad=="WATER") or (user=="GUN" and rad=="SNAKE") or (user=="WATER" and rad=="GUN")):
        print("\t\t***YOU WIN***")
    else:
        print("\t\tYOU LOSS")
    Game()

#importing random module
import random
print("\t\tclick: 0. SNAKE 1.WATER 2.GUN::")
Game()