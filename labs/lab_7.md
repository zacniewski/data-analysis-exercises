# Laboratorium 7: JSON i API w praktyce

## Cel laboratorium
Nauczenie się pobierania danych z serwisów zewnętrznych (API) oraz przetwarzania danych w formacie JSON.

## 1. Pobieranie danych z API
Użyjemy darmowego serwisu `JSONPlaceholder` do testów.

### Zadanie 1: Proste żądanie GET
Stwórz skrypt `lab7_api.py`, który:
1. Pobierze listę użytkowników z adresu: `https://jsonplaceholder.typicode.com/users`.
2. Wyświetli imię, nazwę użytkownika oraz email każdego z nich.
3. Zapisze te dane do pliku tekstowego `Nazwisko_users.txt`.

Wskazówka: Przeanalizuj `scripts/json1.py`.

## 2. Zagnieżdżone struktury JSON
Dane JSON często mają strukturę drzewiastą (słownik w słowniku).

### Zadanie 2: Wydobywanie głębokich danych
1. Korzystając z tej samej listy użytkowników, wypisz miasto (city) każdego z nich. Dane te znajdują się wewnątrz klucza `address`.
2. Stwórz listę samych nazw miast i posortuj ją alfabetycznie.

## 3. JSON a Pandas
Pandas potrafi zamienić listę słowników bezpośrednio w tabelę.

### Zadanie 3: Analiza postów
1. Pobierz posty z API: `https://jsonplaceholder.typicode.com/posts`.
2. Przekonwertuj pobraną listę (JSON) na DataFrame.
3. Policz, ile postów napisał każdy użytkownik (`userId`).
4. Wyświetl posty o `id` od 10 do 20.

## 4. Wykorzystanie skryptów
Przejrzyj pliki od `scripts/json1.py` do `scripts/json5.py`. Zwróć uwagę na obsługę błędów i różne metody zapisu plików JSON.
