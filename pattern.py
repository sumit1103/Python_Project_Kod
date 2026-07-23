# ============================
# 1. Purchase Discount
# ============================

purchase_amount = float(input())

if purchase_amount >= 100:
    print("Congratulations! You are eligible for a discount.")


# ============================
# 2. Membership Discount
# ============================

membership_status = input()

if membership_status == "yes":
    print("You are eligible for a membership discount.")
else:
    print("You are not eligible for a membership discount.")


# ============================
# 3. Student Grade
# ============================

score = int(input())

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# ============================
# 4. Sum of First N Natural Numbers
# ============================

N = int(input())

total_sum = 0

for i in range(1, N + 1):
    total_sum += i

print(f"The sum of the first {N} natural numbers is {total_sum}")


# ============================
# 5. Fibonacci Series
# ============================

N = int(input())

a = 0
b = 1

for i in range(N):
    print(a)
    a, b = b, a + b


# ============================
# 6. Sum of Digits
# ============================

num = int(input())

digit_sum = 0

while num > 0:
    digit = num % 10
    digit_sum += digit
    num = num // 10

print(f"The sum of the digits is {digit_sum}")


# ============================
# 7. Reverse a Number
# ============================

num = int(input())

reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

print(f"The reversed number is {reversed_num}")


# ============================
# 8. Product of Even Numbers up to N
# ============================

N = int(input())

product = 1
i = 2

while i <= N:
    product *= i
    i += 2

print(f"The product of all even numbers up to {N} is {product}.")


# ============================
# 9. Largest Digit in a Number
# ============================

num = int(input())

largest = 0

while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    num = num // 10

print(f"The largest digit is {largest}.")


# ============================
# 10. Last Even Digit
# ============================

num = int(input())

original_num = num

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        print(f"The last even digit in {original_num} is {digit}.")
        break

    num = num // 10
else:
    print("No even digit found.")


# ============================
# 11. Sum of Non-Zero Digits
# ============================

num = int(input())

original_num = num
digit_sum = 0

while num > 0:
    digit = num % 10
    num = num // 10

    if digit == 0:
        continue

    digit_sum += digit

print(f"The sum of non-zero digits in {original_num} is: {digit_sum}")


# ============================
# 12. Rectangle Pattern
# ============================

rows = int(input())
columns = int(input())

for i in range(rows):
    for j in range(columns):
        print("*", end="")
    print()


# ============================
# 13. Right-Angled Triangle Pattern
# ============================

rows = int(input())

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()


# ============================
# 14. Hollow Rectangle Pattern
# ============================

rows = int(input())
columns = int(input())

for i in range(rows):
    for j in range(columns):
        if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# ============================
# 15. Rectangle + Triangle + Reverse Triangle
# ============================

rows = int(input())

# Right Triangle
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

print("------------------")

# Rectangle
for i in range(1, 4):
    for j in range(1, 6):
        print("*", end="")
    print()

print("----------------------")

# Reverse Right Triangle
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)


# ============================
# 16. Alphabet Pyramid
# ============================

rows = int(input())

for i in range(rows):

    # Spaces
    print(" " * (rows - i - 1), end="")

    # A to current letter
    for j in range(i + 1):
        print(chr(65 + j), end="")

    # Current letter back to A
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end="")

    print()