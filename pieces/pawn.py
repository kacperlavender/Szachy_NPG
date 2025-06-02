from pieces.piece import Figura

class Pionek(Figura):
    def mozliwe_ruchy(self, plansza):
        ruchy = []
        rzad, kolumna = self.pozycja
        kierunek = 1 if self.kolor == 'bialy' else -1
        nowy_rzad = rzad + kierunek
        if 0 <= nowy_rzad < 8 and plansza.pola[nowy_rzad][kolumna] is None:
            ruchy.append((nowy_rzad, kolumna))
        return ruchy