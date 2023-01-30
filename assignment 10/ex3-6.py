import math
overall_len = 60
load_data = []
with open('ex3 data.txt') as f:
    for i in f.readlines():
        load_data.append(i.strip())

final_result = []
for i in load_data:
    line_len = len(i)
    if line_len > overall_len:
        continue
    list_line = i.split(' ')
    len_pure = len(''.join(list_line))
    space_len = overall_len - len_pure
    each_space = math.floor(space_len / (len(list_line)-1))
    extra = space_len - (each_space * (len(list_line)-1))
    text = ''
    for k in range(len(list_line)):
        text += list_line[k]
        text += ' ' * each_space
        if extra > 0:
            text += ' '
            extra -= 1
    final_result.append(text)

with open('ex3 result.txt', 'w') as f:
    for i in final_result:
        f.write(i)
        f.write('\n')