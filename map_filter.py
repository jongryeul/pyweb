int_numbers = range(-5, 6)
f = filter(lambda x: x * 2, int_numbers)
m = map(lambda x: x * 2, int_numbers)

print("f=", list(f))
   # f= [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
   # filter는 True 인것만 출력(0은 false이므로 제외)
print("m=", list(m))
   # m= [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]