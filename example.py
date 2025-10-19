#!/usr/bin/env python3
"""
Example Python file for Git learning
"""

def greet(name):
    """Greet a person by name"""
    return f"Hello, {name}! Welcome to Git learning!"

def calculate_age(birth_year):
    """Calculate age from birth year"""
    current_year = 2024
    return current_year - birth_year

def main():
    print("Git Learning Example")
    print("=" * 20)
    
    name = input("What's your name? ")
    print(greet(name))
    
    try:
        birth_year = int(input("What year were you born? "))
        age = calculate_age(birth_year)
        print(f"You are {age} years old!")
    except ValueError:
        print("Please enter a valid year!")

if __name__ == "__main__":
    main()
