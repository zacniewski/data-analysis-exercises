# W Pythonie wybór odpowiedniego trybu (mode) jest kluczowy dla zachowania danych.
# Główne tryby to:
# 'w' (write) - Nadpisywanie. Jeśli plik istnieje, jego zawartość zostanie usunięta.
# 'a' (append) - Dopisywanie. Nowe dane zostaną dodane na końcu istniejącej treści.
# 'x' (exclusive creation) - Tworzenie. Zwraca błąd, jeśli plik już istnieje.

filename = "scripts/Nazwisko_writing2.txt"

# PRZYPADEK 1: Nadpisywanie pliku ('w')
# Używamy tego trybu, gdy chcemy stworzyć nowy plik lub całkowicie zastąpić stary.
with open(filename, "w", encoding="utf-8") as file:
    file.write("To jest pierwsza linia.\n")
    file.write("Użycie trybu 'w' usunęło poprzednią zawartość (jeśli była).\n")

# PRZYPADEK 2: Dopisywanie do pliku ('a')
# Idealne do logów lub zbierania wyników z wielu uruchomień programu.
with open(filename, "a", encoding="utf-8") as file:
    file.write("To jest dodatkowa linia dopisana na końcu.\n")
    file.write("Tryb 'a' nie niszczy istniejących danych.\n")

# PRZYPADEK 3: Zapisywanie listy linii za pomocą writelines()
# Metoda .writelines() pozwala zapisać listę napisów za jednym razem.
lines_to_add = [
    "Linia z listy nr 1\n",
    "Linia z listy nr 2\n",
    "Linia z listy nr 3\n"
]

with open(filename, "a", encoding="utf-8") as file:
    # Uwaga: writelines nie dodaje automatycznie znaków nowej linii!
    # Muszą one być zawarte w elementach listy.
    file.writelines(lines_to_add)

print(f"Zapisano dane do pliku {filename}")
