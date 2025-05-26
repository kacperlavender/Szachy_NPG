class Plansza:
    def __init__(self):
        self.pola = [[None for _ in range(8)] for _ in range(8)]
        self.initialise()

    #podmienić na faktyczne klasy figur
    def initialise(self):
        for c in range(8):
            self.pola[1][c] = "P"
            self.pola[6][c] = "p"
        self.initialise_figure(0,"w");
        self.initialise_figure(1,"k");
        self.initialise_figure(2,"b");
        self.initialise_figure(3,"k");

    def initialise_figure(self, kor,f):
        self.pola[0][kor] = f
        self.pola[0][7-kor] = f
        self.pola[7][kor] = f
        self.pola[7][7-kor] = f

    def __str__(self):
        s = "  a b c d e f g h\n"
        for r in range(7, -1, -1):
            s += f"{r + 1} "
            for c in range(8):
                figura = self.pola[r][c]
                s += (str(figura) + " ") if figura else (". ")
            s += "\n"
        return s

    def get_figure(self, pozycja):
        r, c = pozycja
        return self.pola[r][c] if 0 <= r < 8 and 0 <= c < 8 else None

    def wykonaj_ruch(self, start, koniec):
        sr, sc = start
        dr, dc = koniec
        figura = self.pola[sr][sc]
        if figura and koniec in figura.mozliwe_ruchy(self):
            self.pola[dr][dc] = figura
            self.pola[sr][sc] = None
            figura.pozycja = (dr, dc)
            return True
        return False

plansza = Plansza()
print(plansza)