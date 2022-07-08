# Find and explain the results.
t = (2, 4)
print(t[2])
#result: error
t.append(6)
#result: error
#t = (2, 4) is a tupple, is immutable, so I can't make changes with it like adding, deleting etc.
a, b = t
print(a, b)
#result: 2 4
#t is decoded to a, b and devided to a = 2, b = 4

