import pygame
import random
import math

pygame.init()

# Määritä ruudun koko
leveys, korkeus = 800, 600
ruutu = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption("Punaisia, vihreitä ja sininen pallo")

# Määritä värit
valkoinen = (255, 255, 255)
musta = (0, 0, 0)
sininen = (0, 0, 255)
punainen = (255, 0, 0)
vihrea = (0, 255, 0)

# Pallon ominaisuudet
pallon_sade = 20
sinisen_pallon_sade = 20
sinisen_pallon_x = leveys // 2
sinisen_pallon_y = korkeus // 2
sinisen_pallon_liikkeen_muutos = 5

pallon_pienennys = 2
pallon_kasvatus = 4
maksimi_kasvatus_kerrat = 2

punaiset_pallot = []
vihreat_pallot = []
for _ in range(10):
    punaiset_pallot.append([random.randint(0, leveys - 40), random.randint(40, korkeus - 40)])
    vihreat_pallot.append([random.randint(50, leveys - 50), random.randint(50, korkeus - 50)])

kello = pygame.time.Clock()
running = True

def piirra_pallot():
    ruutu.fill(musta)
    pygame.draw.circle(ruutu, sininen, (sinisen_pallon_x, sinisen_pallon_y), sinisen_pallon_sade)
    for punainen_pallo in punaiset_pallot:
        pygame.draw.circle(ruutu, punainen, (punainen_pallo[0], punainen_pallo[1]), pallon_sade)
    for vihrea_pallo in vihreat_pallot:
        pygame.draw.circle(ruutu, vihrea, (vihrea_pallo[0], vihrea_pallo[1]), pallon_sade)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Liikutetaan sinistä palloa satunnaisesti
    suunta_x = random.choice([-1, 0, 1])
    suunta_y = random.choice([-1, 0, 1])
    sinisen_pallon_x += suunta_x * sinisen_pallon_liikkeen_muutos
    sinisen_pallon_y += suunta_y * sinisen_pallon_liikkeen_muutos

    # Tarkista, ettei sininen pallo mene ruudun ulkopuolelle
    sinisen_pallon_x = max(pallon_sade, min(sinisen_pallon_x, leveys - pallon_sade))
    sinisen_pallon_y = max(pallon_sade, min(sinisen_pallon_y, korkeus - pallon_sade))

    # Tarkista, ettei sininen pallo törmää punaisiin palloihin
    for punainen_pallo in punaiset_pallot:
        etaisyys = math.sqrt((sinisen_pallon_x - punainen_pallo[0])**2 + (sinisen_pallon_y - punainen_pallo[1])**2)
        if etaisyys < pallon_sade + sinisen_pallon_sade:
            sinisen_pallon_sade = max(0, sinisen_pallon_sade - pallon_pienennys)
            suunta_x = random.choice([-1, 0, 1])
            suunta_y = random.choice([-1, 0, 1])
            sinisen_pallon_x += suunta_x * sinisen_pallon_liikkeen_muutos
            sinisen_pallon_y += suunta_y * sinisen_pallon_liikkeen_muutos

    # Tarkista, jos sininen pallo osuu vihreisiin palloihin, kasvata sen kokoa
    for vihrea_pallo in vihreat_pallot:
        etaisyys = math.sqrt((sinisen_pallon_x - vihrea_pallo[0])**2 + (sinisen_pallon_y - vihrea_pallo[1])**2)
        if etaisyys < pallon_sade + sinisen_pallon_sade and sinisen_pallon_sade < maksimi_kasvatus_kerrat * pallon_kasvatus:
            sinisen_pallon_sade += pallon_kasvatus

    # Piirrä pallot
    piirra_pallot()

    pygame.display.flip()
    kello.tick(60)

pygame.quit()
