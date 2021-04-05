class Complex:

    def __init__(self, re = 0, im = 0):
        self.re = re
        self.im = im

    def __str__(self):
        return "{} {} {}i".format(self.re, '+' if self.im >= 0 else '-', abs(self.im))

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Complex(self.re - other.re, self.re - other.im)

    def __neg__(self):
        return Complex(-self.re, -self,im)

    def conjugate(self):
        return Complex(self.re, -self.im)

    def __mul__(self, other):
        re = self.re * other.re - self.im * other.im
        im = self.im * other.re + self.re * other.im
        return Complex(re, im)

    def __truediv__(self, other):
        conj = other.conjugate()

        den = other * conj
        den = den.re

        num = self * conj
        return Complex(num.re/den, num.im/den)

c1 = Complex(10, 20)
c2 = Complex(1, -2)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)