#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

def fibonacci_sequence():
    while True:
        user_input = input("Enter the number of terms: ")

        # Validate that the input is a positive integer
        if not user_input.isdigit():
            print("Please enter a positive integer.")
            continue

        n = int(user_input)
        if n <= 0:
            print("Please enter a positive integer.")
            continue

        # Generate and print the Fibonacci sequence up to n terms
        a, b = 0, 1
        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()
        break
# Run the program
fibonacci_sequence()
