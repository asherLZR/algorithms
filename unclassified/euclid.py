def euclid_gcd(a, b):
    while a % b != 0:
        print("a = " + str(a) + "    b = " + str(b))
        a, b = b, a % b
    return b


print(euclid_gcd(356, 132))
