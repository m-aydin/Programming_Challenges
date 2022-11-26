#Imports
import time
import os
import sys

#Functions
def menu_select(is_skip=False):
    global BUFFER
    global DELAY
    output=""

    p_challenges=os.listdir(os.path.join(os.path.dirname(__file__),"programming_challenges"))
    for current in p_challenges:
        if ".py" in current:
            p_challenges[p_challenges.index(current)]=p_challenges[p_challenges.index(current)][:-3]
        else:
            p_challenges.remove(current)

    for current in p_challenges:
        diff=len(max(p_challenges,key=len))-len(current)
        output+="\n"+current+" "*(diff+2)+"["+str(p_challenges.index(current)+1)+"]"
    output+="\n"

    if not is_skip:
        time.sleep(DELAY[1])
    print(output)

    while True:
        try:
            user_input=int(input("Input File To Select By Number, 0 To Exit: "))
        except:
            print("Input Has To Be A Number"+"\n"*BUFFER[1])
            time.sleep(DELAY[0])
            continue

        if user_input == 0:
            print("Exiting...")
            time.sleep(DELAY[0])
            sys.exit()
        elif user_input not in range(1,len(p_challenges)+1):
            print("Input Has To Be In Range Of Selectable Programs"+"\n"*BUFFER[1])
            time.sleep(DELAY[0])
            continue
        else:
            break
    
    print("\n"*BUFFER[0])
    __import__("programming_challenges."+p_challenges[user_input-1])

#Constants
BUFFER=[4-1,2]
DELAY=[0.5,3]

#Global Variables
output="\n"*BUFFER[0]
p_challenges=[]

#Main Program
if __name__ == "__main__":
    menu_select(True)