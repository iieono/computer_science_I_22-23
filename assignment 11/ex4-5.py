births = {}
lst = []
with open('ex4 births.txt') as b:
    lst = b.read().split('\n')
for i in range(len(lst)):
    if i % 2 == 0:
        births[lst[i]] = lst[i+1]
print(births)

deaths = {}
lst = []
with open('ex4 deaths.txt') as d:
    lst = d.read().split('\n')
for i in range(len(lst)):
    if i % 2 == 0:
        deaths[lst[i]] = lst[i+1]
print(deaths)

with open('ex4 lives.txt', 'w') as l:
    for i in births.keys():
        l.write(f'{i} {births[i]} {deaths[i]}\n')



