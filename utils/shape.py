# -*- coding: UTF-8 -*-
"""
@File    ：shape.py
@Author  ：Csy
@Date    ：2023-09-09 12:05 
@Bref    : 形状格式转换
@Ref     :
"""
import math
import uuid

import numpy as np
import PIL.Image
import PIL.ImageDraw
import logger


def bbox_yolo2dota(x, y, w, h, img_w, img_h):
    x, y, w, h = x * img_w, y * img_h, w * img_w, h * img_h
    x1, y1 = x - w / 2, y - h / 2
    x2, y2 = x + w / 2, y - h / 2
    x3, y3 = x + w / 2, y + h / 2
    x4, y4 = x - w / 2, y + h / 2
    # x1, y1 = (x - w / 2) * img_w, (y - h / 2) * img_h
    # x2, y2 = (x + w / 2) * img_w, (y - h / 2) * img_h
    # x3, y3 = (x + w / 2) * img_w, (y + h / 2) * img_h
    # x4, y4 = (x - w / 2) * img_w, (y + h / 2) * img_h

    return [x1, y1, x2, y2, x3, y3, x4, y4]


def bbox_dota2yolo(points, img_w, img_h):
    # 转换成像素坐标
    x1, y1, x2, y2, x3, y3, x4, y4 = points
    w, h = x3 - x1, y3 - y1
    xc = (x3 + x1) / 2
    yc = (y3 + y1) / 2
    xc, yc = xc / img_w, yc / img_h
    w, h = w / img_w, h / img_h
    return xc, yc, w, h

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

def polygons_to_mask(img_shape, polygons, shape_type=None):
    logger.warning(
        "The 'polygons_to_mask' function is deprecated, "
        "use 'shape_to_mask' instead."
    )
    return shape_to_mask(img_shape, points=polygons, shape_type=shape_type)


def shape_to_mask(
    img_shape, points, shape_type=None, line_width=10, point_size=5
):
    mask = np.zeros(img_shape[:2], dtype=np.uint8)
    mask = PIL.Image.fromarray(mask)
    draw = PIL.ImageDraw.Draw(mask)
    xy = [tuple(point) for point in points]
    if shape_type == "circle":
        assert len(xy) == 2, "Shape of shape_type=circle must have 2 points"
        (cx, cy), (px, py) = xy
        d = math.sqrt((cx - px) ** 2 + (cy - py) ** 2)
        draw.ellipse([cx - d, cy - d, cx + d, cy + d], outline=1, fill=1)
    elif shape_type == "rectangle":
        assert len(xy) == 2, "Shape of shape_type=rectangle must have 2 points"
        draw.rectangle(xy, outline=1, fill=1)
    elif shape_type == "line":
        assert len(xy) == 2, "Shape of shape_type=line must have 2 points"
        draw.line(xy=xy, fill=1, width=line_width)
    elif shape_type == "linestrip":
        draw.line(xy=xy, fill=1, width=line_width)
    elif shape_type == "point":
        assert len(xy) == 1, "Shape of shape_type=point must have 1 points"
        cx, cy = xy[0]
        r = point_size
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=1, fill=1)
    else:
        assert len(xy) > 2, "Polygon must have points more than 2"
        draw.polygon(xy=xy, outline=1, fill=1)
    mask = np.array(mask, dtype=bool)
    return mask


def shapes_to_label(img_shape, shapes, label_name_to_value):
    cls = np.zeros(img_shape[:2], dtype=np.int32)
    ins = np.zeros_like(cls)
    instances = []
    for shape in shapes:
        points = shape["points"]
        label = shape["label"]
        group_id = shape.get("group_id")
        if group_id is None:
            group_id = uuid.uuid1()
        shape_type = shape.get("shape_type", None)

        cls_name = label
        instance = (cls_name, group_id)

        if instance not in instances:
            instances.append(instance)
        ins_id = instances.index(instance) + 1
        cls_id = label_name_to_value[cls_name]

        mask = shape_to_mask(img_shape[:2], points, shape_type)
        cls[mask] = cls_id
        ins[mask] = ins_id

    return cls, ins


def labelme_shapes_to_label(img_shape, shapes):
    logger.warn(
        "labelme_shapes_to_label is deprecated, so please use "
        "shapes_to_label."
    )

    label_name_to_value = {"_background_": 0}
    for shape in shapes:
        label_name = shape["label"]
        if label_name in label_name_to_value:
            label_value = label_name_to_value[label_name]
        else:
            label_value = len(label_name_to_value)
            label_name_to_value[label_name] = label_value

    lbl, _ = shapes_to_label(img_shape, shapes, label_name_to_value)
    return lbl, label_name_to_value


def masks_to_bboxes(masks):
    if masks.ndim != 3:
        raise ValueError(
            "masks.ndim must be 3, but it is {}".format(masks.ndim)
        )
    if masks.dtype != bool:
        raise ValueError(
            "masks.dtype must be bool type, but it is {}".format(masks.dtype)
        )
    bboxes = []
    for mask in masks:
        where = np.argwhere(mask)
        (y1, x1), (y2, x2) = where.min(0), where.max(0) + 1
        bboxes.append((y1, x1, y2, x2))
    bboxes = np.asarray(bboxes, dtype=np.float32)
    return bboxes

# pycocotools mask.encode
