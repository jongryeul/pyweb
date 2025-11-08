
cmd = input("input(usage: 이름,나이,성별)>> ")
print(cmd)

error_msg = "정확히 입력해 주세요!!!"

# 1. 값이 존재여부 체크
if cmd == '':
  print(error_msg)
  exit()

# 2. ,가 있는지 체크(3가지)
#  1)if ',' not in cmd:
#  2)if cmd.find(',') == -1:   # -1은 없다 의미
#  3)
isExistsComma = False
for i in cmd:
  if i == ',':
    isExistsComma = True
    break
if isExistsComma == False:
  print(error_msg)
  exit()

cmds = cmd.split(',')
# 3. 3개의 값이 있는지
if len(cmds) != 3:
  print(error_msg)
  exit()




outmsg = "당신의 이름은 {}, 나이는 {}, 성별은 {} 입니다."
print(outmsg.format(cmds[0],cmds[1],cmds[2]))

# 참고) 실행시 한글깨짐 현상경우; nodemon의문자 인코딩 문제임!!!
# 1.more.py가 있는 폴더에 nodemon.json 파일생성(해당파일 내용 참조)
# 2.실행방법은;
#   bash) npx nodemon try_this_input.py

