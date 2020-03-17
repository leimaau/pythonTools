
# coding=utf-8 

from operator import itemgetter
from itertools import groupby

fdata = open('dialectData.txt', encoding='utf-8')
f_oldfist_first = open('从中古声母看方言声母.txt', 'w', encoding='utf-8')
f_oldfinal_final = open('从中古韵母看方言韵母.txt', 'w', encoding='utf-8')
f_oldtone_tone = open('从中古声调看方言声调.txt', 'w', encoding='utf-8')
f_first_oldfist = open('从方言声母看中古声母.txt', 'w', encoding='utf-8')
f_final_oldfinal = open('从方言韵母看中古韵母.txt', 'w', encoding='utf-8')
f_tone_oldtone = open('从方言声调看中古声调.txt', 'w', encoding='utf-8')

dictList = []

for inx, line in enumerate(fdata):
    tempList = line.split('\t')
    dictList.append({'char': tempList[1], 'first': tempList[3], 'final': tempList[4], 'tone': tempList[5], 'old_first': tempList[12].replace('\n',''), 'old_final': tempList[7]+tempList[8]+tempList[9]+tempList[11], 'old_tone': tempList[10]} )

def showDialect(para):
    dictList.sort(key=itemgetter(para))
    lstg = groupby(dictList,itemgetter(para))
    newlist = []
    for i in dict([key for key in lstg]):
        newlist.append(i)
    return newlist

def listTodict(intput):
    tempdict = {}
    for index in range(len(intput)):
        tempdict[intput[index]] = index
    return tempdict


firstList = showDialect('first')
# 预设方言声母排序
sortRule = listTodict(['p','ph','m','f','w','v','t','th','n','ɬ','l','ts','tsh','s','tʃ','ʧ','tʃh','ʧh','ȵ','ʃ','k','kh','ŋ','h','∅'])
try:
    firstList = sorted(firstList, key=lambda x: sortRule[x])
except KeyError as err:
    print('==> 注意有不存在预设排序中的声母：' + str(err) + '，请处理再排序')
print('该方言的声母有：')
print(firstList)


finalList = showDialect('final')
# 预设方言韵母排序
presetfirst = ['i','u','y','a','ia','ua','ɛ','iɛ','uɛ','œ','ɔ','uɔ','ai','iai','uai','ɐi','uɐi','ei','ɔi','ui','iui','au','iau','ɛu','eu','iu','am','ɐm','iɐm','ɛm','em','im','an','iɛn','uan','ɐn','iɐn','uɐn','ɛn','en','ɔn','in','un','yn','aŋ','iaŋ','uaŋ','ɐŋ','uɐŋ','ɛŋ','eŋ','ieŋ','ueŋ','œŋ','iœŋ','ɔŋ','iɔŋ','uɔŋ','ap','iap','ɐp','iɐp','ɛp','ep','ip','at','uat','ɐt','iɐt','uɐt','ɛt','uɛt','et','ɔt','it','ut','yt','ak','uak','ɐk','ɛk','ek','iek','uek','œk','iœk','ɔk','iɔk','uɔk','ok','iok','uok','ŋ']
diffList = list(set(finalList).difference(set(presetfirst)))
if(len(diffList) != 0):
    print('==> 注意有不存在预设排序中的韵母，目前排在后面：')
    print(diffList)
sortRule = listTodict(presetfirst+diffList)
finalList = sorted(finalList, key=lambda x: sortRule[x])
print('该方言的韵母有：')
print(finalList)


toneList = showDialect('tone')
# 【从方言声调看中古声调，需要自己排序时，把控制台输出的声调写到下一行，手工排序后取消注释再运行】
# toneList = ['', '2', '21', '24', '3', '33', '35', '5', '53']
print('该方言的声调有：')
print(toneList)


# 基本函数
def old_new(para, file, old_p, new_p, sortRule):
    dictList.sort(key=itemgetter(old_p))
    lstg = groupby(dictList,itemgetter(old_p)) 
    newlist = dict([(key,list(group)) for key,group in lstg])

    try:
        newlist[para].sort(key=itemgetter(new_p))
    except KeyError:
        print ('==> 失败，原始数据缺少' + para + '，请检查方言调查字表')
    lstg2 = groupby(newlist[para],itemgetter(new_p)) 
    newlist2 = dict([(key,list(group)) for key,group in lstg2])

    file.writelines(para)
    for key in sorted(newlist2, key=lambda x: sortRule[x]):
        file.writelines('\t' + key + '\t')
        tempList = []
        for inx in newlist2[key]:
            if(inx['char'] not in tempList): file.writelines(inx['char'])
            tempList.append(inx['char'])
        file.writelines('\n')

print('--------------------------从中古看方言--------------------------')

# 预设中古声母排序
oldfirstList = ['帮','滂','並','明','非','敷','奉','微','端','透','定','泥','来','知','彻','澄','精','清','从','心','邪','庄','初','崇','生','章','昌','船','书','禅','日','见','溪','群','疑','晓','匣','影','云','以']

for i in oldfirstList:
    old_new(i, f_oldfist_first, 'old_first', 'first', listTodict(firstList))
print('从中古声母看方言声母完成')

# 预设中古韵母排序
oldfinalList = ['果开一歌','果开三戈','果合一戈','果合三戈','假开二麻','假开三麻','假合二麻','遇合一模','遇合三鱼','遇合三虞','蟹开一咍','蟹开一泰','蟹开二皆','蟹开二佳','蟹开二夬','蟹开三祭','蟹开四齐','蟹合一灰','蟹合一泰','蟹合二皆','蟹合二佳','蟹合二夬','蟹合三祭','蟹合三废','蟹合四齐','止开三支','止开三脂','止开三之','止开三微','止合三支','止合三脂','止合三微','效开一豪','效开二肴','效开三宵','效开四萧','流开一侯','流开三尤','流开三幽','咸开一覃','咸开一合','咸开一谈','咸开一盍','咸开二咸','咸开二洽','咸开二衔','咸开二狎','咸开三盐','咸开三叶','咸开三严','咸开三业','咸开四添','咸开四帖','咸合三凡','咸合三乏','深开三侵','深开三缉','山开一寒','山开一曷','山开二山','山开二黠','山开二删','山开二鎋','山开三仙','山开三薛','山开三元','山开三月','山开四先','山开四屑','山合一桓','山合一末','山合二山','山合二黠','山合二删','山合二鎋','山合三仙','山合三薛','山合三元','山合三月','山合四先','山合四屑','臻开一痕','臻开三真','臻开三质','臻开三殷','臻开三迄','臻合一魂','臻合一没','臻合三谆','臻合三术','臻合三文','臻合三物','宕开一唐','宕开一铎','宕开三阳','宕开三药','宕合一唐','宕合一铎','宕合三阳','宕合三药','江开二江','江开二觉','曾开一登','曾开一德','曾开三蒸','曾开三职','曾合一登','曾合一德','曾合三职','梗开二庚','梗开二陌','梗开二耕','梗开二麦','梗开三庚','梗开三陌','梗开三清','梗开三昔','梗开四青','梗开四锡','梗合二庚','梗合二耕','梗合二麦','梗合三庚','梗合三清','梗合三昔','梗合四青','通合一东','通合一屋','通合一冬','通合一沃','通合三东','通合三屋','通合三锺','通合三烛']

for i in oldfinalList:
    old_new(i, f_oldfinal_final, 'old_final', 'final', listTodict(finalList))
print('从中古韵母看方言韵母完成')

# 预设中古声调排序
oldtoneList = ['平','上','去','入']

for i in oldtoneList:
    old_new(i, f_oldtone_tone, 'old_tone', 'tone', listTodict(toneList))
print('从中古声调看方言声调完成')

print('--------------------------从方言看中古--------------------------')

diffList = list(set(showDialect('old_first')).difference(set(oldfirstList)))
if(len(diffList) != 0):
    print('==> 注意原数据多出以下中古声母：')
    print(diffList)

for i in firstList:
    old_new(i, f_first_oldfist, 'first', 'old_first', listTodict(oldfirstList))
print('从方言声母看中古声母完成')

diffList = list(set(showDialect('old_final')).difference(set(oldfinalList)))
if(len(diffList) != 0):
    #print('==>注意原数据比生成报告多出以下中古韵母：')
    #print(diffList)
    for val in diffList:
        if(len(val)<4): print('==> 注意有中古韵母录入不完整：' + val)

for i in finalList:
    old_new(i, f_final_oldfinal, 'final', 'old_final', listTodict(oldfinalList + diffList))
print('从方言韵母看中古韵母完成')

diffList = list(set(showDialect('old_tone')).difference(set(oldtoneList)))
if(len(diffList) != 0):
    print('==> 注意原数据多出以下中古声调：')
    print(diffList)

for i in toneList:
    old_new(i, f_tone_oldtone, 'tone', 'old_tone', listTodict(oldtoneList))
print('从方言声调看中古声调完成')


f_oldfist_first.close()
f_oldfinal_final.close()
f_oldtone_tone.close()
f_first_oldfist.close()
f_final_oldfinal.close()
f_tone_oldtone.close()
fdata.close()

