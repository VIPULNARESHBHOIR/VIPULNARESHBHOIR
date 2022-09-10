import random

def Game():
    number =random.randint(50,80)
    NO=number
    i=1
    print("\nguess  the number{range 50 to 80}: ")
    while(i<8):
        guess=int(input())
        if (guess == number):
            if(i==1):
                print("\t**** YUhuu WONDERING ****\n")
            elif(i==2):
                print("\t\t**** Very NICE ****\n")
            elif(i==3):
                print("\t**** Beautiful ****\n")
            elif(i==4):
                print("\t**** GOOD ****\n")
            
            print("\t\t************")
            print("\t\t  YOU WON")
            print("\t\t************")
            break
        elif(guess>=(number+5)):
            print("you guessed too high")
            print("Guess Again:")
        elif(guess <= (number-5)):
            print("you guessed too low")
            print("Guess Again:")
        elif(guess <= (number+5) and  guess >=(number-5)):
            print("you closed to the ans.")
            print("Guess Again:")
        i=i+1
    if(i==8):
       print("\t\t_____________")
       print("\t\t You Loss")
       print("\t\t_____________")
       print("\n\tNO:",NO)
       
    Game()

print("_______PLAY______\n\n")
Game()