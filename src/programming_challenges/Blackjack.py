#Blackjack - Just Some Blackjack Thing


#Imports
import random
import launcher

#Functions
def draw_cards(amount):
  global suits
  global type
  global user_hand
  count=0
  cards=[]
  while count < amount:
    card=random.choice(type)+" "+random.choice(suits)
    if card in cards or (card in user_hand):
      continue
    else:
      cards.append(card)
    count+=1
  return(cards)

def display_hand(hand):
  for current in hand:
    split=current.split()
    print(split[0]+" Of "+split[1])

def get_value(hand):
  pass
  global type
  value=0
  ace=0
  for current in hand:
    split=current.split()
    if split[0] in type[1:4]: 
      value+=10
    elif split[0] == type[0]:
      ace+=1
    else:
      value+=int(split[0])
      
  if ((value+(ace*11)) > 21) and (ace >= 1):
    value+=ace
  elif ace >= 1:
    value+=(ace*11)
    
  return(value)
  
#Constants

#Global Variables
suits=["Hearts","Spades","Clubs","Diamonds"]
type=["Ace","Queen","King","Joker","2",
      "3","4","5","6","7","8","9","10"]
user_hand=[]
bot_hand=[]
user_choice=""

#Main Program
user_hand.extend(draw_cards(2))
print("\n\nUsers Hand:")
display_hand(user_hand)
print("User Hand Value: "+str(get_value(user_hand)))
while get_value(user_hand) <= 21:
  user_choice=input("\nD To Draw, S To Stick: ").lower()
  if user_choice == "d":
    user_hand.extend(draw_cards(1))
    print("\nUsers Hand:")
    display_hand(user_hand)
    print("User Hand Value: "+str(get_value(user_hand)))
  if user_choice == "s":
    break
    
if get_value(user_hand) > 21:
  print("\nUser Has Bust")
else:
  bot_hand.extend(draw_cards(2))
  print("\nDealers Hand:")
  display_hand(bot_hand)
  print("Dealers Hand Value: "+str(get_value(bot_hand)))
  
  if get_value(bot_hand) == get_value(user_hand):
    print("\nUser And Bot Have Tied")
  elif get_value(bot_hand) > get_value(user_hand):
    print("\nUser Loses To Dealer")
  else:
    print("\nUser Wins")
launcher.menu_select()