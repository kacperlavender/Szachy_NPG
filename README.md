# Szachy w Pythonie

Prosty program szachowy pozwalający na wykonywanie ruchów na planszy przy użyciu standardowej notacji algebraicznej (np. `a1`, `e2`).

---

## Zasady działania

### Konwersja notacji

- Program korzysta z funkcji `konwertuj_notacje(notacja)`, która tłumaczy standardową notację szachową (np. `a1`, `h8`) na współrzędne indeksowane od 0, które są używane wewnętrznie przez planszę.
- Litery od `a` do `h` odpowiadają kolumnom (0 do 7).
- Cyfry od `1` do `8` odpowiadają rzędowi (0 do 7).

### Interakcja z użytkownikiem

- Program pyta użytkownika o pozycję startową i końcową ruchu, wpisując je w formacie notacji algebraicznej.
- Po podaniu dwóch pozycji program próbuje wykonać ruch na planszy.
- Jeśli ruch jest poprawny zgodnie z zasadami gry, plansza jest aktualizowana i wyświetlana.
- Jeśli ruch jest nieprawidłowy lub format pozycji jest błędny, program informuje użytkownika o błędzie.

### Klasa `Plansza`

- Obiekt klasy `Plansza` reprezentuje aktualny stan gry.
- Metoda `wykonaj_ruch(start, koniec)` przyjmuje dwie pozycje w formie krotek `(rzad, kolumna)` i wykonuje ruch, jeśli jest on legalny.
- Po każdym ruchu stan planszy jest wyświetlany w konsoli.

---

## Przykład użycia

```
Podaj pozycję startową (np. a1): e2
Podaj pozycję końcową (np. a2): e4
```


Jeśli ruch jest poprawny, plansza zostanie zaktualizowana i pokazana na ekranie.

---

## Uwagi

- Program nie obsługuje zaawansowanych zasad takich jak roszada, promocja pionka czy bicie w przelocie (w zależności od implementacji klasy `Plansza`).
- Notacja wejściowa musi mieć dokładnie dwa znaki: literę (a-h) i cyfrę (1-8).


