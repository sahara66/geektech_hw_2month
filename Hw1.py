class Fraction:

    def __init__(self, num, denum):
        if denum == 0:
            raise ValueError("Denominator can't 0!")
        self.num = num
        self.denum = denum

    def add(self, other):
        num = self.num * other.denum + other.num * self.denum
        denum = self.denum * other.denum
        print(num)
        print("-")
        print(denum)

    def sub(self, other):
        num = self.num - other.denum
        denum = self.denum - other.num
        print(num)
        print("-")
        print(denum)

    def div(self, other):
        num = self.num / other.denum
        denum = self.denum * other.num
        print(num)
        print("-")
        print(denum)

    def mul(self, other):
        num = self.num * other.num
        denum = self.denum * other.denum
        print(num)
        print("-")
        print(denum)


fraction1 = Fraction(1, 6)
fraction2 = Fraction(1, 10)
fraction1.mul(fraction2)
fraction1.add(fraction2)
fraction1.sub(fraction2)
fraction1.div(fraction2)
