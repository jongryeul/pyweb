
def input_calc():

  def plus(a, b):
    return a + b 

  def minus(a, b):
    return a - b

  def mul(a, b):
    return a * b

  def div(a, b):
    if b == 0:
      return a
    
    return a / b

  cmd = input("수식을 입력 하세요(usage: 2 + 3)> ")

  cmds = cmd.split(' ')

  # a = cmds[0]
  # op = cmds[1]
  # b = cmds[2]

  # Todo cmds 하나만으로 set해보기!!   => ctrl+shift+ F(검색)
  # a, op, b = int(cmds[0]), cmds[1], int(cmds[2])
  a, op, b = cmds
  a, b = int(a), int(b)

  if op == '+':
    r = plus(a, b)

  elif op == '-':
    r = minus(a, b)

  elif op == '*':
    r = mul(a, b)

  else:
    r = div(a, b)

  #print("Answer is " + r)  # 문자형 + int형  
  if op in '+-*':
    print("Answer is {:d}".format(r))

  else:
    print("Answer is {:.2f}".format(r))

while(True):
  input_calc()