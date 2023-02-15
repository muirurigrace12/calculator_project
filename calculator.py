#this is a calculator project
number1 = eval(input("enter first number"))
number2 = eval(input("enter second number"))

operator = input("enter operator")


def add(number1, number2):
    result = number1 + number2
    return result

def subtract(number1, number2):
    result = number1 - number2
    return result

def divide(number1, number2):
    result = number1 / number2
    return result

def multiply(number1, number2):
    result = number1 * number2
    return result
