# master.py
# Generates a random code and correctly provides the user with feedback 
#
# Callie Harlow
# 2.26.15

# first we need to randomly generate the codemaker's code

import random

color = ""
code = ""

# use if statement to generate random numbers and associate them with colors 
for i in range (0,4): # this means that it runs four times and prints four colors
    rInt = random.randint(1,6)
    if rInt == 1:
        color = "R"
    elif rInt == 2:
        color = "G"
    elif rInt == 3:
        color = "B"
    elif rInt == 4:
        color = "Y"
    elif rInt == 5:
        color = "P"
    elif rInt == 6:
        color = "O"
    print(color)
    code = code + color 
    print(code)
    print()
    
n = input("Enter your guess!") # eval finds the numbers but there are no numbers here
blackPeg = 0
whitePeg = 0
# you can access first character in a string by putting index in [] starting with 0
for j in range (0,4):
    if code[j] == n[j]:
        blackPeg = blackPeg + 1
        code = code[0:j] + "x" + code[j+1:len(code)]
        n = n[0:j] + "z" + n[j+1:len(n)] 
print("You have", blackPeg, "black pegs and")
print(code)
print(n)

for i in range (0,4):
    for j in range (0,4):
        if code[i]==n[j]:
            whitePeg = whitePeg + 1
            code = code[0:i] + "x" + code[i+1:len(code)]
            n = n[0:j] + "z" + n[j+1:len(n)] 
print (whitePeg, "white pegs!")
print(code)
print(n)


if blackPeg == 4: 
    print("You win! Congratulations!") 


