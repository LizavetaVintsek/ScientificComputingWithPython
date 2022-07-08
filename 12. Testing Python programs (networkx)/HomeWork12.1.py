class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "Vector({}, {}, {})".format(self.x, self.y, self.z)
# v == w
    def __eq__(self, other):
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
S = set([v, v, w])

import unittest

class TestVector(unittest.TestCase):
    def setUp(self): pass

    def test_vector(self):
        self.assertEqual(v, w)
        self.assertNotEqual(v, w)
        self.assertTrue(v + w, Vector(3, -1, 5))
        self.assertTrue(v - w, Vector(-1, 5, 1))
        self.assertTrue(v * w, 2)
        self.assertTrue(v.cross(w), Vector(13, 4, -7))
        self.assertTrue(v.length(), math.sqrt(14))
        self.assertTrue(v * w, 2)
        self.assertTrue(len(S), 2)
        print("Tests passed")
    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()
