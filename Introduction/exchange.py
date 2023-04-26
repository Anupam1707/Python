# This program  will change the values of two variables
# 22-07-2022
# Exchange.py
# By Anupam Kanoongo

print("Welcome to the Variable value changer")
print()
print("Enter your values")
print()
va = int(input("Input Number 1 : " ))    # Variable 1
vb = int(input("Input Number 2 : " ))    # Variable 2
Before = va, vb
Final = va, vb = vb, va  # Function to exchange

print("Numbers before Swapping", Before, "Numbers after swapping", Final)   # Final Answer to be printed


##Output
##Welcome to the Variable value changer
##
##Enter you values
##
##Input Number 1 100
##Input Number 2 1
##Numbers before Swapping (100, 1) Numbers after swapping (1, 100)
