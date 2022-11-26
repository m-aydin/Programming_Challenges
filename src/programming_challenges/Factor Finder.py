#Factor Finder - Who be part of ye


#Imports
import launcher

#Global Variables
user_input=""
factors=[]

#Main Program
user_input=int(input("Input Number: "))
for pos in range(1,user_input+1):
  if (user_input % pos == 0) and (pos != 1):
    factors.append(pos)
print("Factors: "+str(factors))
launcher.menu_select()