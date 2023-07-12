def high(num):
    a = 0
    s = str(num)
    ls = list(s)
    ls.sort()

    def loop(ls, idx):
        if idx == 0:
            temp = []
            temp.append(ls[-1])
            ls.remove(ls[-1])
            temp.extend(ls)
            print(temp)
            return temp
        
        else:
            temp = []
            temp.extend(ls[:idx-1])
            for i in range(idx):
                ls.remove(ls[i])
            temp.append(ls[-1])
            ls.remove(ls[-1])
            temp.extend(ls)
            print(temp)
            return temp
        
    n = "".join(loop(ls, a))
    n = int(n)
    
    if n > num:
            print(n)
            
    elif n == num:
        print("No Higher Number")
 
##    else:
##        while n < num:
##            n = "".join(loop(ls,a+1))
##            n = int(n)
##            print(n)
