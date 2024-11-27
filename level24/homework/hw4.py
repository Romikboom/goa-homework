def mini_calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"
print(mini_calculator(10, 5, 'add'))        # Output: 15
print(mini_calculator(10, 5, 'subtract'))   # Output: 5
print(mini_calculator(10, 5, 'multiply'))   # Output: 50
print(mini_calculator(10, 5, 'divide'))     # Output: 2.0
print(mini_calculator(10, 0, 'divide'))     # Output: Error: Division by zero
