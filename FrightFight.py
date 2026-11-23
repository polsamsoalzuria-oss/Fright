import pygame

pygame.init()
ANCHO = 1536
ALTO = 797
screen = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()

pato = pygame.Rect(1, 300, 55, 55)


running = True
while running == True:
    dt = clock.tick(120) / 1000.0
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.display.flip()
pygame.quit()