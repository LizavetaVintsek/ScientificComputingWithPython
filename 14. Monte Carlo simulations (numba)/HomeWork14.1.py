import time
import random

def pi(n):
    circle = 0
    for i in range (n):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1.0:
            circle +=1
    return (4.0 * circle)/n

i = 0
while True:
    i +=1
    n = pow(10,i)
    print("n = {}, pi = {}".format(n,pi(n)))
    start = time.time()
    pi(n)
    end = time.time()
    performance = end-start
    print(f"Time elampsed = {performance:.10f}")
    if i == 6:
        break

from numba import jit

@jit(nopython = True)
def pi(n):
    circle = 0
    for i in range (n):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1.0:
            circle +=1
    return (4.0 * circle)/n

i = 0
while True:
    i +=1
    n = pow(10,i)
    print("n = {}, pi = {}".format(n,pi(n)))
    start = time.time()
    pi(n)
    end = time.time()
    performance = end-start
    print(f"Time elampsed = {performance:.10f}")
    if i == 6:
        break




