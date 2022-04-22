import csv

data = []
for i in range(5):
    data.append([input('course: ')])
    for j in range(4):
        data[i].append(input('date: '))

output = open('/home/jeja/Desktop/projects/exams.csv', 'w')
writer = csv.writer(output)
writer.writerows(data)
