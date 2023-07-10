def happy(n):
    sum = 0
    if n == 1:
        print("yes")
    elif n < 10:
        print("no")
    else:
        st = str(n)
        for i in st:
            sum += int(i)**2
        happy(sum)
