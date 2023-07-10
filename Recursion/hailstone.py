def hail(n):
    if n == 1:
        print()
    elif n % 2 == 0:
        print(int(n/2))
        hail(n/2)
    else:
        print(int(3*n + 1))
        hail(3*n +1)
        
