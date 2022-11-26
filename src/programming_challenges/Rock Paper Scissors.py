#Rock Paper Scissors - Pow!


#Imports
import random
import launcher

#Global Variables
scores=["Rock","Paper","Scissors"]
user_input=0
computer_input=0
score=0

#Main Program
while True:
  computer_input=random.randint(0,2)
  while True:
    user_input=int(input("0 For Rock, 1 For Paper, 2 For Scissors, 3 To Exit: "))
    if user_input == 3:
      launcher.menu_select()
    elif user_input in range(0,3):
      break
    print("Invalid Input")
  print("Computer Picks: "+str(computer_input))
  
  if user_input == computer_input:
    print("Tie\nScore: "+str(score)+"\n\n")
  elif ((user_input == 0) and (computer_input == 1)) or ((user_input == 1) and (computer_input == 2)) or ((user_input == 2) and (computer_input == 0)):
    score=score-1
    print("Lose\nScore: "+str(score)+"\n\n")
  elif ((user_input == 0) and (computer_input == 2)) or ((user_input == 1) and (computer_input == 0)) or ((user_input == 2) and (computer_input == 1)):
    score=score+1
    print("Win\nScore: "+str(score)+"\n\n")
