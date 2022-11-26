#UMS To Grade - Grading?

#Imports
import launcher

#Functions
def ums_to_grade(mark,max_mark):
  global mean_mark
  percent=mark/max_mark
  mean[0]+=int(percent*max_mark)
  mean[1]+=max_mark
  grade=""

  if percent >= 0.9:
    grade="A*"
  elif percent >= 0.8:
    grade="A"
  elif percent >= 0.7:
    grade="B"
  elif percent >= 0.6:
    grade="C"
  elif percent >= 0.5:
    grade="D"
  elif percent >= 0.4:
    grade="E"
  else:
    grade="U"
  return(grade)

#Global Variables
user_input=""
mean=[0,0]
grades=[]

#Main Program
for pos in range(0,2):
  user_input=input('Input "mark,max_mark": ').split(",")
  grades.append(ums_to_grade(int(user_input[0]),int(user_input[1])))
grades.append(ums_to_grade(mean[0],mean[1]))
print("Grade 1: "+grades[0]+"\nGrade 2: "+grades[1]+"\nMean Grade: "+grades[2])
launcher.menu_select()