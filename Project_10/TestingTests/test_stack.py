from stack import * 

# Definiuje zestaw testów dla klasy Stack
def test_stack():
    # Tworzy obiekt Stack
    stack = Stack()

    # Sprawdza, czy stos jest pusty po utworzeniu
    assert stack.is_empty()

    # Dodaje trzy elementy do stosu
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # Sprawdza, czy size() zwraca 3
    assert stack.size() == 3

    # Sprawdza, czy peek() zwraca 3 (ostatni dodany element)
    assert stack.peek() == 3

    # Usuwa trzy elementy ze stosu i sprawdza, czy zwracają odpowiednie wartości
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1

    # Sprawdza, czy stos jest pusty po zakończeniu operacji
    assert stack