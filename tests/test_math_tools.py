import unittest
from my_awesome_lib.math_tools import add, subtract, multiply, divide


class TestMathFunctions(unittest.TestCase):

    # Test dla funkcji add
    def test_add(self):
        # Normalne dodawanie
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(1.5, 2.5), 4.0)  # Dodawanie liczb zmiennoprzecinkowych

        # Przypadki brzegowe
        self.assertEqual(add(0, 5), 5)  # Dodawanie do zera
        self.assertEqual(add(-5, 0), -5)  # Dodawanie z zerem

        # Bardzo duże liczby
        self.assertEqual(add(1e+100, 1e+100), 2e+100)  # Dodawanie bardzo dużych liczb

    # Test dla funkcji subtract
    def test_subtract(self):
        # Normalne odejmowanie
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(2.5, 1.5), 1.0)  # Odejmowanie liczb zmiennoprzecinkowych

        # Przypadki brzegowe
        self.assertEqual(subtract(0, 5), -5)  # Odejmowanie od zera
        self.assertEqual(subtract(-5, -3), -2)  # Odejmowanie liczb ujemnych

    # Test dla funkcji multiply
    def test_multiply(self):
        # Normalne mnożenie
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-3, 3), -9)
        self.assertEqual(multiply(1.5, 2), 3.0)  # Mnożenie liczb zmiennoprzecinkowych

        # Przypadki brzegowe
        self.assertEqual(multiply(0, 5), 0)  # Mnożenie przez zero
        self.assertEqual(multiply(5, 0), 0)  # Mnożenie przez zero
        self.assertEqual(multiply(0, 0), 0)  # Mnożenie przez zero

    # Test dla funkcji divide
    def test_divide(self):
        # Normalne dzielenie
        self.assertEqual(divide(6, 3), 2.0)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(0, 5), 0.0)  # Dzielenie przez liczbę różną od 0

        # Przypadki brzegowe
        self.assertEqual(divide(5, 0), "Błąd: dzielenie przez zero")  # Dzielenie przez zero
        self.assertEqual(divide(-5, 0), "Błąd: dzielenie przez zero")  # Dzielenie przez zero

        # Dzielenie przez bardzo małą liczbę
        self.assertEqual(divide(1, 1e-100), 1e+100)  # Dzielenie przez bardzo małą liczbę (wielka liczba wyniku)

        # Dzielenie przez liczbę ujemną
        self.assertEqual(divide(5, -2), -2.5)  # Dzielenie przez liczbę ujemną

        # Dzielnie liczb zmiennoprzecinkowych
        self.assertEqual(divide(7.5, 2.5), 3.0)


if __name__ == '__main__':
    unittest.main()
