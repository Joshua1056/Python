import sys
import random
from enum import Enum
from colorist import red

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

line01 = "*************************" # header / footer
line02 = "*                       *" # re-use
line03 = "*     Welcome to RPS    *"
line04 = "*                       *"
  
# starts with blank
print('')
print(line01)
print(line02)
print(line03)
print(line02)
print(line01)
print('') # ends with blank

playerchoice = input("Enter ...\n1 for Rock, \n2 for paper, or \n3 for scissors, exit to abort \n")
if playerchoice == 'exit':
    sys.exit("Aborted. Made by Joshua1056.")
    

player = int(playerchoice)

if player < 1 or player > 3:
    red("Number has to be 1, 2 or 3")
    input("Press ENTER To exit")
    sys.exit("")
    
computerchoice = random.choice("123")

computer = int(computerchoice)

print("You chose " + str(RPS(player)).replace("RPS.", '') + ".") 
print("Python chose " + str(RPS(computer)).replace('RPS.' , '') + ".")
print("")

if player == 1 and computer == 3:
    print("🎉 You win!")
elif player == 2 and computer == 1:
    print("🎉 You win!")
elif player == 3 and computer == 2:
    print("🎉 You win!")
elif player == computer:
    print("😲 Tie!")
else:
    print("🐍 Python wins!")
print("")
input("Press ENTER To exit. 😊 Thanks for playing this game made by Joshua1056")
