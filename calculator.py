from replit import clear
from art import logo

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide (n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
} 

def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))
    for items in operations:
            print(items) 
    should_continue = True
    while should_continue:
        operation_item = input("Pick and operation from the line above: ")
        num2 = float(input("What's the next number?: "))
        result = operations[operation_item](num1, num2)
        print(f"{num1} {operation_item} {num2} = {result}") 
        #operation_item = input("Pick and operation from the line above: ")
        #num3 = int(input("What's the next number?: "))
        #result2 = operations[operation_item](result, num3) 
        #print(f"{result} {operation_item} {num3} = {result2}")
        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation.:  ") == 'y':
            num1 = result 
        else: 
            should_continue = False
            clear()
            calculator()
calculator()
