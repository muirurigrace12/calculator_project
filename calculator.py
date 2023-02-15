#this is a calculator project
number1 = eval(input("enter first number"))
number2 = eval(input("enter second number"))

operator = input("enter operator")


def add(number1, number2):
    result = number1 + number2
    print(result)

def subtract(number1, number2):
    result = number1 - number2
    print(result)

def divide(number1, number2):
    result = number1 / number2
    print(result)

def multiply(number1, number2):
    result = number1 * number2
    print(result)

#check operator
if operator == "+":
    add(number1,number2)

elif operator == "/":
    divide(number1, number2)

elif operator == "-":
    subtract(number1, number2)

elif operator == "X" or operator == "*":
    multiply(number1, number2)

else:
    print("invalid operator")
    


