#Subtraction Game - 21 but in reverse.


#Imports
import random
import launcher

#Functions

#Constants
RANGE=[20,30]
PICK_RANGE=[1,3]

#Global Variables
current_number=random.randint(RANGE[0],RANGE[1])
user_input=""
computer_input=0

#Main Program
while True:
  print("Current Number: "+str(current_number))
  while True:
    user_input=int(input("Input Amount To Remove: "))
    if user_input in range(PICK_RANGE[0],PICK_RANGE[1]+1):
      break
    else:
      print("Invalid Input\n")
        
  computer_input=random.randint(PICK_RANGE[0],PICK_RANGE[1])
  current_number=current_number-user_input-computer_input
  
  if (current_number+computer_input) <= 0:
    print("You Lose")
    break
  elif (current_number) <= 0:
    print("You Win")
    break

  print("Computer Pick: "+str(computer_input)+"\n")
launcher.menu_select()