import pygame
from player import Player
from monstre import Monstre

class Game:
    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.pressed_key_x = {}
        self.pressed_key_y = {}
        self.random_verif = {}
        self.game_duration = 500

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def check_collision_missile(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask)
