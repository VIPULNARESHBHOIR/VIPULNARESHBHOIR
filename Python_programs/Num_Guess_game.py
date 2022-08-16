import random
number =random.randint(50,80)
i=0
print("guess  the number{range 50 to 80}: ")
while(i<8):
      guess=int(input())
      if (guess == number):
          print("\t\t************")
          print("\t\t  YOU WON")
          print("\t\t************")
          break
      elif(guess>=(number+6)):
          print("you guessed too high")
          print("Guess Again:")
      elif(guess <= (number-6)):
           print("you guessed too low")
           print("Guess Again:")
      elif(guess <= (number+6) and  guess >=(number-6)):
           print("you closed to the ans.")
           print("Guess Again:")
      i=i+1
if(i==8):
    print("\t\t_____________")
    print("\t\t You Loss")
    print("\t\t_____________")
      