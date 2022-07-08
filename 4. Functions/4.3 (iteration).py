# Create the following infinite generators:
#(a) iter_even(), producing even numbers (0, 2, 4, ...)
def iter_even ():
    n = 0
    while True:
        yield n
        n += 2
#(b) iter_odd(), producing odd numbers (1, 3, 5, ...)
def iter_odd ():
    n = 1
    while True:
        yield n
        n += 2
#(c) iter_power(k), producing powers of k (1, k, k*k, k*k*k, ...)
#var1
def iter_power(k):
    n = 2
    while True:
        yield n
        n = n ** k
even, odd, power = iter_even(), iter_odd(), iter_power(2)
for n in range(10):
    print("{:3d} {:3d} {:3d}".format(next(even), next(odd), next(power)))
#var1
for (a, b, c) in zip (iter_even(), iter_odd(), iter_power(2)):
    print ("{:3d} {:3d} {:3d}".format(a, b, c))
    if a >10: break
