#Write a program to calculate total votes for each of the candidates and declare
#the winner.
#8/2/23
#
#By Anupam Kanoongo

import random

vt = ["a","b","c"]

votes = {}
for i in range(1,31):
    votes[i] = random.choice(vt)
    
# calculate total votes for each candidate

votes_a = 0
votes_b = 0
votes_c = 0

for v in votes.values():
    if v == 'a':
        votes_a += 1
    elif v == 'b':
        votes_b += 1
    elif v == 'c':
        votes_c += 1

# declare the winner
if votes_a > votes_b and votes_a > votes_c:
    winner = 'a'
elif votes_b > votes_a and votes_b > votes_c:
    winner = 'b'
else:
    winner = 'c'

# print results
print("Votes for candidate 'a': ", votes_a)
print("Votes for candidate 'b': ", votes_b)
print("Votes for candidate 'c': ", votes_c)
print("Winner: ", winner)

##Output
##Votes for candidate 'a':  15
##Votes for candidate 'b':  8
##Votes for candidate 'c':  7
##Winner:  a
