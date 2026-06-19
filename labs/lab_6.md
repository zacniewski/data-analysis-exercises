# Laboratorium 6: Obsługa plików Excel

## Cel laboratorium
Zapoznanie się z biblioteką `openpyxl` oraz metodami Pandas do odczytu i zapisu danych w formacie Excel.

## 1. Tworzenie i modyfikacja plików (.xlsx)
Wykorzystaj bibliotekę `openpyxl`, aby stworzyć plik z wieloma arkuszami.

### Zadanie 1: Struktura skoroszytu
Stwórz skrypt `lab6_excel_basic.py`, który:
1. Utworzy nowy skoroszyt.
2. Doda trzy arkusze: "Produkty", "Sprzedaż", "Raport".
3. W arkuszu "Produkty" w komórce A1 wpisze "Nazwa", a w B1 "Cena".
4. Zapisze plik jako `Nazwisko_lab6_test.xlsx`.

Wskazówka: Zobacz przykłady w `scripts/excel1.py` i `scripts/excel2.py`.

## 2. Pandas i Excel
Pandas jest znacznie szybszy do operacji na dużych tabelach.

### Zadanie 2: Eksport danych
1. Wczytaj dowolny plik CSV z katalogu `data/` (np. `film.csv`) do DataFrame.
2. Wybierz tylko 10 pierwszych wierszy i wybrane 3 kolumny.
3. Zapisz ten fragment do pliku Excel `Nazwisko_filmy.xlsx` do arkusza o nazwie "Top10".

## 3. Praca z istniejącymi arkuszami
Uruchom i przeanalizuj skrypt `scripts/excel3.py`. Zobacz, jak można iterować po wierszach i kolumnach istniejącego arkusza.

### Zadanie 3: Prosta analiza w Excelu
1. Wczytaj plik `data/imiona.xlsx`.
2. Oblicz sumę wystąpień wszystkich imion (kolumna z liczbą urodzeń).
3. Wyświetl 5 najpopularniejszych imion męskich i żeńskich.
4. Zapisz wynik do nowego pliku Excel.

## Dokumentacja
Więcej informacji znajdziesz w `docs/pandas.md`.
