import numpy as np
import UI


class Vec:
    def __init__(self, coordinates):
        self.vector = np.array(coordinates)

    def __repr__(self):
        return f"Vec({self.vector})"

    def __getitem__(self, index):
        return self.vector[index]

    def __add__(self, other):
        if isinstance(other, Vec):
            return Vec(self.vector + other.vector)
        else:
            return Vec(self.vector + other)

    def __radd__(self, other):
        if isinstance(other, Vec):
            return Vec(self.vector + other.vector)
        else:
            return Vec(self.vector + other)

    def __sub__(self, other):
        if isinstance(other, Vec):
            return Vec(self.vector - other.vector)
        else:
            return Vec(self.vector - other)

    def __rsub__(self, other):
        if isinstance(other, Vec):
            return Vec(self.vector - other.vector)
        else:
            return Vec(self.vector - other)

    def __mul__(self, other):
        if isinstance(other, Vec):
            return Vec(self.vector * other.vector)
        else:
            return Vec(self.vector * other)

    def __rmul__(self, other):
        if isinstance(other, Vec):
            return Vec(self.vector * other.vector)
        else:
            return Vec(self.vector * other)

    def __truediv__(self, other):
        if isinstance(other, Vec):
            return Vec(self.vector / other.vector)
        else:
            return Vec(self.vector / other)

    def __rtruediv__(self, other):
        if isinstance(other, Vec):
            return Vec([self.vector / other.vector])
        else:
            return Vec([self.vector / other])

    def __ceil__(self):
        return Vec(np.ceil(self.vector).astype(int))

    def __floor__(self):
        return Vec(np.floor(self.vector).astype(int))

    def draw(self, *args):
        """
        :param args: IN ORDER: pygame surface, color (optional, default=(0, 0, 0)), radius (optional, default=1).
        :return:
        """
        UI.draw_circle(self.vector, *args)
