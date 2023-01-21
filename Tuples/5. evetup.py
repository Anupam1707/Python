##To count the number of pairs of subtuples in a tuple where (a,b) are even
#evetup.py
#28-11-22
#By Anupam Kanoongo

print("Welcome to the Even Tuple Finder")
print()
tup = eval(input("Enter a pairs of tuples :"))
lt = len(tup)
nums = range(0,10000,2)
cnt = 0
a, b = 0, 0

for i in tup:
    a, b = i
    if a in nums and b in nums:
        cnt += 1

print("Out of the above tuple",cnt,"pair(s) contain both even numbers")

# Output
# Welcome to the Even Tuple Finder

# Enter a pairs of tuples :((1,2),(2,4),(3,6),(4,8))
# Out of the above tuple 2 pair(s) contain both even numbers