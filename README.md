# My Awesome Lib

My Awesome Lib to wszechstronna biblioteka w Pythonie, która zawiera zestaw narzędzi do przeprowadzania podstawowych operacji na danych, tekstach oraz matematycznych obliczeń. Biblioteka zawiera funkcje, które pozwalają na manipulację danymi, wykonywanie podstawowych operacji matematycznych, oraz przetwarzanie tekstów.

## Funkcjonalności

Biblioteka obejmuje trzy główne moduły:

- **Math Tools** - Operacje matematyczne, takie jak dodawanie, odejmowanie, mnożenie i dzielenie.
- **Data Utils** - Narzędzia do manipulacji danymi, w tym dodawanie elementów do list, łączenie list oraz usuwanie duplikatów.
- **Text Processing** - Funkcje do przetwarzania tekstów, takie jak liczenie słów, usuwanie znaków interpunkcyjnych i odwracanie tekstu.

## Instalacja

Aby zainstalować bibliotekę lokalnie, wykonaj poniższe kroki:

1. Sklonuj repozytorium:

   ```bash
   git clone https://github.com/Preziu97/zadanie3
   ```

2. Zainstaluj bibliotekę lokalnie:

   ```bash
   pip install -e ./zadanie3
   ```

## Przykłady użycia

### Math Tools

#### Dodawanie

```python
from my_awesome_lib.math_tools import add

result = add(3, 5)
print(result)  # Wynik: 8
```

#### Dzielenie

```python
from my_awesome_lib.math_tools import divide

result = divide(10, 2)
print(result)  # Wynik: 5.0
```

### Data Utils

#### Dodawanie elementu do listy

```python
from my_awesome_lib.data_utils import add_element

my_list = [1, 2, 3]
add_element(my_list, 4)
print(my_list)  # Wynik: [1, 2, 3, 4]
```

#### Łączenie list

```python
from my_awesome_lib.data_utils import merge_data

list1 = [1, 2]
list2 = [3, 4]
result = merge_data(list1, list2)
print(result)  # Wynik: [1, 2, 3, 4]
```

### Text Processing

#### Liczenie słów w tekście

```python
from my_awesome_lib.text_processing import count_words

text = "Ala ma kota"
word_count = count_words(text)
print(word_count)  # Wynik: 3
```

#### Usuwanie interpunkcji

```python
from my_awesome_lib.text_processing import remove_punctuation

text = "Hello, world!"
cleaned_text = remove_punctuation(text)
print(cleaned_text)  # Wynik: "Hello world"
```

#### Odwracanie tekstu

```python
from my_awesome_lib.text_processing import reverse_text

text = "Ala"
reversed_text = reverse_text(text)
print(reversed_text)  # Wynik: "alA"
```

## Testowanie

Biblioteka zawiera zestaw testów jednostkowych sprawdzających poprawność funkcji. Aby je wykonać:

1. Upewnij się, że jesteś w katalogu zadanie3:
```bash
cd zadanie3 
```
2. Uruchom testy używając `unittest`:
```bash
python -m unittest discover tests/
```

Testy obejmują różne scenariusze, w tym przypadki brzegowe oraz błędne dane wejściowe.

## Licencja

Ten projekt jest dostępny na licencji MIT.

## Autorzy

- **Przemysław Kierasiński (98031)**

## Wersja

1.0.0
