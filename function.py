def add():
    a = 10
    b = 20
    c = a + b
    print(f"The sum of {a} + {b} is {c}")

add()

# WAF to find square of a number
def square(num):
    return num ** 2

num = int(input("Enter a number to find its square: "))
print(f"The square of {num} is {square(num)}")


# WAF to find largest of two numbers
def largest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

print(f"The largest of 10 and 20 is {largest(10, 20)}")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The largest number is {largest(num1, num2)}")


# WAF to find cube of a number
def cube(num):
    return num ** 3

num = int(input("Enter a number to find its cube: "))
print(f"The cube of {num} is {cube(num)}")


print("--------------------------OR-------------------------------------------------")

# add 2 numbers
def add():
    a = 10
    b = 20
    c = a + b
    print(f"The sum of {a} + {b} is {c}")


add()
add()
add()


# WAF to find square of a number
def sqauare():
    num = 10
    print(f"The square of the number is {num * num}")


sqauare()
# WAF to find largest of 3 numbers
def largest():
    a = 10; b = 30; c = 20
    if a >= b and a >=c:
        return a
    elif b >= a and b >=c:
        return b
    else:
        return c
print(largest())  


# WAF to find cube of a number
def cube():
    num = 10
    print(f"The cube of the number is {num * num * num}")


cube()