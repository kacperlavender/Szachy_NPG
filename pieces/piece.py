# klasa bazowa dla wszytkich figur

class Figura:
    def __init__(self, kolor, pozycja):
        self.kolor = kolor  # Atrybut przechowujący kolor figury.
        self.pozycja = pozycja  # Atrybut przechowujący pozycję figury.

    def mozliwe_ruchy(self, plansza):
        return []  # Metoda zwracająca listę możliwych ruchów (domyślnie pusta - do nadpisania).

    def __str__(self):
        return f"{self.kolor[0].upper()}{self.__class__.__name__[0]}"  
	# Metoda zwracająca tekstową reprezentację figury (pierwsza litera koloru i nazwy klasy).
