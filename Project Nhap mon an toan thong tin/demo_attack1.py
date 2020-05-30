#cipher text = ......
import MyMath
def Euclide_Extend( a, b):
        if a == 1:
            return 1, 0
        x_, y_ = Euclide_Extend( b, a % b)
        x = y_
        y = x_ - (a // b) * y_
        return x, y
m = 0
e1 = 2788276781
e2 = 2750610521
c1 = 41722827324219154502412894777929708295817269862821442985517165993161893049531
c2 = 44554975419623697543042888877641384509200031600063096793963144597106437406168
n = 52593746111299673917462180378616675287554472293960928632820865884284203124461       #256bit (77 digit)

x, y = Euclide_Extend(e1, e2)
if x < 0:
    tmp, c1_ = Euclide_Extend(n, c1)
    m = (MyMath.powmod(c1_, -x, n) * MyMath.powmod(c2, y, n)) % n
else:
    tmp, c2_ = Euclide_Extend(n, c2)
    m = (MyMath.powmod(c1, x, n) * MyMath.powmod(c2_, -y, n)) % n
print(MyMath.long_to_bytes(m))
