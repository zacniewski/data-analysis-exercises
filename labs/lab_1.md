# Laboratorium 1: Środowisko pracy i podstawy NumPy

## Cel laboratorium
Celem zajęć jest konfiguracja środowiska programistycznego oraz zapoznanie się z podstawowymi operacjami na tablicach w bibliotece NumPy.

## 1. Konfiguracja środowiska
Uruchom terminal i wykonaj poniższe kroki (dla systemów Linux/macOS):

```bash
# Tworzenie środowiska wirtualnego
python3 -m venv venv

# Aktywacja środowiska
source venv/bin/activate

# Instalacja bibliotek
pip install numpy pandas matplotlib
```

## 2. Podstawy NumPy (Zadania)

### Zadanie 1: Tworzenie tablic
Stwórz skrypt `lab1_zad1.py`, który:
1. Utworzy tablicę 1D zawierającą liczby od 1 do 10.
2. Utworzy macierz 3x3 wypełnioną zerami.
3. Utworzy macierz 5x5 wypełnioną liczbami losowymi z zakresu 0-1.

### Zadanie 2: Operacje matematyczne
Stwórz skrypt `lab1_zad2.py`, który:
1. Utworzy dwie macierze 2x2.
2. Wykona ich dodawanie, odejmowanie oraz mnożenie macierzowe (użyj `@` lub `np.dot`).
3. Obliczy sumę wszystkich elementów w wynikowej macierzy.

### Zadanie 3: Indeksowanie i wycinanie
Stwórz macierz 4x4 z liczbami od 1 do 16. Wypisz:
- Drugi wiersz.
- Ostatnią kolumnę.
- Środkowy blok 2x2.

## 3. Praca z istniejącymi skryptami
Przeanalizuj i uruchom plik `scripts/numpy1.py` z tego repozytorium. Zobacz jak są tam realizowane podstawowe operacje.

## Zadanie domowe
Zapoznaj się z dokumentacją NumPy w folderze `docs/numpy.md`.
