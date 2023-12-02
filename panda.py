import pygame

class Panda():

    def __init__(self, screen):
        """инициализация панды"""

        self.screen = screen
        self.image = pygame.image.load('image/Panda_sitting.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        self.rect.center = self.screen_rect.center
        self.center = float(self.rect.centerx)



        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False

    def output(self):
        """рисование панды"""
        self.screen.blit(self.image, self.rect)

    def update_panda(self):
        """обновление позиции панды"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        if self.mleft and self.rect.left > 0:
            self.center -= 1.5
        if self.mup and self.rect.up < self.screen_rect.up:
            self.centery += 1.5
        if self.mdown and self.rect.down > 0:
            self.centery -= 1.5

        self.rect.centerx = self.center

