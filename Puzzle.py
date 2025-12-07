import pygame
from EscapeRoom import TextBox

pygame.init()

WIDTH, HEIGHT = 960, 540
screen = pygame.display.set_mode((WIDTH, HEIGHT))

textbox = TextBox("pics/textbox.png", WIDTH / 2, HEIGHT / 2)
text_sprites = pygame.sprite.Group(textbox)

clock_img = pygame.image.load("pics/clock.png")
clock_img = pygame.transform.scale(clock_img, (WIDTH, HEIGHT))

cx = WIDTH // 2
cy = HEIGHT // 2
clock_center = (cx, cy)

min_angles = [(cx, 60), (cx+210, cy), (cx, cy+210), (cx-210, cy)]
min_point = 0

hr_angles = [(cx, 150), (cx+75, cy-100), (cx+120, cy-60), (cx+150, cy), (cx+120, cy+60), (cx+75, cy+100),
             (cx, 390), (cx-75, cy+100), (cx-120, cy+60), (cx-150, cy), (cx-120, cy-60), (cx-75, cy-100)]
hr_point = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if min_point < len(min_angles)-1:
                    min_point += 1
                else:
                    min_point = 0
            if event.button == 3:
                if hr_point < len(hr_angles)-1:
                    hr_point += 1
                else:
                    hr_point = 0


    screen.fill((0, 0, 0))


    c = clock_img.get_rect(center=(cx, cy))
    screen.blit(clock_img, c)

    pygame.draw.line(screen, (0, 0, 0), (cx, cy), min_angles[min_point], 6)
    pygame.draw.line(screen, (0, 0, 0), (cx, cy), hr_angles[hr_point], 8)

    if hr_point == 6 and min_point == 1:
        text_sprites.draw(screen)

    pygame.display.update()

pygame.quit()
