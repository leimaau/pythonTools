import re
import jieba
import jieba.posseg as pseg
from mytool import jyutping_to_ipa

file_name='data_naamning.txt' # 字词典文件 data_naamning 南宁粤拼; data_gwongzau 广州粤拼
data = open(file_name, encoding='utf-8')

char = []
dictionary = {}
cutwordslist = []

for line in data.readlines():
    char = line.replace(' ','_').split()
    if char[0] in dictionary:
        dictionary[char[0]] = dictionary[char[0]] + '/' + char[1].replace('_',' ')
    else:
        dictionary[char[0]] = char[1].replace('_',' ')

def cutwords(words):
    cutwordslist = []
    result = pseg.cut(words)
    for w in result:
        cutwordslist.append(w.word)
    return cutwordslist

# flag: 0-拼音 1-ipa ; flag2: 0-regstr忽略 1-regstr不忽略 ; n_g: n-南宁型ipa g-广州型ipa
def dealfunc_characters(regstr,prose,flag,flag2,n_g):
    prose_list = list(prose)
    try:
        if re.match(r"" + regstr, prose_list[0]):
            if flag2==1:
                s = prose_list[0]
            else:
                s = ''
        else:
            if flag==1:
                s = jyutping_to_ipa(dictionary[prose_list[0]],n_g)
            else:
                s = dictionary[prose_list[0]]
    except KeyError:
        s = 'ERR'

    for char in prose_list[1::]:
        try:
            if re.match(r"" + regstr, char):
                if flag2==1:
                    s += char
                else:
                    s += ''
            else:
                if flag==1:
                    s += ' '+ jyutping_to_ipa(dictionary[char],n_g)
                else:
                    s += ' '+ dictionary[char]
        except KeyError:
            s += ' '+ 'ERR'
    return s

def dealfunc_phrases(regstr,prose,flag,flag2,n_g):
    prose_list = cutwords(prose)
    try:
        if re.match(r"" + regstr, prose_list[0]):
            if flag2==1:
                s = prose_list[0]
            else:
                s = ''
        else:
            if ' ' in dictionary[prose_list[0]] and '/' in dictionary[prose_list[0]]:
                s = dealfunc_characters(regstr,prose_list[0],flag,flag2,n_g)
            else:
                if flag==1:
                    s = jyutping_to_ipa(dictionary[prose_list[0]],n_g)
                else:
                    s = dictionary[prose_list[0]]
    except KeyError:
        s = dealfunc_characters(regstr,prose_list[0],flag,flag2,n_g)

    for char in prose_list[1::]:
        try:
            if re.match(r"" + regstr, char):
                if flag2==1:
                    s += char
                else:
                    s += ''
            else:
                if ' ' in dictionary[char] and '/' in dictionary[char]:
                    s += ' '+ dealfunc_characters(regstr,char,flag,flag2,n_g)
                else:
                    if flag==1:
                        s += ' '+ jyutping_to_ipa(dictionary[char],n_g)
                    else:
                        s += ' '+ dictionary[char]
        except KeyError:
            s += ' '+ dealfunc_characters(regstr,char,flag,flag2,n_g)
    return s

article = open('input.txt', encoding='utf-8')
out = open('output.txt', 'w', encoding='utf-8')

for paragraph in article.readlines():
    try:
        line = paragraph.replace(' ','<space>').split()[0]
    except:
        continue

    sentences = line.split()
    for prose in sentences:
        out.write(prose.replace('<space>',' '))
        out.write('\n')

        prose = re.sub(r'([\u4e00-\u9fa5]+)([0-9A-Za-z-_]+)',r'\1<space>\2',prose)
        
        s = dealfunc_phrases('[0-9A-Za-z-]|[_,，.。·…?—？!！:：;；“”\[\]<>「」『』【】（）《》、 ]+',prose.replace('<space>',' '),0,1,'n' if file_name == 'data_naamning.txt' else 'g')
        #s = dealfunc_characters('[0-9A-Za-z-]|[_,，.。·…?—？!！:：;；“”\[\]<>「」『』【】（）《》、 ]+',prose.replace('<space>',' '),0,1,'n' if file_name == 'data_naamning.txt' else 'g')
        out.write(s+'\n[')

        s2 = dealfunc_phrases('[0-9A-Za-z-]|[_,，.。·…?—？!！:：;；“”\[\]<>「」『』【】（）《》、 ]+',prose.replace('<space>',' '),1,1,'n' if file_name == 'data_naamning.txt' else 'g')
        #s2 = dealfunc_characters('[0-9A-Za-z-]|[_,，.。·…?—？!！:：;；“”\[\]<>「」『』【】（）《》、 ]+',prose.replace('<space>',' '),1,1,'n' if file_name == 'data_naamning.txt' else 'g')
        out.write(s2+']\n')

data.close()
article.close()
out.close()
