x = int(input("Enter a positive number: ")) 

def isPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
            break
    return True

while x > 1:
    if isPrime(x):
        primes = []
        for i in range(2, x+1):
            if isPrime(i):
                primes.append(i)
        print(f'The prime numbers <= {x} are :', end=' ')
        print(*primes, sep=' ')
        break

    x = int(input("Enter a positive number: "))    