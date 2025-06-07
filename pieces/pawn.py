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
            ruchy.append((nowy_rzad, kolumna))  # Dodanie możliwego ruchu do listy

        return ruchy  # Zwrócenie listy możliwych ruchów
