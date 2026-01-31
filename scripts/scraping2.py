# Idea BeautifulSoup polega na przekształceniu skomplikowanego kodu HTML w obiekt Pythona, 
# po którym można łatwo nawigować. BeautifulSoup "rozumie" strukturę tagów (znaczników) 
# i pozwala odwoływać się do nich jak do właściwości obiektu.

import requests
from bs4 import BeautifulSoup # Importujemy klasę BeautifulSoup z pakietu bs4.

# Pobieramy zawartość strony internetowej.
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")

# Tworzymy obiekt "soup" (zupę), który parsuje pobraną treść HTML.
# Drugi argument 'html.parser' wskazuje, jakiego mechanizmu użyć do analizy kodu.
soup = BeautifulSoup(page.content, 'html.parser')

# Wyciągamy tytuł strony (zawartość tagu <title>).
# Atrybut .text wyciąga tylko sam napis, pomijając znaczniki HTML.
page_title = soup.title.text

# page_body = soup.body.text # Przykładowe pobranie całej treści widocznej w <body>.

# Wyświetlamy pobrany tytuł strony w konsoli.
print(page_title)

# Zapisanie tytułu do pliku z Nazwiskiem
with open("scripts/Nazwisko_scraping2.txt", "w", encoding="utf-8") as f:
    f.write(f"Tytuł strony: {page_title}")
