# test = "edward"
# print(test.capitalize())
#
# test1 = "WTO"
# print(test1.casefold())
# print(test1.lower())
#
# test2 = "Ⅱ"
# print(test2.casefold())
# print(test2.lower())
#
# # 德语中符号 变小写用casefold
# test3 = 'ß'
# print(test3.casefold())
# print(test3.lower())

# test = "edward"
# print(test.center(30,"中"))
# print(test.center(3,"文"));
# print(test.center(7,"哈"))

# test = "We are committed to maintaining EOS Platform and making positive contributions to its community."
# print(test.count('mm'))
#
# print(test.encode("utf-8"))
# print(test.decode("gbk"))

# coding:utf-8
# test = "中国"
# print(u'utf-8格式：',test)
# test1 = test.decode('utf-8')
# print(u'unicode格式：',test1)

# # str -> bytes: encode编码
# # bytes -> str: decode解码
# test = '我是superman'
# print(test)
# print(type(test))
# bytesText = test.encode()
# print(bytesText)
# print(type(bytesText))
# test2 = bytesText.decode(encoding="utf-8",errors="strict")
# print(test2)
# print(type(test2))

# test = "Cardano is a decentralised public blockchain and cryptocurrency project and is fully open source. "
# isStart = test.startswith("Cardano")
# print(isStart)
# isEnd = test.endswith("source")
# print(isEnd)

test = "this is \tstring exzample ... wow!!!!"
test1 = test.expandtabs()
test2 = test.expandtabs(16)
print("原字符串" + test, len(test))
print('替换\\t符号：' + test1,len(test1))
print("使用16个空格替换\\t符号：" + test2, len(test2))

demo = "this is a dynamicworld\t. Do you think so"
demo1 = demo.expandtabs()
demo2 = demo.expandtabs(16)
print(demo, len(demo))
print(demo1, len(demo1))
print(demo2, len(demo2))

exzamp = "he\tllo"
exzamp1 = exzamp.expandtabs()
exzamp2 = exzamp.expandtabs(16)
print(exzamp, len(exzamp))
print(exzamp1, len(exzamp1))
print(exzamp2, len(exzamp2))