#Ceaser+ - Still not that good


#Imports
import random
import launcher

#Functions
def encrypt_decrypt(text,is_encrypt):
  global KEY
  random.seed(KEY)
  char_code=0
  char=""
  cipher=""
  
  if is_encrypt:
    for pos in range(0,len(text)):
      char_code=ord(text[pos])+random.randint(0,10)
      char=chr(char_code)
      cipher+=char
    return(cipher)
  else:
    for pos in range(0,len(text)):
      char_code=ord(text[pos])-random.randint(0,10)
      char=chr(char_code)
      cipher+=char
    return(cipher)

#Constants
KEY="706F6F706F6F"

#Global Variables
user_input=""
text=""

#Main Program
user_input=input('Input In Form "x,Text", Where X Is e/d Or Encrypt/Decrypt: ')

if user_input[0] == "e":
  text=encrypt_decrypt(user_input[2:],True)
else:
  text=encrypt_decrypt(user_input[2:],False)

print("Output: "+text)
launcher.menu_select()