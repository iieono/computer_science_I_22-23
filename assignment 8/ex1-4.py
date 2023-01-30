numerator = int(input("Enter the numerator: ")) 
denominator = int(input("Enter the denominator: ")) 

def find_greatest_common(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(up, down):
    if down == 0:
        return "0 not possible"

    common_divisor = find_greatest_common(up, down)
    (reduced_up, reduced_down) = (up / common_divisor, down / common_divisor)

    if reduced_down == 1:
        return f'{numerator}/{denominator} = {reduced_up}'
    elif common_divisor == 1:
        return f'{numerator}/{denominator} is the simplest already'
    else:
        return f'{numerator}/{denominator} = {int(reduced_up)}/{int(reduced_down)}'

print(simplify_fraction(numerator, denominator))