from Assets import *
from picture_puzzle import Game as PicturePuzzle

pygame.init()
FONT = pygame.font.SysFont("constantia", 18)
BIGFONT = pygame.font.SysFont("constantia", 30)

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

note = pygame.image.load("pics/note.png")
note = pygame.transform.scale(note, (WIDTH, HEIGHT))

note_click_box = pygame.Rect(380, 380, 200, 60)
note_exit_click_box = pygame.Rect(0,0, 960, 100)

key = pygame.image.load("pics/key.png")
key = pygame.transform.scale(key, (WIDTH, HEIGHT))

key_click_box = pygame.Rect(870, 300, 70, 100)
key_exit_click_box = pygame.Rect(0,0, 960, 100)

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

def draw_note():
    WIN.blit(note, (0, 0))

def draw_key():
    WIN.blit(key, (0, 0))

# Picture Puzzle
picturepuzzle = PicturePuzzle()

picture_puzzle_click_box = pygame.Rect(410, 90, 145, 140)
picture_exit_click_box = pygame.Rect(0,0, 960, 100)

picturepuzzle_solved = False

# End Puzzle
end_puzzle_click_box = pygame.Rect(750, 130, 110, 380)
end_exit_click_box = pygame.Rect(0,0, 960, 100)

maid_click_box = pygame.Rect(20, 250, 215, 300)
gardener_click_box = pygame.Rect(235, 190, 210, 400)
wife_click_box = pygame.Rect(450, 210, 230, 400)
chef_click_box = pygame.Rect(690, 190, 240, 400)

bg_end_puzzle = pygame.image.load("pics/end.png")
bg_end_puzzle = pygame.transform.scale(bg_end_puzzle, (WIDTH, HEIGHT))

def draw_end_puzzle():
    WIN.blit(bg_end_puzzle, (0, 0))
    # pygame.draw.rect(WIN, (255, 0, 0), gardener_click_box, 3)
    # pygame.draw.rect(WIN, (255, 0, 0), maid_click_box, 3)
    # pygame.draw.rect(WIN, (255, 0, 0), wife_click_box, 3)
    # pygame.draw.rect(WIN, (255, 0, 0), chef_click_box, 3)

# Lose Scene
bg_lose = pygame.image.load("pics/lose.png")
bg_lose = pygame.transform.scale(bg_lose, (WIDTH, HEIGHT))

def draw_lose():
    WIN.blit(bg_lose, (0, 0))

# Win Scene
bg_win = pygame.image.load("pics/win.png")
bg_win = pygame.transform.scale(bg_win, (WIDTH, HEIGHT))

def draw_win():
    WIN.blit(bg_win, (0, 0))

# Game
textbox = TextBox("pics/textbox.png", WIDTH / 2, HEIGHT / 2)
text_sprites = pygame.sprite.Group(textbox)

def draw_start():
    WIN.blit(bg, (0, 0))
    #pygame.draw.rect(WIN, (255, 0, 0), key_click_box, 3)

def main():
    run = True
    scene = "start"
    win = False
    global picturepuzzle_solved

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
                    elif note_click_box.collidepoint(event.pos):
                        scene = "note"
                    elif key_click_box.collidepoint(event.pos):
                        scene = ("key")
                    elif picture_puzzle_click_box.collidepoint(event.pos):
                        scene = "picture_puzzle"
                        picturepuzzle.new()
                    elif end_puzzle_click_box.collidepoint(event.pos):
                        scene = "end_puzzle"

                elif scene == "candle_puzzle": #Candle Puzzle event handling
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

                elif scene == "clock_puzzle": #Clock Puzzle event handling
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
                elif scene == "note":
                    if note_exit_click_box.collidepoint(event.pos):
                        scene = "start"

                elif scene == "key":
                    if key_exit_click_box.collidepoint(event.pos):
                        scene = "start"

                elif scene == "picture_puzzle": #Picture Puzzle scene event handling
                    picturepuzzle.events(event)
                    if picture_exit_click_box.collidepoint(event.pos):
                        scene = "start"

                elif scene == "end_puzzle": # Ending event handling
                    if end_exit_click_box.collidepoint(event.pos):
                        scene = "start"
                    elif maid_click_box.collidepoint(event.pos):
                        scene = "lose"
                    elif gardener_click_box.collidepoint(event.pos):
                        scene = "lose"
                    elif wife_click_box.collidepoint(event.pos):
                        scene = "lose"
                    elif chef_click_box.collidepoint(event.pos):
                        scene = "win"


            elif event.type == pygame.MOUSEBUTTONUP:
                selected_sprite = None
                if scene == "candle_puzzle" and check_order(Candles):
                    win = True

            elif event.type == pygame.MOUSEMOTION: # Moving the candles
                if selected_sprite:
                    mouse_x, mouse_y = event.pos
                    selected_sprite.rect.x = mouse_x + offset_x
                    selected_sprite.rect.y = mouse_y + offset_y

        # Drawing functions for each scene
        if scene == "start":
            draw_start()
        elif scene == "candle_puzzle":
            draw_candle_puzzle()
            candle_sprites.update()
        elif scene == "clock_puzzle":
            draw_clock_puzzle()
        elif scene == "note":
            draw_note()
        elif scene == "key":
            draw_key()
        elif scene == "picture_puzzle":
            if not picturepuzzle_solved:
                picturepuzzle.update()
                picturepuzzle.draw()
        elif scene == "end_puzzle":
            draw_end_puzzle()
            text = BIGFONT.render("WHO DID IT?", True, ((128, 0, 32)))
            WIN.blit(text, (360, 100),)
        elif scene == "lose":
            draw_lose()
        elif scene == "win":
            draw_win()

        if check_order(Candles): # Candle clue display
            win = True
        if win and scene == "candle_puzzle":
            text_sprites.draw(WIN)
            clue_1 = ("After the last candle is in place, a note falls out of the drawer. It is a work"
                      "\nschedule which shows that the Maid could not have been working at"
                      "\nthe time of the murder.")
            clue_1_text = clue_1.splitlines()
            clue_1_lines = []
            for line in clue_1_text:
                clue_1_lines.append(FONT.render(line, True, (76, 38, 15)))
            y_position = 385
            for line_surface_1 in clue_1_lines:
                WIN.blit(line_surface_1,(200 ,y_position))
                y_position += 25

        if hr_point == 6 and min_point == 1 and scene == "clock_puzzle": # Clock clue display and win condition
            text_sprites.draw(WIN)
            clue_2 = ("The clock opens up, and you find a bottle of sleeping pills prescribed"
                      "\nto the Wife. You notice that the time on the clock corresponds to when"
                      "\nshe planned to wake up. 6:15 was past the time of the murder, meaning"
                      "\nshe was asleep during it.")
            clue_2_text = clue_2.splitlines()
            clue_2_lines = []
            for line in clue_2_text:
                clue_2_lines.append(FONT.render(line, True, (76, 38, 15)))
            y_position = 370
            for line_surface_2 in clue_2_lines:
                WIN.blit(line_surface_2, (200, y_position))
                y_position += 25

        if ((picturepuzzle.tiles_grid == picturepuzzle.tiles_completed_grid) and (scene == "picture_puzzle") and
                (not picturepuzzle_solved)):
            text_sprites.draw(WIN)
            clue_3 = ("The painting opens up from the wall, revealing some kind of opening."
                      "\nInside is a calendar, today's date marked with the word RAIN."
                      "\nIt looks to be the Gardener's work schedule, indicating that he could"
                      "\nnot have been working today.")
            clue_3_text = clue_3.splitlines()
            clue_3_lines = []
            for line in clue_3_text:
                clue_3_lines.append(FONT.render(line, True, (76, 38, 15)))
            y_position = 370
            for line_surface_3 in clue_3_lines:
                WIN.blit(line_surface_3, (200, y_position))
                y_position += 25
            picturepuzzle_solved = True

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()