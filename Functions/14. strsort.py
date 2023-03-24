#To arrange l alphabetically separated by hyphens
#strsort.py
#24-3-23
#By Anupam Kanoongo

print("Welcome to the String Sorter")
print()

def srt(st):
    s = ""
    l = st.split("-")
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    for i in l:
        s += i + "-"
    return s

s = str(input("Enter a String separated by Hyphens : "))
r = srt(s)

print("Unsorted : ",s)
print("Sorted : ",r)

##Output
##Welcome to the String Sorter
##
##Enter a String separated by Hyphens : daly-college-indore-madhya-pradesh
##Unsorted :  daly-college-indore-madhya-pradesh
##Sorted :  college-daly-indore-madhya-pradesh-
