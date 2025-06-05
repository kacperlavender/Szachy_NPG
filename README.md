# Szachy w Pythonie

Prosty program szachowy pozwalający na wykonywanie ruchów na planszy przy użyciu standardowej notacji algebraicznej (np. `a1`, `e2`).

---

## Zasady działania

### Konwersja notacji

- Program korzysta z funkcji `konwertuj_notacje(notacja)`, która tłumaczy standardową notację szachową (np. `a1`, `h8`) na współrzędne indeksowane od 0, które są używane wewnętrznie przez planszę.
- Litery od `a` do `h` odpowiadają kolumnom (0 do 7).
- Cyfry od `1` do `8` odpowiadają rzędowi (0 do 7).

