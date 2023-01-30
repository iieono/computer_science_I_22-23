y = int(input("Enter a positive number: "))

def n_exp_n(num):
    power = 1
    for j in range(num):
        power = power * num
    return power

x = 0
for i in range(y):
    if n_exp_n(i) < y:
        x = i
    else: 
        break

print(f'Maximum x: {x}')