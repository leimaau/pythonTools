import re
from opencc import OpenCC
cc = OpenCC('t2s')
cc2 = OpenCC('s2t')

article = open('input.txt', encoding='utf-8')
out = open('output.txt', 'w', encoding='utf-8')

for paragraph in article.readlines():
    try:
        line = paragraph.replace(' ','<space>').split()[0]
    except:
        continue

    sentences = line.split()
    for prose in sentences:
        #out.write(prose.replace('<space>',' ')+'\n')
        
        #s = cc.convert(prose.replace('<space>',' '))
        #out.write(s+'\n')
        s2 = cc2.convert(prose.replace('<space>',' '))
        out.write(s2+'\n')

article.close()
out.close()
