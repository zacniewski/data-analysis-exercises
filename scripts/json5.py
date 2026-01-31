import requests
# Importujemy wyjątki z biblioteki requests, aby móc je precyzyjnie obsłużyć.
from requests.exceptions import HTTPError, Timeout, RequestException

# Definiujemy URL do tworzenia nowych zasobów.
post_url = "http://jsonplaceholder.typicode.com/posts"

# Dane, które chcemy wysłać na serwer w formacie JSON.
new_post_data = {
    "title": "Nowy wpis testowy",
    "body": "Treść nowej wiadomości wysłanej przez skrypt Python.",
    "userId": 1
}

try:
    # 1. METODA POST
    # Służy do wysyłania nowych danych na serwer. 
    # Parametr 'json' automatycznie konwertuje słownik na ciąg JSON i ustawia nagłówek Content-Type.
    # 2. TIMEOUT
    # Parametr 'timeout' określa ile sekund czekamy na odpowiedź serwera zanim przerwiemy połączenie.
    # Jest to bardzo dobra praktyka, zapobiegająca zawieszeniu się skryptu w nieskończoność.
    print(f"Wysyłanie danych POST pod adres: {post_url}...")
    response = requests.post(post_url, json=new_post_data, timeout=5)

    # 3. raise_for_status()
    # Zamiast ręcznie sprawdzać 'if response.status_code == 201', możemy użyć tej metody.
    # Jeśli wystąpił błąd (status 4xx lub 5xx), zostanie rzucony wyjątek HTTPError.
    response.raise_for_status()

    # Jeśli doszliśmy tutaj, oznacza to sukces.
    print(f"Sukces! Utworzono zasób. Status: {response.status_code}")
    
    # Zapisujemy odpowiedź serwera do pliku z Nazwiskiem
    with open("scripts/Nazwisko_json5.json", "w", encoding="utf-8") as f:
        import json
        json.dump(response.json(), f, ensure_ascii=False, indent=4)
    
    print("Otrzymana odpowiedź od serwera:")
    print(response.json())

except HTTPError as http_err:
    # Obsługa specyficznych błędów HTTP (np. 404, 500).
    print(f"Wystąpił błąd HTTP: {http_err}")
except Timeout:
    # Obsługa przekroczenia czasu oczekiwania.
    print("Błąd: Serwer nie odpowiedział w wyznaczonym czasie (Timeout).")
except RequestException as err:
    # Obsługa innych błędów związanych z zapytaniem (np. brak internetu, błędny URL).
    print(f"Wystąpił nieoczekiwany błąd: {err}")

# 4. Inne metody HTTP (krótka demonstracja)
print("\nDemonstracja innych metod (bez ich pełnego wywoływania):")
print("- requests.put(url, json=data)    # Do pełnej aktualizacji zasobu")
print("- requests.patch(url, json=data)  # Do częściowej aktualizacji zasobu")
print("- requests.delete(url)            # Do usuwania zasobu")
