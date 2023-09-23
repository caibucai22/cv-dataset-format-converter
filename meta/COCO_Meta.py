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

info_key = {"descrption": None,
            "url": None,
            "version": None,
            "year": None,
            "contributor": None,
            "date_created": None
            }
license_key = {"url": None,
               "id": None,
               "name": None
               }
category_key = {"supercategory": None,
                "id": None,
                "name": None
                }
annotation_key = {"segmentation": None,
                  "area": None,
                  "iscrowd": None,
                  "image_id": None,
                  "bbox": None,
                  "category_id": None,
                  "id": None}
