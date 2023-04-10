#To add 1 to even numbers and remove 1 from odd
#By Anupam Kanoongo

def lst(ls): 
    for i in range(len(ls)):
        if ls[i]%2 == 0:
            ls[i] = ls[i]+1
        else :
            ls[i] = ls[i]-1           
    return ls

ls = eval(input("Enter a List : "))
l = lst(ls)
print(l)
