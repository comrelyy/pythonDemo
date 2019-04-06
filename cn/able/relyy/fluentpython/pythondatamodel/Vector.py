from math import hypot

class Vector:

    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y

    # 把对象用字符串的形式表示 类似于toString()
    def __repr__(self):
        return 'Vector(%r,%r)'% (self.x, self.y)

    # 取模
    def __abs__(self):
        return hypot(self.x,self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


