#Pyramid - Triangle


#Imports
import math
import launcher

#Functions
def drawstars(spaces,stars):
  return(" "*spaces+"*"*stars)

def draw_pyramid(base_size):
  loop_len=int((base_size+1)/2)
  output=""

  for pos in range(0,loop_len):
    padding=int(math.trunc(base_size/2)-pos)
    cur_seq=2*(pos+1)-1
    output+="\n"+drawstars(padding,cur_seq)
  return(output)

#Global Variables
user_input=""

#Main Program
user_input=input("Enter Pyramid Base Size: ")
print(draw_pyramid(int(user_input)))
launcher.menu_select()