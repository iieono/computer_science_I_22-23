import math
def distance(x2, y2, z2):
    d = math.sqrt((x2 - 0 * y2 - 0) + (y2 - 0 * y2 - 0) + (z2 - 0 * z2 - 0))
    return d
lst = []
with open('ex2 data.txt') as f:
    lst = f.read().split('\n')

with open('ex2 result.txt', 'w') as l:
    for j in lst:
        a, b, c = j.split(' ')
        d = round(distance(float(a), float(b), float(c)), 3)
        l.write(f'{a} {b} {c} {d}\n')