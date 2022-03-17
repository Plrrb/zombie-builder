from math import sqrt


class __Vector__:
    def inbounds(self, v1, v2):
        return v1 < self < v2

    def length(self):
        return sum(abs(self))


class Vector3(__Vector__):
    __slots__ = "x", "y", "z"

    def normal(self):
        n = 1 / sum(self)
        return self * Vector3(n, n, n)

    def distance(self, other):
        d = abs(self - other)

        return sqrt(sum(d ** Vector3(2, 2, 2)))

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"{self.x}, {self.y}, {self.z}"

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        return Vector3(self.x / other.x, self.y / other.y, self.z / other.z)

    def __floordiv__(self, other):
        return Vector3(self.x // other.x, self.y // other.y, self.z // other.z)

    def __mod__(self, other):
        return Vector3(self.x % other.x, self.y % other.y, self.z % other.z)

    def __pow__(self, other):
        return Vector3(self.x ** other.x, self.y ** other.y, self.z ** other.z)

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y and self.z < other.z

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y and self.z <= other.z

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y and self.z > other.z

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y and self.z >= other.z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y and self.z != other.z

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __pos__(self):
        return Vector3(+self.x, +self.y, +self.z)

    def __invert__(self):
        return Vector3(~self.x, ~self.y, ~self.z)

    def __bool__(self):
        return self.x != 0 and self.y != 0 and self.z != 0

    def __abs__(self):
        return Vector3(abs(self.x), abs(self.y), abs(self.z))

    def __round__(self, digit):
        return Vector3(round(self.x, digit), round(self.y, digit), round(self.z, digit))

    def __getitem__(self, index):
        return (self.x, self.y, self.z)[index]


class Vector2(__Vector__):
    __slots__ = "x", "y"

    def normal(self):
        n = 1 / sum(self)
        return self * Vector2(n, n)

    def distance(self, other):
        d = abs(self - other)

        return sqrt(sum(d ** Vector2(2, 2)))

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x}, {self.y}"

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector2(self.x / other.x, self.y / other.y)

    def __floordiv__(self, other):
        return Vector2(self.x // other.x, self.y // other.y)

    def __mod__(self, other):
        return Vector2(self.x % other.x, self.y % other.y)

    def __pow__(self, other):
        return Vector2(self.x ** other.x, self.y ** other.y)

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

    def __neg__(self):
        return Vector3(-self.x, -self.y)

    def __pos__(self):
        return Vector3(+self.x, +self.y)

    def __invert__(self):
        return Vector3(~self.x, ~self.y)

    def __bool__(self):
        return self.x != 0 and self.y != 0

    def __abs__(self):
        return Vector2(abs(self.x), abs(self.y))

    def __round__(self, digit):
        return Vector2(round(self.x, digit), round(self.y, digit))

    def __getitem__(self, index):
        return (self.x, self.y)[index]
