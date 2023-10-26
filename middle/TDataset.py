# -*- coding: utf-8 -*-
"""
# @file name : TDataset.py
# @author    : Csy
# @date      : 2023-07-24 21:25
# @brief     : 构建中间转换数据集
"""
import os


class TDataset():

    def __init__(self, type, source_path, dst_path='./', task='detect', is_copuled=True):
        self.source_path = source_path
        self.dst_path = dst_path
        self.type = type
        self.task = task
        # 标注和图片保持对应关系, 一个标注是一个记录
        self.anns = dict()
        self.cats = dict()
        self.imgs = dict()

        # check 路径下是否存在文件

    def getImageList(self):
        pass

    def getAnnList(self):
        pass

    def getImageAnnPairList(self):
        pass

    def parseJson(self):
        type = self.type
        path = self.source_path

        if type == 'coco':
            pass
        elif type == 'voc':
            pass
        elif type == 'cityscape':
            pass
        elif type == 'labelme' or type == 'labelme':
            pass
        else:
            raise Exception("unsupported dataset type")
