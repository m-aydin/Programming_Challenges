#s=d/t - tdddss/e


#Imports
import launcher

#Global Variables
vars=[]

#Main Program
vars=input('Input In Form: "s,d,t", Leaving Unknowns As Variables: ').split(",")

if vars[0] == "s":
  vars[0]=int(vars[1])/int(vars[2])
  print("Speed: "+str(vars[0]))
if vars[1] == "d":
  vars[1]=int(vars[0])*int(vars[2])
  print("Distance: "+str(vars[1]))
if vars[2] == "t":
  vars[2]=int(vars[1])/int(vars[0])
  print("Time: "+str(vars[2]))
launcher.menu_select()