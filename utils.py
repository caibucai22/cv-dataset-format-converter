# -*- coding: utf-8 -*-
"""
# @file name : utils.py
# @author    : Csy
# @date      : 2023-07-01 17:33
# @brief     : 实现 部分依赖的 工具函数
"""
import os
from meta.Dataset_Meta import *


def print_dirs_info(source_dir):
    for root, dirs, files in os.walk(source_dir):
        for name in dirs:
            print(name)


def get_imgs(source_dir, dataset_type='coco'):
    postfixs = Dataset_setting[dataset_type]['img_types']  # 返回一个 []
    imgs = [img for img in os.listdir(source_dir) if os.path.splitext(img)[-1] in postfixs]
    return len(imgs), imgs


def get_Anns(source_dir, dataset_type='coco'):
    postfix = Dataset_setting[dataset_type]['anno_type']
    anns = [ann for ann in os.listdir(source_dir) if ann.endswith(postfix)]
    return len(anns), anns


def check_anno_file_exist(source_dir, type, exist_with_img=True):
    if type == 'coco':
        if os.path.exists(os.path.join(source_dir, 'annotations', 'annotation.json')):
            return True
    elif type == 'labelme':
        if exist_with_img:
            pass
        else:
            pass
    else:
        raise Exception("unsuport dataset type")
    return False


def getImageListFromSinge(source_dir):
    pass


def getImageListFromMulti(source_dir):
    pass


class BBoxUtils():
    @staticmethod
    def voc2yolo(size, box):
        dw = 1. / size[0]
        dh = 1. / size[1]
        x = (box[0] + box[1]) / 2.0
        y = (box[2] + box[3]) / 2.0
        w = box[1] - box[0]
        h = box[3] - box[2]
        x = x * dw
        w = w * dw
        y = y * dh
        h = h * dh
        return (x, y, w, h)

    def seg2bbox(self, seg):
        pass


if __name__ == '__main__':
    print_dirs_info('./exp_dataset')
