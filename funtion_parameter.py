def add():
    a = 10
    b = 20
    print(a +b)
add()

def add():
    a = 10
    b = 40
    return a + b
res = add()
print(res)

def add(a ,b):
    print(a + b)
add(100, 200)

def add(a,b):
    c = a + b
    return c
print(add(30, 40))

# WAF to find square of a number
#1- NO input no output
def square():
    num = 5
    print(num * num)

square()

#2- No input only output
def square():
    num = 5
    return num * num
res = square()
print(res)

#3- only input no output
def square(num):
    return num * num
square(5)

#4- input and output both
def square(num):
    return num * num
res = square(5)
print(res)

