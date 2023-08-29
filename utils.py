# -*- coding: utf-8 -*-
"""
# @file name : utils.py
# @author    : Csy
# @date      : 2023-07-01 17:33
# @brief     : 实现 部分依赖的 工具函数
"""


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
