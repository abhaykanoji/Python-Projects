from art import logo
import os


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def calculator():
    print(logo)
    num1 = float(input("enter first number: "))
    for i in operation:
        print(i)
    on = True
    while on:
        operation_sign = input("pick operation: ")
        num2 = float(input("enter next number: "))
        calculation_function = operation[operation_sign]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_sign} {num2} = {answer}")
        if input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
        ) == 'y':
            num1 = answer
        else:
            on = False
            os.system("clear")
            calculator()

calculator()