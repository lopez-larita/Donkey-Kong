import pygame
from config import *


class Platform(pygame.sprite.Sprite):
    def __init__(self, groups, x_pos, y_pos, length, screen) -> None:
        super().__init__(groups)

        self.x_pos = x_pos * section_width
        self.y_pos = y_pos
        self.length = length
        self.screen = screen
        self.top = self.draw()

    def draw(self):
        line_width = 6
        line_color = (225, 51, 129)
        for i in range(self.length):
            bot_coord = self.y_pos + section_height
            left_coord = self.x_pos + section_width * i
            mid_coord = left_coord + section_width * 0.5
            right_coord = left_coord + section_width
            top_coord = self.y_pos
            # draw 4 lines, top, bot, left diag, right diag
            pygame.draw.line(self.screen, line_color, (left_coord, top_coord),
                             (right_coord, top_coord), line_width)
            pygame.draw.line(self.screen, line_color, (left_coord, bot_coord),
                             (right_coord, bot_coord), line_width)
            pygame.draw.line(self.screen, line_color, (left_coord, bot_coord),
                             (mid_coord, top_coord), line_width)
            pygame.draw.line(self.screen, line_color, (mid_coord, top_coord),
                             (right_coord, bot_coord), line_width)
        # get the top platform surface
        top_line = pygame.rect.Rect(
            (self.x_pos, self.y_pos), (self.length * section_width, 4))
        # pygame.draw.rect(self.screen, 'blue', top_line)
        return top_line
