import pygame
from config import *


class Barrel(pygame.sprite.Sprite):
    def __init__(self, groups, x_pos, y_pos):
        super().__init__(groups)
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.barrel_img = pygame.transform.scale(pygame.image.load(
            "./src/assets/images/barrel.png").convert_alpha(), (30, 30))
        self.rect = self.barrel_img.get_rect(
            center=(self.x_pos, self.y_pos))

        self.speed_y = 0
        self.speed_x = 3
        self.pos = 0

        self.oil_collision = False
        self.falling = False
        self.check_ladder = False
        self.bottom = self.rect

    def draw_barrels(self, screen):
        screen.blit(pygame.transform.rotate(self.barrel_side_img, 90),
                    (section_width * 1.2, section_height * 6.6))
        screen.blit(pygame.transform.rotate(self.barrel_side_img, 90),
                    (section_width * 2.5, section_height * 6.6))
        screen.blit(pygame.transform.rotate(self.barrel_side_img, 90),
                    (section_width * 2.5, section_height * 8.8))
        screen.blit(pygame.transform.rotate(self.barrel_side_img, 90),
                    (section_width * 1.2, section_height * 8.8))

    def update(self, collide_surface):

        if self.speed_y < 19 and not self.falling:
            self.speed_y += 2
            for i in range(len(collide_surface)):
                if self.bottom.colliderect(collide_surface[i]):
                    self.speed_y = 0
                    self.falling = False
            # if self.rect.colliderect(oil_drum):
            #     if not self.oil_collision:
            #         self.oil_collision = True
            #         if random.randint(0, 4) == 4:
            #             fireball_trigger = True

            if not self.falling:
                if row5_top >= self.rect.bottom or row3_top >= self.rect.bottom >= row4_top or row1_top > self.rect.bottom >= row2_top:
                    self.speed_x = 5
                else:
                    self.speed_x = -5
            else:
                self.x_speed = 0

            self.rect.move_ip(self.speed_x, self.speed_y)
            if self.rect.top > HEIGHT:
                self.kill()

            if self.speed_x > 0:
                if self.pos < 3:
                    self.pos += 1
                else:
                    self.pos = 0
            else:
                if self.pos > 0:
                    self.pos -= 1
                else:
                    self.pos = 3

            # self.bottom = pygame.rect.Rect(
            #     (self.rect[0], self.rect.bottom), (self.rect[2], 3))

    def draw(self, screen):
        screen.blit(pygame.transform.rotate(
            self.barrel_img, 90 * self.pos), self.rect.topleft)
