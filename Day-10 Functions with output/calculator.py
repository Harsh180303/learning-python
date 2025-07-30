# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator() :
    num1 = float(input("Enter your first number: "))
    for symbol in operations:
        print(symbol)

    finished = False
    while not finished :
        operation_symbol = input(f"Enter the operation do you want to perform: ")
        num2 = float(input("Enter your next number: "))

        calculation_function = operations[operation_symbol]
        first_answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {first_answer}")
        should_continue = input(f"Type 'y' to continue with {first_answer}, or type 'n' to start new calculation.: ")
        if should_continue == 'n' :
            finished = True
            calculator()
        if should_continue == 'y':
            num1 = first_answer

calculator()