# master.py
# Generates a random code and correctly provides the user with feedback 
#
# Callie Harlow
# 2.26.15

# first we need to randomly generate the codemaker's code

import random

color = ""


def generateRandomCode():
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
        code = code + color 
    return code
    

def findPegs(code,n):
    blackPeg = 0
    whitePeg = 0
    # you can access first character in a string by putting index in [] starting with 0
    for j in range (0,4):
        if code[j] == n[j]:
            blackPeg = blackPeg + 1
            code = code[0:j] + "x" + code[j+1:len(code)]
            n = n[0:j] + "z" + n[j+1:len(n)] 
   
    for i in range (0,4):
        for j in range (0,4):
            if code[i]==n[j]:
                whitePeg = whitePeg + 1
                code = code[0:i] + "x" + code[i+1:len(code)]
                n = n[0:j] + "z" + n[j+1:len(n)]
                
    return blackPeg, whitePeg


code = generateRandomCode()
print(code)

notDone = True

while notDone:
    n = input("Enter your guess!") # eval finds the numbers but there are no numbers here  
    blackPeg, whitePeg = findPegs(code, n)
    if blackPeg == 4:
        notDone=False
        print("You win! Congratulations!")
    else:
        print ("You have", blackPeg, "black pegs and", whitePeg, "white pegs! Try again.")






