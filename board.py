class Plansza:
    def __init__(self):
        self.pola = [[None for _ in range(8)] for _ in range(8)]

        #dodac ustawienie początkowe

    def __str__(self):
        s = "  a b c d e f g h\n"
        for r in range(7, -1, -1):
            s += f"{r + 1} "
            for c in range(8):
                figura = self.pola[r][c]
                s += (str(figura) + " ") if figura else (". ")
            s += "\n"
        return s
