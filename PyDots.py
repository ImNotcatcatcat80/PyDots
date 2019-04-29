
import pygame


class Digit:

    BG_BLACK = (0, 12, 12)
    GREY = (0, 24, 24)
    YELLOW = (160, 255, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 128, 255)
    RED = (255, 0, 0)

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
        self.color_on = Digit.YELLOW
        self.dot_actual_color = [
            [Digit.GREY, Digit.GREY, Digit.GREY, Digit.GREY],
            [Digit.GREY, Digit.GREY, Digit.GREY, Digit.GREY],
            [Digit.GREY, Digit.GREY, Digit.GREY, Digit.GREY],
            [Digit.GREY, Digit.GREY, Digit.GREY, Digit.GREY],
            [Digit.GREY, Digit.GREY, Digit.GREY, Digit.GREY],
            [Digit.GREY, Digit.GREY, Digit.GREY, Digit.GREY],
            [Digit.GREY, Digit.GREY, Digit.GREY, Digit.GREY]
        ]
        self.dot_frame_ctr = [
            [self.fpt+1, self.fpt+1, self.fpt+1, self.fpt+1],
            [self.fpt+1, self.fpt+1, self.fpt+1, self.fpt+1],
            [self.fpt+1, self.fpt+1, self.fpt+1, self.fpt+1],
            [self.fpt+1, self.fpt+1, self.fpt+1, self.fpt+1],
            [self.fpt+1, self.fpt+1, self.fpt+1, self.fpt+1],
            [self.fpt+1, self.fpt+1, self.fpt+1, self.fpt+1],
            [self.fpt+1, self.fpt+1, self.fpt+1, self.fpt+1]
        ]
        self.dot_closing = [
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False]
        ]

    def _sel_char_list(self, f_char):
        if f_char == "f":
            return Digit.char_full
        elif f_char == "=":
            return Digit.char_stripes
        elif f_char == "0":
            return Digit.char_zero
        elif f_char == "1":
            return Digit.char_one
        elif f_char == "2":
            return Digit.char_two
        elif f_char == "3":
            return Digit.char_three
        elif f_char == "4":
            return Digit.char_four
        elif f_char == "5":
            return Digit.char_five
        elif f_char == "6":
            return Digit.char_six
        elif f_char == "7":
            return Digit.char_seven
        elif f_char == "8":
            return Digit.char_eight
        elif f_char == "9":
            return Digit.char_nine
        else:
            return Digit.char_null

    def draw(self, p_char):
        if len(p_char) > 1:
            raise DrawCharTooLong
        # Background rectangle
        pygame.draw.rect(self.screen, Digit.BG_BLACK, pygame.Rect(self.topleft[0], self.topleft[1], self.width, self.height))
        # Array of dots, nested "for" loops for vertical, horizontal
        for hd in range(0, 4):
            for vd in range(0, 7):
                # statements across 2-dimensional arrays
                # each array element is a single dot
                dot_set_color = self._sel_char_list(p_char)[vd][hd]
                if (dot_set_color != self.dot_actual_color[vd][hd]) and (self.dot_frame_ctr[vd][hd] == self.fpt + 1):
                    self.dot_closing[vd][hd] = True
                    self.dot_frame_ctr[vd][hd] = self.fpt
                if self.dot_frame_ctr[vd][hd] != self.fpt + 1:
                    radius = int((self.width/10)*(self.dot_frame_ctr[vd][hd]/self.fpt))
                else:
                    radius = int(self.width / 10)
                pygame.draw.circle(self.screen, self.dot_actual_color[vd][hd], (self.topleft[0] + int(self.width/8) + int(hd*(self.width/4)), self.topleft[1] + int(self.height/14) + int(vd*(self.height/7))), radius)

                if not self.dot_frame_ctr == self.fpt + 1:
                    if self.dot_closing[vd][hd]:
                        self.dot_frame_ctr[vd][hd] -= 1
                    if not self.dot_closing[vd][hd] and (self.dot_frame_ctr[vd][hd] <= self.fpt):
                        self.dot_frame_ctr[vd][hd] += 1
                if self.dot_frame_ctr[vd][hd] < 1:
                    self.dot_closing[vd][hd] = False
                    self.dot_actual_color[vd][hd] = dot_set_color
        # Lines, vertical, horizontal
        for hl in range(0, 4):
            pygame.draw.line(self.screen, Digit.BG_BLACK, (self.topleft[0] + int(self.width/8) + int(hl*(self.width/4)), self.topleft[1]), (self.topleft[0] + int(self.width/8) + int(hl*(self.width/4)), self.topleft[1] + self.height), 1)
        for vl in range(0, 7):
            pygame.draw.line(self.screen, Digit.BG_BLACK, (self.topleft[0], self.topleft[1] + int(self.height/14) + int(vl*(self.height/7))), (self.topleft[0] + self.width, self.topleft[1] + int(self.height/14) + int(vl*(self.height/7))), 1)
        # Lines, across
        pygame.draw.line(self.screen, Digit.BG_BLACK, (self.topleft[0], self.topleft[1] + 1 * self.height / 7), (self.topleft[0] + 1 * self.width / 4, self.topleft[1]), 1)
        pygame.draw.line(self.screen, Digit.BG_BLACK, (self.topleft[0], self.topleft[1] + 2 * self.height / 7), (self.topleft[0] + 2 * self.width / 4, self.topleft[1]), 1)
        pygame.draw.line(self.screen, Digit.BG_BLACK, (self.topleft[0], self.topleft[1] + 3 * self.height / 7), (self.topleft[0] + 3 * self.width / 4, self.topleft[1]), 1)
        pygame.draw.line(self.screen, Digit.BG_BLACK, (self.topleft[0], self.topleft[1] + 4 * self.height / 7), (self.topleft[0] + 4 * self.width / 4, self.topleft[1]), 1)
        pygame.draw.line(self.screen, Digit.BG_BLACK, (self.topleft[0], self.topleft[1] + 5 * self.height / 7), (self.topleft[0] + 4 * self.width / 4, self.topleft[1] + 1 * self.height / 7), 1)
        pygame.draw.line(self.screen, Digit.BG_BLACK, (self.topleft[0], self.topleft[1] + 6 * self.height / 7), (self.topleft[0] + 4 * self.width / 4, self.topleft[1] + 2 * self.height / 7), 1)
        pygame.draw.line(self.screen, Digit.BG_BLACK, (self.topleft[0], self.topleft[1] + 7 * self.height / 7), (self.topleft[0] + 4 * self.width / 4, self.topleft[1] + 3 * self.height / 7), 1)
        pygame.draw.line(self.screen, Digit.BG_BLACK, (self.topleft[0] + 1 * self.width / 4, self.topleft[1] + 7 * self.height / 7), (self.topleft[0] + 4 * self.width / 4, self.topleft[1] + 4 * self.height / 7), 1)
        pygame.draw.line(self.screen, Digit.BG_BLACK, (self.topleft[0] + 2 * self.width / 4, self.topleft[1] + 7 * self.height / 7), (self.topleft[0] + 4 * self.width / 4, self.topleft[1] + 5 * self.height / 7), 1)
        pygame.draw.line(self.screen, Digit.BG_BLACK, (self.topleft[0] + 3 * self.width / 4, self.topleft[1] + 7 * self.height / 7), (self.topleft[0] + 4 * self.width / 4, self.topleft[1] + 6 * self.height / 7), 1)

    def set_color_on(self, p_col):
        permissible_colors = [Digit.YELLOW, Digit.WHITE, Digit.GREEN, Digit.BLUE, Digit.RED]
        if p_col in permissible_colors:
            self.color_on = p_col
        else:
            raise InvalidColorSet

    char_null = [
        [GREY, GREY, GREY, GREY],
        [GREY, GREY, GREY, GREY],
        [GREY, GREY, GREY, GREY],
        [GREY, GREY, GREY, GREY],
        [GREY, GREY, GREY, GREY],
        [GREY, GREY, GREY, GREY],
        [GREY, GREY, GREY, GREY]
    ]
    char_full = [
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [YELLOW, YELLOW, YELLOW, YELLOW]
    ]
    char_stripes = [
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [GREY, GREY, GREY, GREY],
        [GREY, GREY, GREY, GREY],
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [GREY, GREY, GREY, GREY],
        [GREY, GREY, GREY, GREY],
        [YELLOW, YELLOW, YELLOW, YELLOW]
    ]
    char_zero = [
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [YELLOW, GREY, GREY, YELLOW],
        [YELLOW, GREY, GREY, YELLOW],
        [YELLOW, GREY, GREY, YELLOW],
        [YELLOW, GREY, GREY, YELLOW],
        [YELLOW, GREY, GREY, YELLOW],
        [YELLOW, YELLOW, YELLOW, YELLOW]
    ]
    char_one = [
        [GREY, GREY, GREY, YELLOW],
        [GREY, GREY, YELLOW, YELLOW],
        [GREY, GREY, GREY, YELLOW],
        [GREY, GREY, GREY, YELLOW],
        [GREY, GREY, GREY, YELLOW],
        [GREY, GREY, GREY, YELLOW],
        [GREY, GREY, GREY, YELLOW]
    ]
    char_two = [
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [GREY, GREY, GREY, YELLOW],
        [GREY, GREY, GREY, YELLOW],
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [YELLOW, GREY, GREY, GREY],
        [YELLOW, GREY, GREY, GREY],
        [YELLOW, YELLOW, YELLOW, YELLOW]
    ]
    char_three = [
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [GREY, GREY, GREY, YELLOW],
        [GREY, GREY, GREY, YELLOW],
        [GREY, YELLOW, YELLOW, YELLOW],
        [GREY, GREY, GREY, YELLOW],
        [GREY, GREY, GREY, YELLOW],
        [YELLOW, YELLOW, YELLOW, YELLOW]
    ]
    char_four = [
        [YELLOW, GREY, GREY, YELLOW],
        [YELLOW, GREY, GREY, YELLOW],
        [YELLOW, GREY, GREY, YELLOW],
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [GREY, GREY, GREY, YELLOW],
        [GREY, GREY, GREY, YELLOW],
        [GREY, GREY, GREY, YELLOW]
    ]
    char_five = [
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [YELLOW, GREY, GREY, GREY],
        [YELLOW, GREY, GREY, GREY],
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [GREY, GREY, GREY, YELLOW],
        [GREY, GREY, GREY, YELLOW],
        [YELLOW, YELLOW, YELLOW, YELLOW]
    ]
    char_six = [
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [YELLOW, GREY, GREY, GREY],
        [YELLOW, GREY, GREY, GREY],
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [YELLOW, GREY, GREY, YELLOW],
        [YELLOW, GREY, GREY, YELLOW],
        [YELLOW, YELLOW, YELLOW, YELLOW]
    ]
    char_seven = [
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [GREY, GREY, GREY, YELLOW],
        [GREY, GREY, GREY, YELLOW],
        [GREY, GREY, GREY, YELLOW],
        [GREY, GREY, GREY, YELLOW],
        [GREY, GREY, GREY, YELLOW],
        [GREY, GREY, GREY, YELLOW]
    ]
    char_eight = [
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [YELLOW, GREY, GREY, YELLOW],
        [YELLOW, GREY, GREY, YELLOW],
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [YELLOW, GREY, GREY, YELLOW],
        [YELLOW, GREY, GREY, YELLOW],
        [YELLOW, YELLOW, YELLOW, YELLOW]
    ]
    char_nine = [
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [YELLOW, GREY, GREY, YELLOW],
        [YELLOW, GREY, GREY, YELLOW],
        [YELLOW, YELLOW, YELLOW, YELLOW],
        [GREY, GREY, GREY, YELLOW],
        [GREY, GREY, GREY, YELLOW],
        [YELLOW, YELLOW, YELLOW, YELLOW]
    ]


class Sign:

    BG_BLACK = (0, 12, 12)
    GREY = (0, 24, 24)
    YELLOW = (160, 255, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 128, 255)
    RED = (255, 0, 0)

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
        self.color_on = Sign.YELLOW
        self.dot_actual_color = [
            [Sign.GREY, Sign.GREY, Sign.GREY],
            [Sign.GREY, Sign.GREY, Sign.GREY],
            [Sign.GREY, Sign.GREY, Sign.GREY]
        ]
        self.dot_frame_ctr = [
            [self.fpt + 1, self.fpt + 1, self.fpt + 1],
            [self.fpt + 1, self.fpt + 1, self.fpt + 1],
            [self.fpt + 1, self.fpt + 1, self.fpt + 1]
        ]
        self.dot_closing = [
            [False, False, False],
            [False, False, False],
            [False, False, False]
        ]

    def _sel_char_list(self, f_char):
        if f_char == "x":
            return Sign.char_cross
        elif f_char == ":":
            return Sign.char_dots
        elif f_char == "+":
            return Sign.char_plus
        elif f_char == "-":
            return Sign.char_minus
        elif f_char == "/":
            return Sign.char_slash
        elif f_char == "|":
            return Sign.char_bar
        elif f_char == "b":
            return Sign.char_b_slash
        else:
            return Digit.char_null

    def draw(self, p_char):
        if len(p_char) > 1:
            raise DrawCharTooLong
        # Background rectangle
        pygame.draw.rect(self.screen, Sign.BG_BLACK, pygame.Rect(self.topleft[0], self.topleft[1], self.width, self.height))
        # Array of dots, nested "for" loops for vertical, horizontal
        for hd in range(0, 3):
            for vd in range(0, 3):
                # statements across 2-dimensional arrays
                # each array element is a single dot
                dot_set_color = self._sel_char_list(p_char)[vd][hd]
                if (dot_set_color != self.dot_actual_color[vd][hd]) and (self.dot_frame_ctr[vd][hd] == self.fpt + 1):
                    self.dot_closing[vd][hd] = True
                    self.dot_frame_ctr[vd][hd] = self.fpt
                if self.dot_frame_ctr[vd][hd] != self.fpt + 1:
                    radius = int((self.width/7.5)*(self.dot_frame_ctr[vd][hd]/self.fpt))
                else:
                    radius = int(self.width / 7.5)
                pygame.draw.circle(self.screen, self.dot_actual_color[vd][hd], (self.topleft[0] + int(self.width/6) + int(hd*(self.width/3)), self.topleft[1] + int(self.height/6) + int(vd*(self.height/3))), radius)

                if not self.dot_frame_ctr == self.fpt + 1:
                    if self.dot_closing[vd][hd]:
                        self.dot_frame_ctr[vd][hd] -= 1
                    if not self.dot_closing[vd][hd] and (self.dot_frame_ctr[vd][hd] <= self.fpt):
                        self.dot_frame_ctr[vd][hd] += 1
                if self.dot_frame_ctr[vd][hd] < 1:
                    self.dot_closing[vd][hd] = False
                    self.dot_actual_color[vd][hd] = dot_set_color
        # Lines, vertical, horizontal
        for hl in range(0, 3):
            pygame.draw.line(self.screen, Sign.BG_BLACK, (self.topleft[0] + int(self.width/6) + int(hl*(self.width/3)), self.topleft[1]), (self.topleft[0] + int(self.width/6) + int(hl*(self.width/3)), self.topleft[1] + self.height), 1)
        for vl in range(0, 3):
            pygame.draw.line(self.screen, Sign.BG_BLACK, (self.topleft[0], self.topleft[1] + int(self.height/6) + int(vl*(self.height/3))), (self.topleft[0] + self.width, self.topleft[1] + int(self.height/6) + int(vl*(self.height/3))), 1)
        # Lines, across
        pygame.draw.line(self.screen, Digit.BG_BLACK, (self.topleft[0], self.topleft[1] + 1 * self.height / 3), (self.topleft[0] + 1 * self.width / 3, self.topleft[1]), 1)
        pygame.draw.line(self.screen, Digit.BG_BLACK, (self.topleft[0], self.topleft[1] + 2 * self.height / 3), (self.topleft[0] + 2 * self.width / 3, self.topleft[1]), 1)
        pygame.draw.line(self.screen, Digit.BG_BLACK, (self.topleft[0], self.topleft[1] + 3 * self.height / 3), (self.topleft[0] + 3 * self.width / 3, self.topleft[1]), 1)
        pygame.draw.line(self.screen, Digit.BG_BLACK, (self.topleft[0] + 1 * self.width / 3, self.topleft[1] + 3 * self.height / 3), (self.topleft[0] + 3 * self.width / 3, self.topleft[1] + 1 * self.height / 3), 1)
        pygame.draw.line(self.screen, Digit.BG_BLACK, (self.topleft[0] + 2 * self.width / 3, self.topleft[1] + 3 * self.height / 3), (self.topleft[0] + 3 * self.width / 3, self.topleft[1] + 2 * self.height / 3), 1)

    char_null = [
        [GREY, GREY, GREY],
        [GREY, GREY, GREY],
        [GREY, GREY, GREY]
    ]

    char_cross = [
        [YELLOW, GREY, YELLOW],
        [GREY, YELLOW, GREY],
        [YELLOW, GREY, YELLOW]
    ]

    char_dots = [
        [GREY, YELLOW, GREY],
        [GREY, GREY, GREY],
        [GREY, YELLOW, GREY]
    ]

    char_plus = [
        [GREY, YELLOW, GREY],
        [YELLOW, YELLOW, YELLOW],
        [GREY, YELLOW, GREY]
    ]

    char_minus = [
        [GREY, GREY, GREY],
        [YELLOW, YELLOW, YELLOW],
        [GREY, GREY, GREY]
    ]

    char_slash = [
        [GREY, GREY, YELLOW],
        [GREY, YELLOW, GREY],
        [YELLOW, GREY, GREY]
    ]

    char_b_slash = [
        [YELLOW, GREY, GREY],
        [GREY, YELLOW, GREY],
        [GREY, GREY, YELLOW]
    ]

    char_bar = [
        [GREY, YELLOW, GREY],
        [GREY, YELLOW, GREY],
        [GREY, YELLOW, GREY]
    ]


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

