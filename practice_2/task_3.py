"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, after which you use one of the formulas below to determine the index.
BMI = weight/height**2 
"""
weight = input()
height = input()


#code here
def calculate_bmi(weight, height):
    return weight / (height ** 2)

print(calculate_bmi(weight=77, height=177))

