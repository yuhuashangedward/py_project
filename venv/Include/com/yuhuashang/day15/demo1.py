# name = "zhangsan"
#
# def change_name():
#     print('我的名字', name)
#
# change_name()

# name = "zhangsan"
#
#
# def change_name():
#     name = "lisi"
#     print('我的名字', name)
#
#
# change_name()
# print(name)

name = "zhangsan"


def change_name():
    global name
    name = "lisi"
    print('我的名字', name)


change_name()
print(name)