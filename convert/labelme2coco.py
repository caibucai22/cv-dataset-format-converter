# -*- coding: UTF-8 -*-
"""
@File    ：labelme2dota.py
@Author  ：Csy
@Date    ：2023-09-11 21:28
@Bref    :
@Ref     :
"""
import collections
import json
import os
import math
import shutil
import uuid

import numpy as np
import cv2
import imgviz
from pycocotools import mask as pycoco_mask
import pycocotools
import PIL.Image
from sklearn.model_selection import train_test_split
from collections import OrderedDict

from meta.Dataset_Meta import *
import utils
from utils.Exception import *
from meta import COCO_Meta
# import label_file as labelfile
from convert import label_file as labelfile


class Labelme2COCO():

    # 0.9x = 0.1
    def __init__(self, source_dir, dst_dir,
                 source_dataset_type='labelme', dst_dataset_type='coco',
                 source_labels_txt_path=None,
                 ann_image_together=False, test_size=0.1,
                 val_size=0.11):
        self.source_dir = source_dir
        self.dst_dir = dst_dir

        self.source_dataset_type = 'labelme'
        self.dst_dataset_type = 'coco'

        self.dst_template = self.generate_template(COCO_Meta)

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

        self.dst_images_dir_path = os.path.join(dst_dir, Dataset_setting[self.dst_dataset_type]['no_split_dirs']
        [0])
        self.dst_labels_dir_path = os.path.join(dst_dir, Dataset_setting[self.dst_dataset_type]['no_split_dirs']
        [-1])
        # if self.dst_dataset_type == 'coco':
        #     # coco annotations test train val
        #     dst_dirs = utils.print_dirs_info(dst_dir, display=False)
        #     # test train val
        #     self.dst_images_dir_path = [os.path.join(self.dst_dir, dir) for dir in dst_dirs if
        #                                 dir not in ['annotations']]

        # 根据用户是否提供
        # 1 遍历得到 2 用户提供
        # self.label_id_map = self.get_label_id_map(self.source_labels_dir_path)
        # self.class_name_to_id = self.get_label_id_map_with_txt(self.source_labels_txt_path)

        # for coco use local get_label_id_map_with_txt() func
        if self.source_labels_txt_path is not None and self.dst_dataset_type == 'coco':
            self.class_name_to_id = self.get_label_id_map_with_txt(
                self.source_labels_txt_path)

        # 打印 源文件夹下 目录情况
        print('src dir struct:')
        utils.print_dirs_info(source_dir)

        self.imgs_list, _ = utils.get_imgs(self.source_dir, dataset_type='labelme')
        self.anns_list, _ = utils.get_Anns(self.source_dir, dataset_type='labelme')

        # 划分数据集
        train_img, test_img, train_label, test_label = train_test_split(self.imgs_list, self.anns_list,
                                                                        test_size=test_size, shuffle=True)
        train_img, val_img, train_label, val_label = train_test_split(train_img, train_label,
                                                                      test_size=val_size, shuffle=True)
        self.dst_subdir_image_list = [test_img, train_img, val_img]
        self.dst_subdir_label_list = [test_label, train_label, val_label]

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

    def get_label_id_map_with_txt(self, label_txt_path):
        class_name_to_id = {}
        for i, line in enumerate(open(label_txt_path).readlines()):
            class_id = i - 1  # starts with -1
            class_name = line.strip()
            if class_id == -1:
                assert class_name == "__ignore__"
                continue
            class_name_to_id[class_name] = class_id
            self.dst_template["categories"].append(
                dict(
                    supercategory=None,
                    id=class_id,
                    name=class_name,
                )
            )
        return class_name_to_id

    def generate_template(self, Dataset_Meta):
        template = Dataset_Meta.meta_key
        for key, value in Dataset_Meta.meta_key.items():
            if key == 'type':
                continue
            if key == 'info':
                template[key] = Dataset_Meta.info_key
            elif key == 'licenses':
                template[key].append(Dataset_Meta.license_key)
            elif key in ['categories', 'images', 'annotations']:
                # template[key].append(Dataset_Meta.category_key)
                template[key] = []
            else:
                raise Exception(f"not key {key} in coco meta info")
        template["type"] = 'instances'
        return template

    def convert(self):

        out_ann_file = os.path.join(self.dst_labels_dir_path, "annotations.json")
        image_id = 0
        # fix no categories
        for img_name, json_name in zip(self.imgs_list, self.anns_list):
            # 处理图片
            out_img_path = os.path.join(self.dst_images_dir_path, img_name)
            # 获取图像属性
            label_file = labelfile.LabelFile(filename=self.source_labels_dir_path + '/' + json_name)
            img = utils.img_data_to_arr(label_file.imageData)
            imgviz.io.imsave(out_img_path, img)

            # json
            self.dst_template["images"].append(
                dict(
                    license=0,
                    url=None,
                    # file_name=os.path.relpath(out_img_path, os.path.dirname(out_ann_file)),
                    file_name=img_name,
                    height=img.shape[0],
                    width=img.shape[1],
                    date_captured=None,
                    id=image_id,
                )
            )
            image_id += 1

            # for area
            masks = {}
            segmentations = collections.defaultdict(list)
            for shape in label_file.shapes:
                points = shape["points"]
                label = shape["label"]
                group_id = shape.get("group_id")
                shape_type = shape.get("shape_type", "polygon")
                mask = utils.shape_to_mask(img.shape[:2], points, shape_type)

                if group_id is None:
                    group_id = uuid.uuid1()
                instance = (label, group_id)

                if instance in masks:
                    masks[instance] = masks[instance] | mask  # fix error
                else:
                    masks[instance] = mask

                if shape_type == "rectangle":
                    (x1, y1), (x2, y2) = points
                    x1, x2 = sorted([x1, x2])
                    y1, y2 = sorted([y1, y2])
                    points = [x1, y1, x2, y1, x2, y2, x1, y2]
                if shape_type == 'circle':
                    (x1, y1), (x2, y2) = points
                    r = np.linalg.norm([x2 - x1, y2 - y1])
                    n_points_circle = max(int(np.pi / np.arcos(1 - 1 / r)), 12)
                    i = np.arange(n_points_circle)
                    x = x1 + r * np.sin(2 * np.pi / n_points_circle * i)
                    y = y1 + r * np.cos(2 * np.pi / n_points_circle * i)
                    points = np.stack((x, y), axis=1).flatten().tolist()
                else:
                    points = np.asarray(points).flatten().tolist()

                segmentations[instance].append(points)
            segmentations = dict(segmentations)
            for instance, mask in masks.items():
                cls_name, group_id = instance
                if cls_name not in self.class_name_to_id:
                    continue
                cls_id = self.class_name_to_id[cls_name]

                mask = np.asfortranarray(mask.astype(np.uint8))
                mask = pycoco_mask.encode(mask)
                area = float(pycoco_mask.area(mask))
                bbox = pycoco_mask.toBbox(mask).flatten().tolist()

                self.dst_template['annotations'].append(
                    dict(
                        id=len(self.dst_template["annotations"]),
                        image_id=image_id,
                        category_id=cls_id,
                        segmentation=segmentations[instance],
                        area=area,
                        bbox=bbox,
                        iscrowd=0,
                    )
                )
        with open(out_ann_file, 'w') as f:
            json.dump(self.dst_template, f, indent=2)
        # fix
        if self.source_labels_txt_path is None:
            shutil.copy(self.source_dir + "/" + 'classes.txt', self.dst_dir + "/" + 'classes.txt')
        else:
            shutil.copy(self.source_labels_txt_path, self.dst_dir + "/" + 'classes.txt')

        # print('done!')

    # for img_name, json_name in zip(self.imgs_list, self.anns_list):
    #     json_path = os.path.join(self.source_labels_dir_path, json_name)
    #     json_data = json.load(open(json_path))
    #
    #     img_path = self.save_dota_image(json_data, img_name,
    #                                     self.source_images_dir_path, self.dst_images_dir_path)
    #     dota_obj_list = self.get_dota_object_list(json_data, img_path)
    #     self.save_dota_label(json_name, self.dst_labels_dir_path, dota_obj_list)

    def convert_one(self, json_name):
        json_path = os.path.join(self.source_labels_dir_path, json_name)
        json_data = json.load(open(json_path))

        img_path = self.save_coco_image(json_data, json_name,
                                        self.source_images_dir_path, self.dst_images_dir_path)
        dota_obj_list = self.get_dota_object_list(json_data, img_path)
        self.save_coco_label(json_name, self.dst_labels_dir_path, dota_obj_list)

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

    def save_coco_label(self, json_name, label_dir_path, dota_obj_list):
        txt_path = os.path.join(label_dir_path, json_name.replace('.json', '.txt'))

    def save_coco_image(self, json_data, img_name, source_images_dir_path, dst_images_dir_path):
        sour_img_path = os.path.join(source_images_dir_path, img_name)
        dst_img_path = os.path.join(dst_images_dir_path, img_name)
        if (json_data['imageData'] is not None) and not os.path.exists(dst_img_path):
            img = utils.img_b64_to_arr(json_data['imageData'])
            PIL.Image.fromarray(img).save(dst_img_path)
        else:
            shutil.copyfile(sour_img_path, dst_img_path)
        return dst_img_path


if __name__ == '__main__':
    convertor = Labelme2COCO(source_dir=r'D:\labelme-main\examples\instance_segmentation\data_annotated',
                             dst_dir=r'D:\labelme-main\examples\instance_segmentation\test_my',
                             source_labels_txt_path=r'D:\labelme-main\examples\instance_segmentation\labels.txt',
                             ann_image_together=True)
    # convertor.generate_template(COCO_Meta)
    convertor.convert()
