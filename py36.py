# coding=utf-8

# 求100之内的素数。

arr = []
s = 0
for i in range(2, 100):
  for j in range(2, i - 1):
    if (i % j == 0):
      break
  else:
    arr.append(i)
    s += i

# python for 循环存在else  当for循环完整执行之后执行else
print(arr)
print(s)
