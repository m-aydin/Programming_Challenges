#Fibonacci Rabbits - "Go forth and multiply"

#Imports
import launcher

#Functions
def gen_sequence():
  global FIB_SEED
  global SEQ_LIMIT
  sequence=FIB_SEED

  for pos in range(0,SEQ_LIMIT):
    sequence.append(sequence[len(sequence)-1]+sequence[len(sequence)-2])
  return(sequence)
  
#Constants
FIB_SEED=[0,1]
SEQ_LIMIT=50

#Global Variables
sequence=[]
user_input=""

#Main Program
sequence=gen_sequence()
user_input=int(input("Sequence Pos: "))
print("Fib Num: "+str(sequence[user_input]))
launcher.menu_select()