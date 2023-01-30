x = input("Enter 1st string: ")
y = input("Enter 2nd string: ")
z = input("Enter 3rd string: ")

res = ''
lenY = len(y)
count = 0
for i in range(len(list(x))):
    if count > 0:
        count -= 1
        continue
    if x[i] == y[0]:
        if x[i:i+lenY] == y:
            res += z
            count = len(y)-1
    else:
        res += x[i]
print(f'Resulting string: {res}')
