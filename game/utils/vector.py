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


class Vector3(__Vector__):
    def __new__(cls, x, y, z):
        return super().__new__(Vector3, (x, y, z))

    @property
    def z(self):
        return self[2]

    def normal(self):
        n = 1 / sum(self)
        return self * (n, n, n)

    def distance(self, other):
        d = abs(self - other)
        return sqrt(sum(d ** (2, 2, 2)))

    def __add__(self, other):
        return Vector3(self[0] + other[0], self[1] + other[1], self[2] + other[2])

    def __sub__(self, other):
        return Vector3(self[0] - other[0], self[1] - other[1], self[2] - other[2])

    def __mul__(self, other):
        return Vector3(self[0] * other[0], self[1] * other[1], self[2] * other[2])

    def __truediv__(self, other):
        return Vector3(self[0] / other[0], self[1] / other[1], self[2] / other[2])

    def __floordiv__(self, other):
        return Vector3(self[0] // other[0], self[1] // other[1], self[2] // other[2])

    def __mod__(self, other):
        return Vector3(self[0] % other[0], self[1] % other[1], self[2] % other[2])

    def __pow__(self, other):
        return Vector3(self[0] ** other[0], self[1] ** other[1], self[2] ** other[2])

    def __lt__(self, other):
        return self[0] < other[0] and self[1] < other[1] and self[2] < other[2]

    def __le__(self, other):
        return self[0] <= other[0] and self[1] <= other[1] and self[2] <= other[2]

    def __gt__(self, other):
        return self[0] > other[0] and self[1] > other[1] and self[2] > other[2]

    def __ge__(self, other):
        return self[0] >= other[0] and self[1] >= other[1] and self[2] >= other[2]

    def __neg__(self):
        return Vector3(-self[0], -self[1], -self[2])

    def __pos__(self):
        return Vector3(+self[0], +self[1], +self[2])

    def __invert__(self):
        return Vector3(~self[0], ~self[1], ~self[2])

    def __bool__(self):
        return self[0] != 0 and self[1] != 0 and self[2] != 0

    def __abs__(self):
        return Vector3(abs(self[0]), abs(self[1]), abs(self[2]))

    def __round__(self, digit):
        return Vector3(
            round(self[0], digit), round(self[1], digit), round(self[2], digit)
        )


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
        return Vector3(-self[0], -self[1])

    def __pos__(self):
        return Vector3(+self[0], +self[1])

    def __invert__(self):
        return Vector3(~self[0], ~self[1])

    def __bool__(self):
        return self[0] != 0 and self[1] != 0

    def __abs__(self):
        return Vector2(abs(self[0]), abs(self[1]))

    def __round__(self, digit):
        return Vector2(round(self[0], digit), round(self[1], digit))
