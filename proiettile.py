import pygame


class Proiettile:
    def __init__(self, x, y, size):
        self.image = pygame.image.load('immagini/laser (1).png')
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(center=(x, y))
    def movimento(self):
        self.rect.y -= velocita_proiettile
    def disegno(self, surface):
        surface.blit(self.image, self.rect)


class Bonus:
    def __init__(self, x, y, size):
        self.image = pygame.image.load('immagini/bonus.png')
        self.image = pygame.transform.scale(self.image, size)  
        self.rect = self.image.get_rect(center=(x, y))
    def movimento(self):
        self.rect.y += 2
    def disegno(self, surface):
        surface.blit(self.image, self.rect)