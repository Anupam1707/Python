def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm_recursive(numbers):
    if len(numbers) == 2:
        return lcm(numbers[0], numbers[1])
    else:
        return lcm(numbers[0], lcm_recursive(numbers[1:]))
