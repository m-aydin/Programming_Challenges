#CodeBreaker - Guess A 4 Digit Code.


#Imports
import random
import time
import launcher

#Functions
def code_gen(length,is_debug=False):
  code=""
  for pos in range(0,4):
    code+=str(random.randint(0,9))
  if is_debug:
    print("Code: "+code)
  return(code)

def any_in_str(guess,code):
  for pos in guess:
    if pos in code:
      return(True)
  return(False)

#Constants
GUESS_LIMIT=12

#Global Variables
code=code_gen(4)
guesses=0
guess=""
pos_disp=""

#Main Program
while guesses < 12:
  guess=input("\n\nInput Guess For Code: ")
  if guess == code:
    break
  
  elif (guess != code) and (not any_in_str(guess,code)):
    print("Incorrect Guess")
    
  elif any_in_str(guess,code):
    for pos in enumerate(guess):
      if (pos[1] in code) and (pos[1] == code[pos[0]]):
        pos_disp+="C"
        
      elif pos[1] in code:
        pos_disp+="P"
        
      else:
        pos_disp+="I"
  print("\nC=Correct Digit In Correct Position\nP=Correct Digit In Wrong Position\nI=Incorrect Digit\n\n"+pos_disp+" :Digit Info\n"+guess+" :Your Guess\n")
  
  pos_disp=""
  guesses+=1
  print(str(GUESS_LIMIT-guesses)+" Guesses Left")
  
if guesses < 12:
  print("\n\nYou Won! With "+str(GUESS_LIMIT-guesses)+" Guesses Left")
else:
  print("\n\nYou Lost!")
  time.sleep(2)
  print("\033[1;31;5mget gud scrub\nrepl process died unexpectedly: exit status 1")
  time.sleep(1.5)
  print("\033[1;37;5mlol")
launcher.menu_select()