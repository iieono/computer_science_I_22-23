lst = []
with open('ex3 report.txt') as f:
    lst = f.readlines()
lst = [item.split() for item in lst]
res = {}

for i in lst:
    if i[1] in res:
        a, b = res[i[1]].split(',')
        a = float(a) + float(i[2])
        b = int(b) + 1
        d = f'{a},{b}'
        res[i[1]] = d
    else:
        r = f'{i[2]},{1}'
        res[i[1]] = r

with open('ex3 report result.txt', 'w') as file:
    for k in res.keys():
        i, j = res[k].split(',')
        output = ' '.join( (k, j, str(round(float(i), 2)), str( round( float(i) / float(j), 2 ) )) )

        file.write(f'{output}\n')
