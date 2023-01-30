v = [4, 6, 5, 2, 8, 11, 10, 9, 28, 3]
odd_numbers = []
even_numbers = []
for i in v:
    if i % 2 == 1:
        odd_numbers.append(i)
    else:
        even_numbers.append(i)

print(odd_numbers)
print(even_numbers)
