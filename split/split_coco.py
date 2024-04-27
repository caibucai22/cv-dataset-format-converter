# -*- coding: UTF-8 -*-
"""
@File    ：split_coco.py
@Author  ：Csy
@Date    ：2023-10-22 15:03 
@Bref    :
@Ref     :
"""

import os
import json
import numpy as np
import shutil
from sklearn.model_selection import train_test_split
from meta.Dataset_Meta import Dataset_setting
import utils


class CoCoSplit():

    def __init__(self, source_dir, dst_dir,
                 source_labels_txt_path=None,
                 test_val_size=0.2):
        self.source_dir = source_dir
        self.dst_dir = dst_dir
        self.test_val_size = test_val_size

        self.dataset_type = 'coco'

        self.source_images_dir_path = os.path.join(source_dir, Dataset_setting[self.dataset_type]['no_split_dirs']
        [0])
        self.source_labels_dir_path = os.path.join(source_dir, Dataset_setting[self.dataset_type]['no_split_dirs']
        [-1])
        self.source_labels_txt_path = source_labels_txt_path

        self.dst_labels_dir_path = os.path.join(dst_dir, Dataset_setting[self.dataset_type]['dirs']
        [-1])

    def convert(self):
        with open(self.source_labels_dir_path + '/' + 'annotations.json') as f:
            annotations_data = json.load(f)

        images = annotations_data["images"]
        annotations = annotations_data["annotations"]
        categories = annotations_data["categories"]

        train, test_val = train_test_split(images, test_size=self.test_val_size, random_state=0, shuffle=True)
        test, val = train_test_split(test_val, test_size=0.5, random_state=0, shuffle=True)

        train_folder = os.path.join(self.dst_dir, "train")
        val_folder = os.path.join(self.dst_dir, "val")
        test_folder = os.path.join(self.dst_dir, "test")

        os.makedirs(train_folder, exist_ok=True)
        os.makedirs(val_folder, exist_ok=True)
        os.makedirs(test_folder, exist_ok=True)

        for img in train:
            shutil.copy(os.path.join(self.source_images_dir_path, img["file_name"]),
                        os.path.join(train_folder, img["file_name"]))

        for img in val:
            shutil.copy(os.path.join(self.source_images_dir_path, img["file_name"]),
                        os.path.join(val_folder, img["file_name"]))

        for img in test:
            shutil.copy(os.path.join(self.source_images_dir_path, img["file_name"]),
                        os.path.join(test_folder, img["file_name"]))

        train_ann = utils.filter_annotations(annotations, [img["id"] for img in train])
        val_ann = utils.filter_annotations(annotations, [img["id"] for img in val])
        test_ann = utils.filter_annotations(annotations, [img["id"] for img in test])

        # 生成train.json, val.json, test.json
        train_json = {"images": train, "annotations": train_ann, "categories": categories}
        val_json = {"images": val, "annotations": val_ann, "categories": categories}
        test_json = {"images": test, "annotations": test_ann, "categories": categories}

        with open(os.path.join(self.dst_labels_dir_path, "train.json"), "w") as f:
            json.dump(train_json, f)

        with open(os.path.join(self.dst_labels_dir_path, "val.json"), "w") as f:
            json.dump(val_json, f)

        with open(os.path.join(self.dst_labels_dir_path, "test.json"), "w") as f:
            json.dump(test_json, f)

        print("done！")
