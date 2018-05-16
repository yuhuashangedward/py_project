# 求1-100内的所有数的和
number = list(range(1,101))
sum = 0
for i in number:
    sum = sum + i
print(sum)

start = 1
summ = 0;
max_num = input('The max number add is:')
while start <= int(max_num):
    summ = summ + start
    start += 1
print(summ)
