# -*- coding: UTF-8 -*-
"""
@File    ：coco2yolo.py
@Author  ：Csy
@Date    ：2023-09-12 14:40
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


class COCO2YOLO():

    def __init__(self, source_dir, dst_dir, ann_image_together=False,
                 source_dataset_type='coco', dst_dataset_type='yolo',
                 source_labels_txt_path='../exp_dataset/coco/classes.txt'):
        self.source_dir = source_dir
        self.dst_dir = dst_dir

        self.source_dataset_type = source_dataset_type
        self.dst_dataset_type = dst_dataset_type
        self.source_images_dir_path = os.path.join(source_dir,
                                                   Dataset_setting[self.source_dataset_type]['no_split_dirs'][0]
                                                   )
        self.source_labels_dir_path = self.source_images_dir_path
        self.source_labels_txt_path = source_labels_txt_path

        if not ann_image_together:
            self.source_labels_dir_path = os.path.join(source_dir,
                                                       Dataset_setting[self.source_dataset_type]['no_split_dirs'][-1])

        print("dst dir struct:")
        # 判断 文件夹 与 Dataset_Setting 要求的是否一致
        utils.check_and_create_dir(self.dst_dataset_type, dst_dir)
        self.dst_images_dir_path = os.path.join(dst_dir, Dataset_setting[self.dst_dataset_type]['dirs']
        [0])
        self.dst_labels_dir_path = os.path.join(dst_dir, Dataset_setting[self.dst_dataset_type]['dirs']
        [-1])

        # 根据用户是否提供
        # 1 遍历得到 2 用户提供
        # self.label_id_map = self.get_label_id_map(self.source_labels_dir_path)
        if self.source_labels_txt_path is not None:
            self.class_name_to_id, self.class_id_to_name = utils.get_label_id_map_with_txt(
                self.source_labels_txt_path, dataset_type='coco')

        # 打印 源文件夹下 目录情况
        print('src dir struct:')
        utils.print_dirs_info(source_dir)
        # 打印 目标文件夹下 目录情况
        print("dst dir struct:")
        utils.print_dirs_info(dst_dir)

        # 是否创建文件夹
        # utils.make_dirs()

        self.imgs_list, _ = utils.get_imgs(self.source_dir, dataset_type='coco')
        self.anns_list, _ = utils.get_Anns(self.source_dir, dataset_type='coco')

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
        json_path = os.path.join(self.source_labels_dir_path, 'annotations.json')
        json_data = json.load(open(json_path,'r'))
        # 建立图片名到id的映射
        images_info = json_data['images']
        image_to_id = {}
        id_to_ann = {}
        for image in images_info:
            image_to_id[image['file_name']] = image['id']
        # 建立id到annotations的映射
        anns_info = json_data['annotations']
        for ann in anns_info:
            if ann['image_id'] not in id_to_ann:
                id_to_ann[ann['image_id']] = []
            id_to_ann[ann['image_id']].append(ann)

        for img_name in self.imgs_list:
            img_id = image_to_id[img_name]
            img_ann = id_to_ann[img_id]

            img_path = self.save_yolo_image(json_data, img_name,
                                            self.source_images_dir_path, self.dst_images_dir_path)
            yolo_obj_list = self.get_yolo_object_list(img_ann, img_path)
            self.save_yolo_label(img_name, self.dst_labels_dir_path, yolo_obj_list)

        shutil.copy(self.source_dir + "/" + 'classes.txt', self.dst_dir + "/" + 'classes.txt')
        print('done!')

    def convert_one(self, json_name):
        json_path = os.path.join(self.source_labels_dir_path, json_name)
        json_data = json.load(open(json_path))

        img_path = self.save_yolo_image(json_data, json_name,
                                        self.source_images_dir_path, self.dst_images_dir_path)
        yolo_obj_list = self.get_yolo_object_list(json_data, img_path)
        self.save_yolo_label(json_name, self.dst_labels_dir_path, yolo_obj_list)

    def get_yolo_object_list(self, img_ann, img_path):
        yolo_obj_list = []

        img_h, img_w, _ = cv2.imread(img_path).shape
        for ann in img_ann:
            xmin, ymin, w, h = ann['bbox']
            xc, yc, norm_w, norm_h = utils.bbox_coco2yolo(xmin, ymin, w, h, img_w, img_h)
            class_id = ann['category_id']-1
            yolo_obj_list.append([class_id,xc, yc, norm_w, norm_h])

        return yolo_obj_list

    def get_yolo_circle_object(self, shape, img_h, img_w):
        obj_center_x, obj_center_y = shape['points'][0]

        radius = math.sqrt((obj_center_x - shape['points'][1][0]) ** 2 +
                           (obj_center_y - shape['points'][1][1]) ** 2)
        obj_w = 2 * radius
        obj_h = 2 * radius

        yolo_center_x = round(float(obj_center_x / img_w), 6)
        yolo_center_y = round(float(obj_center_y / img_h), 6)
        yolo_w = round(float(obj_w / img_w), 6)
        yolo_h = round(float(obj_h / img_h), 6)

        label_id = self.label_id_map[shape['label']]

        return label_id, yolo_center_x, yolo_center_y, yolo_w, yolo_h

    def get_other_shape_yolo_object(self, shape, img_h, img_w):
        def __get_object_desc(obj_port_list):
            __get_dist = lambda int_list: max(int_list) - min(int_list)

            x_lists = [port[0] for port in obj_port_list]
            y_lists = [port[1] for port in obj_port_list]

            return min(x_lists), __get_dist(x_lists), min(y_lists), __get_dist(y_lists)

        obj_x_min, obj_w, obj_y_min, obj_h = __get_object_desc(shape['points'])

        yolo_center_x = round(float((obj_x_min + obj_w / 2.0) / img_w), 6)
        yolo_center_y = round(float((obj_y_min + obj_h / 2.0) / img_h), 6)
        yolo_w = round(float(obj_w / img_w), 6)
        yolo_h = round(float(obj_h / img_h), 6)

        label_id = self.label_id_map[shape['label']]

        return label_id, yolo_center_x, yolo_center_y, yolo_w, yolo_h

    # compute polygon points # add by lll
    def get_yolo_polygon_object(self, shape, img_h, img_w):
        def get_points_list(obj_port_list):
            x_lists = [port[0] for port in obj_port_list]
            y_lists = [port[1] for port in obj_port_list]

            return x_lists, y_lists

        label_id_polygon_points = []
        label_id = self.label_id_map[shape['label']]
        label_id_polygon_points.append(label_id)

        x_lists, y_lists = get_points_list(shape['points'])
        for x_point, y_point in zip(x_lists, y_lists):
            yolo_x = round(float(x_point / img_w), 6)
            label_id_polygon_points.append(yolo_x)
            yolo_y = round(float(y_point / img_h), 6)
            label_id_polygon_points.append(yolo_y)

        return tuple(label_id_polygon_points)

    def save_yolo_label(self, img_name, label_dir_path, yolo_obj_list):
        txt_path = os.path.join(label_dir_path, img_name[:-4] + '.txt')

        with open(txt_path, 'w+') as f:  # lll
            for yolo_obj_idx, yolo_obj in enumerate(yolo_obj_list):
                if len(yolo_obj) > 5:  # lll
                    for point in yolo_obj:
                        point_line = '%s ' % point
                        f.write(point_line)
                    f.write('\n')
                else:
                    yolo_line = str(yolo_obj[0])
                    for itm in yolo_obj[1:]:
                        yolo_line += ' '+str(itm)

                    # yolo_obj_line = '%s %s %s %s %s\n' % yolo_obj \
                    #     if yolo_obj_idx + 1 != len(yolo_obj_list) else \
                    #     '%s %s %s %s %s' % yolo_obj
                    yolo_obj_line = yolo_line+'\n' if yolo_obj_idx+1 != len(yolo_obj_list) else yolo_line
                    f.write(yolo_obj_line)

    def save_yolo_image(self, json_data, img_name, source_images_dir_path, dst_images_dir_path):
        sour_img_path = os.path.join(source_images_dir_path, img_name)
        dst_img_path = os.path.join(dst_images_dir_path, img_name)
        if 'imageData' in json_data and json_data['imageData'] is not None and not os.path.exists(dst_img_path):
            img = utils.img_b64_to_arr(json_data['imageData'])
            PIL.Image.fromarray(img).save(dst_img_path)
        else:
            shutil.copyfile(sour_img_path, dst_img_path)
        return dst_img_path


if __name__ == '__main__':
    convertor = COCO2YOLO(source_dir='../exp_dataset/coco', dst_dir='../exp_dataset/yolo')
    convertor.convert()
