import sys

abortmessage = "Aborted. Made by Joshua1056"
line01 = "*************************" # header / footer
line02 = "*                       *" # re-use
line03 = "*    Welcome to Calc    *"
line04 = "*                       *"
  
# starts with blank
print('')
print(line01)
print(line02)
print(line03)
print(line02)
print(line01)
print('') # ends with blank
guideinput = input("Would you like to see the calculator guide? y/n\n")
# exit for guide input
if guideinput == 'exit':
    sys.exit(abortmessage)
#guide
guide = '''
+ for addition,
- for subtraction,
* for multiplication,
/ for division,
% for percentage,
** for expontation,
// for floor division,
Type exit on any input to exit program. 
'''
if guideinput == 'y':
    print(guide)
    
inputfirst = input("Enter first calculation number ...\n")
#exit for inputfirst
if inputfirst == 'exit':
    sys.exit(abortmessage)
    
inputoperator = input("Enter operator for calculation ...\n")
#exit for inputoperator
if inputoperator == 'exit':
    sys.exit(abortmessage)
    
inputlast = input("Enter last calculation number ...\n")
#exit for inputlast
if inputlast == "exit":
    sys.exit(abortmessage)
    
inputfirstint = int(inputfirst)
inputlastint = int(inputlast)
print("")
print("Your total is...")
if inputoperator == '+': # operator checking & calculations
    print(inputfirstint + inputlastint)
elif inputoperator == '-':
    print(inputfirstint - inputlastint) 
elif inputoperator == '*':
    print(inputfirstint * inputlastint) 
elif inputoperator == '/':
    print(inputfirstint / inputlastint) 
elif inputoperator == '%':
    print(inputfirstint % inputlastint)
elif inputoperator == '**':
    print(inputfirstint ** inputlastint)
elif inputoperator == '//':
    print(inputfirstint // inputlastint)
print("")
print('😊 Thanks for using my calculator made by Joshua1056')
input('Press ENTER to exit.')