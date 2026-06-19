# Laboratorium 2: Pozyskiwanie danych - Scraping i formaty plików

## Cel laboratorium
Nabycie umiejętności pobierania danych z internetu oraz pracy z popularnymi formatami plików (CSV, Excel, JSON).

## 1. Web Scraping w praktyce

Wykorzystamy biblioteki `requests` i `beautifulsoup4`.

### Zadanie 1: Prosty scraping
Stwórz skrypt `lab2_scraping.py`, który pobierze tytuły artykułów ze strony `https://news.ycombinator.com/`.

Podpowiedź:
```python
import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# Szukaj znaczników <span class="titleline"> lub <a> wewnątrz nich
```

## 2. Praca z plikami

### Zadanie 2: CSV i Excel
1. Wczytaj plik `data/Countries.csv` (znajduje się w repozytorium) za pomocą standardowej biblioteki `csv` lub biblioteki `pandas`.
2. Wypisz nazwy wszystkich krajów.
3. Spróbuj otworzyć plik `data/imiona.xlsx` i wyświetlić pierwsze 5 wierszy.

### Zadanie 3: JSON
Przeanalizuj pliki `scripts/json1.py` do `scripts/json5.py`. Stwórz własny plik JSON z listą Twoich ulubionych filmów, a następnie napisz skrypt, który go odczyta i wypisze tylko tytuły.

## 3. Integracja (Dla chętnych)
Napisz skrypt, który pobierze dane o pogodzie z otwartego API (np. Open-Meteo) w formacie JSON i zapisze je do pliku CSV.

## Materiały pomocnicze
- Dokumentacja w `docs/others.md` (Requests, BeautifulSoup).
- Skrypty w folderze `scripts/scraping*.py`.
