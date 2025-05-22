class Wieza(Figura):
    # Metoda zwracająca listę możliwych ruchów dla wieży
    def mozliwe_ruchy(self, plansza):
        ruchy = []  # Inicjalizacja pustej listy na możliwe ruchy
        rzad, kolumna = self.pozycja  # Pobranie aktualnej pozycji wieży (rząd i kolumna)
        # Definicja kierunków ruchu dla wieży: (0, 1) - prawo, (0, -1) - lewo, (1, 0) - dół, (-1, 0) - góra
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            for i in range(1, 8):

	# TO DO:

        # Pętla iterująca przez pola w danym kierunku (od 1 do 7 pól od wieży)
        # Obliczenie współrzędnych kolejnego pola
        # Sprawdzenie, czy obliczone współrzędne mieszczą się w granicach planszy (0-7 dla rzędów i kolumn)


        return ruchy  # Zwróć listę wszystkich możliwych ruchów
