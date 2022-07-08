class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
# return string "Vector(x, y, z)"
    def __repr__(self):
        return f"Vector ({self.x}, {self.y}, {self.z})" #using str()
#teachers var
        return "Vector({}, {}, {})".format(self.x, self.y, self.z)
        return "Vector({0!r}, {1!r}, {2!r})".format(self.x, self.y, self.z)
        return f"Vector ({self.x!r}, {self.y!r}, {self.z!r})" #using repr()
# v == w
    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)
#or
        return self.x ==other.x and self.y ==other.y and self.z == other.z
# v != w
    def __ne__(self, other):
        return not self == other
# v + w
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
# v - w
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
# return the dot product (number)
    def __mul__(self, other):
        return ((self.x * other.x) + (self.y * other.y) + (self.z * other.z))
#teachers var
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
        else:
            return Vector (self.x * other, self.y * other, self.x * other)
#__rmul__ = __mul__ number*v
# return the cross product (Vector)
    def cross(self, other):
        return Vector ((self.y * other.z - self.z * other.y),
                       (self.z * other.x - self.x * other.z),
                       (self.x * other.y - self.y * other.x))
# the length of the vector
    def length(self):
        import math
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))
# we assume that vectors are immutable
    def __hash__(self):
        return hash((self.x, self.y, self.z))



import math
v = Vector(1, 2, 3)
w = Vector(2, -3, 2)
print (Vector.cross(v, w))
#assert v == w
assert v != w
assert v + w == Vector(3, -1, 5)
assert v - w == Vector(-1, 5, 1)
assert v * w == 2
assert v.cross(w) == Vector(13, 4, -7)
assert v.length() == math.sqrt(14)
S = set([v, v, w])
print (S)
assert len(S) == 2

print("Tests passed")
