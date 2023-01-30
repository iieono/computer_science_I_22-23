num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
num4 = int(input("Enter 4th number: "))

def fraction_sign(num1, num2):
    if num1 < 0 and num2 < 0:
        return abs(num1), abs(num2)
    elif num1 > 0 and num2 < 0:
        return  num1 * -1, abs(num2)
    else :
        return num1, num2

num1, num2 = fraction_sign(num1, num2)
num3, num4 = fraction_sign(num3, num4)

print(f'{num1}/{num2} + {num3}/{num4}')

res1, res2 = num1*num4 + num3*num2, num2 * num4

def reduceFrac(a, b):
    i = 2
    while i < min(abs(a), abs(b)) + 1:
        if a % i == 0 and b:
            a = a // i
            b = b // i
        else: i += 1
    return a, b

res1, res2 = reduceFrac(res1, res2)

print(f'{res1}/{res2}')

