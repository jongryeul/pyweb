class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # def __str__(self):
    #     return "{}:{}".format(self.name, self.score)
    
students = [
    Student("김일수", 10),
    Student("김삼수", 30),
    Student("김이수", 20)
]
print(students[0])
    #<__main__.Student object at 0x00000261699F4590> => 6,7줄이 없을경우
    # 김일수:10   => 6,7줄 있을경우    