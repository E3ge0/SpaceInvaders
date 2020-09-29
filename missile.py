import pygame

class Missile(pygame.sprite.Sprite):

    def __init__(self, player, game):
        super().__init__()
        self.image = pygame.image.load('assets/basic/missile.png')
        self.rect = self.image.get_rect()
        self.player = player
        self.game = game
        self.rect.x = player.rect.x + (player.rect.width / 3)
        self.rect.y = player.rect.y
        self.velocity = 15

    def auto_move(self):
        if not self.game.check_collision_missile(self, self.player.all_monstre):
            self.rect.y -= self.velocity
            if self.rect.y < 0:
                self.remove()
                print("Missile deleted")
        else:
            self.player.score += 1

    def remove(self):
        self.player.all_missiles.remove(self)
