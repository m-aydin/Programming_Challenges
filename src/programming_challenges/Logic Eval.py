#Logic Eval - Logos!


#Imports
import launcher

#Global Variables
inputs=["",0,0]

#Main Program
inputs=input('Input In Form "Gate,A,B": ').split(",")

if inputs[0] == "or":
  print("Result: "+str(int(bool(int(inputs[1])) or bool(int(inputs[2])))))
elif inputs[0] == "and":
  print("Result: "+str(int(bool(int(inputs[1])) and bool(int(inputs[2])))))
elif inputs[0] == "xor":
  print("Result: "+str(int(bool(int(inputs[1])) != bool(int(inputs[2])))))
elif inputs[0] == "nand":
  print("Result: "+str(int(not(bool(int(inputs[1])) and bool(int(inputs[2]))))))
elif inputs[0] == "nor":
  print("Result: "+str(int(not(bool(int(inputs[1]))) and not(bool(int(inputs[2]))))))
launcher.menu_select()