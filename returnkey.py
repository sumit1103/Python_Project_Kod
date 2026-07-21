#return multiple values
def calculaate(a, b):
    return a + b, a - b, a* b, a % b
x,y,z,m = calculaate(20, 10)

print("Addition:", x)
print("Subtraction:", y)
print("Multiplication:", z)
print("Modulus:", m)


print("--------------------------OR-------------------------------------------------")

#return multiple values 

def student():
    return "John", 20, "A+"
name, age, grade = student()
print("Name:", name)
print("Age:", age)
print("Grade:", grade)