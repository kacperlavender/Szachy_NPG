from pieces.piece import Figura
from pieces.pawn import Pionek
from pieces.rook import Wieza
from pieces.knight import Skoczek
from pieces.bishop import Goniec
from pieces.queen import Krolowa
from pieces.king import Krol

class Plansza:
    def __init__(self):
        self.pola = [[None for _ in range(8)] for _ in range(8)]
        self.initialise()
        self.tura = 'bialy'  # białe zaczynają

    def initialise(self):
        for c in range(8):
            self.pola[1][c] = Pionek('bialy', (1, c))
            self.pola[6][c] = Pionek('czarny', (6, c))
        self.initialise_figure(0, Wieza)
        self.initialise_figure(1, Skoczek)
        self.initialise_figure(2, Goniec)
        self.pola[0][3] = Krol('bialy', (0, 3))
        self.pola[0][4] = Krolowa('bialy', (0, 4))
        self.pola[7][3] = Krol('czarny', (7, 3))
        self.pola[7][4] = Krolowa('czarny', (7, 4))

    def initialise_figure(self, kol, figura_klasa):
        self.pola[0][kol] = figura_klasa('bialy', (0, kol))
        self.pola[0][7 - kol] = figura_klasa('bialy', (0, 7 - kol))
        self.pola[7][kol] = figura_klasa('czarny', (7, kol))
        self.pola[7][7 - kol] = figura_klasa('czarny', (7, 7 - kol))

    def __str__(self):
        s = "  a  b  c  d  e  f  g  h\n"
        for r in range(7, -1, -1):
            s += f"{r + 1} "
            for c in range(8):
                figura = self.pola[r][c]
                s += (str(figura) + " ") if figura else (".. ")
            s += "\n"
        return s

    def get_figure(self, pozycja):
        r, c = pozycja
        return self.pola[r][c] if 0 <= r < 8 and 0 <= c < 8 else None

    def wykonaj_ruch(self, start, koniec):
        sr, sc = start
        dr, dc = koniec
        figura = self.pola[sr][sc]

        if not figura:
            return False  # brak figury na starcie
        if figura.kolor != self.tura:
            return False  # nie ta tura

        if koniec in figura.mozliwe_ruchy(self):
            self.pola[dr][dc] = figura
            self.pola[sr][sc] = None
            figura.pozycja = (dr, dc)

            # Promocja pionka
            if isinstance(figura, Pionek):
                ostatni_rzad = 7 if figura.kolor == 'bialy' else 0
                if dr == ostatni_rzad:
                    self.pola[dr][dc] = Krolowa(figura.kolor, (dr, dc))
                    print(f"Promocja pionka {figura.kolor} na hetmana")

            # Zmiana tury
            self.tura = 'czarny' if self.tura == 'bialy' else 'bialy'
            return True

        return False

