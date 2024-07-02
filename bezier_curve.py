import math
from cust_vec import Vec

# needs controlpoints. At least 2, to then automatically create the last


class BezierQuad:
    def __init__(self, points: list[Vec]):
        if len(points) > 3:
            raise ValueError("Only accepts 2 points")

        self.__points: list[Vec] = points
        self.__curve: list[Vec] = []

        self.create_middle_point(*self.__points)

    def __getitem__(self, item):
        return self.__curve[item]

    def create_middle_point(self, p0, p2):
        self.__points.insert(1, math.floor((p2 - p0) / 2 + p0 + Vec([0, 100])))  # p1

    def get_point_on_curve(self, time):
        return math.floor((1 - time) ** 2 * self.__points[0] + 2 * (1 - time) * time * self.__points[1] + time ** 2 * self.__points[2])

    def calc_curve(self, resolution):
        for step in range(resolution + 1):
            self.__curve.append(self.get_point_on_curve(step / resolution))

    def get_curve(self):
        return self.__curve

    def get_control_points(self):
        return self.__points
