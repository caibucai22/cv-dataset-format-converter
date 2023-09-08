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
        'dirs':['annotations','train','val','test']
    },
    'labelme': {
        'img_types': [],
        'anno_type': '.json',
        'dirs':['images','labels']
    },
    'yolo': {
        'img_types': ['.jpg','.png'],
        'anno_type': '.txt',
        'dirs':['images','labels']
    },
    'dota': {
        'img_types': [],
        'anno_type': '.txt'
    },
}


class Constant():

    def __init__(self):
        pass
