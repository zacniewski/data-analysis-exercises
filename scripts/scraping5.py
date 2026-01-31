# Scraping często polega na wyciąganiu strukturalnych danych z powtarzalnych elementów, 
# takich jak karty produktów. Możemy najpierw znaleźć wszystkie kontenery produktów, 
# a potem wewnątrz każdego z nich szukać szczegółowych informacji (tytuł, cena, ocena).

import requests
from bs4 import BeautifulSoup

# Pobieramy stronę.
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Lista, w której będziemy przechowywać słowniki z danymi o produktach.
top_items = []

# Szukamy wszystkich elementów div o klasie 'thumbnail'. 
# Reprezentują one pojedyncze produkty na tej stronie.
products = soup.select('div.thumbnail')

# Iterujemy przez każdy znaleziony element produktu.
for elem in products:
    # Wewnątrz każdego produktu szukamy tytułu: tag <a> o klasie 'title' będący dzieckiem <h4>.
    title = elem.select('h4 > a.title')[0].text
    # Szukamy oceny: div o klasie 'ratings'.
    review_label = elem.select('div.ratings')[0].text
    
    # Tworzymy słownik z oczyszczonymi danymi (.strip() usuwa zbędne spacje i nowolinie).
    info = {
        "title": title.strip(),
        "review": review_label.strip()
    }
    # Dodajemy słownik do naszej listy wyników.
    top_items.append(info)

# Wyświetlamy listę wszystkich zebranych produktów.
print(top_items)

# Zapisanie produktów do pliku JSON z Nazwiskiem
import json
with open("scripts/Nazwisko_scraping5.json", "w", encoding="utf-8") as f:
    json.dump(top_items, f, ensure_ascii=False, indent=4)
