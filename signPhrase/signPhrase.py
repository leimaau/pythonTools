import re
from opencc import OpenCC

cc = OpenCC('phrase2jyut')
ccbw = OpenCC('phrase2jyut_bw')

def process_file(input_file, output_file, converter):
    with open(input_file, encoding='utf-8') as article, open(output_file, 'w', encoding='utf-8') as out:
        for paragraph in article:  # 直接迭代文件对象
            try:
                line = paragraph.replace(' ', '<space>').split()[0]
            except IndexError:  # 捕获特定异常
                continue

            sentences = line.split()
            for prose in sentences:
                s = converter.convert(prose.replace('<space>', ' '))
                out.write(s.replace('<s>', ' ').strip() + '\n')

# 处理第一个文件
process_file('input.txt', 'output.txt', cc)
# 处理第二个文件
process_file('input2.txt', 'output2.txt', ccbw)