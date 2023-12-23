import math, json


class Ułamek():
    def fix(self):
        if (self.mianownik < 0):
            self.mianownik *= -1
            self.licznik *= -1
        gcd = math.gcd(self.licznik, self.mianownik)
        self.licznik //= gcd
        self.mianownik //= gcd

    def __init__(self, licznik, mianownik):
        if mianownik == 0:
            raise ValueError("Mianownik nie może być zerem.")
        self.licznik = licznik
        self.mianownik = mianownik
        self.fix()

    def __str__(self):
        return str(self.licznik) + "/" + str(self.mianownik)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.licznik}/{self.mianownik})"


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

    def dict(self):
        return {"licznik": self.licznik, "mianownik": self.mianownik}

    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            file.write(self.__str__())

    @classmethod
    def read_from_file(cls, file_path):
        with open(file_path, 'r') as file:
            data = file.read().split("/")
            return cls(int(data[0]), int(data[1]))
