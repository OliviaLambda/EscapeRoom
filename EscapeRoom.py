from Assets import *

pygame.init()
FONT = pygame.font.SysFont("constantia", 18)

WIDTH, HEIGHT = 960, 540
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape Room")

bg = pygame.image.load("pics/startbackground.png").convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

# Candle Puzzle
bg_candle_puzzle = pygame.image.load("pics/candlepuzzlebackground.png").convert()
bg_candle_puzzle = pygame.transform.scale(bg_candle_puzzle, (WIDTH, HEIGHT))

taller = Candle("pics/1.png", 120, 300, "taller")
tall = Candle("pics/2.png", 300, 300, "tall")
normal = Candle("pics/3.png", 480, 300, "normal")
short = Candle("pics/4.png", 660, 300, "short")
shortest = Candle("pics/5.png", 840, 300, "shortest")
Candles = [shortest, short, normal, tall, taller]

candle_sprites = pygame.sprite.Group(shortest, short, normal, tall, taller)
correct_order = ["taller", "normal", "shortest", "tall", "short"]

candle_puzzle_click_box = pygame.Rect(380, 230, 90, 60)
candle_exit_click_box = pygame.Rect(0,0, 960, 100)

def draw_candle_puzzle():
    WIN.blit(bg_candle_puzzle, (0, 0))
    candle_sprites.draw(WIN)

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

# Clock Puzzle
bg_clock_puzzle = pygame.image.load("pics/clock.png")
bg_clock_puzzle = pygame.transform.scale(bg_clock_puzzle, (WIDTH, HEIGHT))

clock_puzzle_click_box = pygame.Rect(780, 30, 100, 100)
clock_exit_click_box = pygame.Rect(0,0, 960, 100)

cx = WIDTH // 2
cy = HEIGHT // 2
clock_center = (cx, cy)

min_angles = [(cx, 60), (cx+210, cy), (cx, cy+210), (cx-210, cy)]
min_point = 0

hr_angles = [(cx, 150), (cx+75, cy-100), (cx+120, cy-60), (cx+150, cy), (cx+120, cy+60), (cx+75, cy+100),
             (cx, 390), (cx-75, cy+100), (cx-120, cy+60), (cx-150, cy), (cx-120, cy-60), (cx-75, cy-100)]
hr_point = 0

def draw_clock_puzzle():
    c = bg_clock_puzzle.get_rect(center=(cx, cy))
    WIN.blit(bg_clock_puzzle, c)
    pygame.draw.line(WIN, (0, 0, 0), (cx, cy), min_angles[min_point], 6)
    pygame.draw.line(WIN, (0, 0, 0), (cx, cy), hr_angles[hr_point], 8)

# Game
textbox = TextBox("pics/textbox.png", WIDTH / 2, HEIGHT / 2)
text_sprites = pygame.sprite.Group(textbox)

def draw_start():
    WIN.blit(bg, (0, 0))
    #pygame.draw.rect(WIN, (255, 0, 0), clock_puzzle_click_box, 3)

def main():
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
                    if candle_puzzle_click_box.collidepoint(event.pos):
                        scene = "candle_puzzle"
                    elif clock_puzzle_click_box.collidepoint(event.pos):
                        scene = "clock_puzzle"
                elif scene == "candle_puzzle":
                    if candle_exit_click_box.collidepoint(event.pos):
                        scene = "start"
                        win = False
                    for sprite in candle_sprites:
                        if sprite.rect.collidepoint(event.pos):
                            selected_sprite = sprite
                            mouse_x, mouse_y = event.pos
                            offset_x = sprite.rect.x - mouse_x
                            offset_y = sprite.rect.y - mouse_y
                            break
                elif scene == "clock_puzzle":
                    if clock_exit_click_box.collidepoint(event.pos):
                        scene = "start"
                    if event.button == 1:
                        global min_point
                        if min_point < len(min_angles) - 1:
                            min_point += 1
                        else:
                            min_point = 0
                    if event.button == 3:
                        global hr_point
                        if hr_point < len(hr_angles) - 1:
                            hr_point += 1
                        else:
                            hr_point = 0
            elif event.type == pygame.MOUSEBUTTONUP:
                selected_sprite = None
                if scene == "candle_puzzle" and check_order(Candles):
                    win = True


            elif event.type == pygame.MOUSEMOTION:
                if selected_sprite:
                    mouse_x, mouse_y = event.pos
                    selected_sprite.rect.x = mouse_x + offset_x
                    selected_sprite.rect.y = mouse_y + offset_y

        if scene == "start":
            draw_start()
        elif scene == "candle_puzzle":
            draw_candle_puzzle()
            candle_sprites.update()
        elif scene == "clock_puzzle":
            draw_clock_puzzle()

        if check_order(Candles):
            win = True
        if win and scene == "candle_puzzle":
            text_sprites.draw(WIN)
            clue_1 = ("After the last candle is in place, a note falls out of the drawer. It is a work"
                      "\nschedule which shows that the Butler could not have been working at"
                      "\nthe time of the murder.")
            clue_1_text = clue_1.splitlines()
            clue_1_lines = []
            for line in clue_1_text:
                clue_1_lines.append(FONT.render(line, True, (76, 38, 15)))
            y_position = 385
            for line_surface_1 in clue_1_lines:
                WIN.blit(line_surface_1,(200 ,y_position))
                y_position += 25

        if hr_point == 6 and min_point == 1 and scene == "clock_puzzle":
            text_sprites.draw(WIN)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()