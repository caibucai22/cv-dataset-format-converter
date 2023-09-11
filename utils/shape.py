# -*- coding: UTF-8 -*-
"""
@File    ：shape.py
@Author  ：Csy
@Date    ：2023-09-09 12:05 
@Bref    : 形状格式转换
@Ref     :
"""


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


def yolo_point_normalize(point_x, point_y, img_w, img_h):
    yolo_x = round(float(point_x / img_w), 6)
    yolo_y = round(float(point_y / img_h), 6)
    return yolo_x, yolo_y


def seg2bbox(self, seg):
    pass
