# Pandas - Data Analysis Library

Pandas to najpopularniejsza biblioteka do manipulacji i analizy danych w Pythonie. Oferuje intuicyjne struktury danych do pracy z danymi tabelarycznymi (podobnie jak w Excelu czy SQL).

## Główne struktury danych
- **Series**: Jednowymiarowa tablica (kolumna).
- **DataFrame**: Dwuwymiarowa struktura danych (tabela).

## Przykłady użycia

### Tworzenie DataFrame i wczytywanie danych
```python
import pandas as pd

# Tworzenie z słownika
data = {
    'Imię': ['Anna', 'Jan', 'Marek'],
    'Wiek': [25, 30, 22]
}
df = pd.DataFrame(data)

# Wczytywanie z pliku CSV
# df = pd.read_csv('data/dane.csv')
```

### Podstawowe operacje
```python
# Wyświetlenie pierwszych wierszy
print(df.head())

# Filtrowanie danych
starszy_niz_25 = df[df['Wiek'] > 25]

# Grupowanie i agregacja
# df.groupby('Kategoria').mean()
```

## Przypadki użycia
- Czyszczenie i przygotowywanie danych (Data Wrangling).
- Analiza szeregów czasowych.
- Statystyka opisowa.
- Integracja z bazami danych i arkuszami kalkulacyjnymi.

## Dokumentacja
[Oficjalna dokumentacja Pandas](https://pandas.pydata.org/docs/)
