# NumPy - Numerical Python

NumPy to fundamentalna biblioteka do obliczeń naukowych w języku Python. Dostarcza wydajne struktury danych (tablice wielowymiarowe) oraz narzędzia do pracy z nimi.

## Kluczowe cechy
- Potężny obiekt tablicy N-wymiarowej (`ndarray`).
- Funkcje do operacji na całych tablicach bez konieczności używania pętli `for` (wektoryzacja).
- Narzędzia do integracji z kodem C/C++ i Fortran.
- Liniowa algebra, transformata Fouriera i generator liczb losowych.

## Przykłady użycia

### Tworzenie tablic
```python
import numpy as np

# Tworzenie tablicy z listy
a = np.array([1, 2, 3, 4, 5])

# Tablica wypełniona zerami
zeros = np.zeros((2, 3))

# Tablica z zakresem wartości
range_arr = np.arange(0, 10, 2)
```

### Operacje matematyczne
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Dodawanie element po elemencie
c = a + b  # array([5, 7, 9])

# Mnożenie przez skalar
d = a * 2  # array([2, 4, 6])
```

## Przypadki użycia
- Analiza danych statystycznych.
- Przetwarzanie obrazów (obrazy jako tablice pikseli).
- Symulacje numeryczne.
- Podstawa dla innych bibliotek, takich jak Pandas czy Scikit-learn.

## Dokumentacja
[Oficjalna dokumentacja NumPy](https://numpy.org/doc/)
