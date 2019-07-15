import re

def  jyutping_to_ipa(inputstr,flag):

    outputstr = inputstr

    outputstr = re.sub(r'(^|[ /])(m)(\d)',r'\1m̩\3',inputstr)
    outputstr = re.sub(r'(^|[ /])(ng)(\d)',r'\1ŋ̩\3',outputstr)
    outputstr = re.sub('sl','ɬ',outputstr)
    outputstr = re.sub('nj','ȵ',outputstr)

    outputstr = re.sub('yu','yː',outputstr)
    outputstr = re.sub('eoi','ɵy',outputstr)
    outputstr = re.sub(r'eo([tn])',r'ɵ\1',outputstr)
    outputstr = re.sub('eo','ɵ',outputstr)

    outputstr = re.sub(r'oe([tk])',r'œː\1',outputstr)
    outputstr = re.sub('oeng','œːŋ',outputstr)
    outputstr = re.sub('oe','œː',outputstr)

    outputstr = re.sub('uk','ʊk',outputstr)  # uk[ok]
    outputstr = re.sub('ung','ʊŋ',outputstr) # ung[oŋ]
    outputstr = re.sub(r'u([in])',r'uː\1',outputstr) # ui[uːy]
    outputstr = re.sub('ut','uːt',outputstr)
    outputstr = re.sub(r'([^aeio])u(\d)',r'\1uː\2',outputstr)

    outputstr = re.sub('eng','ɛːŋ',outputstr)
    outputstr = re.sub(r'e([umnptk])',r'ɛː\1',outputstr)
    outputstr = re.sub(r'e(\d)',r'ɛː\1',outputstr)

    outputstr = re.sub('ing','ɪŋ',outputstr) # ing[eŋ]
    outputstr = re.sub('ik','ɪk',outputstr)  # ik[ek]
    outputstr = re.sub(r'i([umnpt])',r'iː\1',outputstr)
    outputstr = re.sub(r'([^aeuoː])i(\d)',r'\1iː\2',outputstr)

    outputstr = re.sub('ong','ɔːŋ',outputstr)
    outputstr = re.sub(r'o([imnptk])',r'ɔː\1',outputstr) # oi[ɔːy]
    outputstr = re.sub(r'o(\d)',r'ɔː\1',outputstr)

    outputstr = re.sub('aa','Aː',outputstr)
    outputstr = re.sub('a','ɐ',outputstr)

    outputstr = re.sub('gw','Kʷ',outputstr)  # gw[ku]
    outputstr = re.sub('kw','Kʷʰ',outputstr) # kw[kʰu]
    outputstr = re.sub(r'(^|[ /])([ptk])',r'\1\2ʰ',outputstr)
    outputstr = re.sub(r'(^|[ /])b',r'\1p',outputstr)
    outputstr = re.sub(r'(^|[ /])d',r'\1t',outputstr)
    outputstr = re.sub(r'(^|[ /])g',r'\1k',outputstr)

    outputstr = re.sub(r'zy(\d)',r't͡Sɿ\1',outputstr)
    outputstr = re.sub(r'cy(\d)',r't͡Sʰɿ\1',outputstr)
    outputstr = re.sub(r'sy(\d)',r'Sɿ\1',outputstr)
    
    if flag=='n':
        outputstr = re.sub('s','ʃ',outputstr)
        outputstr = re.sub('z','t͡ʃ',outputstr)
        outputstr = re.sub('c','t͡ʃʰ',outputstr)
    else:
        outputstr = re.sub('s','s',outputstr)
        outputstr = re.sub('z','t͡s',outputstr)
        outputstr = re.sub('c','t͡sʰ',outputstr)

    outputstr = re.sub('ng','ŋ',outputstr)

    outputstr = re.sub(r'([ptk])6',r'\1̚˨',outputstr)
    outputstr = re.sub(r'([ptk])3',r'\1̚˧',outputstr)
    outputstr = re.sub(r'([ptk])1',r'\1̚˥',outputstr)
    outputstr = re.sub('4','˨˩',outputstr)
    outputstr = re.sub('1','˥˥',outputstr)

    if flag=='n':
        outputstr = re.sub('5','˨˦',outputstr) # 阳上：南宁24 广州13
    else:
        outputstr = re.sub('5','˩˧',outputstr)

    outputstr = re.sub('2','˧˥',outputstr)
    outputstr = re.sub('6','˨˨',outputstr)
    outputstr = re.sub('3','˧˧',outputstr)

    outputstr = outputstr.lower()

    return outputstr
