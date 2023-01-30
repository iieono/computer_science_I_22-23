n = int(input("Enter number of rows: "))
num = 1

for i in range(1, n+1):
    for j in range(1, i+1):
        print(num, end=' ')
        num = num + 1
    print()

m = int(input("Enter max number: "))
line_break = 1
add = 2

for i in range(1, m+1):
    print(i, end=' ')
    if i == line_break:
        print()
        line_break = line_break + add
        add += 1
