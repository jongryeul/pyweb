from functools import reduce

product = 1
lst = [1,2,3,4]
for num in lst:
    product = product * num
    #print(product)

print("product1>>", product)

product2 = reduce(lambda x, y: x * y, lst)
 # 11줄 = 3~6줄 과 동일(reduce의 기능)
print("product2>>", product2)