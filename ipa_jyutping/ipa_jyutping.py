import re
from mytool import ipa_to_jyutping,jyutping_to_ipa

in_txt = open('input.txt', encoding='utf-8')
out_txt = open('output.txt', 'w', encoding='utf-8')

for paragraph in in_txt.readlines():
    try:
        line = paragraph.replace(' ','$@').split()[0]
    except:
        continue

    sentences = line.split()
    for prose in sentences:

        prose = prose.replace('$@',' ')

        #out_txt.write(prose)
        #out_txt.write('\t')

        #s = ipa_to_jyutping(prose,'p')   # area: n-南宁ipa  g-广州ipa  p-南宁平话《广西通志·汉语方言志》版IPA  p2-《南宁平话词典》版IPA
        s = jyutping_to_ipa(prose,'p',1)
        out_txt.write(s+'\n')
        
in_txt.close()
out_txt.close()
