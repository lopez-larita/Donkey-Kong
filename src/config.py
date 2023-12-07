import pygame


WIDTH = 800
HEIGHT = 750
FPS = 60

GRAVITY = 1


# PLAYER
WIDTH_PLAYER = 40
HEIGHT_PLAYER = 40


# PLATAFORMAS
section_width = WIDTH // 32
section_height = HEIGHT // 32
slope = section_height // 8

row1_y = HEIGHT - 2 * section_height
row2_y = row1_y - 4 * section_height
row3_y = row2_y - 7 * slope - 3 * section_height
row4_y = row3_y - 4 * section_height
row5_y = row4_y - 7 * slope - 3 * section_height
row6_y = row5_y - 4 * section_height

row6_top = row6_y - 4 * slope
row5_top = row5_y - 8 * slope
row4_top = row4_y - 8 * slope
row3_top = row3_y - 8 * slope
row2_top = row2_y - 8 * slope
row1_top = row1_y - 5 * slope


# BARRELS
# barrel_spawn_time = 180  # 6 seconds
# barrel_count = barrel_spawn_time // 2  # 3 seconds
barrel_time = 180
