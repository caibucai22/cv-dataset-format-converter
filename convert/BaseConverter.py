# -*- coding: UTF-8 -*-
"""
@File    ：BaseConverter.py
@Author  ：Csy
@Date    ：2024/4/26 20:18 
@Bref    :
@Ref     :
TODO     :
         :
"""
import os

import utils
from utils import Exception as EXCEPTION_DEFINE
from meta.Dataset_Meta import Dataset_setting
class BaseConverter(object):

    def __init__(self,source_dir,dst_dir,
                 source_dataset_type,dst_dataset_type,
                 source_labels_txt_path,
                 ann_img_together=False):
        self.source_dir = source_dir
        self.dst_dir = dst_dir

        self.source_dataset_type =source_dataset_type
        self.dst_dataset_type =dst_dataset_type

        self.source_labels_txt_path =source_labels_txt_path

        self.source_images_dir_path = os.path.join(source_dir, Dataset_setting[self.source_dataset_type]['dirs']
        [0])
        self.source_labels_txt_path = self.source_images_dir_path

        if not ann_img_together:
            self.source_labels_dir_path = os.path.join(source_dir,
                                                       Dataset_setting[self.source_dataset_type]['dirs'][-1])

    def get_label2id_mapping(self):
        if Dataset_setting[self.source_dataset_type]['anno_type'] == '.txt':
            if not self.source_labels_txt_path:
                raise Exception(EXCEPTION_DEFINE.NOT_PROVIDE_CLASSES_TXT)
            utils.get_label_id_map_with_txt(self.source_labels_txt_path)
        if Dataset_setting[self.source_dataset_type]['anno_type'] == '.json':
            pass


        
