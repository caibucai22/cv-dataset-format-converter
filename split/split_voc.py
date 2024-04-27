# -*- coding: UTF-8 -*-
"""
@File    ：split_voc.py
@Author  ：Csy
@Date    ：2023-10-22 15:45 
@Bref    :
@Ref     :
"""

import os
from sklearn.model_selection import train_test_split
from meta.Dataset_Meta import Dataset_setting
import utils


class VocSplit():

    def __init__(self, source_dir, dst_dir,
                 source_labels_txt_path=None,
                 test_val_size=0.2):
        self.source_dir = source_dir
        self.dst_dir = dst_dir
        self.test_val_size = test_val_size

        self.dataset_type = 'voc'

        self.source_images_dir_path = os.path.join(source_dir, Dataset_setting[self.dataset_type]['dirs']
        [0])
        self.source_labels_dir_path = os.path.join(source_dir, Dataset_setting[self.dataset_type]['dirs']
        [1])
        self.source_labels_txt_path = source_labels_txt_path

        self.dst_labels_dir_path = os.path.join(dst_dir, Dataset_setting[self.dataset_type]['dirs']
        [-1])

        self.imgs_list, _ = utils.get_imgs(self.source_dir, dataset_type=self.dataset_type)
        self.anns_list, _ = utils.get_Anns(self.source_dir, dataset_type=self.dataset_type)

    def split(self):
        train, test_val = train_test_split(self.imgs_list, test_size=self.test_val_size, random_state=0, shuffle=True)
        test, val = train_test_split(test_val, test_size=0.5, random_state=0, shuffle=True)

        trainval_txt = open(os.path.join(self.dst_labels_dir_path, "trainval.txt"), "w")
        train_txt = open(os.path.join(self.dst_labels_dir_path, "train.txt"), "w")

        val_txt = open(os.path.join(self.dst_labels_dir_path, "val.json"), "w")
        test_txt = open(os.path.join(self.dst_labels_dir_path, "test.json"), "w")
        for img_name in self.imgs_list:
            name = img_name[:-4] + '\n'
            if img_name in train:
                train_txt.write(name)
                trainval_txt.write(name)
            elif img_name in val:
                val_txt.write(name)
                trainval_txt.write(name)
            else:
                test_txt.write(name)
        print('done!')
