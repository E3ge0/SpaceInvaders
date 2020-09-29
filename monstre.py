import pygame
import random

class Monstre(pygame.sprite.Sprite):
    def __init__(self, player, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('./assets/basic/Enemy4.png')
        self.rect = self.image.get_rect()
        self.player = player
        self.rect.x = random.randint(1, 1079)
        self.rect.y = 0
        self.velocity = random.randint(2, 10)
        print(" X_Monster : ", self.rect.x)

    def move(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.y += self.velocity
            if self.rect.y > 720:
                self.player.all_monstre.remove(self)
                print("monstre supprimé")
