# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""
def sum_of_digits(number):
    digits = str(number)
    total = 0
    output = " + ".join(digits) + " = "
    
    for digit in digits:
        total += int(digit)

    return output, total
while True:
    user_input = input("Please enter a 4-digit integer: ")
    
    if user_input.isdigit() and len(user_input) == 4:
        break
    else:
        print("Invalid input. Please make sure you enter a 4-digit integer.")

output_string, total_sum = sum_of_digits(user_input)

print(f"{output_string}{total_sum}")