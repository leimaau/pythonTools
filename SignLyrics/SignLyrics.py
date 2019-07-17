import re
from mytool import jyutping_to_ipa

file_name='data_naamning.txt' # 字典文件 data_naamning 南宁粤拼; data_gwongzau 广州粤拼
data = open(file_name, encoding='utf-8')

char = []
dictionary = {}

for line in data.readlines():
    char = line.split()
    if char[0] in dictionary:
        dictionary[char[0]] = dictionary[char[0]] + '/' + char[1]
    else:
        dictionary[char[0]] = char[1]

# flag: 0 拼音 1 ipa ; flag2: 0 regstr忽略 1 regstr不忽略
def dealfunc(regstr,prose,flag,flag2):
        try:
            if re.match(r"" + regstr, list(prose)[0]):
                if flag2==1:
                    s = list(prose)[0]
                else:
                    s = ''
            else:
                if flag==1:
                    s = jyutping_to_ipa(dictionary[list(prose)[0]],'n' if file_name == 'data_naamning.txt' else 'g')
                else:
                    s = dictionary[list(prose)[0]]
        except KeyError:
            s = 'ERR'

        for char in list(prose)[1::]:
            try:
                if re.match(r"" + regstr, char):
                    if flag2==1:
                        s += char
                    else:
                        s += ''
                else:
                    if flag==1:
                        s += ' '+ jyutping_to_ipa(dictionary[char],'n' if file_name == 'data_naamning.txt' else 'g')
                    else:
                        s += ' '+ dictionary[char]
            except KeyError:
                s += ' '+ 'ERR'
        return s

lyrics = open('input.txt', encoding='utf-8')
out = open('output.txt', 'w', encoding='utf-8')

for paragraph in lyrics.readlines():
    try:
        line = paragraph.replace(' ','<space>').split()[0]
    except:
        continue

    sentences = line.split()
    for prose in sentences:
        out.write(prose.replace('<space>',' '))
        out.write('\n')

        prose = re.sub(r'([\u4e00-\u9fa5]+)([0-9A-Za-z-_]+)',r'\1<space>\2',prose)
        
        s = dealfunc('[0-9A-Za-z-]|[_,，.。?？!！:：;；“”\[\]<>「」『』《》、 ]+',prose.replace('<space>',' '),0,1)
        out.write(s+'\n[')

        s2 = dealfunc('[0-9A-Za-z-]|[_,，.。?？!！:：;；“”\[\]<>「」『』《》、 ]+',prose.replace('<space>',' '),1,1)
        out.write(s2+']\n')

data.close()
lyrics.close()
out.close()
