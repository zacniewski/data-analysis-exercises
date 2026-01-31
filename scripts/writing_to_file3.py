import json # Często dane zapisujemy w formacie JSON zamiast zwykłego tekstu.

# Podczas pracy z plikami tekstowymi bardzo ważne jest określenie kodowania (encoding).
# System Windows domyślnie używa kodowania 'cp1252', a Linux/Mac 'utf-8'.
# Aby uniknąć problemów z polskimi znakami (ą, ć, ę...), zawsze zaleca się używanie encoding="utf-8".

data_to_save = {
    "użytkownik": "Jan Kowalski",
    "wiek": 30,
    "miasto": "Warszawa",
    "umiejętności": ["Python", "Analiza danych", "SQL"]
}

filename = "scripts/Nazwisko_writing3.json"

# Zapisywanie danych strukturalnych do pliku JSON.
# Tryb 'w' ponieważ tworzymy/nadpisujemy plik z danymi.
with open(filename, "w", encoding="utf-8") as json_file:
    # json.dump() przyjmuje obiekt Pythona i plik, do którego ma zapisać dane.
    # indent=4 sprawia, że plik będzie czytelny dla człowieka (ładne wcięcia).
    # ensure_ascii=False pozwala na poprawne zapisanie polskich znaków zamiast kodów \uXXXX.
    json.dump(data_to_save, json_file, indent=4, ensure_ascii=False)

print(f"Dane strukturalne zostały zapisane w formacie JSON do pliku: {filename}")

# Bonus: Obsługa błędów przy pracy z plikami.
# Zawsze warto zabezpieczyć się przed sytuacją, gdy np. nie mamy uprawnień do zapisu.
try:
    with open("/system_protected_file.txt", "w") as f:
        f.write("Test")
except PermissionError:
    print("BŁĄD: Brak uprawnień do zapisu w lokalizacji chronionej!")
except Exception as e:
    print(f"Wystąpił nieoczekiwany błąd: {e}")
