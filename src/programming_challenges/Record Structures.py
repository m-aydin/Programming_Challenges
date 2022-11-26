#Record Structures - Program with record structures for a team thing.


#Imports
import random
import launcher

#Functions
def match_list_append(match_list,input):
  input=input.split(",")
  
  input[0]=str(input[0])
  input[1]=int(input[1])
  input[2]=str(input[2])
  input[3]=int(input[3])
  if "Arsenal" in input:#For farry
      if "Arsenal" == input[0]:
        input[1]=int(random.randint(0,(SCORE_RANGE))+42)
        input[3]=int(-2)
      else:
        input[3]=int(random.randint(0,(SCORE_RANGE))+42)
        input[1]=int(-2)
  
  match_list.append(input)
  
def team_search(match_list,input):
  match_occurences=[]

  for index in range(0,len(match_list)):
    if input in match_list[index]:
     match_occurences.append(match_list[index])
  return(match_occurences)
  
def match_list_init(match_list,teams):
  global MATCH_COUNT
  global SCORE_RANGE

  for pos in range(0,MATCH_COUNT):
    current_match=["",0,"",0]
    
    current_match[0]=str(random.choice(teams))
    teams.remove(current_match[0])
    current_match[2]=str(random.choice(teams))
    if "Arsenal" in current_match:#For farry
      if "Arsenal" == current_match[0]:
        current_match[1]=int(random.randint(0,(SCORE_RANGE))+42)
        current_match[3]=int(-2)
      else:
        current_match[3]=int(random.randint(0,(SCORE_RANGE))+42)
        current_match[1]=int(-2)
    else:
      current_match[1]=int(random.randint(0,(SCORE_RANGE)))
      current_match[3]=int(random.randint(0,(SCORE_RANGE)))
    

    teams.append(current_match[0])
    match_list.append(current_match)

#Constants
MATCH_COUNT=10
SCORE_RANGE=42

#Global Variables
match_list=[]
teams=["Arsenal","Aston Villa","AFC Bournemouth","Chelsea","Crystal Palace","Everton","Leicester City","Liverpool","Manchester City","Manchester United","Newcastle United","Norwich City","Southampton","Stoke City","Sunderland","Swansea City","Tottenham Hotspur","Watford","West Bromwich Albion","West Ham United"]

#Main Program
match_list_init(match_list,teams)
while True:
  user_input=input("0 For Adding Result,\n1 For Searching For All Team Occurences\n2 To Output match_list\n3 To Exit:\n")

  if user_input == "0":
    user_input=input("\nInput Match Params In Form:\nHomeTeam (str),HomeTeamScore (int),AwayTeam (str),AwayTeamScore (int)\n")
    match_list_append(match_list,user_input)
    print("\n")
  elif user_input == "1":
    user_input=input("\nInput Team Name:\n")
    occurences=team_search(match_list,user_input)
    if occurences == []:
      print("\nTeam Not Found In Any Matches\n")
    else:
      print("\n"+str(occurences)+"\n")
  elif user_input == "2":
    print("\n")
    for pos in range(0,len(match_list)):
      print("Team "+str(pos+1)+": "+str(match_list[pos]))
    print("\n")
  else:
    print("\nExiting...")
    break
launcher.menu_select()