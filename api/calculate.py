
def calculator(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        if num1>num2:
            return num1 - num2
        else:
            return num2 - num1
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Division by zero error"
        return num1 / num2
    return "Invalid operation"
