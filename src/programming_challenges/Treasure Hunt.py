#Treasure Hunt - Hunt For Treasure


#Imports
import random
import math
import launcher

#Functions
def match_init(search_area):
  global SYMBOLS
  global AREA_SIZE
  global treasure_coords
  current_row=[]

  treasure_coords.append(str(random.randint(0,(AREA_SIZE))))
  treasure_coords.append(str(random.randint(0,(AREA_SIZE))))
  
  for row in range(0,AREA_SIZE):
    for column in range(0,AREA_SIZE):
      if (str(row+1) == treasure_coords[0]) and (str(column+1) == treasure_coords[1]):
        current_row.append(SYMBOLS[0])
      else:
        current_row.append(SYMBOLS[1])
        
    search_area.append(current_row)
    current_row=[]

def disp_heat(user_input):
  global TREASURE_DETECT_RANGE
  global IS_CHEAT
  global treasure_coords
  distance=0
  
  user_input=user_input.split(",")
  distance=math.trunc(math.sqrt((abs(int(treasure_coords[0])-int(user_input[0])))**2+(abs(int(treasure_coords[1])-int(user_input[1])))**2))
  
  if distance <= TREASURE_DETECT_RANGE:
    print("Hot\n\n")
  elif distance <= (TREASURE_DETECT_RANGE*2):
    print("Warm\n\n")
  else:
    print("Cold\n\n")

  if IS_CHEAT:
    print("Treasure Coordinates (Cheats Active): "+str(treasure_coords))
    print("Distance (Cheats Active): "+str(distance))
    print("Inputted Coords (Cheats Active): "+str(user_input)+"\n\n")

#Constants
AREA_SIZE=10
SYMBOLS=["1","0"]
TREASURE_DETECT_RANGE=2
IS_CHEAT=False

#Global Variables
search_area=[]
treasure_coords=[]
user_input=""

#Main Program
match_init(search_area)
while user_input.split(",") != treasure_coords:
  user_input=input("Input Treasure Coords As x,y: ")
  if user_input.split(",") != treasure_coords:
    print("Failure")
    disp_heat(user_input)
print("Success")
launcher.menu_select()