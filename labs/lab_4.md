# Laboratorium 4: Pandas – Czyszczenie i Transformacje

## Cel laboratorium
Opanowanie technik czyszczenia danych, łączenia tabel oraz wykonywania agregacji w Pandas.

## 1. Czyszczenie danych

### Zadanie 1: Obsługa braków
Stwórz DataFrame z celowo wprowadzonymi brakami danych (użyj `np.nan`).
1. Usuń wszystkie wiersze zawierające dowolny brak.
2. W nowym obiekcie, uzupełnij braki średnią wartością z danej kolumny.

## 2. Agregacje i Grupowanie

Użyj pliku `data/Halloween.csv`.

### Zadanie 2: GroupBy
1. Wczytaj dane o Halloween.
2. Zgrupuj dane według kategorii i oblicz średnią wartość dla pozostałych kolumn numerycznych.
3. Sprawdź, która kategoria jest najczęściej reprezentowana w zbiorze.

## 3. Praca z czasem

Użyj pliku `data/film.csv`.

### Zadanie 3: Daty i Tekst
1. Wczytaj dane o filmach.
2. Przekonwertuj kolumnę z rokiem na typ `datetime` (jeśli to możliwe) lub upewnij się, że jest to typ numeryczny.
3. Stwórz nową kolumnę, która będzie zawierać informację "Stary" (rok < 2000) lub "Nowy" (rok >= 2000).

## 4. Wykorzystanie istniejących skryptów
Przeanalizuj pliki `scripts/pandas2.py` do `scripts/pandas5.py`. Zwróć uwagę na metody `merge`, `pivot_table` lub inne zaawansowane operacje tam występujące.

## Dokumentacja
Szukaj informacji w `docs/pandas.md`.
