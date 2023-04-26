#To explore a function
#func.py
#16-3-23
#By Anupam Kanoongo

def main():
    a, b, o = 0, 0, 0
    print("Welcome to the Python Calculator")
    print()
    a = int(input("Enter First Number : "))
    print()
    b = int(input("Enter Second Number : "))
    print()
    o = input("Enter an Operation : ")
    print()
    
    return a, b, o

def add():
    r = a + b
    r = "Answer : " + r
    return r

def sub():
    r = a - b
    r = "Answer : " + r
    return r

def mul():
    r = a * b
    r = "Answer : " + r
    return r

def div():
    r = a / b
    r = "Answer : " + r
    return r

def sqr():
    r1 = a**2
    r2 = b**2
    r = "Square of First : " + r1 + ", " + "Square of Second : " + r2

def sqrt():
    r1 = a**0.5
    r2 = b**0.5
    r = "Square Root of First : " + r1 + ", " + "Square Root of Second : " + r2

def cube():
    r1 = a**3
    r2 = b**3
    r = "Cube of First : " + r1 + ", " + "Cube of Second : " + r2

def cubert():
    r1 = a**0.5
    r2 = b**0.5
    r = "Cube Root of First : " + r1 + ", " + "Cube Root of Second : " + r2
        
a, b, o = main()

if o == "+" or o == "add":
    r = add()
elif o == "-" or o == "subtract":
    r = sub()
elif o == "*" or o == "multiply":
    r = mul()
elif o == "/" or o == "divide":
    r = div()
elif o == "square":
    r = sqr()
elif o == "squareroot":
    r = sqrt()
elif o == "cube":
    r = cube()
elif o == "cuberoot":
    r = cubert()    

print(r)
