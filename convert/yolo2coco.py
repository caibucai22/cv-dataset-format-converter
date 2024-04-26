# -*- coding: UTF-8 -*-
"""
@File    ：yolo2coco.py
@Author  ：Csy
@Date    ：2023-10-17 18:58 
@Bref    :
@Ref     :
TODO 实现基于源数据来制造数据集，包括数据集划分 ，现有版本不支持，只支持从数据转为COCO格式 转换完成是一个整体的数据集
TODO 实现方式 1 增加一个专门划分 dataset 的类 来执行
"""
import os, shutil
import json
from datetime import date, datetime

import cv2
from meta.Dataset_Meta import Dataset_setting
import utils
from sklearn.model_selection import train_test_split


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
                self.source_labels_txt_path, 'coco')

        # 打印 源文件夹下 目录情况
        print('src dir struct:')
        utils.print_dirs_info(source_dir)

        self.imgs_list, _ = utils.get_imgs(self.source_dir, dataset_type='yolo')
        self.anns_list, _ = utils.get_Anns(self.source_dir, dataset_type='yolo')

        if self.anns_list[0] == 'classes.txt':
            self.anns_list = self.anns_list[1:]

    def convert(self, only_json=False):
        categories = []  # 存储类别的列表
        # for coco has +1
        for id, label in self.class_id_to_name.items():
            categories.append({'id': id, 'name': label, 'supercategory': 'None'})

        write_json_context = dict()  # 写入.json文件的大字典
        write_json_context['info'] = {'description': '', 'url': '', 'version': '', 'year': self.today[:4],
                                      'contributor': '',
                                      'date_created': self.today}
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
                    xmax = xmin + w
                    ymax = ymin + h
                    # w = w * img_w
                    # h = h * img_h

                    bbox_dict['id'] = i * 10000 + j  # bounding box的坐标信息
                    bbox_dict['image_id'] = i
                    bbox_dict['category_id'] = self.class_name_to_id[self.class_id_to_name[
                        class_id + 1]]  # plus 1 # class_id:yolo start 0 class_id_to_name:{0:bac,1:c1,2:c2}
                    bbox_dict['iscrowd'] = 0
                    # height, width = abs(ymax - ymin), abs(xmax - xmin)
                    bbox_dict['area'] = w * h
                    bbox_dict['bbox'] = [xmin, ymin, w, h]
                    bbox_dict['segmentation'] = [[xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax]]

                    write_json_context['annotations'].append(bbox_dict)
                yolo_file.close()
            if not only_json:
                shutil.copy(self.source_images_dir_path + "/" + img_name, self.dst_images_dir_path + "/" + img_name)

        with open(self.dst_labels_dir_path + '/' + "annotations" + '.json', 'w') as anno_file:
            json.dump(write_json_context, anno_file, indent=2)

        if self.source_labels_txt_path is None:
            shutil.copy(self.source_dir + "/" + 'classes.txt', self.dst_dir + "/" + 'classes.txt')
        else:
            shutil.copy(self.source_labels_txt_path, self.dst_dir + "/" + 'classes.txt')

    def convert_single(self, imgs_list, anns_list, type, only_json=True):
        categories = []  # 存储类别的列表
        # for coco has +1
        for id, label in self.class_id_to_name.items():
            categories.append({'id': id, 'name': label, 'supercategory': 'None'})

        write_json_context = dict()  # 写入.json文件的大字典
        write_json_context['info'] = {'description': '', 'url': '', 'version': '', 'year': self.today[:4],
                                      'contributor': '',
                                      'date_created': self.today}
        write_json_context['licenses'] = [{'id': 1, 'name': None, 'url': None}]
        write_json_context['categories'] = categories
        write_json_context['images'] = []
        write_json_context['annotations'] = []

        # process images annotations key

        for i, (img_name, label_name) in enumerate(zip(imgs_list, anns_list)):
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
                    xmax = xmin + w
                    ymax = ymin + h
                    # w = w * img_w
                    # h = h * img_h

                    bbox_dict['id'] = i * 10000 + j  # bounding box的坐标信息
                    bbox_dict['image_id'] = i
                    bbox_dict['category_id'] = self.class_name_to_id[self.class_id_to_name[
                        class_id + 1]]  # plus 1 # class_id:yolo start 0 class_id_to_name:{0:bac,1:c1,2:c2}
                    bbox_dict['iscrowd'] = 0
                    # height, width = abs(ymax - ymin), abs(xmax - xmin)
                    bbox_dict['area'] = w * h
                    bbox_dict['bbox'] = [xmin, ymin, w, h]
                    bbox_dict['segmentation'] = [[xmin, ymin, xmax, ymin, xmax, ymax, xmin, ymax]]

                    write_json_context['annotations'].append(bbox_dict)
                yolo_file.close()
            if not only_json:
                shutil.copy(self.source_images_dir_path + "/" + img_name, self.dst_images_dir_path + "/" + img_name)

        with open(self.dst_labels_dir_path + '/' + type + '.json', 'w') as anno_file:
            json.dump(write_json_context, anno_file, indent=2)

        if self.source_labels_txt_path is None:
            shutil.copy(self.source_dir + "/" + 'classes.txt', self.dst_dir + "/" + 'classes.txt')
        else:
            shutil.copy(self.source_labels_txt_path, self.dst_dir + "/" + 'classes.txt')

    def build_dataset(self, test_size, val_size, no_test=False):
        jsons = ['train.json', 'val.json', 'test.json']

        train, test = train_test_split(self.imgs_list, test_size=test_size, shuffle=True, random_state=0)
        train, val = train_test_split(train, test_size=val_size, shuffle=True, random_state=0)

        ann_train = [os.path.splitext(img_name)[0] + Dataset_setting['yolo']['anno_type'] for img_name in train]
        ann_val = [os.path.splitext(img_name)[0] + Dataset_setting['yolo']['anno_type'] for img_name in val]
        ann_test = [os.path.splitext(img_name)[0] + Dataset_setting['yolo']['anno_type'] for img_name in test]

        train_dir_path = os.path.join(self.dst_dir, 'train')
        val_dir_path = os.path.join(self.dst_dir, 'val')
        test_dir_path = os.path.join(self.dst_dir, 'test')

        os.makedirs(train_dir_path, exist_ok=True)
        os.makedirs(val_dir_path, exist_ok=True)
        os.makedirs(test_dir_path, exist_ok=True)

        for img in train:
            shutil.copy(self.source_images_dir_path + "/" + img, os.path.join(train_dir_path, img))
        for img in val:
            shutil.copy(self.source_images_dir_path + "/" + img, os.path.join(val_dir_path, img))
        for img in test:
            shutil.copy(self.source_images_dir_path + "/" + img, os.path.join(test_dir_path, img))

        self.convert_single(train, ann_train, type='train')
        self.convert_single(val, ann_val, type='val')
        self.convert_single(test, ann_test, type='test')

        print("building dataset complete.")


if __name__ == '__main__':
    # convertor = YOLO2COCO(source_dir='../exp_dataset/yolo', dst_dir='../exp_dataset/TDataset',
    #                       source_labels_txt_path='../exp_dataset/yolo/labels/classes.txt')

    convertor = YOLO2COCO(source_dir=r'E:\datasets\data',
                          dst_dir=r'E:\datasets\TestDataset',
                          source_labels_txt_path=r'E:\datasets\new_ScratchDataset3\classes.txt',ann_image_together=True)
    # convertor.convert(only_json=True)
    convertor.build_dataset(0.1,0.1)