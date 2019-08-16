import re
import jieba
import jieba.posseg as pseg
from mytool import jyutping_to_ipa
from opencc import OpenCC
cc = OpenCC('s2t')
jieba.set_dictionary('./extra_dict/dict.txt.big')

file_name='data_naamning.txt' # 字词典文件: data_naamning 南宁白话数据; data_naamning_bingwaa 南宁平话数据; data_gwongzau 广州话数据
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
    result = pseg.cut(cc.convert(words))
    for w in result:
        cutwordslist.append(w.word)
    return cutwordslist

# isIPA: jyutping-拼音 IPA-ipa
# regstr_ignore: yes_ignore-忽略 no_ignore-不忽略
# area: n-南宁型ipa  g-广州型ipa  p-南宁平话型ipa  p2-第二种南宁平话型ipa
# ipatype: 0-宽式音标(上标调值数码) 1-宽式音标(不上标调值数码) 2-严式音标(调值竖线)
def dealfunc_characters(regstr,prose,isIPA,regstr_ignore,area,ipatype):
    prose_list = list(prose)
    try:
        if re.match(r"" + regstr, prose_list[0]):
            if regstr_ignore=='no_ignore':
                s = prose_list[0]
            else:
                s = ''
        else:
            if isIPA=='IPA':
                s = jyutping_to_ipa(dictionary[prose_list[0]],area,ipatype)
            else:
                s = dictionary[prose_list[0]]
    except KeyError:
        s = 'ERR'

    for char in prose_list[1::]:
        try:
            if re.match(r"" + regstr, char):
                if regstr_ignore=='no_ignore':
                    s += char
                else:
                    s += ''
            else:
                if isIPA=='IPA':
                    s += ' '+ jyutping_to_ipa(dictionary[char],area,ipatype)
                else:
                    s += ' '+ dictionary[char]
        except KeyError:
            s += ' '+ 'ERR'
    return s

def dealfunc_phrases(regstr,prose,isIPA,regstr_ignore,area,ipatype):
    prose_list = cutwords(prose)
    # print(prose_list)
    try:
        if re.match(r"" + regstr, prose_list[0]):
            if regstr_ignore=='no_ignore':
                s = prose_list[0]
            else:
                s = ''
        else:
            if ' ' in dictionary[prose_list[0]] and '/' in dictionary[prose_list[0]]:
                s = dealfunc_characters(regstr,prose_list[0],isIPA,regstr_ignore,area,ipatype)
            else:
                if isIPA=='IPA':
                    s = jyutping_to_ipa(dictionary[prose_list[0]],area,ipatype)
                else:
                    s = dictionary[prose_list[0]]
    except KeyError:
        s = dealfunc_characters(regstr,prose_list[0],isIPA,regstr_ignore,area,ipatype)

    for char in prose_list[1::]:
        try:
            if re.match(r"" + regstr, char):
                if regstr_ignore=='no_ignore':
                    s += char
                else:
                    s += ''
            else:
                if ' ' in dictionary[char] and '/' in dictionary[char]:
                    s += ' '+ dealfunc_characters(regstr,char,isIPA,regstr_ignore,area,ipatype)
                else:
                    if isIPA=='IPA':
                        s += ' '+ jyutping_to_ipa(dictionary[char],area,ipatype)
                    else:
                        s += ' '+ dictionary[char]
        except KeyError:
            s += ' '+ dealfunc_characters(regstr,char,isIPA,regstr_ignore,area,ipatype)
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
        out.write(prose.replace('<space>',' ')+'\n')

        regstr = '[0-9A-Za-z-]|[_,，.。·…?—？!！:：;；“”\[\]<>「」『』【】（）《》、 ]+'
        prose = re.sub(r'([\u4e00-\u9fa5]+)([0-9A-Za-z-_]+)',r'\1<space>\2',prose)
        prose = prose.replace('<space>',' ')

        if file_name == 'data_naamning.txt':
            area = 'n'
        elif file_name == 'data_naamning_bingwaa.txt':
            area = 'p2'  # p or p2
        else:
            area = 'g'
        
        s = dealfunc_phrases(regstr,prose,'jyutping','no_ignore',area,0)
        #s = dealfunc_characters(regstr,prose,'jyutping','no_ignore',area,0)
        out.write(s+'\n[')

        s2 = dealfunc_phrases(regstr,prose,'IPA','no_ignore',area,0)
        #s2 = dealfunc_characters(regstr,prose,'IPA','no_ignore',area,0)
        out.write(s2+']\n')

data.close()
article.close()
out.close()
