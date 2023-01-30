base = [1, -2,  3,  4, -5]
exp = [4,  3,  2,  3,  2]

power = []

for i in range(len(base)):
    curr_power = base[i]
    for j in range(exp[i]-1):
        curr_power = curr_power * base[i]
    power.append(curr_power)

print(power)






