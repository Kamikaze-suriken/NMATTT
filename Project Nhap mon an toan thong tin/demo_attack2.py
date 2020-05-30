import MyMath
import math
e = 3
n = [85925521473296748103996018704230027733200125984333817053970930475975541711523, 
    83615174948154287859085759399916697989157104915237434457839839701285068506089,
     51767953724041873740836080153893846861156404977722683323063538826528922176349]
c = [73657910765302391553405737402005671835058800241542375211295217609294713006370,
    51608173304951244585108004391790897361906904154570748554259030579461544208178,
    21517072358787746870986079362948886518301808743626664983456623218824580040542]
def Euclide_Extend( a, b):
        if a == 1:
            return 1, 0
        x_, y_ = Euclide_Extend( b, a % b)
        x = y_
        y = x_ - (a // b) * y_
        return x, y
def sqrt3(n, a, b):
    if a**3 == n:
        return a
    if b**3 == n:
        return b
    mid = (a + b) // 2
    tmp = mid ** 3
    if tmp == n:
        return mid 
    elif tmp < n:
        return sqrt3(n, mid, b)
    else:
        return sqrt3(n, a, mid)
C = 0
N = n[1] * n[2] * n[0]
for i in range(e):
    x = c[i] * N//n[i]
    a, b = Euclide_Extend(N//n[i], n[i])
    if a < 0:
        a += n[i]
    x *= a
    C += x 

C = C% N
m = sqrt3(C, 0, C//2)
print(MyMath.long_to_bytes(round(m)))