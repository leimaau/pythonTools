import re

char = []
list_dialect = []
dict_dialect = {}
dict_dialect_list = {}
dict_koxqim_dialect = {}
dict_out = {}

data_dialect = open('data_dialect.txt', encoding='utf-8')

for line in data_dialect.readlines():
    char = line.split()
    if char[0] in dict_dialect:
        dict_dialect[char[0]] = dict_dialect[char[0]] + '/' + char[1]
    else:
        dict_dialect[char[0]] = char[1]

data_dialect.close()

for key,item in dict_dialect.items():
    dict_dialect_list[key] = item.split('/')

# 第一步 生成中古音与方音对应数据

def judge(koxqim,jyutping):
    if re.match(r'.*[ptk]$', koxqim) and re.match(r'.*[ptk][1-6]$', jyutping):
        return True
    elif re.match(r'.*h$', koxqim) and re.match(r'.*[^ptk][356]$', jyutping):
        return True
    elif re.match(r'.*x$', koxqim) and re.match(r'.*[^ptk][256]$', jyutping):
        return True
    elif re.match(r'.*[^ptkhx]$', koxqim) and re.match(r'.*[^ptk][14]$', jyutping):
        return True
    else:
        return False

data_koxqim = open('data_koxqim.txt', encoding='utf-8')
koxqim_dialect = open('koxqim_dialect.txt', 'w', encoding='utf-8')

for line in data_koxqim.readlines():
    char = line.split()
    if char[0] in dict_koxqim_dialect:
        if char[1] in dict_dialect_list:
            list_dialect = []
            for i in dict_dialect_list[char[1]]:
                if judge(char[0],i):
                    list_dialect.append(i)
                else:
                    continue
            dict_koxqim_dialect[char[0]] = '/'.join(filter(None,set(dict_koxqim_dialect[char[0]].split('/')).union(set(list_dialect))))
        else:
            continue
    else:
        if char[1] in dict_dialect_list:
            list_dialect = []
            for i in dict_dialect_list[char[1]]:
                if judge(char[0],i):
                    list_dialect.append(i)
                else:
                    continue
            dict_koxqim_dialect[char[0]] = '/'.join(list_dialect)
        else:
            continue

for key,item in dict_koxqim_dialect.items():
    koxqim_dialect.write(key+'\t'+item+'\n')

koxqim_dialect.close()
data_koxqim.close()

# 第二步 推导不在方调表中的字音（若手动调整过 koxqim_dialect.txt 需将第一步注释）

out = open('output.txt', 'w', encoding='utf-8')
data_koxqim = open('data_koxqim.txt', encoding='utf-8')

for line in data_koxqim.readlines():
    char = line.split()
    if char[1] in dict_dialect:
        continue
    else:
        try:
            if char[1] in dict_out:
                dict_out[char[1]] = dict_out[char[1]] + '/' + dict_koxqim_dialect[char[0]]
            else:
                dict_out[char[1]] = dict_koxqim_dialect[char[0]]
        except:
            dict_out[char[1]] = 'ERR'
            continue

for key,item in dict_dialect.items():
    out.write(key+'\t'+item+'\t'+'0'+'\n')

for key,item in dict_out.items():
    out.write(key+'\t'+item+'\t'+'1'+'\n')


data_koxqim.close()
out.close()
