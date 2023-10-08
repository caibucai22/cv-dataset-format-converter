# -*- coding: UTF-8 -*-
"""
@File    ：yolo2dota.py
@Author  ：Csy
@Date    ：2023-09-23 10:53 
@Bref    : yolo label x y w h 格式 转 dota x1 y1 x2 y2 x3 y3 x4 y4 label difficulty
@Ref     :
"""
import os
import shutil
import cv2

import utils
from meta.Dataset_Meta import Dataset_setting


class Yolo2Dota():

    def __init__(self, source_dir, dst_dir,
                 source_dataset_type, dst_datatset_type,
                 source_labels_txt_path=None,
                 ann_image_together=False, test_size=0.1,
                 val_size=0.11):
        # super().__init__(source_dir,dst_dir,source_dataset_type,dst_datatset_type)
        self.difficulty = 0
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
        # self.label_id_map = self.get_label_id_map(self.source_labels_dir_path)
        if self.source_labels_txt_path is not None:
            self.class_name_to_id, self.class_id_to_name = utils.get_label_id_map_with_txt(self.source_labels_txt_path)

        # 打印 源文件夹下 目录情况
        print('src dir struct:')
        utils.print_dirs_info(source_dir)

        self.imgs_list, _ = utils.get_imgs(self.source_dir, dataset_type=self.source_dataset_type)
        self.anns_list, _ = utils.get_Anns(self.source_dir, dataset_type=self.source_dataset_type)

        if self.anns_list[0] == 'classes.txt':
            self.anns_list = self.anns_list[1:]

    def convert(self):
        for img_name, label_name in zip(self.imgs_list, self.anns_list):
            print(img_name)
            img = cv2.imread(self.source_images_dir_path + "/" + img_name)
            img_h, img_w, _ = img.shape

            dota_lines = []
            with open(self.source_labels_dir_path + '/' + label_name, ) as f:
                lines = f.readlines()
                for line in lines:
                    # print(line.strip())
                    (idx, x, y, w, h) = [float(itm) for itm in line.split(' ')]
                    points = utils.bbox_yolo2dota(x, y, w, h, img_w, img_h)
                    label = self.class_id_to_name[idx]

                    dota_line = ''
                    for p in points:
                        dota_line += str(int(p)) + ' '
                    dota_line += label + ' '
                    dota_line += str(self.difficulty)

                    cv2.waitKey(0)
                    dota_lines.append(dota_line)
                f.close()
            # write
            with open(self.dst_labels_dir_path + '/' + label_name, 'w') as f:
                for line in dota_lines:
                    f.write(line + '\n')
                f.close()
            # copy image file
            shutil.copy(self.source_images_dir_path + "/" + img_name, self.dst_images_dir_path + "/" + img_name)

        shutil.copy(self.source_dir + "/" + 'classes.txt', self.dst_dir + "/" + 'classes.txt')

        print('done!')


if __name__ == '__main__':
    convert = Yolo2Dota(source_dir='../exp_dataset/yolo', dst_dir='../exp_dataset/dota',
                        source_labels_txt_path='../exp_dataset/yolo/classes.txt',
                        source_dataset_type='yolo', dst_datatset_type='dota')
    convert.convert()
