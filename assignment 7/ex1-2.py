v = [[4, 3, 1, 2], [1, 7, 2, 2], [3, 3, 5, 0]]

csum = [0] * len(v[0])

for i in range(len(v)):
    rsum = 0

    for j in range(len(v[0])):
        print(v[i][j], end=' ')
        rsum += v[i][j]
        csum[j] = csum[j] + v[i][j]

    print(rsum, end=' ')
    print()

print(*csum, sep=' ')