import pandas as pd

df = pd.DataFrame(
    {
        "Osoba": ["Michał Jakub", "Ewa Noga", "Krzysztof Zawierucha"],
        "Wynik": [15, 38, 21],
    }
)


def sprawdz(punkty):
    if punkty > 20:
        return 'Zdany'
    else:
        return 'Oblany'


df["Info"] = df.Wynik.apply(sprawdz)


def rozdziel(wiersz):
    wiersz['Imię'], wiersz['Nazwisko'] = wiersz['Osoba'].split(' ')
    return wiersz


df = df.apply(rozdziel, axis=1)

print(df)
