
import traceback
import pygame
import PyDots

screen_w = 900
screen_h = 720

pygame.init()
pygame.display.set_caption("Counting...")
screen = pygame.display.set_mode((screen_w, screen_h))
clock = pygame.time.Clock()
digit3 = PyDots.Digit(screen, (150, 200), 180, 3)
digit3.set_color_on(PyDots.Colors.GREEN)
digit2 = PyDots.Digit(screen, (330, 200), 180, 3)
digit2.set_color_on(PyDots.Colors.RED)
point1 = PyDots.Point(screen, (510, 485), 30, 3)
point1.set_color_on(PyDots.Colors.WHITE)
digit1 = PyDots.Digit(screen, (540, 200), 180, 3)
digit1.set_color_on(PyDots.Colors.WHITE)
sign1 = PyDots.Sign(screen, (390, 600), 120, 3)
sign1.set_color_on(PyDots.Colors.BLUE)

done = False
dots_on = True
prev_dots_on = False
cnt = 0
sign_str = "n"

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("")
            print("Done.")
            print("")
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                dots_on = not dots_on
            if event.key == pygame.K_UP:
                sign_str = "ar_up"
            if event.key == pygame.K_DOWN:
                sign_str = "ar_dn"
            if event.key == pygame.K_LEFT:
                sign_str = "ar_l"
            if event.key == pygame.K_RIGHT:
                sign_str = "ar_r"

    screen.fill((0, 32, 64))
    pygame.draw.rect(screen, PyDots.Colors.BG_BLACK, pygame.Rect(130, 180, 610, 355))
    pygame.draw.rect(screen, PyDots.Colors.BG_BLACK, pygame.Rect(330, 580, 240, 140))

    cnt += 1
    if cnt >= 25000:
        cnt = 0

    if dots_on:

        if len(str(int(cnt/25))) > 2:
            digit3.draw(str(int(cnt/25))[-3])
        else:
            digit3.draw("n")
        if len(str(int(cnt/25))) > 1:
            digit2.draw(str(int(cnt/25))[-2])
        else:
            digit2.draw("n")
        if dots_on:
            point1.draw(".")
        else:
            point1.draw("n")
        digit1.draw(str(int(cnt/25))[-1])
        sign1.draw(sign_str)
    else:
        digit3.draw("=")
        digit2.draw("=")
        point1.draw("n")
        digit1.draw("f")
        sign1.draw(".")

    clock.tick_busy_loop(25)
    pygame.display.flip()
