# Importujemy bibliotekę requests.
import requests

# Definiujemy podstawowy URL.
url = "http://jsonplaceholder.typicode.com/posts"

# 1. PARAMETRY ZAPYTANIA (query parameters)
# Często chcemy filtrować dane po stronie serwera. Zamiast budować URL ręcznie:
# "http://jsonplaceholder.typicode.com/posts?userId=1"
# używamy słownika i parametru 'params'.
query_params = {
    "userId": 1
}

# 2. NAGŁÓWKI (headers)
# Możemy zdefiniować własne nagłówki, np. User-Agent lub nagłówki autoryzacji.
custom_headers = {
    "User-Agent": "MyPythonScript/1.0",
    "Accept": "application/json"
}

# Wykonujemy żądanie GET z dodatkowymi parametrami i nagłówkami.
response = requests.get(url, params=query_params, headers=custom_headers)

# 3. KOD STATUSU ODPOWIEDZI (status code)
# Serwer zwraca kod statusu informujący o wyniku operacji (np. 200 OK, 404 Not Found).
print(f"Kod statusu odpowiedzi: {response.status_code}")

# Sprawdzamy, czy zapytanie się powiodło (kody z zakresu 200-299).
if response.status_code == 200:
    print("Sukces! Dane zostały pobrane.")
    
    # 4. NAGŁÓWKI ODPOWIEDZI
    # Serwer również wysyła nagłówki, np. informację o formacie danych (Content-Type).
    content_type = response.headers.get("Content-Type")
    print(f"Format danych zwrócony przez serwer: {content_type}")
    
    # Pobieramy sparsowane dane JSON.
    posts = response.json()
    
    # Zapisujemy wyniki do pliku z Nazwiskiem
    with open("scripts/Nazwisko_json4.json", "w", encoding="utf-8") as f:
        import json
        json.dump(posts, f, ensure_ascii=False, indent=4)
    
    print(f"Pobrano {len(posts)} postów dla użytkownika o ID {query_params['userId']}.")
    for post in posts[:3]:  # Wyświetlamy tylko 3 pierwsze posty.
        print(f"- Post ID: {post['id']}, Tytuł: {post['title']}")
else:
    print(f"Wystąpił problem. Kod błędu: {response.status_code}")
