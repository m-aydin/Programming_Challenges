#Array O Names - Ye Be E


#Imports
import launcher

#Functions
def clear_val(val,list):
  while val in list:
    list.remove(val)
  return(list)
  
#Global Variables
name_array=[]

#Main Program
while True:
  user_input=input("Enter Name: ")
  if user_input == "exit":
    break
  else:
    name_array.append(user_input)

for cur_name in name_array:
  if name_array.count(cur_name) > 1:
    print(str(name_array.count(cur_name)-1)+" Duplicates Of "+cur_name)
    name_array=clear_val(cur_name,name_array)
launcher.menu_select()