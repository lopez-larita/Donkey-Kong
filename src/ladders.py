import pygame
from config import *


class Ladder():
    def __init__(self, x_pos, y_pos, length, screen):
        self.x_pos = x_pos * section_width
        self.y_pos = y_pos
        self.length = length
        self.screen = screen
        self.body = self.draw()

    def draw(self):
        line_width = 2
        ladder_color = (255, 255, 255)
        ladder_height = 0.6

        for i in range(self.length):
            top_coord = self.y_pos + ladder_height * section_height * i
            bot_coord = top_coord + ladder_height * section_height
            mid_coord = (ladder_height / 2) * section_height + top_coord
            left_coord = self.x_pos
            right_coord = left_coord + section_width

            pygame.draw.line(self.screen, ladder_color, (left_coord,
                             top_coord), (left_coord, bot_coord), line_width)
            pygame.draw.line(self.screen, ladder_color, (right_coord,
                             top_coord), (right_coord, bot_coord), line_width)
            pygame.draw.line(self.screen, ladder_color, (left_coord,
                             mid_coord), (right_coord, mid_coord), line_width)

        body = pygame.rect.Rect((self.x_pos, self.y_pos - 30),
                                (section_width, (ladder_height * self.length * section_height + section_height)))

        # pygame.draw.rect(self.screen, 'blue', body)
        return body
