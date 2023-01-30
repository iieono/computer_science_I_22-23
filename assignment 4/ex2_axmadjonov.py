n = int(input("Enter a number: "))

if n > 0:
    #first
    for i in range(n, 0, -1):
        print("*"*i)
    print()

    #second
    for i in range(0, n):
        print(f"{' '*i}{'*'*n}")
    print()

    #third
    for i in range(1,n+1):
        if (i==1 or i==n):
            print("*" * n)
        else:
            print("*" + " " * (n-2) + '*')
    print()

    #fourth
    for i in range(1, n+1):
        print(f"{'-'*(i-1)}*{'+'*(n-i)}")
    print()

    #fifth
    for i in range(n):
        for j in range(n):
            if (i == j or j == n - 1 - i):
                print('*', end='')
            else:
                print(' ', end='')
        print()
    print()





