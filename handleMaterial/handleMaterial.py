
# coding=utf-8 

# 【本程序使用前提必须 xx1.txt、xx2.txt 等的单字完全一样，字数一样】

import os
import os.path #文件夹遍历函数  
#获取目标文件夹的路径
filedir = 'data'
#获取当前文件夹中的文件名称列表  
filenames=os.listdir(filedir)
#打开当前目录下的result.txt文件，如果没有则创建
f = open('result.txt', 'w', encoding='utf-8')


dictList = []

#先遍历所有文件
for filename in filenames:
    filepath = filedir + '/' + filename
    for inx, line in enumerate(open(filepath, encoding='utf-8')):
        if (len(line.split())==2):
            dictList.append((inx, filename, line.split()[0], line.split()[1]))
        else:
            dictList.append((inx, filename, line.split()[0], '（无）'))

totalchar = len(list(filter(lambda x: x[1] == filenames[0], dictList)))

# 显示函数
def  showData(first, final):
    for i in range(len(filenames)):
        for j in range(first, final):
            newlist = list(filter(lambda x: x[0] == j, dictList))
            if(i == 0): 
                if(j==first): f.writelines('-')
                f.writelines('\t' + newlist[i][2])
        
        f.write('\n' + filenames[i].replace('.txt','') + '\t')

        for j in range(first, final):
            newlist = list(filter(lambda x: x[0] == j, dictList))
            f.writelines(newlist[i][3] + '\t')


step = 8 # 每多少字换行

for i in range(0, totalchar, step):
    if(totalchar-i<step):
        showData(i, totalchar)
    else:
        showData(i, i + step)
    f.write('\n')

print('成功输出，每'+ str(step) +'字换行')

#关闭文件
f.close()

