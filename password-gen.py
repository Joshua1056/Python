import secrets
import string

line01 = "*************************" # header / footer
line02 = "*                       *" # re-use
line03 = "*Welcome to Password-gen*"
  
# starts with blank
print('')
print(line01)
print(line02)
print(line03)
print(line02)
print(line01)
print('') # ends with blank
alphabet = string.ascii_letters + string.digits + string.punctuation
print("")
length = input("Please enter password length you would like ... \n")
    
length = int(length)
password = ''.join(secrets.choice(alphabet) for i in range(length))
print("")
print("Your password has been generated:")
print(password)
print("")
print("😊 Made by Joshua1056")
input("Press ENTER To exit")