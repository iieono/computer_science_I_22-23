lst = []
with open('ex5 data.txt') as f:
    lst = f.readlines()
lst = [item.split() for item in lst]

# city1 = input('Enter 1st city: ')
# city2 = input('Enter 2nd city: ')
city1 = 'TOR'
city2 = 'PAL'

for i in lst:
    if i[1] == city1 and i[2] == city2:
        print('Direct Flight:')
        print(*i)
    elif i[1] == city1:
        for j in lst:
            if j[2] == city2 and float(j[3]) > float(i[4]) and j[1] != city1:
                print('Flight with stop(s):')
                print(*i)
                print(*j)

