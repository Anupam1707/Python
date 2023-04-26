#To ensure that an email is belonging to "@dalycollege.org"
#emlchk.py
#20-10-22
#By Anupam Kanoongo

print("Welcome to the Daly College Email Verifier")
print()

eml = str(input("Enter Your Email : "))
dc = "dalycollege.org"

l = eml.split("@")

if l[1] != dc:
    print("The Email : ",eml,"belongs to",l[1],"not to",dc)
else :
    print("The Email : ",eml,"belongs to",dc)

##Output
##Welcome to the Daly College Email Verifier
##
##Enter Your Email : anupamkanoongo@gmail.com
##The Email :  anupamkanoongo@gmail.com belongs to gmail.com not to dalycollege.org