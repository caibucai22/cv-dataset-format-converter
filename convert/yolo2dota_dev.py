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

imgs_path = r'E:\01-LabProjects\609\609-images-filter\images'
labels_path = r'E:\01-LabProjects\609\609-images-filter\labels'
dota_label_path = r'E:\01-LabProjects\609\609-images-filter\dota_labels'

img_list = sorted([name for name in os.listdir(imgs_path) if name.endswith('.bmp')])
label_list = sorted([name for name in os.listdir(labels_path) if name.endswith('.txt')])

# class_idx2name = {0: 'rivet1', 1: 'rivet2', 2: 'rivet3',3:'rivet4'}
class_idx2name = {0: 'bump', 1: 'wrinkle', 2: 'scratch', 3: 'rust', 4: 'pit', 5: 'broken_edge'}
difficulty = 0


def bbox_yolo2dota(x, y, w, h, img_w, img_h):
    # 转换成像素坐标
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


for img_name, label_name in zip(img_list, label_list):
    print(img_name)
    img = cv2.imread(imgs_path + "/" + img_name)
    img_h, img_w, _ = img.shape

    dota_lines = []
    with open(labels_path + '/' + label_name, ) as f:
        lines = f.readlines()
        for line in lines:
            # print(line.strip())
            (idx, x, y, w, h) = [float(itm) for itm in line.split(' ')]
            points = bbox_yolo2dota(x, y, w, h, img_w, img_h)
            label = class_idx2name[idx]

            dota_line = ''
            for p in points:
                dota_line += str(int(p)) + ' '
            dota_line += label + ' '
            dota_line += str(difficulty)

            # cv2.rectangle(img, (int(points[0]), int(points[1])), (int(points[4]), int(points[5])), (0, 0, 255),
            #               thickness=2)

            cv2.waitKey(0)
            dota_lines.append(dota_line)

        # cv2.rectangle(img, (100, 100), (300, 300), (255, 0, 0), thickness=1)
        # # cv2.namedWindow("vis", 0)
        # # cv2.resizeWindow("vis", 1000, 800)
        # # cv2.imshow('vis', img)
        # # cv2.waitKey(0)
        # cv2.imwrite('vis.png', img)
        f.close()
    # write
    with open(dota_label_path + '/' + label_name, 'w') as f:
        for line in dota_lines:
            f.write(line + '\n')
        f.close()

print('done!')
