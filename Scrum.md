Epik 1: Podstawy gry
Jako gracz, chcę zobaczyć planszę szachową, aby wiedzieć, gdzie są figury.
– Priorytet: Wysoki

Jako gracz, chcę mieć możliwość ustawienia figur na planszy zgodnie z zasadami gry.
– Priorytet: Wysoki

Jako gracz, chcę móc poruszać figurami zgodnie z zasadami szachów.
– Priorytet: Wysoki


Epik 2: Zasady gry
Jako gracz, chcę żeby system sprawdzał poprawność ruchów.
– Priorytet: Wysoki

Jako gracz, chcę żeby ruchy specjalne (roszada, en passant, promocja) były możliwe.
– Priorytet: Średni

Jako gracz, chcę żeby gra wykrywała szach, mat i pat.
– Priorytet: Wysoki

Epik 3: Interfejs i UX
Jako gracz, chcę widzieć, który gracz ma ruch.
– Priorytet: Średni

Jako gracz, chcę móc zresetować grę.
– Priorytet: Średni

Jako gracz, chcę widzieć historię ruchów.
– Priorytet: Niski



# 🧩 Plan pracy – Epik 1: Podstawy gry (Scrum)
**Cel epiku:** Umożliwić wyświetlanie planszy szachowej, ustawienie figur i wykonywanie podstawowych ruchów.  
**Założenie:** 5-dniowy sprint, 4 zadania dziennie, każde maks. 15 minut.

1. [ ] Zainicjalizuj projekt (`git init`, `main.cpp` / `main.py`)
2. [ ] Stwórz podstawową strukturę katalogów (np. `src/`, `assets/`, `main`)
3. [ ] Załaduj bibliotekę graficzną (np. Pygame, SFML, HTML Canvas)
4. [ ] Stwórz okno aplikacji z pustym tłem
5. [ ] Zaimplementuj funkcję do wyświetlania okna gry

## Siatka szachownicy
1. [ ] Narysuj siatkę 8x8 kwadratów
2. [ ] Zaimplementuj kolorowanie pól (czarne i białe)
3. [ ] Dodaj marginesy i linie oddzielające pola
4. [ ] Sprawdź, czy siatka jest poprawnie wyświetlana
5. [ ] Przetestuj działanie na różnych rozdzielczościach

## Implementacja figur
1. [ ] Dodaj reprezentację figur (np. pionki, wieże) na szachownicy
2. [ ] Zaimplementuj funkcję rysującą figury na odpowiednich polach
3. [ ] Sprawdź poprawność rozmieszczenia figur na planszy
4. [ ] Dodaj podstawowy interfejs dla ruchu figur
5. [ ] Przetestuj funkcję wyświetlania wszystkich figur

## Ruchy figur
1. [ ] Zaimplementuj funkcję sprawdzającą dozwolone ruchy dla pionka
2. [ ] Dodaj możliwość poruszania pionkami
3. [ ] Wprowadź podstawowy algorytm dla ruchów innych figur
4. [ ] Dodaj możliwość usuwania figury z planszy (jeśli zbijesz)
5. [ ] Sprawdź, czy figury poruszają się zgodnie z zasadami

## Interfejs użytkownika
1. [ ] Dodaj możliwość kliknięcia na figurę, by ją wybrać
2. [ ] Zaimplementuj wyświetlanie informacji o aktualnym graczu
3. [ ] Dodaj prosty licznik czasu dla gry
4. [ ] Zaimplementuj przyciski "Nowa gra" i "Zakończ grę"
5. [ ] Testuj interfejs pod kątem wygody obsługi

