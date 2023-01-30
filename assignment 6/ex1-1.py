v = [18, 11, -4, 5, 0, 0, -2, 3, 25, 0]
vp = []
vn = []

for i in v:
    if i > 0:
        vp.append(i)
    elif i < 0:
        vn.append(i)
    else:
        continue
print(vp)
print(vn)