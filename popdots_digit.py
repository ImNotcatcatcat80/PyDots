
import traceback
import pygame
import PyDots

screen_w = 400
screen_h = 720

pygame.init()
pygame.display.set_caption("Pop Dots")
screen = pygame.display.set_mode((screen_w, screen_h))
clock = pygame.time.Clock()
digit0 = PyDots.Digit(screen, (35, 72), 330, 2)
digit0.set_color_on(PyDots.Colors.GREEN)

done = False
dots_on = True
prev_dots_on = False
cnt = 0

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

    screen.fill((0, 128, 255))

    cnt += 1
    if cnt >= 240:
        cnt = 0

    if dots_on:
        pygame.draw.circle(screen, (0, 0, 0), (screen_w-15, screen_h-15), 10)
        if cnt < 200:
            digit0.draw(str(int(cnt / 20)))
        elif 200 <= cnt <= 220:
            digit0.draw("=")
        elif 220 < cnt <= 240:
            digit0.draw("f")
        else:
            digit0.draw("n")
    else:
        digit0.draw("n")

    # prev_dots_on = dots_on
    clock.tick_busy_loop(10)
    pygame.display.flip()
