#Guessing Game - Get to guessing!


#Imports
import random
import launcher

#Constants
RANGE=100

#Global Variables
user_input=""
number=random.randint(0,RANGE)
tries=0

#Main Program
while True:
  tries+=1
  user_input=int(input("Input Number: "))
  
  if user_input == number:
    print("got it\n")
    break
  elif user_input > number:
    print("too high\n")
  else: 
    print("too low\n")
print("It Took "+str(tries)+" Tries For You To Guess The Number")
launcher.menu_select()