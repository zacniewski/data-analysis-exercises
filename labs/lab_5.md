# Laboratorium 5: Wizualizacja danych w praktyce

## Cel laboratorium
Nauczenie się tworzenia różnorodnych wykresów przy użyciu bibliotek Matplotlib i Seaborn na podstawie przetworzonych danych.

## 1. Matplotlib - Podstawy

### Zadanie 1: Wykres liniowy i słupkowy
Stwórz skrypt `lab5_plots.py`, który:
1. Wygeneruje wykres funkcji sinus dla zakresu 0-10.
2. Doda tytuł, opisy osi oraz legendę.
3. Obok (na osobnym rysunku lub subplocie) stworzy wykres słupkowy pokazujący sprzedaż 3 produktów (A, B, C) o wartościach (100, 150, 80).

## 2. Wizualizacja danych z Pandas

Użyj pliku `data/worldcities.csv` lub `data/Countries.csv`.

### Zadanie 2: Histogram i Scatter Plot
1. Wczytaj dane o miastach.
2. Stwórz histogram populacji miast (ogranicz się np. do 20 największych miast, aby wykres był czytelny).
3. Stwórz wykres punktowy (scatter plot) zależności między szerokością a długością geograficzną miast (zobacz, czy "narysuje" to mapę świata).

## 3. Zaawansowane wykresy z Seaborn

### Zadanie 3: Boxplot i Heatmap
1. Zainstaluj bibliotekę seaborn: `pip install seaborn`.
2. Stwórz wykres pudełkowy (boxplot) populacji miast w podziale na kraje (wybierz 3-5 krajów).
3. (Opcjonalnie) Stwórz macierz korelacji dla kolumn numerycznych i wyświetl ją jako heatmapę.

## 4. Wykorzystanie istniejących skryptów
Przeanalizuj i uruchom pliki `scripts/plot1.py` do `scripts/plot5.py`. Zobacz, jak są tam konfigurowane kolory, rozmiary czcionek i zapisywanie do plików graficznych.

## Dokumentacja
Szukaj informacji w `docs/matplotlib.md`.
