#Guessing Game Reversed - Get to trolling!


#Imports
import launcher

#Constants
IS_DEBUG=False
RANGE=100

#Global Variables
user_input=""
computer_input=0
computer_bound=[0,RANGE]
tries=0

#Main Program
computer_input=int(abs(computer_bound[0]-computer_bound[1])/2)

while True:
  tries+=1
  print("Computer Guess: "+str(computer_input))
  if IS_DEBUG:
    print(computer_bound)
  user_input=input("Input h For Too High, l For Too Low, And g For Got It: ")
  print("\n")

  if user_input == "h":
    computer_bound[1]=computer_input
    computer_input=int(computer_bound[0]+(abs(computer_bound[0]-computer_bound[1])/2))
  elif user_input == "l":
    computer_bound[0]=computer_input
    computer_input=int(computer_bound[1]-(abs(computer_bound[0]-computer_bound[1])/2))
  else:
    break
print("It Took "+str(tries)+" Tries For The Computer To Guess Your Number")
launcher.menu_select()