"""

   ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄
  ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
  ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀
  ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌
  ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄
  ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌
  ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌
  ▐░▌               ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌               ▐░▌
  ▐░▌               ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌      ▄▄▄▄▄▄▄▄▄█░▌
  ▐░▌               ▐░▌     ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌
   ▀                 ▀       ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀

  Python recreation of a flip dot display
  Built on Python 3.x using PyGame
  DavidG - Italy - April 2019

  Elements (as of first release):
    - Digit (4 * 7)
    - Sign (3 * 3)
    - Point

"""


import pygame


class Digit:

    def __init__(self, p_screen, p_topleft, p_width, p_frames_transition):
        self.width = p_width
        self.height = int(self.width*7/4)
        self.screen = p_screen
        if not isinstance(p_topleft, tuple):
            raise InvalidTopLeftType
        self.topleft = p_topleft
        self.prev_char = None
        if not 0 < p_frames_transition <= 10:
            raise FramesPerTransitionOutOfRange
        self.fpt = p_frames_transition
        self.color_on = Colors.YELLOW
        self.dot_array = [
            [Dot(self.fpt, self.color_on, self.width / 10), Dot(self.fpt, self.color_on, self.width / 10), Dot(self.fpt, self.color_on, self.width / 10), Dot(self.fpt, self.color_on, self.width / 10)],
            [Dot(self.fpt, self.color_on, self.width / 10), Dot(self.fpt, self.color_on, self.width / 10), Dot(self.fpt, self.color_on, self.width / 10), Dot(self.fpt, self.color_on, self.width / 10)],
            [Dot(self.fpt, self.color_on, self.width / 10), Dot(self.fpt, self.color_on, self.width / 10), Dot(self.fpt, self.color_on, self.width / 10), Dot(self.fpt, self.color_on, self.width / 10)],
            [Dot(self.fpt, self.color_on, self.width / 10), Dot(self.fpt, self.color_on, self.width / 10), Dot(self.fpt, self.color_on, self.width / 10), Dot(self.fpt, self.color_on, self.width / 10)],
            [Dot(self.fpt, self.color_on, self.width / 10), Dot(self.fpt, self.color_on, self.width / 10), Dot(self.fpt, self.color_on, self.width / 10), Dot(self.fpt, self.color_on, self.width / 10)],
            [Dot(self.fpt, self.color_on, self.width / 10), Dot(self.fpt, self.color_on, self.width / 10), Dot(self.fpt, self.color_on, self.width / 10), Dot(self.fpt, self.color_on, self.width / 10)],
            [Dot(self.fpt, self.color_on, self.width / 10), Dot(self.fpt, self.color_on, self.width / 10), Dot(self.fpt, self.color_on, self.width / 10), Dot(self.fpt, self.color_on, self.width / 10)]
        ]

    def _sel_char_list(self, f_char):
        ret_char_list = [
            [Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY],
            [Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY],
            [Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY],
            [Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY],
            [Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY],
            [Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY],
            [Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY]
        ]
        selected_char_list = [
            [Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY],
            [Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY],
            [Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY],
            [Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY],
            [Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY],
            [Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY],
            [Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY]
        ]
        if f_char == "f":
            selected_char_list = Digit.char_full
        elif f_char == "=":
            selected_char_list = Digit.char_stripes
        elif f_char == "0":
            selected_char_list = Digit.char_zero
        elif f_char == "1":
            selected_char_list = Digit.char_one
        elif f_char == "2":
            selected_char_list = Digit.char_two
        elif f_char == "3":
            selected_char_list = Digit.char_three
        elif f_char == "4":
            selected_char_list = Digit.char_four
        elif f_char == "5":
            selected_char_list = Digit.char_five
        elif f_char == "6":
            selected_char_list = Digit.char_six
        elif f_char == "7":
            selected_char_list = Digit.char_seven
        elif f_char == "8":
            selected_char_list = Digit.char_eight
        elif f_char == "9":
            selected_char_list = Digit.char_nine
        elif f_char == "a":
            selected_char_list = Digit.char_a
        elif f_char == "p":
            selected_char_list = Digit.char_p
        else:
            selected_char_list = Digit.char_null
        for hc in range(0, len(selected_char_list[0])):    # columns
            for vc in range(0, len(selected_char_list)):    # rows
                if selected_char_list[vc][hc] == 1:
                    ret_char_list[vc][hc] = self.color_on
                elif selected_char_list[vc][hc] == 0:
                    ret_char_list[vc][hc] = Colors.OFF_GREY
        return ret_char_list

    def draw(self, p_char):
        if len(p_char) > 1:
            raise DrawCharTooLong
        # Background rectangle
        pygame.draw.rect(self.screen, Colors.BG_BLACK, pygame.Rect(self.topleft[0], self.topleft[1], self.width, self.height))
        # Array of dots, nested "for" loops for vertical, horizontal (2-dimensions arrays)
        for hd in range(0, len(self.dot_array[0])):    # columns
            for vd in range(0, len(self.dot_array)):    # rows
                dot_set_color = self._sel_char_list(p_char)[vd][hd]    # color of this dot, given the char we want to draw
                radius = self.dot_array[vd][hd].dot_draw(dot_set_color)    # compute radius relative to the size of the matrix
                # Draw the dot
                pygame.draw.circle(self.screen, self.dot_array[vd][hd].actual_color, (self.topleft[0] + int(self.width/8) + int(hd*(self.width/4)), self.topleft[1] + int(self.height/14) + int(vd*(self.height/7))), radius)
                self.dot_array[vd][hd].dot_frames_sequence(dot_set_color)    # advance transition, and change set > actual color when transition closing > not closing

        # Lines, vertical, horizontal
        for hl in range(0, 4):
            pygame.draw.line(self.screen, Colors.BG_BLACK, (self.topleft[0] + int(self.width/8) + int(hl*(self.width/4)), self.topleft[1]), (self.topleft[0] + int(self.width/8) + int(hl*(self.width/4)), self.topleft[1] + self.height), 1)
        for vl in range(0, 7):
            pygame.draw.line(self.screen, Colors.BG_BLACK, (self.topleft[0], self.topleft[1] + int(self.height/14) + int(vl*(self.height/7))), (self.topleft[0] + self.width, self.topleft[1] + int(self.height/14) + int(vl*(self.height/7))), 1)
        # Lines, across
        pygame.draw.line(self.screen, Colors.BG_BLACK, (self.topleft[0], self.topleft[1] + 1 * self.height / 7), (self.topleft[0] + 1 * self.width / 4, self.topleft[1]), 1)
        pygame.draw.line(self.screen, Colors.BG_BLACK, (self.topleft[0], self.topleft[1] + 2 * self.height / 7), (self.topleft[0] + 2 * self.width / 4, self.topleft[1]), 1)
        pygame.draw.line(self.screen, Colors.BG_BLACK, (self.topleft[0], self.topleft[1] + 3 * self.height / 7), (self.topleft[0] + 3 * self.width / 4, self.topleft[1]), 1)
        pygame.draw.line(self.screen, Colors.BG_BLACK, (self.topleft[0], self.topleft[1] + 4 * self.height / 7), (self.topleft[0] + 4 * self.width / 4, self.topleft[1]), 1)
        pygame.draw.line(self.screen, Colors.BG_BLACK, (self.topleft[0], self.topleft[1] + 5 * self.height / 7), (self.topleft[0] + 4 * self.width / 4, self.topleft[1] + 1 * self.height / 7), 1)
        pygame.draw.line(self.screen, Colors.BG_BLACK, (self.topleft[0], self.topleft[1] + 6 * self.height / 7), (self.topleft[0] + 4 * self.width / 4, self.topleft[1] + 2 * self.height / 7), 1)
        pygame.draw.line(self.screen, Colors.BG_BLACK, (self.topleft[0], self.topleft[1] + 7 * self.height / 7), (self.topleft[0] + 4 * self.width / 4, self.topleft[1] + 3 * self.height / 7), 1)
        pygame.draw.line(self.screen, Colors.BG_BLACK, (self.topleft[0] + 1 * self.width / 4, self.topleft[1] + 7 * self.height / 7), (self.topleft[0] + 4 * self.width / 4, self.topleft[1] + 4 * self.height / 7), 1)
        pygame.draw.line(self.screen, Colors.BG_BLACK, (self.topleft[0] + 2 * self.width / 4, self.topleft[1] + 7 * self.height / 7), (self.topleft[0] + 4 * self.width / 4, self.topleft[1] + 5 * self.height / 7), 1)
        pygame.draw.line(self.screen, Colors.BG_BLACK, (self.topleft[0] + 3 * self.width / 4, self.topleft[1] + 7 * self.height / 7), (self.topleft[0] + 4 * self.width / 4, self.topleft[1] + 6 * self.height / 7), 1)

    def set_color_on(self, p_col):
        permissible_colors = [Colors.YELLOW, Colors.WHITE, Colors.GREEN, Colors.BLUE, Colors.RED]
        if p_col in permissible_colors:
            self.color_on = p_col
        else:
            raise InvalidColorSet

    char_null = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    char_full = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    char_stripes = [
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 1]
    ]
    char_zero = [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1]
    ]
    char_one = [
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1]
    ]
    char_two = [
        [1, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 1, 1, 1]
    ]
    char_three = [
        [1, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 1]
    ]
    char_four = [
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1]
    ]
    char_five = [
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 1]
    ]
    char_six = [
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1]
    ]
    char_seven = [
        [1, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1]
    ]
    char_eight = [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1]
    ]
    char_nine = [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 1]
    ]
    char_a = [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1]
    ]
    char_p = [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0]
    ]


class Sign:

    def __init__(self, p_screen, p_topleft, p_width, p_frames_transition):
        self.width = p_width
        self.height = self.width
        self.screen = p_screen
        if not isinstance(p_topleft, tuple):
            raise InvalidTopLeftType
        self.topleft = p_topleft
        self.prev_char = None
        if not 0 < p_frames_transition <= 10:
            raise FramesPerTransitionOutOfRange
        self.fpt = p_frames_transition
        self.color_on = Colors.YELLOW
        self.dot_array = [
            [Dot(self.fpt, self.color_on, self.width / 7.5), Dot(self.fpt, self.color_on, self.width / 7.5), Dot(self.fpt, self.color_on, self.width / 7.5)],
            [Dot(self.fpt, self.color_on, self.width / 7.5), Dot(self.fpt, self.color_on, self.width / 7.5), Dot(self.fpt, self.color_on, self.width / 7.5)],
            [Dot(self.fpt, self.color_on, self.width / 7.5), Dot(self.fpt, self.color_on, self.width / 7.5), Dot(self.fpt, self.color_on, self.width / 7.5)]
        ]

    def _sel_char_list(self, f_char):
        ret_char_list = [
            [Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY],
            [Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY],
            [Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY]
        ]
        selected_char_list = [
            [Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY],
            [Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY],
            [Colors.OFF_GREY, Colors.OFF_GREY, Colors.OFF_GREY]
        ]
        if f_char == "x":
            selected_char_list = Sign.char_cross
        elif f_char == ":":
            selected_char_list = Sign.char_dots
        elif f_char == "+":
            selected_char_list = Sign.char_plus
        elif f_char == "-":
            selected_char_list = Sign.char_minus
        elif f_char == "/":
            selected_char_list = Sign.char_slash
        elif f_char == "|":
            selected_char_list = Sign.char_bar
        elif f_char == "b":
            selected_char_list = Sign.char_b_slash
        elif f_char == "ar_up":
            selected_char_list = Sign.char_ar_up
        elif f_char == "ar_dn":
            selected_char_list = Sign.char_ar_dn
        elif f_char == "ar_r":
            selected_char_list = Sign.char_ar_r
        elif f_char == "ar_l":
            selected_char_list = Sign.char_ar_l
        elif f_char == ".":
            selected_char_list = Sign.char_dot
        else:
            selected_char_list = Digit.char_null
        for hc in range(0, len(ret_char_list[0])):    # columns
            for vc in range(0, len(ret_char_list)):    # rows
                if selected_char_list[vc][hc] == 1:
                    ret_char_list[vc][hc] = self.color_on
                elif selected_char_list[vc][hc] == 0:
                    ret_char_list[vc][hc] = Colors.OFF_GREY
        return ret_char_list

    def draw(self, p_char):
        # Background rectangle
        pygame.draw.rect(self.screen, Colors.BG_BLACK, pygame.Rect(self.topleft[0], self.topleft[1], self.width, self.height))
        # Array of dots, nested "for" loops for vertical, horizontal (2-dimensions arrays)
        for hd in range(0, len(self.dot_array[0])):    # columns
            for vd in range(0, len(self.dot_array)):    # rows
                dot_set_color = self._sel_char_list(p_char)[vd][hd]    # color of this dot, given the char we want to draw
                radius = self.dot_array[vd][hd].dot_draw(dot_set_color)    # compute radius relative to the size of the matrix
                # Draw the dot
                pygame.draw.circle(self.screen, self.dot_array[vd][hd].actual_color, (self.topleft[0] + int(self.width/6) + int(hd*(self.width/3)), self.topleft[1] + int(self.height/6) + int(vd*(self.height/3))), radius)
                self.dot_array[vd][hd].dot_frames_sequence(dot_set_color)    # advance transition, and change set > actual color when transition closing > not closing

        # Lines, vertical, horizontal
        for hl in range(0, 3):
            pygame.draw.line(self.screen, Colors.BG_BLACK, (self.topleft[0] + int(self.width/6) + int(hl*(self.width/3)), self.topleft[1]), (self.topleft[0] + int(self.width/6) + int(hl*(self.width/3)), self.topleft[1] + self.height), 1)
        for vl in range(0, 3):
            pygame.draw.line(self.screen, Colors.BG_BLACK, (self.topleft[0], self.topleft[1] + int(self.height/6) + int(vl*(self.height/3))), (self.topleft[0] + self.width, self.topleft[1] + int(self.height/6) + int(vl*(self.height/3))), 1)
        # Lines, diagonal
        pygame.draw.line(self.screen, Colors.BG_BLACK, (self.topleft[0], self.topleft[1] + 1 * self.height / 3), (self.topleft[0] + 1 * self.width / 3, self.topleft[1]), 1)
        pygame.draw.line(self.screen, Colors.BG_BLACK, (self.topleft[0], self.topleft[1] + 2 * self.height / 3), (self.topleft[0] + 2 * self.width / 3, self.topleft[1]), 1)
        pygame.draw.line(self.screen, Colors.BG_BLACK, (self.topleft[0], self.topleft[1] + 3 * self.height / 3), (self.topleft[0] + 3 * self.width / 3, self.topleft[1]), 1)
        pygame.draw.line(self.screen, Colors.BG_BLACK, (self.topleft[0] + 1 * self.width / 3, self.topleft[1] + 3 * self.height / 3), (self.topleft[0] + 3 * self.width / 3, self.topleft[1] + 1 * self.height / 3), 1)
        pygame.draw.line(self.screen, Colors.BG_BLACK, (self.topleft[0] + 2 * self.width / 3, self.topleft[1] + 3 * self.height / 3), (self.topleft[0] + 3 * self.width / 3, self.topleft[1] + 2 * self.height / 3), 1)

    def set_color_on(self, p_col):
        permissible_colors = [Colors.YELLOW, Colors.WHITE, Colors.GREEN, Colors.BLUE, Colors.RED]
        if p_col in permissible_colors:
            self.color_on = p_col
        else:
            raise InvalidColorSet

    char_null = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    char_cross = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]

    char_dots = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 1, 0]
    ]

    char_plus = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]

    char_minus = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]

    char_slash = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0]
    ]

    char_b_slash = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]

    char_bar = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]

    char_ar_up = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 0, 0]
    ]

    char_ar_dn = [
        [0, 0, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]

    char_ar_r = [
        [0, 1, 0],
        [0, 0, 1],
        [0, 1, 0]
    ]

    char_ar_l = [
        [0, 1, 0],
        [1, 0, 0],
        [0, 1, 0]
    ]

    char_dot = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]


class Point:

    def __init__(self, p_screen, p_topleft, p_width, p_frames_transition):
        self.width = p_width
        self.height = self.width
        self.screen = p_screen
        if not isinstance(p_topleft, tuple):
            raise InvalidTopLeftType
        self.topleft = p_topleft
        self.prev_char = None
        if not 0 < p_frames_transition <= 10:
            raise FramesPerTransitionOutOfRange
        self.fpt = p_frames_transition
        self.color_on = Colors.YELLOW
        self.dot_array = [
            [Dot(self.fpt, self.color_on, self.width / 2.4)]
        ]

    def _sel_char_list(self, f_char):
        ret_char_list = [
            [Colors.OFF_GREY]
        ]
        selected_char_list = [
            [Colors.OFF_GREY]
        ]
        if f_char == ".":
            ret_char_list[0][0] = self.color_on
        else:
            ret_char_list[0][0] = Colors.OFF_GREY
        return ret_char_list

    def draw(self, p_char):
        if len(p_char) > 1:
            raise DrawCharTooLong
        # Background rectangle
        pygame.draw.rect(self.screen, Colors.BG_BLACK, pygame.Rect(self.topleft[0], self.topleft[1], self.width, self.height))
        # Array of dots, nested "for" loops for vertical, horizontal (2-dimensions arrays)
        for hd in range(0, len(self.dot_array[0])):    # columns
            for vd in range(0, len(self.dot_array)):    # rows
                dot_set_color = self._sel_char_list(p_char)[vd][hd]    # color of this dot, given the char we want to draw
                radius = self.dot_array[vd][hd].dot_draw(dot_set_color)    # compute radius relative to the size of the matrix
                # Draw the dot
                pygame.draw.circle(self.screen, self.dot_array[vd][hd].actual_color, (self.topleft[0] + int(self.width/2), self.topleft[1] + int(self.height/2)), radius)
                self.dot_array[vd][hd].dot_frames_sequence(dot_set_color)    # advance transition, and change set > actual color when transition closing > not closing

        # One line, diagonal
        pygame.draw.line(self.screen, Colors.BG_BLACK, (self.topleft[0], self.topleft[1] + self.height), (self.topleft[0] + self.width, self.topleft[1]), 1)

    def set_color_on(self, p_col):
        permissible_colors = [Colors.YELLOW, Colors.WHITE, Colors.GREEN, Colors.BLUE, Colors.RED]
        if p_col in permissible_colors:
            self.color_on = p_col
        else:
            raise InvalidColorSet

    char_null = [
        [0]
    ]

    char_point = [
        [1]
    ]


class Dot:

    def __init__(self, fpt, color_on, radius):
        self.color_on = color_on
        self.fpt = fpt
        self.radius = radius
        self.actual_color = Colors.OFF_GREY
        self.frame_ctr = self.fpt + 1
        self.closing = False

    def dot_draw(self, p_set_color):
        dot_set_color = p_set_color
        if (dot_set_color != self.actual_color) and (self.frame_ctr == self.fpt + 1):
            self.closing = True
            self.frame_ctr = self.fpt
        if self.frame_ctr != self.fpt + 1:
            actual_radius = int(self.radius * (self.frame_ctr / self.fpt))
        else:
            actual_radius = int(self.radius)
        return actual_radius

    def dot_frames_sequence(self, p_set_color):
        if not self.frame_ctr == self.fpt + 1:
            if self.closing:
                self.frame_ctr -= 1
            if not self.closing and (self.frame_ctr <= self.fpt):
                self.frame_ctr += 1
        if self.frame_ctr < 1:
            self.closing = False
            self.actual_color = p_set_color


class Colors:

    BG_BLACK = (0, 12, 12)
    OFF_GREY = (0, 24, 24)
    YELLOW = (160, 255, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 128, 255)
    RED = (255, 0, 0)


class InvalidTopLeftType(Exception):
    """Parameter p_topleft is not a Tuple"""
    pass


class FramesPerTransitionOutOfRange(Exception):
    """Parameter p_frames_transition less than 1 or larger than 10"""


class DrawCharTooLong(Exception):
    """Parameter p_char is not a single character"""
    pass


class InvalidColorSet(Exception):
    """Parameter p_col not in the permissible color list [Digit.YELLOW, Digit.WHITE, Digit.GREEN, Digit.BLUE, Digit.RED]"""

