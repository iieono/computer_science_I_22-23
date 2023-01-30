for i in range(10):
    for j in range(10):
        print(f"({i},{j})", end="\t")
    print()


for i in range(100):
    if i % 10 == 0:
        print()
    print(i, end="\t")