# test = "Cardano is developing a smart contract platform which seeks to deliver more advanced features than any protocol previously developed"
# # 存在返回下标
# r1 = test.find('seeks')
# # 不存在返回-1
# r2 = test.find('wonderful')
# print(r1)
# print(r2)
#
# r3 = test.index('seeks')
# r4 = test.index('wonderful')
# print(r3)
# print(r4)

# test1 = "The development {org} consists of a large global collective of expert {res} and researchers"
# # 格式化1：format()
# r1 = test1.format(org = 'team', res = 'engineers')
# print(r1)
# # 格式化2：format()
# test2 = "The development {0} consists of a large global collective of expert {1} and researchers"
# r2 = test2.format('team', 'engineers')
# print(r2)
# # 格式化3：format_map()
# test3 = "The development {org} consists of a large global collective of expert {res} and researchers"
# r3 = test3.format_map({"org":'team', 'res':'engineers'})
# print(r3)

# test = "nameEdwardage20"
# # 是否为数字 True
# r1 = test.isalnum()
# print(r1)
# # 是否为字母 False
# r2 = test.isalpha()
# print(r2)
#
# test1 = "nameage"
# # 是否为数字 True
# r11 = test1.isalnum()
# print(r11)
# # 是否为字母 False
# r12 = test1.isalpha()
# print(r12)
#
# test2 = "123456789"
# # 是否为数字 True
# r21 = test2.isalnum()
# print(r21)
# # 是否为字母 False
# r22 = test2.isalpha()
# print(r22)
#
# demo = "中国"
# dd = demo.isalpha()
# print(dd)
# d1 = demo.isalnum()
# print(d1)

# test = "123456"
# r1 = test.isdecimal()
# r2 = test.isdigit()
# r3 = test.isnumeric()
# print(r1, r2, r3)
#
# test1 = "456hello"
# r11 = test1.isdecimal()
# r12 = test1.isdigit()
# r13 = test1.isnumeric()
# print(r11, r12, r13)
#
# test2 = "二"
# r21 = test2.isdecimal()
# r22 = test2.isdigit()
# r23 = test2.isnumeric()
# print(r21, r22, r23)
#
# test3 = "②"
# r31 = test3.isdecimal()
# r32 = test3.isdigit()
# r33 = test3.isnumeric()
# print(r31, r32, r33)
#
# test4 = "Ⅱ"
# r41 = test4.isdecimal()
# r42 = test4.isdigit()
# r43 = test4.isnumeric()
# print(r41, r42, r43)

# test = "It is the first blockchain platform to evolve out of a scientific philosophy and a research-first driven approach."
# print(test.isprintable())
# test1 = "small\t"
# print(test1.isprintable())
# test2 = "big\n"
# print(test2.isprintable())

# test = "    "
# print(test.isspace())
# test1 = ""
# print(test1.isspace())

# test = "Explore a timeline showing the development of the project, and learn more about its goals and vision."
# print(test.istitle())
# test1 = "GET STARTED WITH CARDANO"
# print(test1.istitle())
# test2 = "The Daedalus Wallet"
# print(test2.istitle())

# test = "你是风儿我是沙"
# t = "  "
# r = t.join(test)
# print(r)
#
# test1 = "Ethereum Classic and Bitcoin support."
# t1 = "ETH"
# r1 = t1.join(test1)
# print(r1)