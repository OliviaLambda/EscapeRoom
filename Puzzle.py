import pygame

pygame.init()

screen = pygame.display.set_mode((500, 600))

clock_img = pygame.image.load("clock.png")
min_img = pygame.image.load("min hand.png")
hr_img = pygame.image.load("hr hand.png")

clock_img = pygame.transform.scale(clock_img, (400, 400))

cx = 275
cy = 325

min_angle = -30
hr_angle = -30

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                min_angle = min_angle + 30
            if event.button == 3:
                hr_angle = hr_angle + 30


    if min_angle >= 360:
        min_angle -= 360
    if hr_angle >= 360:
        hr_angle -= 360

    screen.fill((0, 0, 0))


    c = clock_img.get_rect(center=(cx, cy))
    screen.blit(clock_img, c)


    min_rot = pygame.transform.rotate(min_img, -min_angle)
    min_rect = min_rot.get_rect(center=(cx, cy))
    screen.blit(min_rot, min_rect)


    hr_rot = pygame.transform.rotate(hr_img, -hr_angle)
    hr_rect = hr_rot.get_rect(center=(cx, cy))
    screen.blit(hr_rot, hr_rect)

    pygame.display.update()

pygame.quit()
