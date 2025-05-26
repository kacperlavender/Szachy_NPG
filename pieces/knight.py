class Skoczek(Figura):
    def mozliwe_ruchy(self, plansza):
        # Inicjalizacja listy przechowującej możliwe ruchy skoczka
        ruchy = []
        # Pobranie aktualnej pozycji skoczka (wiersz, kolumna)
        rzad, kolumna = self.pozycja
        
        # Wszystkie możliwe kierunki ruchu skoczka (kształt litery 'L')
        for dr, dc in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
            # Nowa pozycja po ruchu
            nr, nc = rzad + dr, kolumna + dc
            
            # Sprawdzenie, czy nowa pozycja jest na planszy (8x8)
            # oraz czy pole jest puste lub przeciwnik (można bić)
            if 0 <= nr < 8 and 0 <= nc < 8 and (
                plansza.pola[nr][nc] is None or plansza.pola[nr][nc].kolor != self.kolor
            ):
                # Jeśli warunek spełniony, dodaj ruch do listy
                ruchy.append((nr, nc))
        
        # Zwróć listę możliwych ruchów
        return ruchy


