#Jokey - Hahahaa


#Imports
import launcher
import time

#Functions
def rainbow(text):
  global LOOP_COUNT
  global SLEEP
  cur_text=""
  count=0
  offset=0

  
  print("\n"*100)
  while True:
    if count == LOOP_COUNT:
      print("\033[1;31;5mSorry\nrepl process died unexpectedly: exit status 1\033[0m")
      launcher.menu_select()
    for pos in range(0,len(text)):
      if offset == 8:
        offset=0
      cur_text=cur_text+"\033[1;"+str(30+offset)+";"+str(47-offset)+"m"+text[pos]
      offset+=1
    print(cur_text+"\033[1;30;40m")
    cur_text=""
    count+=1
    time.sleep(SLEEP)

#Constants
LOOP_COUNT=300
SLEEP=0.02
    
#Global Variables

#Main Program
input("Why Did The Chicken Cross The Road?\n\n")
rainbow("Because RAINBOW!!!!11!")