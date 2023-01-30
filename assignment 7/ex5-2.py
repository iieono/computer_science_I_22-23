# v = [ 
#     [0, 1, 2, 3, 4],
#     [0, 1, 2, 3, 4], 
#     [0, 1, 2, 3, 4], 
#     [0, 1, 2, 3, 4], 
#     [0, 1, 2, 3, 4] ]

n = 5

print_index = [0, 0]
print('(', end='')
print(*print_index, sep=', ', end=') ')

idx = 1
def print_res():
    global idx
    print('(', end='')
    print(*print_index, sep=', ', end=') ')
    idx += 1
    if idx == n:
        print() 
        idx = 0

while True:
    if print_index[1] + 1 < n:
        print_index[1] = print_index[1] + 1
    else:
        print_index[0] = print_index[0] + 1

    print_res()

    while print_index[1] > 0 and print_index[0] < n-1:
        print_index[0] = print_index[0] + 1
        print_index[1] = print_index[1] - 1
        print_res()

    if print_index[0] + 1 < n:
        print_index[0] = print_index[0] + 1
    else:
        print_index[1] = print_index[1] + 1 

    print_res()

    while print_index[1] < n-1 and print_index[0] > 0:
        print_index[0] = print_index[0] - 1
        print_index[1] = print_index[1] + 1
        print_res()
    
    if print_index[0] == n-1 and print_index[1] == n-1:
        break