#DOB In Seconds - Pob


#Imports
from datetime import date
import launcher

#Global Variables
user_input=""

#Main Program
user_input=input("Input DOB As year/month/day: ").split("/")
print("Seconds You Have Lived For: "+str(int((date.today()-date(int(user_input[0]),int(user_input[1]),int(user_input[2]))).total_seconds())))
launcher.menu_select()