#Let p=(x,y) be a point in a plane. Define the following functions using lambda:
#(a) a test if p is in unit circle
#var1
(x, y) = (0.1, 0.1)
p= (x, y)
test_unit_circle = lambda x,y: x**2 + y**2 <= 1
print(test_unit_circle(x,y))
#var2
lam_unit = lambda p: pow(p[0],2) + pow(p[1],2) < 1
lam_pos = lambda p: (p[0] > 0) and (p[1] > 0)
assert lam_unit((0.5, 0.5))
assert not lam_unit ((1, 1))
L = [(2,-2), (-1,2), (7,4), (-1, 4)]
for p in L:
    print(p, lam_unit(p), lam_pos(p))
#(b) a test if the coordinates of p are positive
(x, y) = (2,-2)
p= (x, y)
test = lambda x, y: x > 0 and y > 0
print(test(x,y))
#(c) a sorting key:
# y decreasing:
#var1
L = [(2,-2), (-1,2), (7,4), (-1, 4)]
L.sort (key=lambda p: (-p[1], p[0]))
print(L)
#var2
L.sort (key = lambda p: -p[1])
print (L)
#x increasing:
L.sort (key = lambda p: p[0])
print (L)
# according to distance from (0,0), increasing
L.sort (key = lambda p: pow(p[0],2) + pow(p[1],2))
print(L)
#(d) a sorting key (the sum |x|+|y|)
L = [(2,-2), (-1,2), (7,4), (-1, 4)]
L.sort (key=lambda p: (abs(p[0]) + abs(p[1])))
print(L)




