from pieces.piece import Figura

# Klasa Krolowa (królowa), która dziedziczy po klasie Figura
class Krolowa(Figura):
    # Metoda zwracająca wszystkie możliwe ruchy królowej na danej planszy
    def mozliwe_ruchy(self, plansza):
        ruchy_wiezy = Wieza(self.kolor, self.pozycja).mozliwe_ruchy(plansza)
        ruchy_gonca = Goniec(self.kolor, self.pozycja).mozliwe_ruchy(plansza)
        return ruchy_wiezy + ruchy_gonca
