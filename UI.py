import pygame as pg
from pygame import gfxdraw


def draw_circle(pos, surface, color=(0, 0, 0), radius=1):
    gfxdraw.aacircle(surface, int(pos[0]), int(pos[1]), radius, color)
    gfxdraw.filled_circle(surface, int(pos[0]), int(pos[1]), radius, color)


class UIWidgets:
    allWidgets = []

    def __init__(self):
        self.allWidgets.append(self)

    def draw_widgets(self):
        for widget in UIWidgets.allWidgets:
            widget.draw()


class Slider(UIWidgets):
    def __init__(self, surface, min_val, max_val, start_val, step):
        """
        :param min_val: minimum value of the slider
        :param max_val: maximum value of the slider
        :param start_val: default value of the slider when created
        :param step: step size for each tick of the slider
        """
        super().__init__()

        self.surface = surface
        self.min = min_val
        self.max = max_val
        self.value = start_val
        self.step = step

        self.showValue = True

    def draw(self):
        pg.draw.rect(self.surface, [211, 211, 211], [200, 100, 200, 10])
        draw_circle(self.surface, [100, 100], 10, [83, 83, 83])
        # gray rectangle
        # black circle
        # if self.showValue, show value

    def position(self):
        pass

    def size(self):
        pass

    def get_value(self):
        return self.value

    def set_value(self, value):
        pass

    def on_click(self):
        pass
