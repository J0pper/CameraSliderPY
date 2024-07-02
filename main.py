import sys

import pygame as pg
from pygame import gfxdraw
from UI import *
from cust_vec import Vec
from bezier_curve import BezierQuad
import numpy as np

RES: list[float] = [1920 / 3, 1080 / 3]
display: pg.Surface = pg.display.set_mode(RES)

drawPoints = []
subPoints = []
slider = Slider(display, 0, 100, 0, 1)

oneTime = True
times = [0, 0.25, 0.5, 0.75, 1]
curves = []


running: bool = True
while running:
    display.fill((34, 34, 34))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            point = Vec(pg.mouse.get_pos())
            drawPoints.append(point)
            subPoints.append(point)

            if len(subPoints) == 2:
                bezier = BezierQuad(subPoints)
                bezier.calc_curve(100)
                drawPoints += bezier.get_control_points()
                set(drawPoints)
                print(drawPoints)

                curves.append(bezier)

                subPoints = []

    for curve in curves:
        for index in range(0, len(curve.get_curve()) - 1):
            x = curve[index]
            y = curve[index + 1]
            gfxdraw.line(display, x[0], x[1], y[0], y[1], (0, 255, 0))

    for point in drawPoints:
        point.draw(display, (255, 0, 0), 3)

    pg.display.update()

pg.quit()
sys.exit()
