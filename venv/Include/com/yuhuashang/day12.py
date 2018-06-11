import sys
print(sys.getdefaultencoding())

test = "HelloWorld"
for item in test:
    print(item)
dd = "*"
res = dd.join(test)
print(res)

print(test[0:-1])