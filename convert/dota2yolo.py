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
from collections import OrderedDict

from utils import utils
from meta.Dataset_Meta import Dataset_setting
from xx2yy import XX2YY
class Dota2Yolo(XX2YY):

    def __init__(self,source_dir, dst_dir,
                 source_dataset_type, dst_datatset_type,
                 source_labels_txt_path=None,
                 ann_image_together=False, test_size=0.1,
                 val_size=0.11):
        super().__init__(source_dir,dst_dir,source_dataset_type,dst_datatset_type)
        self.source_dir = source_dir
        self.dst_dir = dst_dir

        self.source_dataset_type = source_dataset_type
        self.dst_dataset_type = dst_datatset_type

        self.source_images_dir_path = os.path.join(source_dir, Dataset_setting[self.source_dataset_type]['dirs']
        [0])
        self.source_labels_dir_path = self.source_images_dir_path
        self.source_labels_txt_path = source_labels_txt_path
        if not ann_image_together:
            self.source_labels_dir_path = os.path.join(source_dir,
                                                       Dataset_setting[self.source_dataset_type]['dirs'][-1])

        # 打印 目标文件夹下 目录情况
        print("dst dir struct:")
        # 判断 文件夹 与 Dataset_Setting 要求的是否一致
        utils.check_and_create_dir(self.dst_dataset_type, dst_dir)
        self.dst_images_dir_path = os.path.join(dst_dir, Dataset_setting[self.dst_dataset_type]['dirs']
        [0])
        self.dst_labels_dir_path = os.path.join(dst_dir, Dataset_setting[self.dst_dataset_type]['dirs']
        [-1])

        if self.dst_dataset_type == 'coco':
            # coco annotations test train val
            dst_dirs = utils.print_dirs_info(dst_dir, display=False)
            # test train val
            self.dst_images_dir_path = [os.path.join(self.dst_dir, dir) for dir in dst_dirs if
                                        dir not in ['annotations']]

        # 根据用户是否提供
        # 1 遍历得到 2 用户提供
        self.label_id_map = self.get_label_id_map(self.source_labels_dir_path)
        if self.source_labels_txt_path is not None:
            self.class_name_to_id = self.get_label_id_map_with_txt(self.source_labels_txt_path)

        # 打印 源文件夹下 目录情况
        print('src dir struct:')
        utils.print_dirs_info(source_dir)

        self.imgs_list, _ = utils.get_imgs(self.source_dir, dataset_type=self.source_dataset_type)
        self.anns_list, _ = utils.get_Anns(self.source_dir, dataset_type=self.source_dataset_type)

    def convert(self):
        for img_name, label_name in zip(self.imgs_list, self.anns_list):
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
                        yolo_line += ' ' + str(round(p, 7))

                    yolo_lines.append(yolo_line.strip())
                f.close()
            # write
            with open(yolo_labels_path + '/' + label_name, 'w') as f:
                for line in yolo_lines:
                    f.write(line + '\n')
                f.close()

        print('done!')

imgs_path = r'E:\01-Lab Projects\800\rivet\patchs\rivet_split\images'
yolo_labels_path = r'E:\01-Lab Projects\800\rivet\patchs\rivet_split\labels'
dota_labels_path = r'E:\01-Lab Projects\800\rivet\patchs\rivet_split\labelTxt'


img_list = sorted([name for name in os.listdir(imgs_path) if name.endswith('.png')])
dota_label_list = sorted([name for name in os.listdir(dota_labels_path) if name.endswith('.txt')])

class_idx2name = {0: 'rivet1', 1: 'rivet2', 2: 'rivet3', 3: 'rivet4'}
class_name2idx = {'rivet1': 0, 'rivet2': 1, 'rivet3': 2, 'rivet4': 3}

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

if __name__ == '__main__':
    Dota2Yolo(source_dir='../exp_dataset/dota',dst_dir='../exp_dataset/yolo',
              source_dataset_type='dota',dst_datatset_type='yolo')