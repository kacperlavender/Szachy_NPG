# Klasa Krolowa (królowa), która dziedziczy po klasie Figura
class Krolowa(Figura):
    # Metoda zwracająca wszystkie możliwe ruchy królowej na danej planszy
    def mozliwe_ruchy(self, plansza):
        # TO DO:
        # Tworzymy tymczasowy obiekt Wieza (wieża) w tej samej pozycji i kolorze,
        # i pobieramy wszystkie możliwe ruchy wieży (ruchy w pionie i poziomie)


        # Tworzymy tymczasowy obiekt Goniec (goniec) w tej samej pozycji i kolorze,
        # i pobieramy wszystkie możliwe ruchy gońca (ruchy po skosach)


        # Łączymy oba zestawy ruchów, bo królowa porusza się jak wieża + jak goniec
        return ruchy_wiezy + ruchy_gonca
