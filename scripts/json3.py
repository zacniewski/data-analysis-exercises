# Importujemy bibliotekę requests.
import requests

# URL do endpointu z danymi użytkowników.
users_url = "http://jsonplaceholder.typicode.com/users"

# Pobieramy dane w formacie JSON.
all_users = requests.get(users_url).json()

# Otwieramy (lub tworzymy) plik 'scripts/Nazwisko_json3.txt' do zapisu.
with open("scripts/Nazwisko_json3.txt", "a+") as f:
    # Iterujemy po liście użytkowników.
    for item in all_users:
        # Pobieramy podstawowe dane: ID oraz imię/nazwisko.
        id = item["id"]
        name = item["name"]
        
        # Przykład dostępu do zagnieżdżonych struktur w JSON.
        # Pobieramy miasto z klucza 'address'.
        city = item["address"]["city"]
        
        # Pobieramy długość geograficzną (longitude) z jeszcze głębszego poziomu (address -> geo).
        longitude = item["address"]["geo"]["lng"]

        # Przygotowujemy linię z informacjami o użytkowniku i jego lokalizacji.
        linia_do_zapisu = f"{id}. {name} from {city} (longitude: {longitude}).\n"
        
        # Zapisujemy do pliku.
        f.write(linia_do_zapisu)
