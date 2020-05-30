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
def powmod( a, b, c):
    if b == 0:
        return 1
    b0 = b >> 1
    power = powmod( a, b0, c)
    power = (power * power) % c  
    if b & 1 == 0:
        return power 
    else:
        return (power * a) % c