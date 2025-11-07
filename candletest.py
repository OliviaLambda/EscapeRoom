import pygame

pygame.init()
FONT = pygame.font.SysFont("constantia", 48)

WIDTH, HEIGHT = 960, 540
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape Room")


bg = pygame.image.load("startbackground.png").convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

bg_puzzle = pygame.image.load("puzzlebackground.png").convert()
bg_puzzle = pygame.transform.scale(bg_puzzle, (WIDTH, HEIGHT))


class Candle(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, name):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (176, 352))
        self.rect = self.image.get_rect(center=(x, y))
        self.name = name

class TextBox(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (352, 176))
        self.rect = self.image.get_rect(center=(x, y))


taller = Candle("pics/1.png", 200, 300, "taller")
tall = Candle("pics/2.png", 400, 300, "tall")
normal = Candle("pics/3.png", 600, 300, "normal")
short = Candle("pics/4.png", 800, 300, "short")
Candles = [short, normal, tall, taller]


textbox = TextBox("textbox.png", 480, 400)

candle_sprites = pygame.sprite.Group(short, normal, tall, taller)
correct_order = ["taller", "normal", "tall", "short"]

text_sprites = pygame.sprite.Group(textbox)

puzzle_click_box = pygame.Rect(380, 230, 90, 60)
exit_click_box = pygame.Rect(0,0, 960, 100)


def draw_start():
    WIN.blit(bg, (0, 0))
    #pygame.draw.rect(WIN, (255, 0, 0), puzzle_click_box, 3)

def draw_puzzle():
    WIN.blit(bg_puzzle, (0, 0))
    candle_sprites.draw(WIN)
    #pygame.draw.rect(WIN, (255, 0, 0), exit_click_box, 3)

def check_order(Candles):
    order = Candles[:]

    for i in range(len(order)):
        for j in range(0, len(order) - i - 1):
            if order[j].rect.x > order[j + 1].rect.x:
                order[j], order[j + 1] = order[j + 1], order[j]

    current_order = []
    for c in order:
        current_order.append(c.name)

    if len(current_order) != len(correct_order):
        return False

    for i in range(len(current_order)):
        if current_order[i] != correct_order[i]:
            return False

    return True

def main():
    clock = pygame.time.Clock()
    run = True
    scene = "start"
    win = False

    selected_sprite = None
    offset_x = 0
    offset_y = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            if event.type == pygame.MOUSEBUTTONDOWN:
                if scene == "start":
                    if puzzle_click_box.collidepoint(event.pos):
                        scene = "puzzle"
                elif scene == "puzzle":
                    if exit_click_box.collidepoint(event.pos):
                        scene = "start"
                    for sprite in candle_sprites:
                        if sprite.rect.collidepoint(event.pos):
                            selected_sprite = sprite
                            mouse_x, mouse_y = event.pos
                            offset_x = sprite.rect.x - mouse_x
                            offset_y = sprite.rect.y - mouse_y
                            break
            elif event.type == pygame.MOUSEBUTTONUP:
                selected_sprite = None

            elif event.type == pygame.MOUSEMOTION:
                if selected_sprite:
                    mouse_x, mouse_y = event.pos
                    selected_sprite.rect.x = mouse_x + offset_x
                    selected_sprite.rect.y = mouse_y + offset_y

        if scene == "start":
            draw_start()
        elif scene == "puzzle":
            draw_puzzle()
            candle_sprites.update()

        if check_order(Candles):
            win = True
        if win and scene == "puzzle":
            text_sprites.draw(WIN)
            text = FONT.render("yippee!", True, (76, 38, 15))
            WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, 100))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()