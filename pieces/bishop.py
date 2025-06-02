from pieces.piece import Figura

#Klasa Goniec dziedziczy po klasie Figura
class Goniec(Figura):
    # Metoda zwracająca listę możliwych ruchów dla gońca
    def mozliwe_ruchy(self, plansza):
        ruchy = []
        rzad, kolumna = self.pozycja  # Obecna pozycja gońca (rząd i kolumna)

        # Możliwe kierunki ruchu dla gońca (po skosach)
        for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            for i in range(1, 8):  # Maksymalnie 7 pól w jednym kierunku
                nr, nc = rzad + i * dr, kolumna + i * dc  # Nowa pozycja

                # Sprawdzenie czy nowa pozycja jest w granicach planszy
                if 0 <= nr < 8 and 0 <= nc < 8:
                    pole = plansza.pola[nr][nc]

                    if pole is None:
                        ruchy.append((nr, nc))  # Pole wolne — można się tam ruszyć
                    elif pole.kolor != self.kolor:
                        ruchy.append((nr, nc))  # Przeciwnik — można zbić
                        break  # Nie można iść dalej za przeciwnika
                    else:
                        break  # Swój pionek — koniec kierunku
                else:
                    break  # Poza planszą — koniec kierunku

        return ruchy
