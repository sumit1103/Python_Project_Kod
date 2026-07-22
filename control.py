#Selection Statement
# if
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
print("Thank you for using our service.")
print("------------------------------------------------")
#elif
age = int(input("Enter your age: "))
if age >= 18:
    print("You are not eligible to vote.")
else:
    print("You are eligible to vote.")
print("Thank you for using our service.")
print("------------------------------------------------")
#elif ladder (if-elif-else)
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")   
print("------------------------------------------------")   
# Nested if
free_tonight = True
friends_available = False
if free_tonight:
    if friends_available:
        print("Let's go out!")
    else:
        print("Maybe we can hang out another time.")
else:
    print("I have other plans tonight.")
print("------------------------------------------------")   
#matching statement
day = 4
match day:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case _: print("Invalid")
print("------------------------------------------------")   
#Case 3, 4, 5 - Summer Days , 6,7,8 - rainy, 9,10,11,12 - Winter, 1,2 - Atumn
month = int(input("Enter month number: "))
match month:
    case 3 | 4 | 5:
        print("Summer Days")
    case 6 | 7 | 8:
        print("Rainy Days")
    case 9 | 10 | 11 | 12:
        print("Winter Days")
    case 1 | 2:
        print("Autumn Days")
    case _:
        print("Invalid month number")
print("--------------------For ----------------------------")      
# Looping Statement
# For Loop 0 to 5 (12345) (1,6)
for i in range(1, 6):
    print(i)
print("------------------------------------------------")
# first 5 number
for i in range(5):
    print(i)
print("------------------------------------------------")
#even number 2 ,4, 6, 8, 10
for num in range(1, 11):
    if num % 2 == 0:
        print(num) 
print("---------------------while---------------------------")
#while loop
i = 0
while i <= 5:
    print(i)
    i += 1

print("--------------------break----------------------------")
#Jump Statement
# break statement
for i in range(1, 6):
    if i == 3:
        break
    print(i)
print("---------------------continue---------------------------")
# continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
print("---------------------pass---------------------------")    
# pass statement
for i in range(1, 6):
    if i == 3:
        pass
    else:
        print(i)
print("---------------------return---------------------------")
# return statement
def square(n):
    return n * n
print(square(5))