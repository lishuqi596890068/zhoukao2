# 编写一个函数，判断一个字符串是否为回文，如果是回文返回整数1，否则返回返 回整数0（20分）
# 	回文：就是前后对称。例如：”abba”，”evilolive”是回文，”abxd”和”efga”不是回文。
# 1)参数和返回值定义正确(5分)
# 2）正确实现功能(10分)
# 3)进行功能测试(5分)
def hui(str):
    if len(str)%2==0:
        num = len(str)
        num = num//2
        print(str[:num])
        print(str[:num-1:-1])
        if str[:num] == str[:num-1:-1]:
            return 1
        else:
            return 0
    else:
        num = len(str)
        num = num//2
        if str[:num] == str[:num:-1]:
            return 1
        else:
            return 0
s = input("请输入一个字符串判断是否是回文")
print(hui(s))
