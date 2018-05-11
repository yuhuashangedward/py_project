# coding:utf-8
# while True:
#     number = int(input('请输入数字'))
#     if number == 7:
#         continue
#     elif number >10:
#         exit()
#     print(number)

import time
a = 1
while True:
    print(a)
    time.sleep(0.5)
    if a == 6:
        a = a+1
    elif a == 10:
        break
    a = a + 1

