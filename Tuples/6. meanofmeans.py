#To find the mean of subtuples of a tuple aand the mean of the final means
#meanofmeans.py
#28-11-22
#By Anupam Kanoongo

print("Welcome to the Mean of Means of Subtuples finder")
print()
tup = eval(input("Enter a tuples of non-uniform nested tuples : "))
m, mm = 0, 0
ct = 0

print("SubMeans as Follows : ")
print()
for i in tup:
    lt = len(i)
    for j in i:
        m += j
    m = m/lt
    print(m)
    print()
    mm += m
    ct += 1
    m = 0
mm/=ct
print("The Mean of the above means is",mm)

# Output
# Welcome to the Mean of Means of Subtuples finder

# Enter a tuples of non-uniform nested tuples : ((1,2),(3,4,5),(6,7),(8,9,10))
# SubMeans as Follows :

# 1.5

# 4.0

# 6.5

# 9.0

# The Mean of the above means is 5.25