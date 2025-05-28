import pygame

class Esplosione:
    def __init__(self, x, y, size):
        self.image = pygame.image.load('immagini/esplosione (1).png')
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(center=(x, y))
        self.start_time = pygame.time.get_ticks()
        self.duration = 300  

    def disegno(self, surface):
        surface.blit(self.image, self.rect)

    def scaduta(self):
        return pygame.time.get_ticks() - self.start_time > self.duration

class Esplosione2:
    def __init__(self, x, y, size):
        self.image = pygame.image.load('immagini/esplosione2 (1).png')
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(center=(x, y))
        self.start_time = pygame.time.get_ticks()
        self.duration = 300  

    def disegno(self, surface):
        surface.blit(self.image, self.rect)

    def scaduta(self):
        return pygame.time.get_ticks() - self.start_time > self.duration