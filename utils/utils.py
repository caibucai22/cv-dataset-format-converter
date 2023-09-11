# -*- coding: utf-8 -*-
"""
# @file name : utils.py
# @author    : Csy
# @date      : 2023-07-01 17:33
# @brief     : 实现 部分依赖的 工具函数
"""
import os
import shutil
from meta.Dataset_Meta import *
from utils.Exception import *
from utils.image import *


def print_dirs_info(source_dir):
    for root, dirs, files in os.walk(source_dir):
        for name in dirs:
            print(name)


def get_imgs(source_dir, dataset_type):
    imgs = []
    if dataset_type == 'coco':
        pass
    elif dataset_type == 'yolo':
        imgs = getImageListFromMulti(source_dir, dataset_type='yolo')
    elif dataset_type == 'labelme':
        imgs = getImageListFromMulti(source_dir, dataset_type='yolo')
    else:
        raise Exception(UNSUPPORTED_DATASET_TYPE)
    return sorted(imgs), len(imgs),


def get_Anns(source_dir, dataset_type='coco'):
    postfix = Dataset_setting[dataset_type]['anno_type']
    anns = []
    if dataset_type == 'coco':
        pass
    elif dataset_type == 'yolo':
        anns = getAnnListFromMulti(source_dir, dataset_type='yolo')
    elif dataset_type == 'labelme':
        anns = getAnnListFromMulti(source_dir, dataset_type='labelme')
    else:
        raise Exception(UNSUPPORTED_DATASET_TYPE)
    return anns, len(anns),


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
        raise Exception(UNSUPPORTED_DATASET_TYPE)
    return False


def getImageListFromSinge(source_dir):
    pass


def getImageListFromMulti(source_dir, dataset_type):
    sub_dirs = Dataset_setting[dataset_type]['dirs']
    postfixs = Dataset_setting[dataset_type]['img_types']
    img_list = []
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if os.path.splitext(file)[-1] in postfixs:
                img_list.append(file)
    # for dir in sub_dirs:
    #     imgs = [img for img in os.listdir(source_dir) if os.path.splitext(img)[-1] in postfixs]
    #     img_list += imgs
    return img_list


def getAnnListFromMulti(source_dir, dataset_type):
    sub_dirs = Dataset_setting[dataset_type]['dirs']
    postfix = Dataset_setting[dataset_type]['anno_type']
    ann_list = []
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(postfix):
                ann_list.append(file)
    return ann_list


def save_dota_image(json_data, img_name, source_images_dir_path, dst_images_dir_path):
    sour_img_path = os.path.join(source_images_dir_path, img_name)
    dst_img_path = os.path.join(dst_images_dir_path, img_name)
    if json_data is not None and (json_data['imageData'] is not None) and not os.path.exists(dst_img_path):
        img = img_b64_to_arr(json_data['imageData'])
        PIL.Image.fromarray(img).save(dst_img_path)
    else:
        shutil.copyfile(sour_img_path, dst_img_path)
    return dst_img_path

if __name__ == '__main__':
    # test
    # print_dirs_info('./exp_dataset')
    source_dir = '../exp_dataset/labelme'
    # img_list = getImageListFromMulti('./exp_dataset/yolo', dataset_type='yolo')
    # print(img_list)
    # ann_list = getAnnListFromMulti('./exp_dataset/yolo',dataset_type='yolo')
    # print(ann_list)

    # imgs_list, imgs_len = get_imgs(source_dir, dataset_type='labelme')
    # anns_list, anns_len = get_Anns(source_dir, dataset_type='labelme')
    # print(imgs_list)
    # print(anns_list)
    # test
