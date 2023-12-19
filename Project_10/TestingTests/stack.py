# exmaple class with tests in pytest - wklejamy do pycharma i testujemy
# Poniższa klasa reprezentuje stos (stack), a także zestaw testów dla tej klasy, napisanych w bibliotece pytest

# Importuje potrzebne moduły i biblioteki
from typing import List
import pytest

# Definiuje klasę Stack do reprezentowania stosu
class Stack:
    # Inicjalizuje stos jako pustą listę (poniższe operacje są więc wykonywane na liście)
    def __init__(self):
        self._items: List[int] = []

    # Dodaje element na wierzch stosu
    def push(self, item: int):
        self._items.append(item)

    # Usuwa i zwraca element z wierzchu stosu
    def pop(self) -> int:
        return self._items.pop()

    # Sprawdza, czy stos jest pusty
    def is_empty(self) -> bool:
        return len(self._items) == 0

    # Zwraca element na wierzchu stosu, ale nie usuwa go
    def peek(self) -> int:
        return self._items[-1]

    # Zwraca liczbę elementów na stosie
    def size(self) -> int:
        return len(self._items)

