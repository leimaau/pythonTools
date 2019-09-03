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
    regstr = '([bdzgmnljiy]|dr|zr|zj|zs|zsr|zsj|gh|nr|nj|ng).*'
    regstr2 = '([ptckqsh]|tr|cr|cj|ph|th|sr|sj|thr|ch|chr|chj|kh).*'
    if re.match(r'.*[ptk]$', koxqim) and re.match(r'.*[ptk][1-6]$', jyutping):
        if re.match(r''+regstr+'[ptk]$', koxqim) and re.match(r'.*[ptk][56]$', jyutping):
            return True
        elif re.match(r''+regstr2+'[ptk]$', koxqim) and re.match(r'.*[ptk][123]$', jyutping):
            return True
        else:
            return False
    elif re.match(r'.*h$', koxqim) and re.match(r'.*[^ptk][356]$', jyutping):
        if re.match(r''+regstr+'h$', koxqim) and re.match(r'.*[^ptk][56]$', jyutping):
            return True
        elif re.match(r''+regstr2+'h$', koxqim) and re.match(r'.*[^ptk][3]$', jyutping):
            return True
        else:
            return False
    elif re.match(r'.*x$', koxqim) and re.match(r'.*[^ptk][256]$', jyutping):
        if re.match(r''+regstr+'x$', koxqim) and re.match(r'.*[^ptk][56]$', jyutping):
            return True
        elif re.match(r''+regstr2+'x$', koxqim) and re.match(r'.*[^ptk][2]$', jyutping):
            return True
        else:
            return False
    elif re.match(r'.*[^ptkhx]$', koxqim) and re.match(r'.*[^ptk][14]$', jyutping):
        if re.match(r''+regstr+'[^ptkxh]$', koxqim) and re.match(r'.*[^ptkxh][4]$', jyutping):
            return True
        elif re.match(r''+regstr2+'[^ptkxh]$', koxqim) and re.match(r'.*[^ptkxh][1]$', jyutping):
            return True
        else:
            return False
    elif re.match(r'.*d$', koxqim) and re.match(r'.*[36]$', jyutping):
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
        #dict_out[char[1]] = dict_koxqim_dialect[char[0]]
    else:
        try:
            if char[1] in dict_out:
                dict_out[char[1]] = dict_out[char[1]] + '/' + dict_koxqim_dialect[char[0]]
            else:
                dict_out[char[1]] = dict_koxqim_dialect[char[0]]
        except:
            dict_out[char[1]] = '_noData_'
            continue

for key,item in dict_dialect.items():
    out.write(key+'\t'+item+'\t'+'0'+'\n')

for key,item in dict_out.items():
    out.write(key+'\t'+item+'\t'+'1'+'\n')


data_koxqim.close()
out.close()
