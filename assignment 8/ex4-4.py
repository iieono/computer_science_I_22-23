columns = int(input("Input the number of elements: "))
rows = int(input("Input the size of elements: "))

def internal(num):
    print('|', end='')
    for i in range(num):
        print('  |', end='')
    print()
        
def external(num):
    print('+', end='')
    for i in range(num):
        print('--+', end='')
    print()

if columns > 0 and rows > 0:
    external(columns)
    for i in range(rows):
        internal(columns)
    external(columns)
else:
    print("Not valid")
