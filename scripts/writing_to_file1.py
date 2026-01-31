# Praca z plikami w Pythonie opiera się na wbudowanej funkcji open(), 
# która tworzy obiekt pliku, umożliwiający komunikację z systemem plików.
# Najbezpieczniejszym sposobem otwierania plików jest użycie menedżera kontekstu 'with'.
# Gwarantuje on, że plik zostanie poprawnie zamknięty nawet w przypadku wystąpienia błędu,
# co zapobiega wyciekom pamięci i blokowaniu zasobów systemowych.

# Funkcja open(nazwa_pliku, tryb)
# "demofile.txt" - ścieżka do pliku.
# "a+" - tryb otwarcia: 'a' (append) oznacza dopisywanie na końcu pliku, 
# '+' oznacza, że plik jest otwarty zarówno do zapisu, jak i do odczytu. 
# Jeśli plik nie istnieje, zostanie utworzony.
with open("scripts/Nazwisko_writing1.txt", "a+") as f:
    # Wykonujemy pętlę, aby zapisać wiele linii danych.
    for i in range(10):
        # Przygotowujemy ciąg znaków do zapisu. 
        # Ważne: metoda .write() przyjmuje tylko napisy (stringi).
        # Dodajemy znak nowej linii "\n", aby każda liczba była w osobnym wierszu.
        zm = str(i) + "\n"
        
        # Metoda .write() zapisuje dane do bufora pliku.
        f.write(zm)

# Po wyjściu z bloku 'with' plik jest automatycznie zamykany.
