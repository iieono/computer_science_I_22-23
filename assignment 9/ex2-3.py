s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

res = list(s1)
for i in list(s1):
    for k in list(s2):
        if k == i:
            res.remove(i)
print("".join(res))