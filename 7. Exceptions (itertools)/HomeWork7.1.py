import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return f"Vector ({self.x}, {self.y}, {self.z})"
    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)
    def __ne__(self, other):
        return not self == other
    def cross(self, other):
        return Vector ((self.y * other.z - self.z * other.y),
                       (self.z * other.x - self.x * other.z),
                       (self.x * other.y - self.y * other.x))
    def __mul__(self, other):
            if isinstance(other, Vector):
                return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
            else:
                return Vector (self.x * other, self.y * other, self.x * other)
    def length (self):
        return math.sqrt (self*self)

def find_axis (v1, v2):
    v3 = v1.cross(v2)
    if v3 == Vector(0,0,0):
        raise ValueError ("Vectors v1 and v2 can't be parallel (or zero)!")
    d = v3.length()
    v3 = v3 * (1.0 / d)
    return v3

v1 = Vector (9, 8, 0)
v2 = Vector (0, 7, 6)
print (find_axis (v1, v2))

