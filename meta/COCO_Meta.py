# -*- coding: UTF-8 -*-
"""
@File    ：COCO_Meta.py
@Author  ：Csy
@Date    ：2023-08-30 18:40 
@Bref    :
@Ref     :
"""

meta_key = {
    "info": {},
    "licenses": [],
    "categories": [],
    "type": "",
    "images": [],
    "annotations": []
}

info_key = {"descrption", "url", "version", "year", "contributor", "date_created"}
license_key = {"url","id","name"}
category_key = {"supercategory","id","name"}
annotation_key = {"segmentation", "area", "iscrowd", "image_id", "bbox", "category_id", "id"}
