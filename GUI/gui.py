import pygame
from board import Plansza

ROZMIAR_OKNA = 480
ROZMIAR_POLA = ROZMIAR_OKNA // 8
KOLORY = [(238, 238, 210), (118, 150, 86)]  # jasne / ciemne pola

def rysuj_plansze(ekran):
    for rzad in range(8):
        for kol in range(8):
            kolor = KOLORY[(rzad + kol) % 2]
            pygame.draw.rect(
                ekran,
                kolor,
                pygame.Rect(kol * ROZMIAR_POLA, rzad * ROZMIAR_POLA, ROZMIAR_POLA, ROZMIAR_POLA)
            )

def main():
    pygame.init()
    ekran = pygame.display.set_mode((ROZMIAR_OKNA, ROZMIAR_OKNA))
    pygame.display.set_caption("Szachy w Pythonie")

    clock = pygame.time.Clock()
    plansza = Plansza()

    running = True
    while running:
        ekran.fill((0, 0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
