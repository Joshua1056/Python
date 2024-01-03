import sys

guideinput = input("Would you like to see the calculator guide? y/n\n")
# exit for guide input
if guideinput == 'exit':
    sys.exit("Aborted.")
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
    sys.exit("Aborted.")
    
inputoperator = input("Enter operator for calculation ...\n")
#exit for inputoperator
if inputoperator == 'exit':
    sys.exit("Aborted.")
    
inputlast = input("Enter last calculation number ...\n")
#exit for inputlast
if inputlast == "exit":
    sys.exit("Aborted.")
    
inputfirstint = int(inputfirst)
inputlastint = int(inputlast)
print("")
print("Your total is...")
if inputoperator == '+': # operator checking & calculations
    print(inputfirstint + inputlastint)

if inputoperator == '-':
    print(inputfirstint - inputlastint)
    
if inputoperator == '*':
    print(inputfirstint * inputlastint)
    
if inputoperator == '/':
    print(inputfirstint / inputlastint)
    
if inputoperator == '%':
    print(inputfirstint % inputlastint)
    
if inputoperator == '**':
    print(inputfirstint ** inputlastint)
    
if inputoperator == '//':
    print(inputfirstint // inputlastint)