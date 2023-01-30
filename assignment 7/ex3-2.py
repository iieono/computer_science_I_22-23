m1=[[0, 1, 2], 
    [5, 6, 7],
    [5, 3, 4]]

m2=[[4, 3, 2, 1], 
    [9, 8, 7, 2], 
    [0, 1, 2, 4]]

m3=[]

# r x C = R x c

if(len(m1[0]) == len(m2)):

    for i in range(len(m1)):
        row = []
        for j in range(len(m2[0])):
            product = 0

            for k in range(len(m1[i])):
                product += m1[i][k] * m2[k][j]
            row.append(product)
            
        m3.append(row)

    for e in m3:
        print(*e, sep=', ')
        print
else:
    print('Not eligible')
