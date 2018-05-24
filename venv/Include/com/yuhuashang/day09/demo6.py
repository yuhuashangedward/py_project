sysParam = 3
username = 'eos'
password = '123'
while sysParam >= 1:
    print("请输入用户名：")
    tryUser = input()
    print(tryUser)
    print("请输入密码")
    tryPass = input()
    print(tryPass)

    if tryUser == username:
        if tryPass == password:
            print("登录成功！")
            sysParam = 0
    else:
        print("登录失败！")
        sysParam = sysParam -1

