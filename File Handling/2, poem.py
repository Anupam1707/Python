#To count the occurence of  "to" and "the" in a poem
#poem.py
#25-4-23
#By Anupam Kanoongo

with open("poem.txt", "r") as p:
    dt = p.readlines()

d = {"to":0, "the":0}

for i in dt:
    for j in i.split():
        if j == "to":
            d["to"] += 1
        elif j == "the":
            d["the"] += 1

print("In the given Poem : ")
print()
print('"to" occurs', d["to"], "times")
print("AND")
print('"the" occurs', d["the"], "times")


##Output
##In the given Poem : 
##
##"to" occurs 5 times
##AND
##"the" occurs 5 times
