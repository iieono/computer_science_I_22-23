students = {}
marks = {}
with open('ex4 students.txt') as f:
    for i in f.readlines():
        students[i.strip().split(' ', 1)[0]] = i.strip().split(' ', 1)[1]

with open('ex4 marks.txt') as f:
    for i in f.readlines():
        marks[i.strip().split(' ', 1)[0]] = i.strip().split(' ', 1)[1]

for i in students.keys():
    mark1, mark2 = marks[students[i]].split(' ')
    average = round((int(mark1) + int (mark2)) / 2)
    print(i, end=' ')
    if int(mark1) < 15 or int(mark2) < 15 or average < 18:
        print('FAIL')
    else:
        print(average)
