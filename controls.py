import pygame
import sys

import panda


def events(panda):
    """обработка собітий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                panda.mright = True
            elif event.key == pygame.K_a:
                panda.mleft = True
            elif event.key == pygame.K_w:
                panda.mup = True
            elif event.key == pygame.K_s:
                panda.mdown = True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                panda.mright = False
            elif event.key == pygame.K_a:
                panda.mleft = False
            elif event.key == pygame.K_w:
                panda.mup = False
            elif event.key == pygame.K_s:
                panda.mdown = False




def update (bg_color, screen, panda):
    """обновление єкрана"""
    screen.fill(bg_color)
    panda.output()
    pygame.display.flip()

