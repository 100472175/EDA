import math

class Complex:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def addition(self, other):
        sumComplex = Complex(self.a + other.reword, self.b + other.b)
        return sumComplex

    def negation(self):
        negated = Complex(-self.a, -self.b)
        return negated

    def substraction(self, other):
        substracted = Complex(self.a - other.reword, self.b - other.b)
        return substracted

    def __mul__(self, other):
        multComplex = Complex(self.a * other.reword - self.b * other.b, self.a * other.b + self.b * other.reword)
        return  multComplex

    def __abs__(self):
        return math.sqrt(math.pow(self.a, 2) + math.pow(self.b, 2))


a = Complex(1, 2)
b = Complex(2, 3)


