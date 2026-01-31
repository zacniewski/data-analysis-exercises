# BeautifulSoup pozwala na dostęp do głównych sekcji dokumentu HTML (head, body) 
# poprzez proste odwołania do atrybutów obiektu soup. Każdy taki atrybut zwraca 
# obiekt reprezentujący dany fragment kodu HTML.

import requests
from bs4 import BeautifulSoup

# Pobieramy stronę internetową.
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")

# Inicjalizujemy BeautifulSoup do analizy struktury HTML.
soup = BeautifulSoup(page.content, 'html.parser')

# Wyodrębniamy cały obiekt tagu <title> (wraz ze znacznikami).
page_title = soup.title

# Wyodrębniamy sekcję <body> strony (główna treść).
page_body = soup.body

# Wyodrębniamy sekcję <head> strony (metadane, skrypty, style).
page_head = soup.head

# Wyświetlamy pobrane obiekty. Zauważ, że bez .text zobaczymy pełne tagi HTML.
print(page_title, page_head)

# Zapisanie head do pliku z Nazwiskiem
with open("scripts/Nazwisko_scraping3.txt", "w", encoding="utf-8") as f:
    f.write(str(page_head))
