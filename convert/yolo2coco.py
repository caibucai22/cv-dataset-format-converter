# -*- coding: UTF-8 -*-
"""
@File    ：yolo2coco.py
@Author  ：Csy
@Date    ：2023-10-17 18:58 
@Bref    :
@Ref     :
TODO 实现基于源数据来制造数据集，包括数据集划分 ，现有版本不支持，只支持从数据转为COCO格式 转换完成是一个整体的数据集
"""
import os, shutil
import json
from datetime import date, datetime

import cv2
from meta.Dataset_Meta import Dataset_setting
import utils


class YOLO2COCO():

    def __init__(self, source_dir, dst_dir,
                 source_dataset_type='yolo', dst_datatset_type='coco',
                 source_labels_txt_path=None,
                 ann_image_together=False):
        self.today = datetime.today().strftime('%Y-%m-%d')
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

        print('dst_dir struct:')
        utils.check_and_create_dir(self.dst_dataset_type, dst_dir)

        self.dst_images_dir_path = os.path.join(dst_dir, Dataset_setting[self.dst_dataset_type]['no_split_dirs']
        [0])
        self.dst_labels_dir_path = os.path.join(dst_dir, Dataset_setting[self.dst_dataset_type]['no_split_dirs']
        [-1])

        # 根据用户是否提供
        # 1 遍历得到 2 用户提供
        if self.source_labels_txt_path is not None:
            self.class_name_to_id, self.class_id_to_name = utils.get_label_id_map_with_txt(
                self.source_labels_txt_path)

        # 打印 源文件夹下 目录情况
        print('src dir struct:')
        utils.print_dirs_info(source_dir)

        self.imgs_list, _ = utils.get_imgs(self.source_dir, dataset_type='yolo')
        self.anns_list, _ = utils.get_Anns(self.source_dir, dataset_type='yolo')

        if self.anns_list[0] == 'classes.txt':
            self.anns_list = self.anns_list[1:]

    def convert(self):
        categories = []  # 存储类别的列表
        for id, label in self.class_id_to_name.items():
            categories.append({'id': id + 1, 'name': label, 'supercategory': 'None'})

        write_json_context = dict()  # 写入.json文件的大字典
        write_json_context['info'] = {'description': '', 'url': '', 'version': '', 'year': 2021, 'contributor': '',
                                      'date_created': '2021-07-25'}
        write_json_context['licenses'] = [{'id': 1, 'name': None, 'url': None}]
        write_json_context['categories'] = categories
        write_json_context['images'] = []
        write_json_context['annotations'] = []

        # process images annotations key

        for i, (img_name, label_name) in enumerate(zip(self.imgs_list, self.anns_list)):
            print(img_name)
            img_h, img_w, img_c = cv2.imread(self.source_images_dir_path + '/' + img_name).shape

            img_context = {}
            img_context['file_name'] = img_name
            img_context['height'] = img_h
            img_context['width'] = img_w
            img_context['date_captured'] = self.today
            img_context['id'] = i  # 该图片的id
            img_context['license'] = 1
            img_context['color_url'] = ''
            img_context['flickr_url'] = ''
            write_json_context['images'].append(img_context)

            with open(os.path.join(self.source_labels_dir_path, label_name), 'r') as yolo_file:
                yolo_lines = yolo_file.readlines()

                for j, line in enumerate(yolo_lines):
                    bbox_dict = {}

                    class_id, x, y, w, h = line.strip().split(' ')
                    class_id, x, y, w, h = int(class_id), float(x), float(y), float(w), float(h)

                    xmin, ymin, w, h = utils.bbox_yolo2coco(x, y, w, h, img_w, img_h)
                    xmax = xmin+w
                    ymax = ymin+h
                    # w = w * img_w
                    # h = h * img_h

                    bbox_dict['id'] = i * 10000 + j  # bounding box的坐标信息
                    bbox_dict['image_id'] = i
                    bbox_dict['category_id'] = class_id + 1  # plus 1
                    bbox_dict['iscrowd'] = 0
                    # height, width = abs(ymax - ymin), abs(xmax - xmin)
                    bbox_dict['area'] = w * h
                    bbox_dict['bbox'] = [xmin, ymin, w, h]
                    bbox_dict['segmentation'] = [[xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax]]

                    write_json_context['annotations'].append(bbox_dict)
                yolo_file.close()
            shutil.copy(self.source_images_dir_path + "/" + img_name, self.dst_images_dir_path + "/" + img_name)

        shutil.copy(self.source_dir + "/" + 'classes.txt', self.dst_dir + "/" + 'classes.txt')
        with open(self.dst_labels_dir_path + '/' + "annotations" + '.json', 'w') as anno_file:
            json.dump(write_json_context, anno_file, indent=2)


if __name__ == '__main__':
    # convertor = YOLO2COCO(source_dir='../exp_dataset/yolo', dst_dir='../exp_dataset/TDataset',
    #                       source_labels_txt_path='../exp_dataset/yolo/labels/classes.txt')
    convertor = YOLO2COCO(source_dir=r'E:\datasets\new_ScratchDataset3', dst_dir=r'E:\datasets\Scratch3CoCo',
                          source_labels_txt_path=r'E:\datasets\new_ScratchDataset3\classes.txt')
    convertor.convert()
