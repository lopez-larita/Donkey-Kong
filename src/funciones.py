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
    phase_time = barrel_time // 4
    if barrel_spawn_time - barrel_count > 3 * phase_time:
        pass
