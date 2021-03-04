import math

def lerp(a, b, t):
    return a + (b-a)*t

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'[{self.x}, {self.y}]'

    def __add__(self, v):
        return Vector(self.x+v.x, self.y+v.y)

    def __sub__(self, v):
        return Vector(self.x-v.x, self.y-v.y)

    def __mul__(self, y):
        return Vector(self.x * y, self.y * y)

    def __rmul__(self, y):
        return Vector(self.x * y, self.y * y)

    def __truediv__(self, y):
        return Vector(self.x / y, self.y / y)

    def __rtruediv__(self, y):
        return Vector(self.x / y, self.y / y)

    def __iadd__(self, v):
        self.x += v.x
        self.y += v.y
        return self

    def __isub__(self, v):
        self.x -= v.x
        self.y -= v.y
        return self

    def __eq__(self, v):
        return self.x == v.x and self.y == v.y

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def lerp(self, other, t):
        return Vector(lerp(self.x, other.x, t), lerp(self.y, other.y, t))

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError

    def __iter__(self):
        yield self.x
        yield self.y

    def copy(self):
        return Vector(self.x, self.y)

if __name__ == "__main__":
    a = Vector(2,2)
    b = Vector(1,1)
    print(a)
    print(abs(a))
    print(a-b)
    print(a[0])
    a[0] = 3
    print(a)
    print(a * 2)
    print(2 * a)