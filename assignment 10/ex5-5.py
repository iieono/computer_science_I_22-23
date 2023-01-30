load_data = []
with open('ex5 data.txt') as f:
    for i in f.readlines():
        load_data.append([*i.strip()])

# print(load_data)
number = 1
for i in range(len(load_data)):
    print('---------------------------------')
    for num in range(3):
        print('|', end='')
        for j in range(len(load_data[0])):
            if load_data[i][j] == '1':
                print('***', end='|')
            elif load_data[i][j] == '0':
                if i == 0 or (i-1 > 0 and i+1 < len(load_data)):
                    if i == 0 and load_data[i+1][j] == '0':
                        print(f'{number}   '[0:3], end='|')
                        number += 1
                        continue
                    if load_data[i-1][j] != '0' and load_data[i+1][j] == '0':
                        print(f'{number}   '[0:3], end='|')
                        number += 1
                        continue
                
                if j == 0 or (j-1 > 0 and j+1 < len(load_data[0])):
                    if j == 0 and load_data[i][j+1] == '0':
                        print(f'{number}   '[0:3], end='|')
                        number += 1
                        continue
                    if load_data[i][j-1] != '0' and load_data[i][j+1] == '0':
                        print(f'{number}   '[0:3], end='|')
                        number += 1
                        continue
                print('   ', end='|')
        print()
print('---------------------------------')



