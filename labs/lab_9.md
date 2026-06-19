# Laboratorium 9: Analiza szeregów czasowych

## Cel laboratorium
Opanowanie technik pracy z danymi zależnymi od czasu przy użyciu biblioteki Pandas.

## 1. Konwersja na Datetime
Praca z czasem wymaga poprawnego typu danych w kolumnach.

### Zadanie 1: Przygotowanie danych
1. Wczytaj plik `data/Halloween.csv`.
2. Sprawdź typy danych kolumn.
3. Przekonwertuj kolumnę zawierającą datę na typ `datetime` (użyj `pd.to_datetime`).
4. Ustaw tę kolumnę jako indeks DataFrame.

## 2. Wybieranie zakresów i Resampling
Dzięki indeksowi czasowemu możemy łatwo filtrować dane.

### Zadanie 2: Agregacja czasowa
1. Wybierz dane tylko dla konkretnego roku (np. 2016).
2. Oblicz średnią popularność frazy "Halloween" w skali miesiąca (użyj `.resample('M').mean()`).
3. Stwórz wykres liniowy pokazujący zmiany popularności w czasie.

## 3. Analiza trendów i okna przesuwne
Wygładzanie danych pozwala lepiej widzieć trendy długoterminowe.

### Zadanie 3: Średnia krocząca
1. Oblicz średnią kroczącą z 7 dni (window=7) dla danych z pliku.
2. Na jednym wykresie narysuj dane oryginalne oraz średnią kroczącą (użyj różnych kolorów).
3. Dodaj legendę i tytuł wykresu.

## Dokumentacja
Szukaj informacji o "Time Series" w oficjalnej dokumentacji Pandas lub w lokalnym pliku `docs/pandas.md`.
