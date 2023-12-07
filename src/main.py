import pygame
from pygame.locals import *
import random
from config import *
from platforms import Platform
from ladders import Ladder
from barrels import Barrel
from sprite_sheet import SpriteSheet
from player import Player


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Donkey Kong")
# pygame.display.set_icon("image file")
clock = pygame.time.Clock()


font = pygame.font.Font("freesansbold.ttf", 50)
font2 = pygame.font.Font("freesansbold.ttf", 22)

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
barrels = pygame.sprite.Group()
player = pygame.sprite.Group()


sprite_sheet_player = SpriteSheet(pygame.image.load(
    "./src/assets/images/mario_sheet.png"). convert_alpha(), 6, 2, WIDTH_PLAYER, HEIGHT_PLAYER, ["left", "right", "jump", "climb", "hit_left", "hit_right"])

player = Player([all_sprites, player], sprite_sheet_player)


running = True

active_level = 0
levels = [{'platforms': [
    ([platforms], 1, row1_y, 15, screen),
    ([platforms], 16, row1_y - slope, 3, screen),
    ([platforms], 19, row1_y - 2 * slope, 3, screen),
    ([platforms], 22, row1_y - 3 * slope, 3, screen),
    ([platforms], 25, row1_y - 4 * slope, 3, screen),
    ([platforms], 28, row1_y - 5 * slope, 3, screen),
    ([platforms], 25, row2_y, 3, screen),
    ([platforms], 22, row2_y - slope, 3, screen),
    ([platforms], 19, row2_y - 2 * slope, 3, screen),
    ([platforms], 16, row2_y - 3 * slope, 3, screen),
    ([platforms], 13, row2_y - 4 * slope, 3, screen),
    ([platforms], 10, row2_y - 5 * slope, 3, screen),
    ([platforms], 7, row2_y - 6 * slope, 3, screen),
    ([platforms], 4, row2_y - 7 * slope, 3, screen),
    ([platforms], 2, row2_y - 8 * slope, 2, screen),
    ([platforms], 4, row3_y, 3, screen),
    ([platforms], 7, row3_y - slope, 3, screen),
    ([platforms], 10, row3_y - 2 * slope, 3, screen),
    ([platforms], 13, row3_y - 3 * slope, 3, screen),
    ([platforms], 16, row3_y - 4 * slope, 3, screen),
    ([platforms], 19, row3_y - 5 * slope, 3, screen),
    ([platforms], 22, row3_y - 6 * slope, 3, screen),
    ([platforms], 25, row3_y - 7 * slope, 3, screen),
    ([platforms], 28, row3_y - 8 * slope, 2, screen),
    ([platforms], 25, row4_y, 3, screen),
    ([platforms], 22, row4_y - slope, 3, screen),
    ([platforms], 19, row4_y - 2 * slope, 3, screen),
    ([platforms], 16, row4_y - 3 * slope, 3, screen),
    ([platforms], 13, row4_y - 4 * slope, 3, screen),
    ([platforms], 10, row4_y - 5 * slope, 3, screen),
    ([platforms], 7, row4_y - 6 * slope, 3, screen),
    ([platforms], 4, row4_y - 7 * slope, 3, screen),
    ([platforms], 2, row4_y - 8 * slope, 2, screen),
    ([platforms], 4, row5_y, 3, screen),
    ([platforms], 7, row5_y - slope, 3, screen),
    ([platforms], 10, row5_y - 2 * slope, 3, screen),
    ([platforms], 13, row5_y - 3 * slope, 3, screen),
    ([platforms], 16, row5_y - 4 * slope, 3, screen),
    ([platforms], 19, row5_y - 5 * slope, 3, screen),
    ([platforms], 22, row5_y - 6 * slope, 3, screen),
    ([platforms], 25, row5_y - 7 * slope, 3, screen),
    ([platforms], 28, row5_y - 8 * slope, 2, screen),
    ([platforms], 25, row6_y, 3, screen),
    ([platforms], 22, row6_y - slope, 3, screen),
    ([platforms], 19, row6_y - 2 * slope, 3, screen),
    ([platforms], 16, row6_y - 3 * slope, 3, screen),
    ([platforms], 2, row6_y - 4 * slope, 14, screen),
    ([platforms], 13, row6_y - 4 * section_height, 6, screen),
    ([platforms], 10, row6_y - 3 * section_height, 3, screen)],
    'ladders': [
    (12, row2_y + 8 * slope, 2, screen),
    (12, row2_y + 31 * slope, 2, screen),
    (25, row2_y + 13 * slope, 4, screen),
    (6, row3_y + 12 * slope, 3, screen),
    (14, row3_y + 8 * slope, 4, screen),
    (10, row4_y + 9 * slope, 1, screen),
    (10, row4_y + 30 * slope, 2, screen),
    (16, row4_y + 6 * slope, 5, screen),
    (25, row4_y + 10 * slope, 4, screen),
    (6, row5_y + 13 * slope, 3, screen),
    (11, row5_y + 8 * slope, 4, screen),
    (23, row5_y + 7 * slope, 1, screen),
    (23, row5_y + 26 * slope, 2, screen),
    (25, row6_y + 11 * slope, 4, screen),
    (13, row6_y + 6 * slope, 2, screen),
    (13, row6_y + 29 * slope, 2, screen),
    (18, row6_y - 32 * slope, 4, screen),
    (12, row6_y - 20 * slope, 2, screen),
    (10, row6_y - 20 * slope, 2, screen),
]}]


# EVENTOS PERSONALIZADOS
EVENT_BARREL_FREQUENCE = pygame.USEREVENT + 1
pygame.time.set_timer(EVENT_BARREL_FREQUENCE, 6000)


def draw_screen():
    platforms_surfaces = []
    platform_objects = []
    ladder_objects = []
    climbers = []

    ladders = levels[active_level]["ladders"]
    platforms = levels[active_level]["platforms"]

    for ladder in ladders:
        ladder_objects.append(Ladder(*ladder))
        if ladder[2] >= 3:
            climbers.append(ladder_objects[-1].body)
    for platform in platforms:
        platform_objects.append(Platform(*platform))
        platforms_surfaces.append(platform_objects[-1].top)
    return platforms_surfaces, climbers


def draw_extras():
    draw_oil()
    draw_barrels()


def draw_oil():
    x_coord, y_coord = 4 * section_height, HEIGHT - 4.5 * section_height
    oil = pygame.draw.rect(
        screen, "blue", [x_coord, y_coord, 2*section_width, 2.5 * section_height])
    pygame.draw.rect(screen, "blue", [
                     x_coord - 0.1 * section_width, y_coord, 2.2 * section_width, 0.2*section_height])
    pygame.draw.rect(screen, "blue", [x_coord - 0.1 * section_width, y_coord +
                     2.3 * section_height, 2.2 * section_width, 0.2*section_height])

    pygame.draw.rect(screen, "light blue", [
                     x_coord + 0.1 * section_width, y_coord + 0.2 * section_height, 0.2 * section_width, 2 * section_height])
    pygame.draw.rect(screen, "light blue", [
        x_coord, y_coord + 0.5 * section_height, 2 * section_width, 0.2 * section_height])
    pygame.draw.rect(screen, "light blue", [
        x_coord, y_coord + 1.7 * section_height, 2 * section_width, 0.2 * section_height])

    screen.blit(font2.render("OIL", True, "light blue"),
                (x_coord + 0.4*section_width, y_coord + 0.7*section_height))

    for i in range(4):
        pygame.draw.circle(screen, "red", (x_coord + 0.5 *
                           section_width + i * 0.4 * section_width, y_coord + 2.1*section_height), 3)
    return oil


def draw_barrels():
    barrel_side = pygame.transform.scale(pygame.image.load(
        "./src/assets/images/barrel_side.png").convert_alpha(), (section_width * 2, section_height * 2.5))

    screen.blit(pygame.transform.rotate(barrel_side, 90),
                (section_width * 1.2, section_height * 6.6))
    screen.blit(pygame.transform.rotate(barrel_side, 90),
                (section_width * 2.5, section_height * 6.6))
    screen.blit(pygame.transform.rotate(barrel_side, 90),
                (section_width * 2.5, section_height * 8.8))
    screen.blit(pygame.transform.rotate(barrel_side, 90),
                (section_width * 1.2, section_height * 8.8))


def draw_kong():
    pass


def detect_collide(player, platforms):
    pass


while running:
    screen.fill((0, 0, 0,))
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                pass
        if event.type == EVENT_BARREL_FREQUENCE:
            barrel = Barrel([barrels], 240, 240)

    # if barrel_count < barrel_spawn_time:
    #     barrel_count += 1
    # else:
    #     barrel_count = random.randint(0, 120)
    #     barrel_time = barrel_count - barrel_spawn_time
    #     barrel = Barrel([all_sprites, barrels], 240, 240)

    plats, lads = draw_screen()

    player.update()

    for barrel in barrels:
        barrel.draw(screen)
        barrel.update(plats)

    draw_extras()

    # detect_collide(player, platforms)

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
