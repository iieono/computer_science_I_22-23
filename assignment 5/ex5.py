v = [2.0, 3.1, 4.3, -10.6, -2.0, 5.2, 1.2, 8.9, 3.1, -9.2, 8.3]
index_start = 0
max_index_start = 0
max_sequence = 0
sequence = 0
for i in v:
    if i > 0 and sequence > 0:
        sequence += 1
        if sequence > max_sequence:
            max_sequence = sequence
            max_index_start = index_start
    elif i > 0:
        index_start = v.index(i)
        sequence = 1
    elif i < 0:
        sequence = 0
        index = 0
print(f'The longest positive sequence ({max_sequence} elements) starts from index {max_index_start}.')








