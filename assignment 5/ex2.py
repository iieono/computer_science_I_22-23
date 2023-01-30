n = int(input('Input n: '))
v = []
if n > 0 and n <= 100:
    for i in range(n):
        number = int(input(f'Input v[{i}]: '))
        v.append(number)
    continu = True
    while continu == True:
        x = int(input('Input x: '))
        count = 0
        for i in v:
            if i == x:
                count += 1
        print(f'Value {x} appears {count} time(s) in the array.')
        count = 0
        continu = bool(int(input('Would you like to continue (1=yes, 0=no)? ')))

else:
    print('Input invalid!')
print('Program terminated.')
