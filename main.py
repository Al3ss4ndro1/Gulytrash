import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 600, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
ciano = (0, 255, 255)
rosso = (255, 0, 0)
magenta = (230, 150, 255)
font = pygame.font.SysFont("Arial", 30)
clock = pygame.time.Clock()
fps = 60
WHITE = (255, 255, 255)
size = ((60, 50))
velocita_navicella = 5
proiettile_img = pygame.Surface((5, 10))
proiettile_img.fill(magenta)
velocita_proiettile = 7
sizen = ((40, 30))
velocita_nemico = 3
class Navicella:
    def __init__(self, size):
        self.image = pygame.image.load('immagini/navicella_nosfondo.png')
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 100))

    def movimento(self, dx, dy):
        self.rect.x += dx * velocita_navicella
        self.rect.y += dy * velocita_navicella
        self.rect.x = max(0, min(WIDTH - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(HEIGHT - self.rect.height, self.rect.y))

    def disegno(self, surface):
        surface.blit(self.image, self.rect)


class Nemico:
    def __init__(self, size):
        self.image = pygame.image.load('immagini/nemico_nosfondo.png')
        self.image = pygame.transform.scale(self.image, size)
        x = random.randint(0, WIDTH - self.image.get_width())
        self.rect = self.image.get_rect(topleft=(x, -40))

    def move(self):
        self.rect.y += velocita_nemico

    def disegno(self, surface):
        surface.blit(self.image, self.rect)


class Proiettile:

    def __init__(self, x, y):
        self.rect = proiettile_img.get_rect(center=(x, y))

    def movimento(self):
        self.rect.y -= velocita_proiettile

    def disegno(self, surface):
        surface.blit(proiettile_img, self.rect)


navicella = Navicella(size)
proiettili = []
nemici = []
score = 0
spawn_timer = 0
running = True
while running:
    clock.tick(fps)
    win.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        navicella.movimento(-1,0)
    if keys[pygame.K_RIGHT]:
        navicella.movimento(1,0)
    if keys[pygame.K_UP]:
        navicella.movimento(0,-1)
    if keys[pygame.K_DOWN]:
        navicella.movimento(0,1)
    if keys[pygame.K_SPACE] and len(proiettili) < 5:
        proiettili.append(
            Proiettile(navicella.rect.centerx, navicella.rect.top))

    for proiettile in proiettili[:]:
        proiettile.movimento()
        if proiettile.rect.bottom < 0:
            proiettili.remove(proiettile)

    spawn_timer += 4
    if spawn_timer > 60:  
        nemici.append(Nemico(sizen))
        spawn_timer = 0

    for nemico in nemici[:]:
        nemico.move()
        if nemico.rect.top > HEIGHT:
            nemici.remove(nemico)
        
        if nemico.rect.colliderect(navicella.rect):
            running = False  

    for proiettile in proiettili[:]:
        for nemico in nemici[:]:
            if proiettile.rect.colliderect(nemico.rect):
                proiettili.remove(proiettile)
                nemici.remove(nemico)
                score += 1
                break

    navicella.disegno(win)
    for proiettile in proiettili:
        proiettile.disegno(win)
    for nemico in nemici:
        nemico.disegno(win)
    score_text = font.render(f"Score: {score}", True, WHITE)
    win.blit(score_text, (10, 10))
    pygame.display.flip()

game_over_text = font.render(f"Game Over! Final Score: {score}", True, WHITE)
text_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2))
win.blit(game_over_text, text_rect)
pygame.display.flip()
pygame.time.wait(2000)  
pygame.quit()
sys.exit()

if __name__ == "__main__":
    main()
        