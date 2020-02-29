from itertools import permutations as pt


combol = pt(range(1, 10), 3)
for t in combol:
    if sum(t) == 15:
        print(t)
