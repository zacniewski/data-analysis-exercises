# Wykład 8: Podsumowanie i dobre praktyki w analizie danych

Ostatni wykład poświęcony jest zebraniu wiedzy w całość oraz omówieniu, jak pisać kod, który jest czytelny, wydajny i łatwy do utrzymania.

## 1. Cykl życia projektu Data Science
1. **Zrozumienie problemu**: Co chcemy osiągnąć? Jakie dane są potrzebne?
2. **Pozyskanie danych**: CSV, SQL, API, Scraping.
3. **Eksploracja i czyszczenie (EDA)**: Obsługa braków, outliers, typy danych.
4. **Analiza i wizualizacja**: Odpowiedź na pytania biznesowe.
5. **Raportowanie**: Prezentacja wyników (Jupyter Notebook, Dashboard, Streamlit).

## 2. Dobre praktyki w Pythonie
- **Nazywanie zmiennych**: `df_sales_clean` zamiast `df2`.
- **Komentarze i Docstringi**: Wyjaśniaj *dlaczego* coś robisz, a nie tylko *co*.
- **Unikanie pętli**: Używaj wektoryzacji w NumPy i Pandas (`df['a'] + df['b']` zamiast `for index, row in df.iterrows()`).
- **Pamięć**: Wybieraj odpowiednie typy danych (np. `category` dla kolumn z powtarzającymi się tekstami).

## 3. Praca z Notebookami
Jupyter Notebook to świetne narzędzie do eksperymentów, ale:
- Pamiętaj o kolejności komórek.
- Czyść kod przed udostępnieniem.
- Eksportuj finalne skrypty do plików `.py`.

## 4. Co dalej?
Analiza danych to wstęp do:
- **Machine Learning**: Przewidywanie przyszłości na podstawie danych.
- **Big Data**: Praca ze zbiorami danych, które nie mieszczą się w pamięci RAM.
- **Business Intelligence**: Budowanie interaktywnych dashboardów.

Dziękujemy za udział w kursie!
