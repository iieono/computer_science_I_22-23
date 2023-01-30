x = input("Enter a string without spaces: ").lower()
xArray = list(x)

def isPalindrome():
    for i in range(len(xArray) // 2):
        if xArray[i] != xArray[-(i+1)]:
            return ("Not palindrome!")
        else:
            return ("Palindrome!")

print(isPalindrome())