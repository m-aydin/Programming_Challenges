#Alphabet - Think fast chucklenuts!


#Imports
from datetime import datetime
import launcher

#Global Variables
time=["","",""]
alphabet="abcdefghijklmnopqrstuvwxyz"
user_input=""

#Main Program
time[0]=datetime.now()
user_input=input("Input Alphabet NOW: ").lower()
time[1]=datetime.now()
if user_input == alphabet:
  time[2]=time[1]-time[0]
  print("Time Took: "+str(time[2]))
else:
  print("Incorrect Alphabet")
launcher.menu_select()