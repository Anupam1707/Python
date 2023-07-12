def high(num):
    digits = list(str(num))

    a = len(digits) -2
    while a >= 0 and digits[a] >= digits[a +1]:
        a -= 1

    b = len(digits) -1
    while digits[b] < digits[a]:
        b -= 1

    digits[a], digits[b] = digits[b], digits[a]
    n = int("".join(digits))
    return n
