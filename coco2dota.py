# -*- coding: utf-8 -*-
"""
# @file name : labelimg2dota.py
# @author    : Csy
# @date      : 2023-06-22 14:14
# @brief     : coco json 转换 dota 格式 标注未
"""

import json
import os
from glob import glob


# convert labelimg json to DOTA txt format

def custombasename(fullname):
    return os.path.basename(os.path.splitext(fullname)[0])


IN_PATH = './data_annotated'
OUT_PATH = './dota_txt'

file_list = glob(IN_PATH + '/*.json')

for i in range(len(file_list)):
    with open(file_list[i]) as f:
        label_str = f.read()
        label_dict = json.loads(label_str)  # json文件读入dict

        # 输出 txt 文件的路径
        out_file = OUT_PATH + '/' + custombasename(file_list[i]) + '.txt'

        # 写入 poly 四点坐标 和 label
        fout = open(out_file, 'w')
        out_str = ''
        for shape_dict in label_dict['shapes']:
            points = shape_dict['points']
            x1,y1 = points[0]
            x2,y2 = points[1]
            # 从x小的点 开始 原因：标注时 起始点不一致

            if x1 < x2:
                x3,y3 = x2,y1
                x4,y4 = x1,y2

                points = [[x1,y1],[x3,y3],[x2,y2],[x4,y4]]
            else:
                x3, y3 = x1, y2
                x4, y4 = x2, y1
                points = [[x2, y2], [x3, y3], [x1, y1], [x4, y4]]
            for p in points:
                out_str += (str(round(p[0])) + ' ' + str(round(p[1])) + ' ')
            out_str += shape_dict['label'] + ' 0\n'
        fout.write(out_str)
        fout.close()
    print('%d/%d' % (i + 1, len(file_list)))
    # break