import math, random, sys

class Ułamek:
    # Wersja2 __slots__ = ('licznik', 'mianownik') 
    
    def fix(self):
        if (self.mianownik < 0):
            self.mianownik *= -1
            self.licznik *= -1
        gcd = math.gcd(self.licznik, self.mianownik)
        self.licznik //= gcd
        self.mianownik //= gcd
    
    def __init__(self, licznik, mianownik):
        assert(mianownik != 0)
        self.licznik = licznik
        self.mianownik = mianownik
        self.fix()
        
    def __str__(self):
        return str(self.licznik) + "/" + str(self.mianownik)
    
    def __repr__(self):
        return Ułamek.__str__(self)
    
    def __eq__(self, other):
        return self.mianownik == other.mianownik and self.licznik == other.licznik
    
    def __gt__(self, other):
        return self.licznik * other.mianownik > self.mianownik * other.licznik
    
    def __ge__(self, other):
        return Ułamek.__eq__(self, other) or Ułamek.__gt__(self, other)
    
    def __add__(self, other):
        return Ułamek(self.licznik * other.mianownik + self.mianownik * other.licznik, self.mianownik * other.mianownik)
    
    def __sub__(self, other):
        return Ułamek.__add__(self, other * Ułamek(-1, 1))
	
    def __mul__(self, other):
        return Ułamek(self.licznik * other.licznik, self.mianownik * other.mianownik)
    
    def __truediv__(self, other):
        return Ułamek.__mul__(self, Ułamek(other.mianownik, other.licznik))

    

n = int(sys.argv[1])
k = int(sys.argv[2])

arr = [Ułamek(random.randint(-100, 100), random.randint(1, 200)) for _ in range(n)]

for i in range(k):
    arr[i % n] += arr[(i + 1) % n]


