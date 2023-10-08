# -*- coding: UTF-8 -*-
"""
@File    ：labelimg2dota.py
@Author  ：Csy
@Date    ：2023-09-11 21:28
@Bref    :
@Ref     :
"""

import json
import os
import math
import shutil

import cv2
import PIL.Image
from collections import OrderedDict

from meta.Dataset_Meta import *
import utils
from utils.Exception import *


class Labelimg2Dota():

    def __init__(self, source_dir, dst_dir, ann_image_together=True):
        self.source_dir = source_dir
        self.dst_dir = dst_dir

        self.source_dataset_type = 'labelme'
        self.dst_dataset_type = 'dota'
        self.diffculty = 0
        self.source_images_dir_path = os.path.join(source_dir, Dataset_setting[self.source_dataset_type]['dirs']
        [0])
        self.source_labels_dir_path = self.source_images_dir_path
        if not ann_image_together:
            self.source_labels_dir_path = os.path.join(source_dir,
                                                       Dataset_setting[self.source_dataset_type]['dirs'][-1])

        self.dst_images_dir_path = os.path.join(dst_dir, Dataset_setting[self.dst_dataset_type]['dirs']
        [0])
        self.dst_labels_dir_path = os.path.join(dst_dir, Dataset_setting[self.dst_dataset_type]['dirs']
        [-1])

        # 根据用户是否提供
        # 1 遍历得到 2 用户提供
        self.label_id_map = self.get_label_id_map(self.source_labels_dir_path)

        # 打印 源文件夹下 目录情况
        print('src dir struct:')
        utils.print_dirs_info(source_dir)
        # 打印 目标文件夹下 目录情况
        print("dst dir struct:")
        utils.print_dirs_info(dst_dir)

        # 是否创建文件夹
        # utils.make_dirs()

        self.imgs_list, _ = utils.get_imgs(self.source_dir, dataset_type='labelme')
        self.anns_list, _ = utils.get_Anns(self.source_dir, dataset_type='labelme')

    def get_label_id_map(self, json_dir):
        label_set = set()

        for file_name in os.listdir(json_dir):
            if file_name.endswith('.json'):
                json_path = os.path.join(json_dir, file_name)
                json_exist = os.path.exists(json_path)
                json_file = open(json_path, 'r')
                data = json.load(json_file)
                for shape in data['shapes']:
                    label_set.add(shape['label'])

        return OrderedDict([(label, label_id) \
                            for label_id, label in enumerate(label_set)])

    def convert(self):
        for img_name, json_name in zip(self.imgs_list, self.anns_list):
            json_path = os.path.join(self.source_labels_dir_path, json_name)
            json_data = json.load(open(json_path))

            img_path = self.save_dota_image(json_data, img_name,
                                            self.source_images_dir_path, self.dst_images_dir_path)
            dota_obj_list = self.get_dota_object_list(json_data, img_path)
            self.save_dota_label(json_name, self.dst_labels_dir_path, dota_obj_list)



    def convert_one(self, json_name):
        json_path = os.path.join(self.source_labels_dir_path, json_name)
        json_data = json.load(open(json_path))

        img_path = self.save_dota_image(json_data, json_name,
                                        self.source_images_dir_path, self.dst_images_dir_path)
        dota_obj_list = self.get_dota_object_list(json_data, img_path)
        self.save_dota_label(json_name, self.dst_labels_dir_path, dota_obj_list)

    def get_dota_object_list(self, json_data, img_path):
        dota_obj_list = []

        img_h, img_w, _ = cv2.imread(img_path).shape
        for shape_dict in json_data['shapes']:
            points = shape_dict['points']
            x1, y1 = points[0]
            x2, y2 = points[1]

            # 从x小的点 开始 原因：标注时 起始点不一致

            if x1 < x2:
                x3, y3 = x2, y1
                x4, y4 = x1, y2

                points_ = [[x1, y1], [x3, y3], [x2, y2], [x4, y4]]
            else:
                x3, y3 = x1, y2
                x4, y4 = x2, y1
                points_ = [[x2, y2], [x3, y3], [x1, y1], [x4, y4]]
            label = shape_dict['label']
            dota_obj = []
            for p in points_:
                dota_obj.append(p)
            dota_obj.append(label)
            dota_obj_list.append(dota_obj)
        return dota_obj_list

    def save_dota_label(self, json_name, label_dir_path, dota_obj_list):
        txt_path = os.path.join(label_dir_path, json_name.replace('.json', '.txt'))

        with open(txt_path, 'w+') as f:  # lll
            for dota_obj_idx, dota_obj in enumerate(dota_obj_list):
                dota_obj_line = ''
                for obj in dota_obj:
                    if isinstance(obj, list):
                        dota_obj_line += (str(round(obj[0])) + ' ' + str(round(obj[1])) + ' ')
                    else:
                        dota_obj_line += obj + ' ' + str(self.diffculty) + '\n'
                f.write(dota_obj_line)

    def save_dota_image(self, json_data, img_name, source_images_dir_path, dst_images_dir_path):
        sour_img_path = os.path.join(source_images_dir_path, img_name)
        dst_img_path = os.path.join(dst_images_dir_path, img_name)
        if (json_data['imageData'] is not None) and not os.path.exists(dst_img_path):
            img = utils.img_b64_to_arr(json_data['imageData'])
            PIL.Image.fromarray(img).save(dst_img_path)
        else:
            shutil.copyfile(sour_img_path, dst_img_path)
        return dst_img_path


if __name__ == '__main__':
    convertor = Labelme2Dota(source_dir='../exp_dataset/labelme_test', dst_dir='../exp_dataset/TDataset')
    convertor.convert()
