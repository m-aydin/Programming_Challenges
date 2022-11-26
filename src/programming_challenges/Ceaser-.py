#Ceaser- - Not very good


#Imports
import launcher

#Functions
def encrypt_decrypt(text,is_encrypt):
  global OFFSET
  char_code=0
  char=""
  cipher=""
  
  if is_encrypt:
    for pos in range(0,len(text)):
      char_code=ord(text[pos])+OFFSET
      char=chr(char_code)
      cipher+=char
    return(cipher)
  else:
    for pos in range(0,len(text)):
      char_code=ord(text[pos])-OFFSET
      char=chr(char_code)
      cipher+=char
    return(cipher)

#Constants
OFFSET=2

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