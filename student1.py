from functools import reduce

g_grades = ['A','B','C','D','F']
g_grades.reverse()

class Student:
    grade = ''
    def __init__(self, line):
        name, gender, age, score = line.strip().split(',')
        self.name = name
        self.gender = gender
        self.age = age
        self.score = int(score)

    def __str__(self):
        return "{}**\t{}\t{}\t{}".format(self.name[0], self.gender, self.age, self.grade)

    def make_grade(self):
        if self.score == 100:
            self.grade = 'A+'
        else:
            self.grade = g_grades[self.score // 10 - 5]

students = []  
with open('students.csv', 'r') as file:
    for i, line in enumerate(file):
        if i == 0: continue    # 제목줄 삭제
        students.append(Student(line))

students.sort(key = lambda stu: stu.score, reverse= True)
m = map(lambda stu: stu.make_grade(), students)
list(m)   # m은 map의 어드레스값임

def sumfn(x, y):
    if type(x) == int:  # x값이 연산한 결과의 값이면
        return x + y.score
    else:
        return x.score + y.score

# total = reduce(lambda x, y: (x if type(x) == int else x.score) + y.score, students)
total = reduce(sumfn, students)   # reduce1.py 참고요!!!
avg = total / len(students)
print("총계, 평균>>>", total, avg)


print("이름\t성별\t나이\t학점")
print("----\t----\t----\t----")

for s in students:
    print(s)

print("-------------------------")
for s in students:
    if s.score >= avg:
        print(s.name, s.score)