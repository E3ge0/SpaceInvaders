import pygame
import random
from game import Game
from missile import Missile
from monstre import Monstre

pygame.init()

pygame.display.set_caption("SpaceInvaders")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load('assets/Backgrounds/default.png')
finish = pygame.image.load('assets/basic/flag.png')

running = True

t = 0

verif = False
verif2 = False

game = Game()

tps = 0

while running and tps < game.game_duration:

    tps += 1
    print(tps)

    for missiles in game.player.all_missiles:
        missiles.auto_move()
    for monstre in game.player.all_monstre:
        monstre.move()

    if game.pressed_key_x.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_x(pygame.K_LEFT)
    elif game.pressed_key_x.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < 1080:
        game.player.move_x(pygame.K_RIGHT)

    if game.pressed_key_y.get(pygame.K_UP) and game.player.rect.y > 0:
        game.player.move_y(pygame.K_UP)
    elif game.pressed_key_y.get(pygame.K_DOWN) and game.player.rect.y + game.player.rect.width < 720:
        game.player.move_y(pygame.K_DOWN)

    if verif2 == True:
        verif2 = False
        t = random.randint(1, 200)

    t += 1
    if t == 200:
        game.player.spawn_monster()
        verif = True
        verif2 = True
        game.player.all_monstre.draw(screen)
        t = 0

    screen.blit(background, (0, 0))
    screen.blit(game.player.image, game.player.rect)
    game.player.all_missiles.draw(screen)

    if verif == True: game.player.all_monstre.draw(screen)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Closing the Game ...")
        if event.type == pygame.KEYDOWN:
            game.pressed_key_x[event.key] = True
            game.pressed_key_y[event.key] = True
            if event.key == pygame.K_SPACE:
                game.player.tir()
        elif event.type == pygame.KEYUP:
            game.pressed_key_x[event.key] = False
            game.pressed_key_y[event.key] = False

pygame.quit()
print("-----------------------------------------------------")
print(f"Le jeu est terminé, vous avez tué {game.player.score} monstre !")
print("--")
print("Appuyez sur une touche pour fermer le jeu !")
input("-----------------------------------------------------")


