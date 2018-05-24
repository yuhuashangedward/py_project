count = 0
while count < 3:
    user = input('>>>')
    pwd = input('>>>')
    if user == 'alex' and pwd == '123':
        print('欢迎登录')
        print('.........')
        break
    else:
        print('用户名或密码错误')
    count = count + 1
