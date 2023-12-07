import pygame
from pygame.locals import *
from config import *
from sprite_sheet import SpriteSheet


class Kong(pygame.sprite.Sprite):
    def __init__(self, groups, sprite_sheet):
        super().__init__(groups)
        self.animations = sprite_sheet.get_animations_dict()
        self.current_sprite = 0
        self.image = self.animations["right"][self.current_sprite]
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.speed = 5
        self.last_update = pygame.time.get_ticks()
        self.time_animation = 100

    def update(self):

        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.time_animation:
            self.current_sprite += 1
            self.image = self.animations["right"][self.current_sprite]
            if self.current_sprite == 3:
                self.current_sprite = 0
            self.last_update = current_time
