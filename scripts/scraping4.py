# Metoda .select() w BeautifulSoup pozwala na używanie selektorów CSS do znajdowania elementów.
# Jest to potężne narzędzie, ponieważ pozwala precyzyjnie wskazać, które dane chcemy pobrać, 
# używając składni znanej z arkuszy stylów CSS (np. nazwy tagów, klasy, identyfikatory).

import requests
from bs4 import BeautifulSoup

# Wykonujemy zapytanie do strony.
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Tworzymy pustą listę na teksty z nagłówków H1.
all_h1_tags = []

# Używamy soup.select('h1'), aby znaleźć WSZYSTKIE znaczniki <h1> na stronie.
# Następnie iterujemy po nich i dodajemy ich treść tekstową do listy.
for element in soup.select('h1'):
    all_h1_tags.append(element.text)

# soup.select('p') zwraca listę wszystkich akapitów <p>.
# Wybieramy trzeci element z tej listy (indeks 2) i pobieramy jego tekst.
seventh_p_text = soup.select('p')[2].text

# Wyświetlamy zebrane dane.
print(all_h1_tags, seventh_p_text)

# Zapisanie nagłówków h1 do pliku z Nazwiskiem
with open("scripts/Nazwisko_scraping4.txt", "w", encoding="utf-8") as f:
    for h1 in all_h1_tags:
        f.write(h1 + "\n")
