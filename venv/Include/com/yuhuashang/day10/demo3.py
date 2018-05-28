test = "alEx"
a = test.capitalize()
print(a)
b = test.casefold()
print(b)

c = test.lower()
print(c)

d = test.center(21, "中")
print(d)

e = test.center(20)
print(e)

test1 = "asdadsadsddas"
print(test1.count('sd'))

print(test1.startswith('as'))
print(test1.endswith('es'))

print(test1.find('dd'))

print(test1.find('dd', 5, 15))

print(test1.index('dda'))

print()