v = [[2.6, 4.4, 5.0], [4.8, 3.4, 7.2], [2.0, 2.6, 3.8]]

ready_list = []

for i in range(len(v)):
    ready_list.append(v[i])
    if i+1 == len(v): break

    insert_list =[]
    for j in range(len(v[0])):

        insert_list.append( round( (v[i][j] + v[i+1][j]) / 2, 2 ) )
    ready_list.append(insert_list)

for i in ready_list:
    print(*i, sep=' ')

