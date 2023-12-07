import pygame
from pygame.locals import *
from config import *
from sprite_sheet import SpriteSheet
from platforms import Platform


class Player(pygame.sprite.Sprite):
    def __init__(self, groups, sprite_sheet) -> None:
        super().__init__(groups)

        self.animations = sprite_sheet.get_animations_dict()
        self.current_sprite = 0
        self.image = self.animations["right"][self.current_sprite]
        self.rect = self.image.get_rect(topleft=(150, row1_y))
        self.speed = 5
        self.last_update = pygame.time.get_ticks()
        self.time_animation = 100

        self.speed_y = 0
        self.jump_power = -10

    def update(self):
        self.speed_y += GRAVITY
        self.rect.y += self.speed_y

        if self.rect.bottom >= row1_y:
            self.rect.bottom = row1_y
            self.speed_y = 0
        elif self.rect.bottom >= row2_y:
            self.rect.bottom = row2_y
            self.speed_y = 0
        elif self.rect.bottom >= row3_y:
            self.rect.bottom = row3_y
            self.speed_y = 0
        elif self.rect.bottom >= row4_y:
            self.rect.bottom = row4_y
            self.speed_y = 0
        elif self.rect.bottom >= row5_y:
            self.rect.bottom = row5_y
            self.speed_y = 0
        elif self.rect.bottom >= row6_y:
            self.rect.bottom = row6_y
            self.speed_y = 0

        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            if self.rect.right <= WIDTH:
                self.rect.x += self.speed
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite += 1
                    self.image = self.animations["right"][self.current_sprite]
                    if self.current_sprite == 1:
                        self.current_sprite = 0
                    self.last_update = current_time

        if keys[K_LEFT]:
            if self.rect.left >= 0:
                self.rect.x -= self.speed
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite += 1
                    self.image = self.animations["left"][self.current_sprite]
                    if self.current_sprite == 1:
                        self.current_sprite = 0
                    self.last_update = current_time

        if keys[K_SPACE]:
            self.jump()

    def jump(self):
        self.speed_y = self.jump_power
