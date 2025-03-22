import unittest
from my_awesome_lib.text_processing import count_words, remove_punctuation, reverse_text


class TestTextProcessingFunctions(unittest.TestCase):

    # Testowanie funkcji count_words
    def test_count_words(self):
        # Testujemy różne przypadki
        self.assertEqual(count_words("Ala ma kota"), 3)  # Trzy słowa
        self.assertEqual(count_words("   "), 0)  # Pusty tekst (spacje)
        self.assertEqual(count_words("Hello world!"), 2)  # Dwa słowa z interpunkcją
        self.assertEqual(count_words("Python 123 test."), 3)  # Trzy słowa (liczby też są traktowane jako słowa)

    # Testowanie funkcji remove_punctuation
    def test_remove_punctuation(self):
        # Testujemy, czy usuwane są wszystkie znaki interpunkcyjne
        self.assertEqual(remove_punctuation("Hello, world!"), "Hello world")  # Usunięcie przecinka i wykrzyknika
        self.assertEqual(remove_punctuation("Ala ma kota."), "Ala ma kota")  # Usunięcie kropki
        self.assertEqual(remove_punctuation("Python..."), "Python")  # Usunięcie wielokropka
        self.assertEqual(remove_punctuation("!@#$%^&*()_+"), "")  # Usunięcie wszystkich znaków interpunkcyjnych
        self.assertEqual(remove_punctuation("No punctuation here"), "No punctuation here")  # Brak zmian w tekście

    # Testowanie funkcji reverse_text
    def test_reverse_text(self):
        # Testujemy poprawność odwrócenia tekstu
        self.assertEqual(reverse_text("Ala"), "alA")  # Odwrócony tekst
        self.assertEqual(reverse_text("Hello, world!"), "!dlrow ,olleH")  # Odwrócenie tekstu z interpunkcją
        self.assertEqual(reverse_text("Python123"), "321nohtyP")  # Odwrócenie tekstu z liczbami
        self.assertEqual(reverse_text(""), "")  # Test pustego tekstu (brak zmiany)
        self.assertEqual(reverse_text("   "), "   ")  # Odwrócenie tekstu z samymi spacjami


if __name__ == "__main__":
    unittest.main()
