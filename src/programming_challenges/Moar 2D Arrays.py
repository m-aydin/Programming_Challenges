#Moar 2D Arrays - 3D Arrays When?


#Imports
import random
import launcher

#Functions
def array_init(num_array):
  global ARRAY_SIZE
  global NUM_RANGE
  current_row=[]
  random_num=0

  for row in range(0,(ARRAY_SIZE)):
    for column in range(0,(ARRAY_SIZE)):
      random_num=random.randint(0,NUM_RANGE)
      current_row.append("\033[1;37;"+str((random_num+40))+"m "+str(random_num))
    num_array.append(current_row)
    current_row=[]
    
  return(num_array)

def array_disp(num_array):
  disp_array=""
  current_row=""
  
  for row in range(0,(ARRAY_SIZE)):
    for column in range(0,(ARRAY_SIZE)):
      current_row+=str(num_array[row][column])
    disp_array+=current_row+"\n"
    current_row=""
    
  print(disp_array+"\033[0m")

#Constants
ARRAY_SIZE=10
NUM_RANGE=7

#Global Variables
num_array=[]

#Main Program
num_array=array_init(num_array)
array_disp(num_array)
launcher.menu_select()