#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
# Define Methods #

def fibonacci(terms):
 	  # Debug # 
		# print("Calculating: " + str(terms));
    # Special Cases #
    if (terms <= 1):
        return 0;
    elif (terms <= 2):
        return 1;
    # Calculation #
    return fibonacci(terms - 2) + fibonacci(terms - 1)

# Request Input #
termAmount = 0;
while (True):
    inpt = input("Fibonacci term amount?")
    if (inpt.isnumeric() and int(inpt) > 0):
        termAmount = int(inpt);
        break;
		
print(fibonacci(termAmount));
