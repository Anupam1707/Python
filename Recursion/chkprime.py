def chkprime(num, test = 2):
    if num != test:
        remainder = num%test
        while test <= num:
            if remainder == 0:
                return "Not Prime"
            elif test < num:
                return chkprime(num, test+1)
    else:
        return "Prime"
