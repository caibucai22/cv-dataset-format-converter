# -*- coding: UTF-8 -*-
"""
@File    ：yolo2dota.py
@Author  ：Csy
@Date    ：2023-09-23 10:53 
@Bref    : yolo label x y w h 格式 转 dota x1 y1 x2 y2 x3 y3 x4 y4 label difficulty
@Ref     :
"""
import os
import cv2

imgs_path = r'E:\01-LabProjects\609\609_split\images'
yolo_labels_path = r'E:\01-LabProjects\609\609_split\labels'
dota_labels_path = r'E:\01-LabProjects\609\609_split\labelTxt'


img_list = sorted([name for name in os.listdir(imgs_path) if name.endswith('.bmp')])
dota_label_list = sorted([name for name in os.listdir(dota_labels_path) if name.endswith('.txt')])

class_idx2name = {0: 'rivet1', 1: 'rivet2', 2: 'rivet3', 3: 'rivet4'}
# class_name2idx = {'rivet1': 0, 'rivet2': 1, 'rivet3': 2, 'rivet4': 3}
class_name2idx = { 'bump':0, 'wrinkle':1, 'scratch':2, 'rust':3, 'pit':4, 'broken_edge':5}


difficulty = 0


def bbox_yolo2dota(x, y, w, h, img_w, img_h):
    x, y, w, h = x * img_w, y * img_h, w * img_w, h * img_h
    x1, y1 = x - w / 2, y - h / 2
    x2, y2 = x + w / 2, y - h / 2
    x3, y3 = x + w / 2, y + h / 2
    x4, y4 = x - w / 2, y + h / 2
    # x1, y1 = (x - w / 2) * img_w, (y - h / 2) * img_h
    # x2, y2 = (x + w / 2) * img_w, (y - h / 2) * img_h
    # x3, y3 = (x + w / 2) * img_w, (y + h / 2) * img_h
    # x4, y4 = (x - w / 2) * img_w, (y + h / 2) * img_h

    return [x1, y1, x2, y2, x3, y3, x4, y4]


def bbox_dota2yolo(points, img_w, img_h):
    # 转换成像素坐标
    x1, y1, x2, y2, x3, y3, x4, y4 = points
    w, h = x3 - x1, y3 - y1
    xc = (x3 + x1) / 2
    yc = (y3 + y1) / 2
    xc, yc = xc / img_w, yc / img_h
    w, h = w / img_w, h / img_h
    return xc, yc, w, h


for img_name, label_name in zip(img_list, dota_label_list):
    print(img_name)
    img = cv2.imread(imgs_path + "/" + img_name)
    img_h, img_w, _ = img.shape

    yolo_lines = []
    with open(dota_labels_path + '/' + label_name, ) as f:
        lines = f.readlines()
        for line in lines:
            if len(line.strip()) == 0:
                continue
            # print(line.strip())
            (x1, y1, x2, y2, x3, y3, x4, y4, label, difficult) = [itm for itm in line.split(' ')]
            dota_points = [x1, y1, x2, y2, x3, y3, x4, y4]
            dota_points = [float(itm) for itm in dota_points]
            points = bbox_dota2yolo(dota_points, img_w, img_h)
            label_idx = class_name2idx[label]

            yolo_line = str(label_idx)
            for p in points:
                yolo_line += ' '+str(round(p, 7))

            yolo_lines.append(yolo_line.strip())
        f.close()
    # write
    with open(yolo_labels_path + '/' + label_name, 'w') as f:
        for line in yolo_lines:
            f.write(line + '\n')
        f.close()

print('done!')
