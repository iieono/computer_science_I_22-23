v = [5, 1, 7, 9, 11, 13, 2, 17, 19, 21]
w = [3, 33, -4, 5, 6, 0, 1, 1, 19, 17]

max_diff = 0

for i in range(len(v)):
    diff = abs(v[i] - w[i])
    if diff > max_diff:
        max_diff = diff

print(max_diff)






