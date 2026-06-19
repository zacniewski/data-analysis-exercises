# Laboratorium 8: Pozyskiwanie danych z WWW (Web Scraping)

## Cel laboratorium
Praktyczne zastosowanie bibliotek `requests` i `BeautifulSoup` do wydobywania informacji ze stron HTML.

## 1. Analiza kodu strony
Zanim zaczniesz pisać kod, musisz sprawdzić strukturę strony w przeglądarce (F12 -> Inspect).

### Zadanie 1: Pierwszy scraper
Stwórz skrypt `lab8_scraper.py`, który:
1. Pobierze treść strony: `https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/`.
2. Wyciągnie i wyświetli tekst z pierwszego znacznika `<h1>` na stronie.
3. Wyciągnie tytuł strony (znacznik `<title>`).

## 2. Pobieranie list i tabel
Większość danych na stronach znajduje się w powtarzalnych elementach.

### Zadanie 2: Lista produktów
Na tej samej stronie znajdź wszystkie nazwy produktów (użyj klasy CSS lub odpowiedniego tagu).
1. Pobierz nazwy wszystkich produktów wyświetlonych na stronie.
2. Pobierz ich ceny.
3. Zapisz zestawienie (Nazwa - Cena) do listy słowników.

## 3. Zapis do CSV
Dane pozyskane z sieci najlepiej od razu zapisać w formacie czytelnym dla Pandas.

### Zadanie 3: Scraper do pliku
1. Wykorzystaj dane z zadania 2.
2. Zapisz je do pliku `Nazwisko_produkty.csv` przy użyciu modułu `csv` lub DataFrame w Pandas.
3. Sprawdź, czy plik poprawnie otwiera się w Excelu lub Notatniku.

## 4. Analiza istniejących przykładów
Uruchom skrypty `scripts/scraping1.py` do `scripts/scraping7.py`. Zwróć uwagę na:
- Pobieranie linków (`<a>` i atrybut `href`).
- Pobieranie obrazków (`<img>` i atrybut `src`).
- Obsługę paginacji (przechodzenie do kolejnych stron).
