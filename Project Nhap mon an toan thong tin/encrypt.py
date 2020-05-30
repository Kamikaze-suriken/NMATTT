import base64
from generate_prime import generate
from  MyMath import *
class encrypt:
    e = 0
    n = 0
    
    def __init__(self, e, n):
        self.e = e 
        self.n = n 

    def encrypt(self, plain, n, e):
        m = bytes_to_long(plain)
        cipher = powmod( m, e, n)
        print(cipher)
        return hex(cipher)[2:]
    
    def encrypt_r(self, plain):
        p = generate(40)
        q = generate(40)

        self.e = generate(16)
        self.n = p * q 

        print("e = ", self.e)
        print("n = ", self.n)
        m = bytes_to_long(plain)
        cipher = powmod( m, self.e, self.n)
        return hex(cipher)[2:]
