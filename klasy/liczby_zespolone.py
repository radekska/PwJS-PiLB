"""
Zdefiniuj klasę reprezentującą liczby zespolone (wraz z funkc- jami na nich działającymi np. dodawanie, odejmowanie itd.)
"""

class LiczbyZespolone:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __check_valid(self, complex_object):
        if isinstance(complex_object, LiczbyZespolone):
            return True
        else:
            raise ValueError('Objekt nie nalezy do liczb zespolonych!')


    def __repr__(self):
        return 'Re:{real:.2f}, Im:{imag:+.2f}i'.format(real=self.real, imag=self.imaginary)

    def __str__(self):
        return '{real:.2f}{imag:+.2f}i'.format(real=self.real, imag=self.imaginary)

    def __add__(self, complex_object):
        if self.__check_valid(complex_object):
            real = self.real + complex_object.real
            imaginary = self.imaginary + complex_object.imaginary
            
            return LiczbyZespolone(real, imaginary)

    def __sub__(self, complex_object):
        if self.__check_valid(complex_object):
            real = self.real - complex_object.real
            imaginary = self.imaginary - complex_object.imaginary
            
            return LiczbyZespolone(real, imaginary)
        

    def __mul__(self, complex_object):
        if self.__check_valid(complex_object):
            real = self.real * complex_object.real +  ( -1 * self.imaginary * complex_object.imaginary)
            imaginary = (self.imaginary * complex_object.real)  + (self.real * complex_object.imaginary)

            return LiczbyZespolone(real, imaginary)
        
    def __truediv__(self, complex_object):
        if self.__check_valid(complex_object):
            conjugate = LiczbyZespolone(complex_object.real, -complex_object.imaginary)

            numerator = self * conjugate
            denominator = complex_object * conjugate

            return LiczbyZespolone(numerator.real / denominator.real, numerator.imaginary / denominator.real)






# print('### PRZYKŁADOWE LICZBY ###')
# moja_liczba = LiczbyZespolone(12, -13)
# moja_liczba_2 = LiczbyZespolone(15, 30)
# print(repr(moja_liczba))
# print(repr(moja_liczba_2))


# print('### DODAWANIE ###')
# print('### 1 sposób ###')
# moja_liczba_3 = moja_liczba + moja_liczba_2
# print(moja_liczba_3)

# print('### 2 sposób ###')
# print(moja_liczba.__add__(moja_liczba_2))

# print('### ODEJMOWANIE ###')
# moja_liczba_3 = moja_liczba - moja_liczba_2
# print(moja_liczba_3)

# print('### MNOŻENIE ###')
# print(moja_liczba * moja_liczba_2)

# print('### DZIELENIE ###')
# moja_liczba = LiczbyZespolone(1, 8)
# moja_liczba_2 = LiczbyZespolone(2, 3)

# print(moja_liczba / moja_liczba_2)

