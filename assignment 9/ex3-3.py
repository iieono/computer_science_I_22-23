x = input("Enter a character: ")
words = []
wordWith = ''
if len(x) == 1:
    word = input("Enter a word: ")
    while word != 'stop':
        words.append(word)
        word = input("Enter a word: ")

    count_most = 0
    for i in (words):
        count = 0
        for j in list(i):
            if j == x:
                count += 1
        if count > count_most:
            count_most = count
            wordWith = i
    print(f'The word with the most "{x}" is "{wordWith}"')
else:
    print('Wrong!')

