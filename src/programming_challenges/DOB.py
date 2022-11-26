#DOB - Hob


#Imports
import datetime
#from datetime import date
import launcher

#Global Variables
user_input=""
age=0

#Main Program
user_input=input("Input DOB As year/month/day: ").split("/")
if int((datetime.date.today()-datetime.date(int(user_input[0]),int(user_input[1]),int(user_input[2]))).days) >= 6570:
  print("You Can Vote")
else:
  print("You Can't Vote")
launcher.menu_select()