# # p_s = {'szw', 'lcg', 'lnh'}
# # l_s = {'szw', 'zws'}
# # print(p_s.intersection(l_s))
#
# # p_s = {'szw', 'lcg', 'lnh'}
# # l_s = {'szw', 'zws', 'sb'}
# # print(p_s.union(l_s))
#
# # p_s = {'szw', 'lcg', 'lnh'}
# # l_s = {'szw', 'zws', 'sb'}
# #
# # print(p_s.difference(l_s))
# # print(p_s-l_s)
#
#
#
#
# # p_s = {'szw', 'lcg', 'lnh'}
# # l_s = {'szw', 'zws', 'sb'}
# # ### p_s = p_s.difference(l_s)
# # print(p_s.difference_update(l_s))
# # print(p_s)
# #
# #
# # p_s = {'szw', 'lcg', 'lnh'}
# # l_s = {'szw', 'zws', 'sb'}
# # print(p_s.isdisjoint(l_s))
#
#
# # p_s = {'szw', 'lcg', 'lnh', 'zws', 'sb'}
# # l_s = {'szw', 'zws', 'sb'}
# # print(p_s.issubset(l_s))
# # print(l_s.issubset(p_s))
#
# #
# # p_s = {'szw', 'lcg', 'lnh', 'zws', 'sb'}
# # l_s = {'szw', 'zws', 'sb'}
# # print(p_s.issuperset(l_s))
# # # print(l_s.issuperset(p_s))
#
# s1 = {1, 2, 4}
#
# s2 = {1, 2, 3}
#
# s1.update(s2)
#
# print(s1)
#
# s = forzenset('hello')
#
#
# names = ['alex', 'alex', 'wupeiqi']
# names = list(set(names))
# print(names)
#
# msg = "i am \033[42;1m%(name)+60s\033[0m my hobby is alex" %{"name":"lhf"}
# print(msg)
#
# print('root','x','0','0',sep=':')

# tpl = "i am {}, age {}".format("Steven", 18)
# print(tpl)

# tpl = "i am {1}, age {0}".format("Steven", 18)
# print(tpl)

# tpl = "i am {name}, age {age}".format(name="Steven", age=18)
# print(tpl)
#
# tpl = "i am {name}, age {age}".format(**{"name":"Steven", "age":18})
# print(tpl)

# tpl = "i am {0[0]}, age {0[1]}, really {0[2]}".format([1, 2, 3], [11, 22, 33])
# print(tpl)
#
# tpl = "i am {:s}, age {:d}, really {:f}".format("seven", 18, 6876.67)
# print(tpl)
#
# tpl = "i am {:s}, age {:d}, really {:f}".format(*["seven", 18, 6876.67])
# print(tpl)

tpl = "numbers: {:b}, {:o}, {:d}, {:x}, {:X}, {:%}".format(15, 15, 10, 16, 12, 12.534)
print(tpl)