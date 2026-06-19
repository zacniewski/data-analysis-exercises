# Laboratorium 10: Kompleksowa analiza i raportowanie (Projekt końcowy)

## Cel laboratorium
Wykorzystanie wszystkich zdobytych umiejętności (Pandas, Matplotlib, Seaborn) do przeprowadzenia pełnej analizy zbioru danych i sformułowania wniosków.

## 1. Zbiór danych: Recenzje win
Wykorzystamy plik `data/winemag-data-130k-v2.csv.zip`. Jest to duży zbiór danych zawierający recenzje win z całego świata.

### Zadanie 1: Eksploracja i czyszczenie
1. Wczytaj dane bezpośrednio z pliku ZIP przy użyciu Pandas.
2. Sprawdź, ile jest rekordów i jakie są kolumny.
3. Usuń duplikaty i obsłuż braki w kolumnie `price` (np. wypełniając je średnią lub usuwając te wiersze).
4. Stwórz nową kolumnę `price_per_point`, która będzie ilorazem ceny i liczby punktów.

## 2. Analiza statystyczna i grupowanie
1. Jakie kraje produkują najwięcej win? (Top 10).
2. Jaka jest średnia cena wina dla każdego z tych 10 krajów?
3. Znajdź najtańsze wino, które otrzymało 100 punktów.

## 3. Zaawansowana wizualizacja
1. Stwórz wykres pudełkowy (`boxplot`) pokazujący rozkład punktacji dla 5 najpopularniejszych odmian win (`variety`).
2. Stwórz wykres punktowy (`scatter plot`) zależności ceny od punktacji. Czy korelacja jest wyraźna? (Użyj skali logarytmicznej dla ceny, jeśli to konieczne).
3. Stwórz mapę ciepła (heatmap) pokazującą korelację między wszystkimi zmiennymi numerycznymi.

## 4. Raport końcowy
W komentarzach pod skryptem lub w osobnym pliku Markdown (`Raport_Nazwisko.md`) odpowiedz na pytania:
- Czy droższe wina zawsze dostają więcej punktów?
- Który kraj oferuje najlepszy stosunek jakości (punktów) do ceny?
- Jakie są Twoje 3 główne wnioski z analizy tego zbioru danych?

## Podsumowanie kursu
To ostatnie laboratorium. Gratulacje! Twoje umiejętności analizy danych są teraz na solidnym poziomie podstawowym.
