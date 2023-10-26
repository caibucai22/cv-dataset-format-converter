# -*- coding: UTF-8 -*-
"""
@File    ：xx2yy.py
@Author  ：Csy
@Date    ：2023-09-27 10:31 
@Bref    :
@Ref     :
"""
import os
import json
from collections import OrderedDict

from utils import util
from meta.Dataset_Meta import Dataset_setting


class XX2YY():

    def __init__(self, source_dir, dst_dir,
                 source_dataset_type, dst_datatset_type,
                 source_labels_txt_path=None,
                 ann_image_together=True, test_size=0.1,
                 val_size=0.11):

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
            dst_dirs = util.print_dirs_info(dst_dir, display=False)
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

        self.imgs_list, _ = util.get_imgs(self.source_dir, dataset_type=self.source_dataset_type)
        self.anns_list, _ = utils.get_Anns(self.source_dir, dataset_type=self.source_dataset_type)

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

if __name__ == '__main__':
    model = XX2YY(source_dir='../exp_dataset/labelme', dst_dir='../exp_dataset/TDataset',
                  source_dataset_type='labelme', dst_datatset_type='coco')
