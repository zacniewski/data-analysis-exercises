# Laboratorium 3: Biblioteka Pandas i EDA

## Cel laboratorium
Zapoznanie się z podstawami biblioteki Pandas oraz przeprowadzenie Eksploracyjnej Analizy Danych (EDA).

## 1. Wprowadzenie do Pandas

### Zadanie 1: Tworzenie DataFrame
Stwórz skrypt `lab3_df.py`, który:
1. Utworzy obiekt DataFrame z słownika zawierającego dane 5 osób (Imię, Nazwisko, Wiek, Miasto).
2. Wyświetli tylko kolumnę 'Imię'.
3. Wyświetli osoby starsze niż 25 lat.

## 2. Praca na rzeczywistym zbiorze danych

Wykorzystamy plik `data/worldcities.csv`.

### Zadanie 2: Wstępna analiza (EDA)
1. Wczytaj plik `worldcities.csv`.
2. Wyświetl pierwsze 10 wierszy.
3. Sprawdź liczbę wierszy i kolumn (`.shape`).
4. Wyświetl podstawowe statystyki opisowe dla kolumn numerycznych (`.describe()`).
5. Sprawdź, czy w danych występują braki (`.isnull().sum()`).

### Zadanie 3: Filtrowanie i sortowanie
1. Wyświetl wszystkie miasta z Polski.
2. Znajdź 5 najbardziej zaludnionych miast w zbiorze danych.
3. Posortuj miasta alfabetycznie według nazwy.

## 3. Praca z istniejącymi przykładami
Uruchom i przeanalizuj skrypt `scripts/pandas1.py`. Zwróć uwagę na to, jak wczytywane są dane i jak nazywane są pliki wynikowe.

## Dokumentacja
Szukaj informacji w `docs/pandas.md`.
