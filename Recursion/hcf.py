def hcf_recursive(a, b):
    if b == 0:
        return a
    else:
        return hcf_recursive(b, a % b)
