import pygame
from missile import Missile
from monstre import Monstre


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('assets/basic/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 540
        self.velocity = 7
        self.all_missiles = pygame.sprite.Group()
        self.all_monstre = pygame.sprite.Group()
        self.score = 0

    def move_x(self, sens_x):
        if sens_x == pygame.K_LEFT:
            if not self.game.check_collision(self, self.all_monstre):
                self.rect.x -= self.velocity
            else:
                self.rect.x += self.velocity
        if sens_x == pygame.K_RIGHT:
            if not self.game.check_collision(self, self.all_monstre):
                self.rect.x += self.velocity
            else:
                self.rect.x -= self.velocity

    def move_y(self, sens_y):
        if sens_y == pygame.K_UP:
            if not self.game.check_collision(self, self.all_monstre):
                self.rect.y -= self.velocity
            else:
                self.rect.y += self.velocity
        if sens_y == pygame.K_DOWN:
            if not self.game.check_collision(self, self.all_monstre):
                self.rect.y += self.velocity
            else:
                self.rect.y -= self.velocity

    def tir(self):
        self.all_missiles.add(Missile(self, self.game))

    def spawn_monster(self):
        self.all_monstre.add(Monstre(self, self.game))
