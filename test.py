import numpy as np


class Vector:
    def __init__(self, *args):
        self.data = np.array(args)

    def __repr__(self):
        return f"Vector({self.data})"

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __add__(self, other):
        if isinstance(other, Vector):
            other = other.data
        return Vector(*(self.data + other))

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vector):
            other = other.data
        return Vector(*(self.data - other))

    def __rsub__(self, other):
        return Vector(*(other - self.data))

    def __mul__(self, other):
        if isinstance(other, Vector):
            other = other.data
        return Vector(*(self.data * other))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Vector):
            other = other.data
        return Vector(*(self.data / other))

    def __rtruediv__(self, other):
        return Vector(*(other / self.data))

    def __neg__(self):
        return Vector(*(-self.data))

    def __array__(self):
        return np.asarray(self.data)


# Example Usage
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1)  # Output: Vector([1 2 3])
print(v1 + v2)  # Output: Vector([5 7 9])
print(v1 * 2)  # Output: Vector([2 4 6])
print(np.sum(v1))  # Output: 6
print(np.dot(v1, v2))  # Output: 32
