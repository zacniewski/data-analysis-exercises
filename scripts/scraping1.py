# Scraping polega na automatycznym pobieraniu danych ze stron internetowych.
# Biblioteka BeautifulSoup to narzędzie do "parsowania" (analizowania) dokumentów HTML i XML.
# Tworzy ona drzewo struktury strony, co pozwala na łatwe wyszukiwanie i wyciąganie konkretnych informacji,
# takich jak nagłówki, linki, tabele czy opisy produktów.

import requests # Importujemy bibliotekę requests, która służy do wysyłania zapytań HTTP i pobierania zawartości stron.

# Wysyłamy zapytanie GET do określonego adresu URL.
# Wynik (odpowiedź serwera) przechowujemy w zmiennej 'res'.
res = requests.get(
    'https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')

# Wyciągamy surowy tekst (kod źródłowy HTML) z odpowiedzi serwera.
txt = res.text

# Pobieramy kod statusu HTTP (np. 200 oznacza sukces, 404 - nie znaleziono).
status = res.status_code

# Wyświetlamy pobraną treść strony oraz status zapytania.
print(txt, status)
# print(dir(res)) # Opcjonalnie: wyświetla listę wszystkich dostępnych metod i atrybudów obiektu odpowiedzi.

# Zapisanie pobranej treści do pliku z Nazwiskiem
with open("scripts/Nazwisko_scraping1.html", "w", encoding="utf-8") as f:
    f.write(txt)
