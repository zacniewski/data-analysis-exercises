# Ostatnim etapem procesu scrapingu jest często zapisanie zebranych danych do pliku, 
# aby móc je później analizować (np. w Excelu lub bibliotece Pandas). 
# Format CSV (Comma Separated Values) jest do tego celu idealny.

import requests
from bs4 import BeautifulSoup
import csv # Importujemy moduł do obsługi plików CSV.

# Pobieramy zawartość strony.
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Lista na wszystkie dane o produktach.
all_products = []

# Wybieramy wszystkie elementy div o klasie 'thumbnail'.
products = soup.select('div.thumbnail')

# Iterujemy po produktach i wyciągamy szczegółowe informacje.
for product in products:
    # Nazwa: link <a> wewnątrz <h4>.
    name = product.select('h4 > a')[0].text.strip()
    # Opis: akapit <p> o klasie 'description'.
    description = product.select('p.description')[0].text.strip()
    # Cena: <h4> o klasie 'price'.
    price = product.select('h4.price')[0].text.strip()
    # Recenzje: div o klasie 'ratings'.
    reviews = product.select('div.ratings')[0].text.strip()
    # Link do obrazka: atrybut 'src' tagu <img>.
    image = product.select('img')[0].get('src')

    # Dodajemy komplet informacji o produkcie jako słownik do listy.
    all_products.append({
        "name": name,
        "description": description,
        "price": price,
        "reviews": reviews,
        "image": image
    })

# Pobieramy nazwy kluczy z pierwszego słownika (będą to nagłówki kolumn w CSV).
keys = all_products[0].keys()

# Otwieramy plik 'scripts/Nazwisko_scraping7.csv' do zapisu ('w'). newline='' zapobiega pustym liniom.
with open('scripts/Nazwisko_scraping7.csv', 'w', newline='', encoding='utf-8') as output_file:
    # Tworzymy obiekt DictWriter, który automatycznie mapuje słowniki na wiersze CSV.
    dict_writer = csv.DictWriter(output_file, keys)
    # Zapisujemy nagłówki (name, description, price, itd.).
    dict_writer.writeheader()
    # Zapisujemy wszystkie wiersze z danymi.
    dict_writer.writerows(all_products)
