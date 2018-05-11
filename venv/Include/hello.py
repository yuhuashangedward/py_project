# import sys
# print(sys.argv)
#
# name="wupeiqi"
# print(name)
#
# # !/usr/bin/env python
# # -*- coding:utf-8 -*-
# name1=raw_input("请输入用户名：")
#
# #打印输入的内容
# print(name1)

# 输入密码，不想可见，需要利用getpass模块中的getpass方法，即：
import getpass
# 将用户输入的内容赋值给name变量
pwd=getpass.getpass("请输入密码：")
# 打印输出的内容
print(pwd)
