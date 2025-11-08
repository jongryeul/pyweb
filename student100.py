#다음의 성(family name)과 이름을 이용하여 임의의 
# 학생데이터 100개를 test.db.Student 테이블에 insert 하시오.

# fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
# first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")

import sqlite3
import random

fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")

first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")

def make_name():
  sung = random.choice(fam_names)   #type:string
  #name = random.sample(first_names, 2)  #type:list
  name = "".join(random.sample(first_names, 2))
  
  #return sung + name  => 리스트 형식
  return (sung + name, ) #=>튜플형식
     #executemany()는 다음과 같은 형태의 “튜플 리스트” 를 인자로 받아야 합니다.
     # cur.executemany(sql, [("홍길동",), ("이순신",), ("강감찬",)])

#print(make_name())  #typeError: can only concatenate str (not "list") to str
      # 리스트를 문자열로 변환하기
      # a = "Hello "
      # b = ["World"]
      # print(a + "".join(b))
#exit()

data = []
for i in range(0, 100):
  data.append(make_name())

# print(data)
# exit()

conn = sqlite3.connect("test.db")

with conn:
  cur = conn.cursor()
  sql = "insert into Student(name) values(?)"
  cur.executemany(sql, data)

  conn.commit()
