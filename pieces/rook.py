class Wieza(Figura):
    # Metoda do wyliczania możliwych ruchów wieży
    def mozliwe_ruchy(self, plansza):
        ruchy = []  # Lista na legalne ruchy
        rzad, kolumna = self.pozycja  # Aktualna pozycja wieży

        # Iteruj przez cztery kierunki: prawo, lewo, dół, góra
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            # Sprawdź pola w danym kierunku, od 1 do 7 pól od wieży
            for i in range(1, 8):
                nr, nc = rzad + i * dr, kolumna + i * dc  # Oblicz nową pozycję

                # Sprawdź, czy nowa pozycja jest na szachownicy
                if 0 <= nr < 8 and 0 <= nc < 8:
                    # Jeśli pole jest puste, dodaj je do możliwych ruchów
                    if plansza.pola[nr][nc] is None:
                        ruchy.append((nr, nc))
                    # Jeśli na polu jest figura przeciwnika, dodaj ruch zbicia i zatrzymaj się w tym kierunku
                    elif plansza.pola[nr][nc].kolor != self.kolor:
                        ruchy.append((nr, nc))
                        break
                    # Jeśli na polu jest własna figura, wieża jest zablokowana w tym kierunku
                    else:
                        break
                # Jeśli nowa pozycja wykracza poza szachownicę, zakończ sprawdzanie w tym kierunku
                else:
                    break
        return ruchy  # Zwróć listę wszystkich możliwych ruchów
