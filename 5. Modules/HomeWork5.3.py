import random
def random_walk(start=0):
    n = start
    while True:
        yield n
        n = n + random.choice([-1, 1])

results = []
for iteration in range(1):
    rw = random_walk()
    for step in range(100):
        next(rw)
    results.append(next(rw))
print(results)

