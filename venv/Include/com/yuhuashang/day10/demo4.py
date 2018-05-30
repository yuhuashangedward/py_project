test = "I am {name}, age{t}"
v = test.format(name = 'edward',t=19 )
print(v)

v2 = test.format_map({"name":'Edward',"t":17})
print(v2)

dem = "1232"
r1 = dem.isalnum()
r2 = dem.isalpha()
print(r1)
print(r2)

test1 = "12341526\t9"
vv = test1.expandtabs(6)
print(vv, len(vv))

vvv = test1.expandtabs()
print(vvv,len(vvv))
vvvv = test1.expandtabs(9)
print(vvvv)


