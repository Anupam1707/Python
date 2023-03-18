# To create a function to find the interest by Principle, Rate and Time
#18-03-23
#Interest.py
#By Anupam Kanoongo

print("Welcome to the Interest Calculator")

def interest(P = 10000, R = 5, T = 1):
    Interest = (P * R * T)/100
    return Interest, P, R, T

def start():
    P = eval(input("Principle : "))
    print()
    R = eval(input("Rate of Interest : "))
    print()
    T = eval(input("Duration : "))
    print()

    if P == "No":
        i, a, b, c = interest(R = R, T = T)
        
    elif R == "No":
        i, a, b, c = interest(P = P, T = T)
        
    elif T == "No":
        i, a, b, c = interest(P = P, R = R)
        
    elif P == "No" and R == "No":
        i, a, b, c = interest(T = T)
        
    elif R == "No" and T == "No":
        i, a, b, c = interest(P = P)
        
    elif P == "No" and T == "No":
        i, a, b, c = interest(R = R)
        
    elif P == "No" and R == "No" and T == "No":
        i, a, b, c = interest()
    

    print("The Interset at Principle : ",a,", Rate of Interest : ",b,", Duration : ",c,"is",i)

start()
