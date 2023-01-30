v = []
n = int(input('Enter a positive value: '))
while n <= 99 and n > 0:
    v.append(n)
    n = int(input('Enter a positive value: '))

# test values from example
# v = [1, 2, 3, 4, 5, 10, 20, 24, 55, 62, 73, 74, 89, 93, 94, 95]

counts = []
for i in range(10):
    count = 0
    for y in v:
        num = y - (i*10)
        if num >= 0 and num < 10:
            count += 1
    counts.append(count)

for i in range(max(counts)):
    for y in counts:
        if y > i:
            print('*', end=' ')
        else: 
            print(' ', end=' ')
    print()
