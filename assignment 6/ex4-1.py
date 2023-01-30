v = [ 10, 20, 30, 40, 50, 60, 70, 80 ]

for i in range(len(v)):
    if i == len(v)-2:
        print(f'Triplet {i+1}: {v[i]} + {v[i+1]} + {v[0]} = {v[i]+v[i+1]+v[0]}')
        continue
    elif i == len(v)-1:
        print(f'Triplet {i+1}: {v[i]} + {v[0]} + {v[1]} = {v[i]+v[0]+v[1]}')
        continue
    print(f'Triplet {i+1}: {v[i]} + {v[i+1]} + {v[i+2]} = {v[i]+v[i+1]+v[i+2]}')