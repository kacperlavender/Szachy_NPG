from pieces.piece import Figura

class Krol(Figura):
    def mozliwe_ruchy(self, plansza):
        ruchy = []
        rzad, kolumna = self.pozycja
      
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = rzad + dr, kolumna + dc
                if 0 <= nr < 8 and 0 <= nc < 8 and (plansza.pola[nr][nc] is None or plansza.pola[nr][nc].kolor != self.kolor):
                    ruchy.append((nr, nc))
      
        return ruchy
