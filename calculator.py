#!/usr/bin/env python3
"""
Simple Calculator for Git Learning
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    """Calculate a raised to the power of b"""
    return a ** b

def main():
    print("Welcome to the Enhanced Calculator!")
    print("Available operations: +, -, *, /, ^ (power)")
    
    try:
        num1 = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /, ^): ")
        num2 = float(input("Enter second number: "))
        
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        elif operation == '^':
            result = power(num1, num2)
        else:
            result = "Invalid operation"
            
        print(f"Result: {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
