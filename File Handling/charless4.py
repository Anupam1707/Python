#To write a function displaywords() to read lines from text file and display words with have chars less than 4
#charless4.py
#27-4-23
#By Anupam Kanoongo

with open("story.txt", "r") as s:
    dt = s.readlines()

def displaywords():
    print("Words with characters less the 4 are : ")
    for i in dt:
        for j in i.split():
            if len(j) < 4:
                print(j)

displaywords()

##Output
##Words with characters less the 4 are : 
##I
##for
##a
##for
##a
##had
##by
##an
##who
##had
##on.
##of
##the
