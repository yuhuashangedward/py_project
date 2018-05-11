# 根据用户输入内容打印其权限
# alex-->超级管理员
# eric-->普通管理员
# tony,,rain -->业务主管
# 其他-->普通用户

name = input("请输入用户名：")

if name == "alex":
    print("超级管理员")
elif name =="eirc":
    print("普通管理员")
elif name =="tony" or name == "rain":
    print("业务主管")
else:
    print("普通用户")

# 1、 基本循环
# while 条件：
#   循环体
#   如果条件为真，那么循环体执行
#   如果条件为假，那么循环体不执行

# 2、break
# break用于退出所有循环
#   while True:
#         print('123')
#         break
#         print('456')

# Continue
# continue用于退出当前循环，继续下一次循环
# while True:
#       print('123')
#       continue
#       print('345')

