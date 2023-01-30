full_text = ''
with open('ex1 data.txt') as f:
    full_text = f.read()


numbers = []
number = ''
for i in full_text :
    if i == ' ' or i == '\n':
        if number != '':
            numbers.append(int(number))
            number = ''
    else :
        number = number + i
print(numbers)

print(f'Number of values: {len(numbers)}')
print(f'Overall sum: {sum(numbers)}')
print(f'Maximum value: {max(numbers)}')
print(f'Minimum value: {min(numbers)}')
