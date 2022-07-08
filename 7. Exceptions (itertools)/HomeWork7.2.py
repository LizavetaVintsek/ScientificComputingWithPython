import itertools
import random
class MyIter01:
    def __init__(self):
        self.n = 1
    def __call__(self):
        self.n = (self.n +1) % 2
        return self.n
class MyIterRandom:
    def __init__(self):
        pass
    def __call__ (self):
        return random.choice([0,1])
class IterCycle:
    def __init__(self):
        delf.seq = seq
        self.idx = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.idx = self.idx + 1) % len(self.seq)
        return self.seq[self.idx]

def iter_cycle(sequence):
    while True:
        for item in sequence:
            yeld item

def iter_random(seqence):
    while True:
        yeld random.choice(sequence)

#(a) returning 0, 1, 0, 1, 0, 1, ...,
iter_a = itertools.cycle([0, 1])
iter_a = iter_cycle((0, 1))
iter_a = iter((MyIter01(), -1)
iter_a = IterCycle([0, 1])

#(b) returning random sequence with 0 and 1,
iter_b = iter_random ([0, 1])
iter_b = iter(lambda: random.choice ([0, 1]), -1)
iter_b = iter (MyIterRandom(), -1)
#(c) returning 0, 1, 0, -1, 0, 1, 0, -1, ...
iter_c = itertools.cycle([0, 1, 0, -1])
iter_c = iter_cycle((0, 1, 0, -1))
iter_c = IterCycle([0, 1, 0, -1])

