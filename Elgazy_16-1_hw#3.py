class Fraction :

    def __init__ (self, numerator , denumerator):
        self.num=numerator
        self.denum=denumerator

    def __add__(self, otherfraction ):
        a = self.num * otherfraction.denum + self.denum * otherfraction.num
        b = self.denum * otherfraction.denum
        print(f'{self.num}/{self.denum} + {otherfraction.num}/{otherfraction.denum} = ')
        return f'Answer is {a}/{b}'

    def __sub__(self,otherfraction):
        a = self.num * otherfraction.denum - self.denum * otherfraction.num
        b = self.denum * otherfraction.denum
        print(f'{self.num}/{self.denum} - {otherfraction.num}/{otherfraction.denum} = ')
        return f'Answer is {a}/{b}'

    def __mul__(self,otherfraction):
        a = self.num * otherfraction.denum 
        b = self.denum * otherfraction.num
        print(f'{self.num}/{self.denum} * {otherfraction.num}/{otherfraction.denum} = ')
        return f'Answer is {a}/{b}'

    def __floordiv__(self,otherfraction):
        a = self.num  //  otherfraction.num
        b = self.denum // otherfraction.denum
        print(f'{self.num}/{self.denum} // {otherfraction.num}/{otherfraction.denum} = ')
        return f'Answer is {a}/{b}'

x = Fraction(2,3)
y = Fraction(3,7)
print(x // y)