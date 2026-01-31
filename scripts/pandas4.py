import pandas as pd

# Tworzenie ramki danych z osobami i ich wynikami
df = pd.DataFrame(
    {
        "Osoba": ["Michał Jakub", "Ewa Noga", "Krzysztof Zawierucha"],
        "Wynik": [15, 38, 21],
    }
)

# Funkcja klasyfikująca wynik
def sprawdz(punkty):
    """Zwraca status w zależności od liczby punktów."""
    if punkty > 20:
        return 'Zdany'
    else:
        return 'Oblany'

# Użycie metody apply na kolumnie 'Wynik', aby stworzyć nową kolumnę 'Info'
df["Info"] = df.Wynik.apply(sprawdz)

# Funkcja operująca na całym wierszu
def rozdziel(wiersz):
    """Rozdziela kolumnę 'Osoba' na dwie nowe kolumny: 'Imię' i 'Nazwisko'."""
    # split(' ') dzieli tekst po spacji
    wiersz['Imię'], wiersz['Nazwisko'] = wiersz['Osoba'].split(' ')
    return wiersz

# Użycie apply na całym DataFrame (axis=1 oznacza operację na wierszach)
df = df.apply(rozdziel, axis=1)

print("Przetworzona ramka danych:")
print(df)

# Przykład dodatkowy: obliczenie średniej wyników
print(f"\nŚredni wynik: {df.Wynik.mean():.2f}")

# Zapisanie przetworzonej ramki do pliku z Nazwiskiem
df.to_excel("scripts/Nazwisko_pandas4.xlsx", index=False)
