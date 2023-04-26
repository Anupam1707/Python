#To remove all capitalisations and punctuations from a string
#2-11-22
#rmvcp.py
#By Anupam Kanoongo

print("Welcome to the Capitalisation and Punctuation Remover")
print()
print("Enter you Sentence (Give SPACES for clear result)  :-")
print()
st = str (input())
print()
nst = ""
sp = st.split()


for j in sp:
    for i in j:
        if i.isupper() or i == "." or i == "," or i == ";" or i == "!"or i == ":" \
            or i == "'" or i == "(" or i == ")" or i == "[" or i == "]" or i == '"' \
            or i == "-" or i == "_" or i == "/" or i == "@" or i == "{" or i == "}" or i == "*":
            pass
        else :
            nst = nst+i
    nst = nst + " "

print("The Cleaned Sentence :-")
print()
print(nst)


##Output
##Welcome to the Capitalisation and Punctuation Remover
##
##Enter you Sentence (Give SPACES for clear result)  :-
##
##"(English Grammar teacher)", [said to {Smith}] , "is useless  !!!! ".
##
##The Cleaned Sentence :-
##
##nglish rammar teacher said to mith  is useless   
