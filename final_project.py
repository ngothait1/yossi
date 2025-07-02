"""
Yossi Abu 312219322
Python Course First Chapter (מתחילים) Final Project
"""

import time

print("Hello, This is my final project")
name = input("What is your name? ")
print(f"Hi {name}, nice to meet you")

print("This is a special calculator, I would need two numbers from you")
firstNumber = int(input("First number "))
secondNumber = int(input("Second number "))
print(f"Thank you for putting in your numbers, {firstNumber} and {secondNumber}")

firstStatus = "even" if firstNumber % 2 == 0 else "odd"
secondStatus = "even" if secondNumber % 2 == 0  else "odd"

print("I can see that the first number is " + firstStatus)
print("And the second is " + secondStatus)

if firstStatus != secondStatus:
    print("So one of them is even, and one is odd")
else:
    # Same string for even/odd variables (instead of different string in the original solution)
    print("So both of them are " + firstStatus)

errorFlag = False
operator = input("Operator (+, -, *, /): ")

if operator == '/':
    answer = input("You chose division, should the result be integer? (y/n) ")
    if secondNumber != 0:
        if answer == 'y':
            print(f"{firstNumber} / {secondNumber} = {firstNumber // secondNumber}")
        # Check if the user enter `no` instead of any other output (different from the original solution)
        elif answer == 'n':
            print(f"{firstNumber} / {secondNumber} = {firstNumber / secondNumber}")
        else:
            print("Invalid response for division type. Please enter 'y' or 'n'.")
            errorFlag = True
    else:
        # secondNumber == 0
        print("Error: num_2 is zero")
        errorFlag = True

elif operator == '+' or operator == '-' or operator == '*':
    if operator == '+':
        result = firstNumber + secondNumber
    elif operator == '-':
        result = firstNumber - secondNumber
    else:
        result = firstNumber * secondNumber
    print(f"{firstNumber} {operator} {secondNumber} = {result}")
    
else:
    print(f"Error: Operator {operator} is not supported")
    errorFlag = True
    
if errorFlag:
    print("An error had occured, please try again")
    
print(f"Thank you {name} for using the calculator on {time.ctime()}")