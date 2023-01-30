x = input("Enter a line: ")
res = []
for i in x.split(' '):
    res.append(i.capitalize())
print(' '.join(res))
