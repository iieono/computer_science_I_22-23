v = []
n = int(input('Enter a positive value: '))
while len(v) < 200 and n > 0:
    v.append(n)
    n = int(input('Enter a positive value: '))
vn = []
for i in v:
    if i not in vn:
        vn.append(i)
print(vn)
