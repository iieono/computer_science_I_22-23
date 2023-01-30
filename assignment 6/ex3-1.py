v = [2, -3, 1, 2, 3, 1, 4, -6, 7, -5, -1]

for i in range(len(v)):
    start_index = i
    max_length = 0
    length = 1
    num = v[i]
    for y in range(i+1, len(v)):
        num = num + v[y]
        length += 1

        if num == 0:
            max_length = length

    if max_length > 0:
        print(f'Sub-array starting from index {start_index}, length {max_length}.')