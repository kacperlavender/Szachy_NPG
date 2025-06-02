def konwertuj_notacje(notacja):
    if len(notacja) == 2 and 'a' <= notacja[0] <= 'h' and '1' <= notacja[1] <= '8':
        kolumna = ord(notacja[0]) - ord('a')
        rzad = int(notacja[1]) - 1
        return (rzad, kolumna)
    return None


plansza = Plansza()
print(plansza)



