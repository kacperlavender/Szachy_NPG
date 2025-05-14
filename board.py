class Plansza:
    def __init__(self):
        self.pola = [[None for _ in range(8)] for _ in range(8)]

        #dodac ustawienie początkowe

    def __str__(self):
        s=""
        for r in range(7, -1, -1):
            for c in range(8):
                #dodac sprawdzanie figur
                s += ". "
            s += "\n"
        return s