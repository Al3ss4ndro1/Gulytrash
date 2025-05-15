import pygame 
import random
import sys

pygame.init()
WIDTH, HEIGHT = 600,800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
ciano = (0, 255, 255)
rosso =(255, 0, 0)
magenta = (230, 150, 255)
font = pygame.font.SysFont("Arial", 30)
clock= pygame.time.Clock()
fps = 60

navicella = pygame.Surface(50, 40)
navicella.fill(ciano)
velocita_navicella = 5
proiettile = pygame.Surface(5, 10)
proiettile.fill(magenta)
velocita_proiettile = 7
nemico= pygame.Surface(30, 20)
nemico.fill(rosso)
velocita_nemico= 3

class Navicella:
    def __init__(self):
        self.rect = navicella.get_rect(center = (WIDTH //2, HEIGHT - 60))
    
    def movimento(self, sdx):
        self.rect.x = sdx * velocita_navicella
        self.rect.x = max(0, min(WIDTH - self.rect.width, self.rect.x))

    def disegno(self, surface):
        surface.blit(navicella, self.rect)
    

class Proiettile:
    def __init__(self, x, y):
        self.rect = proiettile.get_rect(center = (x, y))
    
    def movimento(self):
        self.rect.y -= velocita_proiettile
    
    def disegno(self, surface):
        surface.blit(proiettile,self.rect)

class Nemico:
    def __init__(self):
        x = random.randint(0, WIDTH - nemico.get_width())
        self.rect =nemico.get_rect(topleft =) 

         
