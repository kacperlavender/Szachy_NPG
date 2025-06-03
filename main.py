from board import Plansza


def konwertuj_notacje(notacja):
    if len(notacja) == 2 and 'a' <= notacja[0] <= 'h' and '1' <= notacja[1] <= '8':
        kolumna = ord(notacja[0]) - ord('a')
        rzad = int(notacja[1]) - 1
        return (rzad, kolumna)
    return None


plansza = Plansza()
print(plansza)
print(f"Tura gracza: {plansza.tura}")


while True:
    start_str = input("Podaj pozycję startową (np. a1): ")
    koniec_str = input("Podaj pozycję końcową (np. a2): ")

    start_pozycja = konwertuj_notacje(start_str)
    koniec_pozycja = konwertuj_notacje(koniec_str)

    if start_pozycja and koniec_pozycja:
        if plansza.wykonaj_ruch(start_pozycja, koniec_pozycja):
            print(plansza)
        else:
            print("Nieprawidłowy ruch.")
    else:
        print("Nieprawidłowy format pozycji.")
