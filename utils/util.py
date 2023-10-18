# -*- coding: utf-8 -*-
"""
# @file name : util.py
# @author    : Csy
# @date      : 2023-07-01 17:33
# @brief     : 实现 部分依赖的 工具函数
"""
import os
import PIL
import shutil
from meta.Dataset_Meta import *
from utils import Exception as Exception_Define
import utils


def print_dirs_info(source_dir, display=True):
    cur_dirs = []
    for root, dirs, files in os.walk(source_dir):
        for name in dirs:
            cur_dirs.append(name)
            if display:
                print(name)
    return sorted(cur_dirs)


def check_and_create_dir(dst_dataset_type, dst_dir):
    cur_dirs = print_dirs_info(dst_dir)
    if dst_dataset_type in ['coco']:
        dst_dirs = Dataset_setting[dst_dataset_type]['no_split_dirs']
    else:
        dst_dirs = Dataset_setting[dst_dataset_type]['dirs']
    if len(dst_dirs) != len(cur_dirs) or dst_dirs != cur_dirs:
        # 移除已有文件夹
        # a,b = len(dst_dirs),len(cur_dirs)
        # while b > 0:
        #     shutil.rmtree(os.path.join(dst_dir,))
        for dir in cur_dirs:
            # 不为空也可删
            if os.path.exists(os.path.join(dst_dir, dir)):
                shutil.rmtree(os.path.join(dst_dir, dir))
        # 创建目标数据集格式文件夹
        for dir in dst_dirs:
            os.makedirs(os.path.join(dst_dir, dir))


def get_imgs(source_dir, dataset_type):
    imgs = []
    if dataset_type == 'coco':
        pass
    elif dataset_type == 'yolo':
        imgs = getImageListFromMulti(source_dir, dataset_type='yolo')
    elif dataset_type == 'labelimg':
        imgs = getImageListFromMulti(source_dir, dataset_type='yolo')
    elif dataset_type == 'dota':
        imgs = getImageListFromMulti(source_dir, dataset_type='dota')
    elif dataset_type == 'voc':
        imgs = getImageListFromMulti(source_dir, dataset_type='voc')
    else:
        raise Exception(Exception_Define.UNSUPPORTED_DATASET_TYPE)
    return sorted(imgs), len(imgs),


def get_Anns(source_dir, dataset_type='coco'):
    postfix = Dataset_setting[dataset_type]['anno_type']
    anns = []
    if dataset_type == 'coco':
        pass
    elif dataset_type == 'yolo':
        anns = getAnnListFromMulti(source_dir, dataset_type='yolo')
    elif dataset_type == 'labelimg':
        anns = getAnnListFromMulti(source_dir, dataset_type='labelimg')
    elif dataset_type == 'dota':
        anns = getAnnListFromMulti(source_dir, dataset_type='dota')
    elif dataset_type == 'voc':
        anns = getAnnListFromMulti(source_dir, dataset_type='voc')
    else:
        raise Exception(Exception_Define.UNSUPPORTED_DATASET_TYPE)
    return anns, len(anns),


def check_anno_file_exist(source_dir, type, exist_with_img=True):
    if type == 'coco':
        if os.path.exists(os.path.join(source_dir, 'annotations', 'annotation.json')):
            return True
    elif type == 'labelimg':
        if exist_with_img:
            pass
        else:
            pass
    else:
        raise Exception(Exception_Define.UNSUPPORTED_DATASET_TYPE)
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
        img = utils.img_b64_to_arr(json_data['imageData'])
        PIL.Image.fromarray(img).save(dst_img_path)
    else:
        shutil.copyfile(sour_img_path, dst_img_path)
    return dst_img_path


def get_label_id_map_with_txt(label_txt_path):
    class_id2name = {}
    class_name2id = {}
    for i, line in enumerate(open(label_txt_path).readlines()):
        class_id = i  # starts with -1
        class_name = line.strip()

        class_name2id[class_name] = class_id
        class_id2name[class_id] = class_name
    return class_name2id, class_id2name


def clear_hidden_files(path):
    dir_list = os.listdir(path)
    for i in dir_list:
        abspath = os.path.join(os.path.abspath(path), i)
        if os.path.isfile(abspath):
            if i.startswith("._"):
                os.remove(abspath)
        else:
            clear_hidden_files(abspath)


if __name__ == '__main__':
    # test
    # print_dirs_info('./exp_dataset')
    source_dir = '../exp_dataset/labelimg'
    # img_list = getImageListFromMulti('./exp_dataset/yolo', dataset_type='yolo')
    # print(img_list)
    # ann_list = getAnnListFromMulti('./exp_dataset/yolo',dataset_type='yolo')
    # print(ann_list)

    # imgs_list, imgs_len = get_imgs(source_dir, dataset_type='labelimg')
    # anns_list, anns_len = get_Anns(source_dir, dataset_type='labelimg')
    # print(imgs_list)
    # print(anns_list)
    # test
    # class_name2id, class_id2name = get_label_id_map_with_txt(r'E:\01-LabProjects\800\scratch\raw\ScratchDataset_all\classes.txt')
    # print(class_name2id)
    # print(class_id2name)

    print_dirs_info(source_dir='../exp_dataset/yolo')