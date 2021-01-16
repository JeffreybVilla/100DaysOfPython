from art import logo
print(logo)


#Add function that takes 2 inputs
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

user_operation = input("Pick an operation from the line above: ")

num2 = int(input("What's the second number?: "))

calculation_function = operations[user_operation]

first_answer = calculation_function(num1, num2)

print(f"{num1} {user_operation} {num2} = {first_answer}")


#Since the functions return the result you can re-use the output.
#If you use print statements, cant use output to perform other calculation


user_operation = input("Pick another operation: ")
num3 = int(input("What's the next number?: "))
calculation_function = operations[user_operation]
second_answer = calculation_function(first_answer, num3)

print(f"{first_answer} {user_operation} {num3} = {second_answer}")
