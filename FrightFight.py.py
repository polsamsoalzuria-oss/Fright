from api_login import *
import pygame

app="fright"

pygame.init()
ANCHO = 1536
ALTO = 797
screen = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()

player = pygame.Rect(100, 300, 50, 50)
player_puño = pygame.Rect(100, 3000, 50, 50)


fredbear = pygame.image.load("fredbearv2.png")
fredbear_puño = pygame.image.load("fredbear_puño.png")

suelo = pygame.Rect(0, 650, ANCHO, ALTO - 650)
velocidad_y = 0
en_el_suelo = False

running = True
while running:
    dt = clock.tick(120) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

<<<<<<< HEAD
    #if keys[pygame.K_w]: player.y -= 5
    #if keys[pygame.K_s]: player.y += 5
    if keys[pygame.K_a]: player.x -= 5
    if keys[pygame.K_d]: player.x += 5
    if keys[pygame.K_e]: player_puño.x = player.x - 50
    if keys[pygame.K_e]: player_puño.y = player.y
    
    if keys[pygame.K_SPACE]: player.x += 10 #dash
=======
    if keys[pygame.K_a]:
        player.x -= 300 * dt
    if keys[pygame.K_d]:
        player.x += 300 * dt

    if keys[pygame.K_SPACE] and en_el_suelo:
        velocidad_y = -650
        en_el_suelo = False

    gravedad = 1800
    velocidad_y += gravedad * dt
    player.y += velocidad_y * dt

    if player.colliderect(suelo):
        if velocidad_y >= 0:
            player.bottom = suelo.top
            velocidad_y = 0
            en_el_suelo = True

    player.left = max(0, player.left)
    player.right = min(ANCHO, player.right)

>>>>>>> 712ad83 (pau)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (100, 65, 35), suelo)
    screen.blit(fredbear, player)
    screen.blit(fredbear_puño, player_puño)

    pygame.display.flip()

pygame.quit()



