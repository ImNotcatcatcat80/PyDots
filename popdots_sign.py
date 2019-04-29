import traceback
import pygame
import PyDots

screen_w = 300
screen_h = 300

pygame.init()
pygame.display.set_caption("Pop Dots Sign")
screen = pygame.display.set_mode((screen_w, screen_h))
clock = pygame.time.Clock()
sign0 = PyDots.Sign(screen, (60, 60), 180, 2)
# sign0.set_color_on(dots_digit.Digit.BLUE)

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

        if event.type == pygame.KEYDOWN and False:    # Disabled
            if event.key == pygame.K_RETURN:
                dots_on = not dots_on
                if dots_on and dots_on != prev_dots_on:
                    cnt += 1

    screen.fill((128, 128, 128))

    dots_on = True
    cnt += 1
    if cnt >= 150:
        cnt = 0

    if dots_on:
        pygame.draw.circle(screen, (0, 128, 255), (screen_w-15, screen_h-15), 10)
        if 0 < cnt < 20:
            sign0.draw("|")
        elif 20 < cnt < 40:
            sign0.draw("x")
        elif 40 < cnt < 60:
            sign0.draw(":")
        elif 60 < cnt < 80:
            sign0.draw("+")
        elif 80 < cnt < 100:
            sign0.draw("/")
        elif 100 < cnt < 120:
            sign0.draw("-")
        elif 120 < cnt < 140:
            sign0.draw("b")
        else:
            sign0.draw("n")
    else:
        sign0.draw("n")

    # prev_dots_on = dots_on
    clock.tick_busy_loop(10)
    pygame.display.flip()
