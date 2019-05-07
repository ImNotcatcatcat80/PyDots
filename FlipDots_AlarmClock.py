
import traceback
import sys
import pygame
import PyDots
import datetime


screen_w = 1200
screen_h = 720
w_dig = int(screen_w / 8.75)
h_dig = int(screen_w / 5)
sep_dig = int(screen_w / 70)
y_dig = int((screen_h - h_dig) / 2)
w_sig = h_sig = int(screen_w / 11.666)
y_sig = int(y_dig + (h_dig - h_sig) / 2)
w_point = h_point = int(screen_w / 35)
l_margin = int((screen_w - (6*w_dig + 2*w_sig + 3*sep_dig)) / 2)
disp_tl = (l_margin, y_dig)
disp_tr = (l_margin + 6*w_dig + 3*sep_dig + 2*w_sig, y_dig)
disp_bl = (l_margin, y_dig + h_dig)
disp_br = (l_margin + 6*w_dig + 3*sep_dig + 2*w_sig, y_dig + h_dig)
list_colors = [PyDots.Colors.YELLOW, PyDots.Colors.GREEN, PyDots.Colors.RED, PyDots.Colors.WHITE]
permissible_fonts_small = ["arial", "calibri", "verdana", "lucidaconsole", "tahoma", "dejavusans"]
permissible_fonts_large = ["arialblack", "calibri", "verdana", "lucidaconsole", "tahoma", "dejavusans"]
font_small = None
font_large = None
colors_index = 0
done = False
display_on = True
dots_on = True
show_date = False
prev_time_str = ""
cnt = 0
sign_str = "n"
date_str = "init"
time = "init"
dt_set_datemode = datetime.datetime.now()

pygame.init()
pygame.display.set_caption("FD Clock")
screen = pygame.display.set_mode((screen_w, screen_h))
clock = pygame.time.Clock()
# font_large = pygame.font.SysFont("arial black", 36)
# font_small = pygame.font.SysFont("arial", 12)
# font_roboto_black = pygame.font.Font("fonts/Roboto-Black.ttf", 40)
# font_roboto_regular = pygame.font.Font("fonts/Roboto-Regular.ttf", 14)
for fs in permissible_fonts_small:
    if fs in pygame.font.get_fonts():
        font_small = pygame.font.SysFont(fs, 12)
        break
if font_small is None:
    font_small = pygame.font.Font(None, 12)
for fl in permissible_fonts_large:
    if fl in pygame.font.get_fonts():
        font_large = pygame.font.SysFont(fl, 36)
        break
if font_large is None:
    font_large = pygame.font.Font(None, 32)
# font_large.set_bold(True)
text_clock_name = font_large.render("FD CLOCK", True, (0, 0, 0))
text_clock_description = font_small.render("software operated flip dot calendar clock - using system time as time source - v0.2", True, (0, 0, 0))
text_system_version = font_small.render("Running on Python " + sys.version, True, (0, 0, 0))
digit_h1 = PyDots.Digit(screen, (l_margin, y_dig), w_dig, 2)
digit_h0 = PyDots.Digit(screen, (l_margin + 1*w_dig + 1*sep_dig, y_dig), w_dig, 2)
sign_hm = PyDots.Sign(screen, (l_margin + 2*w_dig + 1*sep_dig, y_sig), w_sig, 2)
digit_m1 = PyDots.Digit(screen, (l_margin + 2*w_dig + 1*sep_dig + 1*w_sig, y_dig), w_dig, 2)
digit_m0 = PyDots.Digit(screen, (l_margin + 3*w_dig + 2*sep_dig + 1*w_sig, y_dig), w_dig, 2)
sign_ms = PyDots.Sign(screen, (l_margin + 4*w_dig + 2*sep_dig + 1*w_sig, y_sig), w_sig, 2)
digit_s1 = PyDots.Digit(screen, (l_margin + 4*w_dig + 2*sep_dig + 2*w_sig, y_dig), w_dig, 2)
digit_s0 = PyDots.Digit(screen, (l_margin + 5*w_dig + 3*sep_dig + 2*w_sig, y_dig), w_dig, 2)
point_h = PyDots.Point(screen, (l_margin + 2*w_dig + 2*sep_dig, y_dig + h_dig - h_point), w_point, 2)
point_m = PyDots.Point(screen, (l_margin + 4*w_dig + 3*sep_dig + 1*w_sig, y_dig + h_dig - h_point), w_point, 2)


def round_corn_rect(p_tl, p_tr, p_bl, p_br, p_rad, p_color):
    pygame.draw.rect(screen, p_color, pygame.Rect(p_tl[0] - p_rad, p_tl[1], p_tr[0] - p_tl[0] + 2 * p_rad, p_bl[1] - p_tl[1]))
    pygame.draw.rect(screen, p_color, pygame.Rect(p_tl[0], p_tl[1] - p_rad, p_tr[0] - p_tl[0], p_bl[1] - p_tl[1] + 2 * p_rad))
    pygame.draw.circle(screen, p_color, p_tl, p_rad)
    pygame.draw.circle(screen, p_color, p_tr, p_rad)
    pygame.draw.circle(screen, p_color, p_bl, p_rad)
    pygame.draw.circle(screen, p_color, p_br, p_rad)


while not done:

    date_str = datetime.datetime.now().date()
    time = datetime.datetime.now().time()
    time_str = str(time)[:8]

    if time_str != prev_time_str:
        dots_on = not dots_on

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("")
            print("Done.")
            print("")
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                show_date = not show_date
                if show_date:
                    dt_set_datemode = datetime.datetime.now()
            if event.key == pygame.K_UP:
                sign_str = "ar_up"
            if event.key == pygame.K_DOWN:
                sign_str = "ar_dn"
            if event.key == pygame.K_LEFT:
                sign_str = "ar_l"
            if event.key == pygame.K_RIGHT:
                sign_str = "ar_r"
            if event.key == pygame.K_c:
                colors_index += 1
            if event.key == pygame.K_ESCAPE:
                display_on = not display_on

    cnt += 1
    if cnt >= 100000:
        cnt = 0

    dt_reset_datemode = dt_set_datemode + datetime.timedelta(milliseconds=10000)
    if datetime.datetime.now() > dt_reset_datemode:
        show_date = False

    if colors_index >= 4:
        colors_index = 0
    digit_h1.set_color_on(list_colors[colors_index])
    digit_h0.set_color_on(list_colors[colors_index])
    sign_hm.set_color_on(list_colors[colors_index])
    digit_m1.set_color_on(list_colors[colors_index])
    digit_m0.set_color_on(list_colors[colors_index])
    sign_ms.set_color_on(list_colors[colors_index])
    digit_s1.set_color_on(list_colors[colors_index])
    digit_s0.set_color_on(list_colors[colors_index])
    point_h.set_color_on(list_colors[colors_index])
    point_m.set_color_on(list_colors[colors_index])

    # Light blue background
    screen.fill(PyDots.Colors.BLUE)
    # White area
    white_tl = (disp_tl[0] - int(w_dig/16), disp_tl[1] - int(h_sig))
    white_tr = (disp_tr[0] + int(w_dig/16), disp_tr[1] - int(h_sig))
    white_bl = (disp_bl[0] - int(w_dig/16), disp_bl[1] + int(h_sig/2))
    white_br = (disp_br[0] + int(w_dig/16), disp_br[1] + int(h_sig/2))
    white_area = PyDots.RoundCornerRect(white_tl, white_tr, white_bl, white_br, int(w_dig / 8))
    white_area.draw_rect(screen, PyDots.Colors.WHITE)
    white_area_top_y = white_area.get_y_min()
    # Black area around display
    black_area = PyDots.RoundCornerRect(disp_tl, disp_tr, disp_bl, disp_br, int(w_dig / 8))
    black_area.draw_rect(screen, PyDots.Colors.BG_BLACK)
    black_area_top_y = black_area.get_y_min()
    black_area_bottom_y = black_area.get_y_max()
    # Text
    name_w = text_clock_name.get_width()
    name_h = text_clock_name.get_height()
    description_w = text_clock_description.get_width()
    description_h = text_clock_description.get_height()
    description_y = black_area_bottom_y + int(sep_dig / 4)
    screen.blit(text_clock_description, (screen_w / 2 - description_w / 2, description_y))
    screen.blit(text_clock_name, (screen_w / 2 - name_w / 2, (black_area_top_y + white_area_top_y)/2 - (name_h / 2)))
    screen.blit(text_system_version, (screen_w / 2 - text_system_version.get_width() / 2, description_y + description_h))

    if display_on:
        if show_date:
            display_str = str(date_str)
            display_str = display_str[2:]
        else:
            display_str = time_str
        digit_h1.draw(str(display_str)[0])
        digit_h0.draw(str(display_str)[1])
        if not show_date:
            if dots_on:
                sign_hm.draw(str(display_str)[2])
            else:
                sign_hm.draw("n")
        else:
            sign_hm.draw(".")
        digit_m1.draw(str(display_str)[3])
        digit_m0.draw(str(display_str)[4])
        if not show_date:
            if dots_on:
                sign_ms.draw(str(display_str)[5])
            else:
                sign_ms.draw("n")
        else:
            sign_ms.draw(".")
        digit_s1.draw(str(display_str)[6])
        digit_s0.draw(str(display_str)[7])
        point_h.draw("n")
        point_m.draw("n")
    else:
        digit_h1.draw("f")
        digit_h0.draw("f")
        sign_hm.draw("f")
        digit_m1.draw("f")
        digit_m0.draw("f")
        sign_ms.draw("f")
        digit_s1.draw("f")
        digit_s0.draw("f")
        point_h.draw(".")
        point_m.draw(".")

    prev_time_str = time_str
    clock.tick_busy_loop(10)
    pygame.display.flip()
