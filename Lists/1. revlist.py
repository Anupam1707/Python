#To reverse the elements of a list
#revlist.py
#4-11-22
#By Anupam Kanoongo

print("Welcome to the List Reverser")
print()
print("Enter your list")
print()

ls = eval(input())
print()
nls = []

nls = ls[ : : -1]

print("Reversed List :-")
print()
print(nls)

##Welcome to the List Reverser
##
##Enter your list
##
##['The','Daly','College']
##
##Reversed List :-
##
##['College', 'Daly', 'The']
