import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Available Fonts in Pygame')

font_list = pygame.font.get_fonts()

y_position = 0
for font in font_list:
    try:
        font_surface = pygame.font.SysFont(font, 24).render(font, True, (255, 255, 255))
        screen.blit(font_surface, (10, y_position))
        y_position += 30
        if y_position > 580:  # stop before going off-screen
            break
    except Exception as e:
        print(f"Skipping font '{font}': {e}")

pygame.display.flip()
pygame.time.wait(5000)
pygame.quit()