# -*- coding: UTF-8 -*-
"""
@File    ：Dataset_Meta.py
@Author  ：Csy
@Date    ：2023-09-06 15:30 
@Bref    : 描述不同 数据集 文件格式
@Ref     :
"""

Dataset_setting = {
    'coco': {
        'img_types': ['.jpg','.png','.bmp'],
        'anno_type': '.json',
        'no_split_dirs':['images','annotations'],
        'dirs': ['train', 'val', 'test', 'annotations']
    },
    'labelme': {
        'img_types': ['.jpg','.png','.bmp'],
        'anno_type': '.json',
        'dirs': ['images', 'labels']
    },
    'yolo': {
        'img_types': ['.jpg', '.png', '.bmp'],
        'anno_type': '.txt',
        'dirs': ['images', 'labels']
    },
    'dota': {
        'img_types': ['.png', '.bmp'],
        'anno_type': '.txt',
        'dirs': ['images', 'labelTxt']
    },
    'voc':
        {
            'img_types': ['.jpg','.png', '.bmp'],
            'anno_type': '.xml',
            'dirs': ['JPEGImages', 'Annotations', 'ImageSets\Main']
        }
}

TDATASET_PATH='../exp_dataset/TDataset'
class Constant():

    def __init__(self):
        pass
