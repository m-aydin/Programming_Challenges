#Timekeeping - Are you a proffeffsor of time?


#Imports
import datetime
import launcher

#Global Variables
time=["","",""]

#Main Program
time[0]=datetime.datetime.now()
user_input=input("Input Enter When 10 secs passed")
time[1]=datetime.datetime.now()
time[2]=abs(10-(time[1]-time[0]).total_seconds())
print("How Far From 10 Seconds: "+str(round(time[2],3)))
launcher.menu_select()