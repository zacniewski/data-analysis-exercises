# Importujemy bibliotekę requests, która służy do wysyłania żądań HTTP.
import requests

# Definiujemy adres URL do endpointu 'todos' z serwisu JSONPlaceholder.
# Jest to darmowe API do testów, które zwraca przykładowe dane w formacie JSON.
todos_url = "http://jsonplaceholder.typicode.com/todos"

# Wysyłamy żądanie GET pod wskazany adres URL.
# Metoda .json() automatycznie parsuje otrzymaną odpowiedź JSON na listę słowników w Pythonie.
all_todos = requests.get(todos_url).json()

# Inicjalizujemy licznik dla zadań, które zostały zakończone (completed=True).
counter = 0

# Otwieramy plik tekstowy 'Nazwisko_json1.txt' w trybie 'a+' (append + read).
# Tryb 'a+' sprawia, że nowe dane są dopisywane na końcu pliku, a jeśli plik nie istnieje, zostaje utworzony.
with open("scripts/Nazwisko_json1.txt", "a+") as f:
    # Iterujemy po każdym elemencie (zadaniu) pobranym z API.
    for item in all_todos:
        # Wyciągamy interesujące nas dane ze słownika reprezentującego pojedyncze zadanie.
        id = item["id"]
        title = item["title"]
        completed = item["completed"]

        # Sprawdzamy, czy zadanie jest oznaczone jako wykonane.
        if completed:
            # Zwiększamy licznik wykonanych zadań.
            counter += 1
            # Przygotowujemy czytelny format linii do zapisu w pliku.
            linia_do_zapisu = f"Wpis o id={id} ma tytuł '{title}', a jego status to {completed}.\n"
            # Zapisujemy sformatowaną linię do pliku.
            f.write(linia_do_zapisu)

    # Na końcu dopisujemy podsumowanie z łączną liczbą znalezionych wykonanych zadań.
    f.write(f"Liczba elementów ze statusem 'True' to {counter}.")
