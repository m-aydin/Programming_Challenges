#Draw Stars - Stars in your eyes

#Imports
import launcher

#Functions
def drawstars(spaces,stars):
  return(" "*spaces+"*"*stars)

#Main Program
print(drawstars(2,3))
print(drawstars(2,3))
print(drawstars(3,1))
print(drawstars(2,3))
print(drawstars(0,7))
print(drawstars(2,3))
print(drawstars(2,1)+drawstars(1,1))
print(drawstars(1,2)+drawstars(1,2))
launcher.menu_select()