from api_login import *
import pygame

app="fright"

pygame.init()
screen = pygame.display.set_mode((1536, 797))
clock = pygame.time.Clock()

player = pygame.Rect(100, 300, 50, 50)
player_puño = pygame.Rect(100, 3000, 50, 50)


fredbear = pygame.image.load("fredbearv2.png")
fredbear_puño = pygame.image.load("fredbear_puño.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    #if keys[pygame.K_w]: player.y -= 5
    #if keys[pygame.K_s]: player.y += 5
    if keys[pygame.K_a]: player.x -= 5
    if keys[pygame.K_d]: player.x += 5
    if keys[pygame.K_e]: player_puño.x = player.x - 50
    if keys[pygame.K_e]: player_puño.y = player.y
    
    if keys[pygame.K_SPACE]: player.x += 10 #dash
    screen.fill((0, 0, 0))
    screen.blit(fredbear, player)
    screen.blit(fredbear_puño, player_puño)


    pygame.display.flip()
    clock.tick(120)

pygame.quit()



