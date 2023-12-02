import pygame, controls
from panda import Panda

def run():

    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    #background=pygame.image.load('images//bg1.jpg')
    pygame.display.set_caption("Bamboo Quest")
    bg_color = (1, 128, 1)
    panda = Panda(screen)



    while True:
        controls.events(panda)
        panda.update_panda()
        controls.update(bg_color, screen, panda)

run()

