# Oprócz wyciągania tekstu widocznego na stronie, często potrzebujemy wartości atrybutów 
# tagów HTML, takich jak adresy URL z atrybutu 'href' w linkach <a> czy źródła obrazów 'src'. 
# Służy do tego metoda .get('nazwa_atrybutu').

import requests
from bs4 import BeautifulSoup

# Pobieramy stronę.
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Lista na wszystkie znalezione linki.
all_links = []

# Wybieramy wszystkie tagi <a> (linki) ze strony.
links = soup.select('a')

# Przechodzimy przez każdy link.
for ahref in links:
    # Pobieramy tekst wyświetlany w linku.
    text = ahref.text
    text = text.strip() if text is not None else ''

    # Pobieramy wartość atrybutu 'href' (czyli docelowy adres URL).
    href = ahref.get('href')
    href = href.strip() if href is not None else ''
    
    # Zapisujemy parę: adres i tekst linku jako słownik.
    all_links.append({"href": href, "text": text})

# Wyświetlamy listę wszystkich linków.
print(all_links)

# Zapisanie linków do pliku tekstowego z Nazwiskiem
with open("scripts/Nazwisko_scraping6.txt", "w", encoding="utf-8") as f:
    for link in all_links:
        f.write(f"Link: {link['text']} -> {link['href']}\n")
