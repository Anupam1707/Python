#To figure out the longest sub string from a string
#lngstr.py
#1-11-22
#By Anupam Kanoongo

print("Welcome to the Statement Sorter")
print()
mx = ""
ln = 0
m = 0
st = str(input("Enter your Statement : "))

a = st.split()

l = len(a)

for i in range(l):
     ln = len(a[i])
     if ln>m:
         m=ln
         mx=a[i]
         
print("The longest substring of ","'",st,"'","is","'",mx,"'")

##Output
##Welcome to the Statement Sorter
##
##Enter your Statement : Life is an Icecream
##The longest substring of  ' Life is an Icecream ' is ' Icecream '
