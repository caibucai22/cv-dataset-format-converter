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
        'img_types': [],
        'anno_type': '.json',
        'dirs': ['train', 'val','test','annotations']
    },
    'labelme': {
        'img_types': [],
        'anno_type': '.json',
        'dirs': ['images', 'labels']
    },
    'yolo': {
        'img_types': ['.jpg', '.png','.bmp'],
        'anno_type': '.txt',
        'dirs': ['images', 'labels']
    },
    'dota': {
        'img_types': ['.png','.bmp'],
        'anno_type': '.txt',
        'dirs': ['images', 'labelTxt']
    },
}


class Constant():

    def __init__(self):
        pass
