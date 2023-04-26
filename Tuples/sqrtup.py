#To create a tuple containing squares of numbers between 1 and 50
#sqrtup.py
#27-11-22
#By Anupam Kanoongo

print("Welcome to the Square of Number Tuple Generator")
print()
n = 50
tup = ()

for i in range(1,n+1):
    tup += (i*i,)

print(tup)

# Output
# Welcome to the Square of Number Tuple Generator

# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100,
# 121, 144, 169, 196, 225, 256, 289, 324, 361, 400,
# 441, 484, 529, 576, 625, 676, 729, 784, 841, 900,
# 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600,
# 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500)