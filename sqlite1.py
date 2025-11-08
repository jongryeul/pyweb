import sqlite3

conn = sqlite3.connect("test.db")

with conn:
  cur = conn.cursor()

  # 프로그램 처리 속도문제로 인해 ? 사용
  # sql = "select * from Student where id > 1"
  # cur.execute(sql)
  sql ="select * from Student where id=? or name=?"
  cur.execute(sql, (1, '홍길순'))

  rows = cur.fetchall()

  for row in rows:
    print(row)