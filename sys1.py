# 다음은 Try this 내용
# 터미널에서 
# $> python sys1.py

# import mysis
# mysis.clear()

from mysis import clear
clear()
#++++++++++++++++++++++++++++++++++++++

import sys

print(sys.argv, len(sys.argv))

sa = sys.argv
if len(sa) <2 :
    sys.exit()

with open(sa[1], "r", encoding='utf-8') as file:
    for line in file:
        print(line)

## sys.argv 설명(from Chat_gpt)
# sys.argv는 **파이썬 스크립트를 실행할 때 전달된 명령줄 인자(arguments)**를
# 리스트(list) 형태로 담고 있는 변수입니다.
# 즉, 터미널이나 명령 프롬프트에서 파이썬 파일을 실행할 때 입력한
# 인자값들을 읽을 수 있게 해주는 기능이에요.

# 📘 기본 개념
# (python)
# import sys
# print(sys.argv)

# 실행 예시: 
# (bash)
# python test.py hello world 123

# 출력:
# ['test.py', 'hello', 'world', '123']

# 🔍 설명

# sys.argv[0] → 실행된 파이썬 파일 이름
# sys.argv[1] 이후 → 실행 시 입력한 인자들

# 예를 들어:
# (python)
# import sys
# print("스크립트 이름:", sys.argv[0])
# print("첫 번째 인자:", sys.argv[1])
# print("두 번째 인자:", sys.argv[2])

# 실행:
# (bash)
# python test.py apple banana

# 출력:
# 스크립트 이름: test.py
# 첫 번째 인자: apple
# 두 번째 인자: banana

# 🧠 활용 예시
# 1️⃣ 간단한 계산기 예제
# # calc.py
# import sys

# x = int(sys.argv[1])
# y = int(sys.argv[2])
# print("합계:", x + y)

# 실행:
# python calc.py 3 5

# 결과:
# 합계: 8

# ⚠️ 주의

# sys.argv는 문자열 리스트이므로, 숫자를 쓸 때는 int()로 변환해야 합니다.
# 인자를 입력하지 않으면 IndexError가 발생하므로 예외 처리를 해주는 것이 좋습니다.

# 예:
# if len(sys.argv) < 3:
#     print("사용법: python calc.py <num1> <num2>")
#     sys.exit()


