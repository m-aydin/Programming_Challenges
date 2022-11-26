#C U B E - Boxy


#Imports
import launcher

#Global Variables
vars=[]

#Main Program
vars=input('Input Lengths In Form: "l,w,h" ,Leaving Out Length If Area Desired: ').split(",")

if len(vars) == 2:
  print("Area: "+str(int(vars[0])*int(vars[1])))
else:
  print("Volume: "+str(int(vars[0])*int(vars[1])*int(vars[2])))
launcher.menu_select()