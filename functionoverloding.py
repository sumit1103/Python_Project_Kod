# function overloading - function with same but different parametrer not possible
# default parameter values - default values are used when no value is passed for that parameter
def add(a, b, c = 0, d = 0):
    return a + b + c + d

print(add(5, 10))
print(add(5, 10, 15))
print(add(5, 10, 15, 20))

print("--------------------------OR-------------------------------------------------")
# varags, variable number of arguments *args 0....n
def add(*number):
    return sum(number)
print(add(5, 10))
print(add(5, 10, 15))   
print(add(5, 10, 15, 20))