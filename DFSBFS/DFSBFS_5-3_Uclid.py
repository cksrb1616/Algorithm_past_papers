def ucli(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

print(ucli(192,162))
