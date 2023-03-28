ls=[]
def space (n):
    for i in range(n):
        print(" ",end="")

def PT( no):
    
    m=[]
    for i in range(1,no+1):
        if i==1 :
            ls.append([i])
        elif i==2 :
            m=[1,1]
            ls.append(m)
        else :
            t=[1]
            for p in range(1,len(m)):
                t.append(m[p-1]+ m[p])
            t.append(1)
            ls.append(t)
            m=t
        
PT(4)
for i in ls:
    space(20-len(i*2))
    for j in i :
        print(j,end="   ")
    print()
