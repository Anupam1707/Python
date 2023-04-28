#To save all lower case characters in a file "lower.txt", upper case characters in a file "upper.txt" and other characters in "others.txt"
#keyboard.py
#28-4-23
#By Anupam Kanoongo

import sys

def check():
    inp = ""
    while inp == " ":
        inp = input()
        if inp.islower():
            with open("lower.txt", "a") as l:
                l.write(inp)
        elif inp.isupper():
            with opne("upper.txt", "a") as u:
                u.write(inp)
        else:
            with open("others.txt", "a") as o:
                o.write(inp)

check()