# Wykład 1: Wprowadzenie do Obróbki i Analizy Danych

## 1. Czym jest analiza danych?

Analiza danych to proces inspekcji, czyszczenia, transformacji i modelowania danych w celu odkrycia przydatnych informacji, sformułowania wniosków i wsparcia procesu decyzyjnego.

### Cykl życia analizy danych
```mermaid
graph LR
    A[Definicja problemu] --> B[Pozyskanie danych]
    B --> C[Obróbka/Czyszczenie]
    C --> D[Eksploracja - EDA]
    D --> E[Modelowanie/Wnioski]
    E --> F[Komunikacja wyników]
    F --> A
```

## 2. Architektura narzędzi w Pythonie

Python stał się standardem w analizie danych dzięki bogatemu ekosystemowi bibliotek:

- **NumPy**: Obliczenia numeryczne, operacje macierzowe.
- **Pandas**: Manipulacja danymi tabelarycznymi.
- **Matplotlib/Seaborn**: Wizualizacja danych.
- **Scikit-learn**: Machine Learning.

## 3. Fundament: NumPy

NumPy (`Numerical Python`) wprowadza obiekt `ndarray` – wielowymiarową tablicę o wysokiej wydajności.

### Dlaczego NumPy?
- **Szybkość**: Operacje są zoptymalizowane w C.
- **Wygoda**: Operacje wektorowe zamiast pętli.
- **Pamięć**: Mniejsze zużycie pamięci niż listy Pythona.

### Przykład praktyczny: Wektoryzacja
Zamiast pętli `for` do dodawania dwóch list:
```python
import numpy as np

# Pythonowe listy
a = [1, 2, 3]
b = [4, 5, 6]

# NumPy
na = np.array([1, 2, 3])
nb = np.array([4, 5, 6])

# Operacja wektorowa
wynik = na + nb
print(wynik) # [5 7 9]
```

## 4. Podstawowe pojęcia NumPy
- **Shape**: Kształt tablicy (np. `(3, 3)` dla macierzy).
- **Dtype**: Typ danych (int64, float64).
- **Broadcasting**: Mechanizm pozwalający na operacje między tablicami o różnych kształtach.

## 5. Podsumowanie
Wykład wprowadził w świat analizy danych i pokazał fundament, na którym budowane są kolejne biblioteki. Na laboratorium przećwiczymy konfigurację środowiska i operacje na macierzach.
