import re
from itertools import product

def process_pinyin(input_file, output_file):
    with open(input_file, encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            line = line.strip()
            if not line:
                continue
            
            # 第一步：按中文逗号分割大块
            blocks = [b.strip() for b in line.split('，')]  # 注意这里是中文逗号
            
            # 第二步：处理每个大块内部的组合
            all_combos = []
            for block in blocks:
                # 处理块内的斜杠组合
                parts = re.split(r'\s+', block)
                combinations = [p.split('/') for p in parts]
                block_combos = [' '.join(c) for c in product(*combinations)]
                all_combos.append(block_combos)
            
            # 第三步：生成跨块组合并用中文逗号连接
            final = ['，'.join(cross_combo) for cross_combo in product(*all_combos)]
            
            outfile.write(','.join(final) + '\n')

# 调用函数处理文件
process_pinyin('dealIn.txt', 'dealOut.txt')
