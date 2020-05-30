import base64
import math
import MyMath
def g(x, n):
  return (x * x + 1) % n 
class decrypt:
    def Euclide_Extend(self, a, b):
        if a == 1:
            return 1, 0
        x_, y_ = self.Euclide_Extend(self, b, a % b)
        x = y_
        y = x_ - (a // b) * y_
        return x, y
    def normal_factorising(self, n):
        if n % 2 == 0:
            return 2, n // 2
        i = 3
        while(i * i <= n):
            if n % i == 0:
                return i, n // i
            i += 2
    def Pollard_factorising(self, n):
        x = 2
        d = 1
        y = 2
        while d == 1:
            x = g(x, n)
            y = g(g(y, n), n)
            d = math.gcd(abs(x - y), n)
        return d, n // d

    def decrypt(self, cipher, n, e):
        c = int(cipher, 16)
        if n < 1e10:
            p, q = self.normal_factorising(self, n)
        elif n < 1e28:
            p, q = self.Pollard_factorising(self, n)
        else:
            print("N too big")
            exit(0)
        
        phi = (p - 1) * (q - 1)
        d, tmp = self.Euclide_Extend(self, e, phi)
        if d < 0:
            d += phi
        m = MyMath.powmod(c, d, n)
        plain = MyMath.long_to_bytes(m)

        return plain