##
# students.csv읽기
# 데이터 변환
# 저장
# select

import sqlite3
from Student import Student

params = []
with open('students.csv', 'r', encoding='utf-8') as file:
    for i, line in enumerate(file):
        if i == 0: continue
        stu = Student(line)
        t = stu.make_params()
        print(type(t), list(t))
        params.append(t)

conn = sqlite3.connect("exam.db")

def insert_data():
    with conn:
        cur = conn.cursor()
        sql = "insert into Student(name, gender, age, grade, addr) values(?,?,?,?,?)"
        cur.executemany(sql, params)

        conn.commit()

def select_data():
    with conn:
        cur = conn.cursor()
        sql = """select id, name, gender, age, grade, addr
                    from Student order by substr(grade,1,1), grade desc"""
                # SUBSTR(문자열, 시작위치, 길이)
                # → 문자열의 **일부분(부분 문자열)**을 잘라냅니다.

                # SUBSTR(grade, 1, 1)
                # → grade의 첫 번째 문자만 추출합니다.
                # (SQL에서는 인덱스가 1부터 시작)

                # 예:
                # grade	SUBSTR(grade,1,1)
                # A+	A
                # A0	A
                # B+	B
                # C0	C

        #print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)

select_data()
#insert_data()
