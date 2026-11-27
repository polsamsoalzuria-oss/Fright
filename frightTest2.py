from api_login import *
import pygame

app="fright"

print("\n\n#############################")
print("Prem una tecla")
print("#############################\n\n")
input("");

print(api_userlist(app))

#exemple de registre d'usuari
print (f"Esborrem per la app {app}, usuari=userdel amb pass=1234 ")
print(api_deleteuser(app, "alex","mypasswordzz"))

print("\n\n#############################")
print("Prem una tecla")
print("#############################\n\n")
input("");

print (f"Registrem per la app {app}, usuari=user2 amb pass=1234 ")
print(api_register(app, "user2","1234"))


print("\n\n#############################")
print("Prem una tecla")
print("#############################\n\n")
input("");

#exemple de login sense exit
print (f"\nFem login per la app {app}, usuari=alex amb pass=1234 ")
print(api_login(app,"alex","1234"))


print("\n\n#############################")
print("Prem una tecla")
print("#############################\n\n")
input("");



print("\n\n#############################")
print("Prem una tecla")
print("#############################\n\n")
input("");

print("Fes un login amb un dels usuaris existents")
# exemple bucle login
while True:
    nom_aplicacio  = app
    username = input("Nom: ")
    passw = input ("Contrasenya: ")
    
    
    if api_login(nom_aplicacio, username, passw):
        print ("HAS ENTRAT!", username)
        #print(api_updatepunts(nom_aplicacio, username, passw,int(input("Update punts: "))))

        break
    else:
        print ("El login ha fallat, Torna-ho a intentar... ")

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
    
    screen.fill((0, 0, 0))
    screen.blit(fredbear, player)
    screen.blit(fredbear_puño, player_puño)


    pygame.display.flip()
    clock.tick(120)

pygame.quit()



