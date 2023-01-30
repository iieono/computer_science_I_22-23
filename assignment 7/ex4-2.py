v = [[1, -2, 0, 3], [3, 1, 5, 4], [7, 2, 3, 1], [4, 6, -1, 5]]

n = int((input('Enter search value: ')))

def print_matrix(row, column):
        print(f'Row: {row+1}, Column: {column+1}')

        if column > 0 and row > 0:
            print('Top-left sub-matrix:')
            for i in range(row):
                for j in range(column):
                    print(v[i][j], end=' ')
                print()

        if column != len(v[0])-1 and row < len(v)-1:
                print('Top-right sub-matrix:')
                for i in range(row):
                    for j in range(column+1, len(v[0])):
                        print(v[i][j], end=' ')
                    print()
            
        if column > 0 and row < len(v)-1:
            print('Bottom-left sub-matrix:')
            for i in range(row+1, len(v)):
                for j in range(column):
                    print(v[i][j], end=' ')
                print()

        if column != len(v[0])-1 and row < len(v)-1:
            print('Bottom-right sub-matrix:')
            for i in range(row+1, len(v)):
                for j in range(column+1, len(v[0])):
                    print(v[i][j], end=' ')
                print()

        print('----------------')

for i in range(len(v)):
    for j in range(len(v[0])):
        if v[i][j] == n:
            print_matrix(i, j)