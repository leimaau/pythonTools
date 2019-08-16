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

        s = ipa_to_jyutping(prose,'p')   # area: n-南宁型ipa  g-广州型ipa  p-南宁平话型ipa  p2-第二种南宁平话型ipa
        #s = jyutping_to_ipa(prose,'p',1)
        out_txt.write(s+'\n')
        
in_txt.close()
out_txt.close()
