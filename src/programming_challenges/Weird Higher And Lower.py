#Weird Higher And Lower - Weïrd


#Imports
import random
import time
import launcher

#Functions

#Constants
IS_DEBUG=True
RANGE=13
NUMS=10

#Global Variables
sequence=random.sample(range(1,RANGE+1),NUMS)
user_input=""
pos=0
tries=0
lives=2

#Main Program
print("Sequence: "+str(sequence)+"\nRemember This")
time.sleep(2)
print("\n"*100)


while True:
  if ((tries+1) == NUMS) or (lives == 0):
    break
  
  if pos == 0:
    print("First Num: "+str(sequence[pos]))
  else:
    print("Next Num: "+str(sequence[pos]))
  
  while True:
    if IS_DEBUG:
      print("Sequence: "+str(sequence))
    user_input=input("Higher(h), Or Lower(l): ").lower()
    if (user_input == "h") or (user_input == "l"):
      break
    print("Invalid Input\n")
    
  if ((user_input == "h") and (sequence[pos] >= sequence[pos+1])) or ((user_input == "l") and (sequence[pos] <= sequence[pos+1])):
    print("Correct\n")
  else:
    print("Incorrect\n")
    lives=lives-1
  pos+=1
  tries+=1

if tries == 0:
  print("You Lose")
else:
  print("You Win")
launcher.menu_select()