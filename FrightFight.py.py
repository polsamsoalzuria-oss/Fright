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

ANCHO, ALTO = 1536, 797
NEGRO, BLANCO = (0, 0, 0), (255, 255, 255)


def dibujar_menu(screen, fuente, botones):
    screen.fill(BLANCO)
    for boton, texto in botones:
        pygame.draw.rect(screen, NEGRO, boton)
        imagen = fuente.render(texto, True, BLANCO)
        screen.blit(imagen, imagen.get_rect(center=boton.center))



def actualizar_juego(player, suelo, velocidad_y, en_el_suelo, dt):
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a]:

        player.x -= 300 * dt
    if teclas[pygame.K_d]:
        player.x += 300 * dt
    if teclas[pygame.K_LSHIFT]:   #dash impulso)
        player.x += 450 * dt
    if teclas[pygame.K_w] and en_el_suelo:
        velocidad_y, en_el_suelo = -650, False

    velocidad_y += 1800 * dt
    player.y += velocidad_y * dt
    if player.colliderect(suelo) and velocidad_y >= 0:
        player.bottom, velocidad_y, en_el_suelo = suelo.top, 0, True
    player.left = max(0, player.left)
    player.right = min(ANCHO, player.right)
    return velocidad_y, en_el_suelo


    screen.fill((0, 0, 0))


def dibujar_juego(screen, suelo, player, fredbear):
    screen.fill(NEGRO)

    pygame.draw.rect(screen, (100, 65, 35), suelo)
    screen.blit(fredbear, player)
    screen.blit(fredbear_puño, player_puño)


def main():
    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Fright Fight")
    clock = pygame.time.Clock()
    fuente = pygame.font.Font(None, 48)
    fredbear = pygame.image.load("fredbearv2.png")
    player = pygame.Rect(100, 300, *fredbear.get_size())
    suelo = pygame.Rect(0, 650, ANCHO, ALTO - 650)
    botones = [
        (pygame.Rect((ANCHO - 320) // 2, y, 320, 70), texto)
        for y, texto in ((260, "START"), (360, "REGISTRARSE"), (460, "INICIAR SESION"))
    ]
    estado, velocidad_y, en_el_suelo = "menu", 0, False
    ejecutando = True

    while ejecutando:
        dt = clock.tick(120) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
            elif estado == "menu" and event.type == pygame.MOUSEBUTTONDOWN:
                if botones[0][0].collidepoint(event.pos):
                    estado = "juego"

        if estado == "menu":
            dibujar_menu(screen, fuente, botones)
        else:
            velocidad_y, en_el_suelo = actualizar_juego(
                player, suelo, velocidad_y, en_el_suelo, dt
            )
            dibujar_juego(screen, suelo, player, fredbear)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
 