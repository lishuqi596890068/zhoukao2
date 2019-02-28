# 2.	读入文件‘a.txt’.统计文件中每个单词的数量并且进行输出。
# txt的文本文件为
# a.	Every single time you access a website, you leave tracks.
# Tracks that others can access. If you don't like the idea,
# find out what software can help you cover them
with open('a.txt','w') as f:
    f.write('Every single time you access a website, you leave tracks. Tracks that others can access. If you dont like the idea, '
            'find out what software can help you cover them')
with open('a.txt','r') as f:
    dict = {}
    conten = f.read()
    conten = conten.split(' ')
    print(conten)
    for temp in conten:
        key = dict.get(temp)
        if key == None:
            dict[temp] = 1
        else:
            dict[temp] += 1
    print(dict)


