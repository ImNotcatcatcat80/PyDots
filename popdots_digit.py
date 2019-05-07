
import traceback
import pygame
import PyDots

screen_w = 500
screen_h = 720

pygame.init()
pygame.display.set_caption("Pop Dots")
screen = pygame.display.set_mode((screen_w, screen_h))
clock = pygame.time.Clock()
digit0 = PyDots.Digit(screen, (90, 80), 320, 2)

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
    if cnt >= 250:
        cnt = 0

    black_area = PyDots.RoundCornerRect((90, 80), (410, 80), (90, 640), (410, 640), 36)
    black_area.draw_rect(screen, PyDots.Colors.BG_BLACK)
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
