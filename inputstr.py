# Get name
name = input("Enter the name: ")
print(f"{name} is a Python student")

# Get age
age = int(input("Enter the age: "))
print(f"{name}'s age is {age}")

# Add two numbers
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

result = num1 + num2

print("The sum is", result)

# Find the area of a rectangle

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width

print("Area of the rectangle is:", area)

#Using bool() Typecasting...
name = input("Enter student name: ")
placed = bool(int(input("Enter 1 if placed, 0 if not placed: ")))

print("Student Name:", name)
print("Placement Status:", placed)

message = """
Python is a powerful programming language.
It is easy to learn.
It is widely used in data science, web development, and more.
"""


print(message)


#---- practice code-----

# Define the full name
full_name = "John Michael Doe"


# Split the full name into a list
name_parts = full_name.split()


# Create the formatted name with initials
initials_name = f"{name_parts[0]} {name_parts[1][0]}. {name_parts[2][0]}."


# Print the results
print("Name parts:", name_parts)
print("Formatted name with initials:", initials_name)
