# Import biblioteki requests do komunikacji sieciowej.
import requests

# URL prowadzący do listy komentarzy.
comments_url = "http://jsonplaceholder.typicode.com/comments"

# Wykonanie żądania GET i konwersja odpowiedzi bezpośrednio na format JSON (lista słowników).
all_comments = requests.get(comments_url).json()

# Otwarcie pliku 'Nazwisko_json2.txt' w trybie dopisywania ('a+').
with open("scripts/Nazwisko_json2.txt", "a+") as f:
    # Przechodzimy przez listę wszystkich pobranych komentarzy.
    for comment in all_comments:
        # Pobieramy ID komentarza oraz adres email autora.
        id = comment["id"]
        email = comment["email"]
        
        # Tworzymy sformatowany ciąg znaków do zapisu.
        linia_do_zapisu = f"{id}. {email}\n"
        
        # Zapisujemy linię do pliku tekstowego.
        f.write(linia_do_zapisu)
