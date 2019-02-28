# 四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
count = 0
for i in range(1,5):
    for k in range(1,5):
        for j in range(1,5):
            if i != k and i != j and k!=j:
                print('%d%d%d'%(i,k,j))
                count += 1
print('共计有',count)