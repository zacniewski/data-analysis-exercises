# Wykład 7: Szeregi czasowe w Pandas

Wiele danych analitycznych (giełda, logi serwera, sprzedaż) ma charakter czasowy. Pandas posiada potężne narzędzia do ich analizy.

## 1. Typ Datetime
W Pandas używamy obiektów `Timestamp` oraz typu danych `datetime64`.

```python
import pandas as pd
df['data'] = pd.to_datetime(df['data_kolumna'])
```

## 2. Ustawianie daty jako indeksu
Pozwala na łatwe wybieranie zakresów czasowych.
```python
df.set_index('data', inplace=True)
# Wybierz dane tylko z 2023 roku
df_2023 = df.loc['2023']
```

## 3. Resampling (Zmiana częstotliwości)
Możemy łatwo agregować dane (np. z dziennych na miesięczne).
- `D` - dni
- `M` - miesiące
- `Y` - lata
- `W` - tygodnie

```python
# Średnia miesięczna
df_monthly = df['sprzedaz'].resample('M').mean()
```

## 4. Rolling Windows (Okna przesuwne)
Służą do wygładzania wykresów (np. średnia krocząca z 7 dni).
```python
df['moving_avg'] = df['sprzedaz'].rolling(window=7).mean()
```

## 5. Przesunięcia (Shifting)
Porównywanie wartości z poprzednim okresem (np. wczoraj vs dzisiaj).
```python
df['prev_day'] = df['sprzedaz'].shift(1)
df['change'] = df['sprzedaz'] - df['prev_day']
```
