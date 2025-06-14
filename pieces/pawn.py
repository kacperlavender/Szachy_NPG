# Import klasy bazowej Figura, z której dziedziczy Pionek
from pieces.piece import Figura

# Definicja klasy Pionek, dziedziczącej po Figurze
class Pionek(Figura):
    # Metoda zwracająca listę możliwych ruchów pionka na podanej planszy
    def mozliwe_ruchy(self, plansza):
        ruchy = []  # Lista na możliwe ruchy
        rzad, kolumna = self.pozycja  # Aktualna pozycja pionka (rzad i kolumna)

        # Kierunek ruchu zależy od koloru pionka: biały porusza się "w dół" (1), czarny "w górę" (-1)
        kierunek = 1 if self.kolor == 'bialy' else -1
        nowy_rzad = rzad + kierunek  # Nowy rząd po wykonaniu ruchu

        # Sprawdzenie, czy nowa pozycja mieści się w granicach planszy i czy pole przed pionkiem jest puste
        if 0 <= nowy_rzad < 8 and plansza.pola[nowy_rzad][kolumna] is None:
            ruchy.append((nowy_rzad, kolumna))
            rzad_startowy = 1 if self.kolor == 'bialy' else 6
            dwa_pola_rzad = rzad + 2 * kierunek
            if rzad == rzad_startowy and plansza.pola[dwa_pola_rzad][kolumna] is None:
                ruchy.append((dwa_pola_rzad, kolumna))


        for delta_kol in [-1, 1]:
            nowa_kolumna = kolumna + delta_kol
            if 0 <= nowa_kolumna < 8:
                pole = plansza.pola[nowy_rzad][nowa_kolumna]
                if pole is not None and pole.kolor != self.kolor:
                    ruchy.append((nowy_rzad, nowa_kolumna))

        return ruchy