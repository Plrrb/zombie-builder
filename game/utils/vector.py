from math import sqrt


class __Vector__(tuple):
    def inbounds(self, v1, v2):
        return v1 < self < v2

    def length(self):
        return sum(abs(self))

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]


class Vector2(__Vector__):
    def __new__(cls, x, y):
        return super().__new__(Vector2, (x, y))

    def magnitude(self):
        return sqrt(sum(self ** (2, 2)))

    def normalize(self):
        vmag = self.magnitude()
        return Vector2(self[0] / vmag, self[1] / vmag)

    def distribute(self):
        n = 1 / sum(self)
        return self * (n, n)

    def distance(self, other):
        d = abs(self - other)
        return sqrt(sum(d ** (2, 2)))

    def __add__(self, other):
        return Vector2(self[0] + other[0], self[1] + other[1])

    def __sub__(self, other):
        return Vector2(self[0] - other[0], self[1] - other[1])

    def __mul__(self, other):
        return Vector2(self[0] * other[0], self[1] * other[1])

    def __truediv__(self, other):
        return Vector2(self[0] / other[0], self[1] / other[1])

    def __floordiv__(self, other):
        return Vector2(self[0] // other[0], self[1] // other[1])

    def __mod__(self, other):
        return Vector2(self[0] % other[0], self[1] % other[1])

    def __pow__(self, other):
        return Vector2(self[0] ** other[0], self[1] ** other[1])

    def __lt__(self, other):
        return self[0] < other[0] and self[1] < other[1]

    def __le__(self, other):
        return self[0] <= other[0] and self[1] <= other[1]

    def __gt__(self, other):
        return self[0] > other[0] and self[1] > other[1]

    def __ge__(self, other):
        return self[0] >= other[0] and self[1] >= other[1]

    def __neg__(self):
        return Vector2(-self[0], -self[1])

    def __pos__(self):
        return Vector2(+self[0], +self[1])

    def __invert__(self):
        return Vector2(~self[0], ~self[1])

    def __bool__(self):
        return self[0] != 0 and self[1] != 0

    def __abs__(self):
        return Vector2(abs(self[0]), abs(self[1]))

    def __round__(self, digit):
        return Vector2(round(self[0], digit), round(self[1], digit))
