import sys
import math
def g(x, n):
  return (x * x + 1) % n 
def Euclide_Extend(a, b):
    if a == 1:
        return 1, 0
    x_, y_ = Euclide_Extend(b, a % b)
    x = y_
    y = x_ - (a // b) * y_
    return x, y

def GCD(x, y):
    if x % y == 0:
        return y 
    else:
        return GCD(y, x % y)
def Pollard_factorising( n):
        x = 2
        d = 1
        y = 2
        while d == 1:
            x = g(x, n)
            y = g(g(y, n), n)
            d = math.gcd(abs(x - y), n)
        return d, n // d
def powmod(a, b, c):
    if b == 0:
        return 1
    b0 = b >> 1
    power = powmod(a, b0, c)
    power = (power * power) % c  
    if b & 1 == 0:
        return power 
    else:
        return (power * a) % c
def bytes_to_long(string):
    ret = 0
    for char in string:
        ret *= 256
        ret += ord(char)
    return ret
def long_to_bytes(number):
    ret = ""
    while number > 0:
        ret = chr(number % 256) + ret
        number //= 256
    return ret

if __name__ == "__main__":
    if sys.argv[1] == "encrypt":
        plain = input("Input plain text:")
        e = int(input("Input public key e:"))
        n = int(input("Input public key n:"))

        m = bytes_to_long(plain)
        cipher = powmod(m, e, n)
        print("String encrypted : ", cipher)
    
    elif sys.argv[1] == "decrypt":
        cipher = int(input("Input cipher text:"))
        e = int(input("Input public key e:"))
        n = int(input("Input public key n : "))

        result = Pollard_factorising(n)
        if result == -1:
            print("N cannot be prime")
            exit(0)

        p, q = result
        phi = (p - 1) * (q - 1)
        if GCD(phi, e) != 1:
            print("GCD(phi, e) must be 1")
            exit(0)
        tmp, d = Euclide_Extend(phi, e)
        if(d < 0):
            d += phi
        print(tmp," ", d)
        m = powmod(cipher, d, n)
        plain = long_to_bytes(m)
        print("Plain text is : ", plain)