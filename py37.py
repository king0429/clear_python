# coding=utf-8

# 求一个3*3矩阵主对角线元素之和。

arr = []

for i in range(9):
  arr.append(input('请输入一个整数:'))

sum1 = 0
sum2 = 0
for i, val in enumerate(arr):
  if (i != 0 and (i + 1) % 3 == 0):
    print(val, end='\n')
  else:
    print(val, end='    ')
  if (i % 4 == 0):
    sum1 += int(val)

print('左侧对角线和为', sum1)
