import random
from fractions import Fraction
from math import gcd


class RSA:
    a = 0  # first prime number
    b = 0  # second prime number
    c = 0  # product between a and b
    e = 0  # coprime value with phi function
    d = 0

    def __init__(self):
        self.a = 0
        self.b = 0

    def check_if_prime(self, num):
        # to check if a namber is prime, it is sufficient to
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True

    def main(self):
        self.a = random.randint(10, 500)
        self.b = random.randint(10, 500)
        while (self.check_if_prime(self.a) != True):
            self.a = random.randint(10, 500)

        while (self.check_if_prime(self.b) != True):
            self.b = random.randint(10, 500)

        self.c = self.a * self.b
        phi = self.phi(self.a, self.b)
        self.e = self.coprime(self.phi(self.a, self.b))
        self.d = self.mod_inverse(self.e,phi)
        print(self.a, self.b, self.c, phi, self.e, self.d)

    def phi(self, a, b):
        return (a - 1) * (b - 1)

    def coprime(self, n):
        # Find largest coprime to n and return it
        j = 1
        for i in range(2, (n - 1)):
            if Fraction(gcd(n, i)) == 1:  # Coprime
                j = i
        return j

    def encrypt(self, msg):
        formatted = ((ord(chr)) for chr in msg)
        encrypted = []
        for chr in formatted:
            chrEnc = pow(int(chr), self.e, self.c)
            encrypted.append(chrEnc)

        return encrypted

    def decrypt(self, msg):
        decrypted = ""
        for chrs in msg:
            decrypted += chr(pow(chrs, self.d, self.c))

        return decrypted


    def mod_inverse(self, x,y):

        def eea(a,b):
            if b==0:return (1,0)
            (q,r) = (a//b,a%b)
            (s,t) = eea(b,r)
            return (t, s-(q*t) )

        inv = eea(x,y)[0]
        if inv < 1: inv += y
        return inv
