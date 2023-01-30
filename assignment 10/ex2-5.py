full_text = ''
with open('ex2 data.txt') as f:
    full_text = f.read()
# print(full_text)

punctuations = '!"#$%&\'()*+, -./:;<=>?@[\]^_`{|}~'

row_count = 1
char_count = len(full_text)
digit_count = 0
cap_letter_count = 0
small_letter_count = 0
spacing_count = 0
punctuation_count = 0
other = 0

for i in full_text:
    if i.isdigit():
        digit_count +=1
    elif i.isupper():
        cap_letter_count += 1
    elif i.isalpha():
        small_letter_count += 1
    elif i == ' ' or i == '\n' or i == '\t':
        spacing_count += 1
        if i == '\n':
            row_count += 1
    elif i in punctuations :
        punctuation_count += 1
    else:
        other += 1

print("row_count" , row_count)
print("char_count", char_count)
print("digit_count" , digit_count)
print("cap_letter_count" , cap_letter_count)
print("small_letter_count" , small_letter_count)
print("spacing_count" , spacing_count)
print("punctuation_count" , punctuation_count)
print("other" , other)
