# -*- coding: utf-8 -*-
"""
# @file name : voc2yolo.py
# @author    : Csy
# @date      : 2023-06-30 16:20
# @brief     :
"""
import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import random
from shutil import copyfile

# 根据自己的数据标签修改
classes = ["crack"]


def clear_hidden_files(path):
    dir_list = os.listdir(path)
    for i in dir_list:
        abspath = os.path.join(os.path.abspath(path), i)
        if os.path.isfile(abspath):
            if i.startswith("._"):
                os.remove(abspath)
        else:
            clear_hidden_files(abspath)


def convert(size, box):
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


def convert_annotation(image_id, in_file_path, out_file_path):
    in_file = open(in_file_path, encoding='gb18030', errors='ignore')
    # in_file = open(in_file_path)

    out_file = open(out_file_path, 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    in_file.close()
    out_file.close()


wd = os.getcwd()
wd = os.getcwd()
wd = './'

data_base_dir = os.path.join(wd, "sampling-part/")
if not os.path.isdir(data_base_dir):
    os.mkdir(data_base_dir)

work_sapce_dir = os.path.join(data_base_dir, "SPDataset/")
if not os.path.isdir(work_sapce_dir):
    os.mkdir(work_sapce_dir)

annotation_dir = os.path.join(work_sapce_dir, "data/Annotations/")
if not os.path.isdir(annotation_dir):
    os.makedirs(annotation_dir)
clear_hidden_files(annotation_dir)

image_dir = os.path.join(work_sapce_dir, "data/JPEGImages/")
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)
clear_hidden_files(image_dir)

yolo_labels_dir = os.path.join(work_sapce_dir, "YOLOLabels/")
if not os.path.isdir(yolo_labels_dir):
    os.mkdir(yolo_labels_dir)
clear_hidden_files(yolo_labels_dir)

yolov5_images_dir = os.path.join(data_base_dir, "data/images/")
if not os.path.isdir(yolov5_images_dir):
    os.makedirs(yolov5_images_dir)
clear_hidden_files(yolov5_images_dir)

yolov5_labels_dir = os.path.join(data_base_dir, "data/labels/")
if not os.path.isdir(yolov5_labels_dir):
    os.mkdir(yolov5_labels_dir)
clear_hidden_files(yolov5_labels_dir)

yolov5_images_train_dir = os.path.join(yolov5_images_dir, "train/")
if not os.path.isdir(yolov5_images_train_dir):
    os.mkdir(yolov5_images_train_dir)
clear_hidden_files(yolov5_images_train_dir)

yolov5_images_val_dir = os.path.join(yolov5_images_dir, "val/")
if not os.path.isdir(yolov5_images_val_dir):
    os.mkdir(yolov5_images_val_dir)
clear_hidden_files(yolov5_images_val_dir)

yolov5_images_test_dir = os.path.join(yolov5_images_dir, "test/")
if not os.path.isdir(yolov5_images_test_dir):
    os.mkdir(yolov5_images_test_dir)
clear_hidden_files(yolov5_images_test_dir)

yolov5_labels_train_dir = os.path.join(yolov5_labels_dir, "train/")
if not os.path.isdir(yolov5_labels_train_dir):
    os.mkdir(yolov5_labels_train_dir)
clear_hidden_files(yolov5_labels_train_dir)

yolov5_labels_val_dir = os.path.join(yolov5_labels_dir, "val/")
if not os.path.isdir(yolov5_labels_val_dir):
    os.mkdir(yolov5_labels_val_dir)
clear_hidden_files(yolov5_labels_val_dir)

yolov5_labels_test_dir = os.path.join(yolov5_labels_dir, "test/")
if not os.path.isdir(yolov5_labels_test_dir):
    os.mkdir(yolov5_labels_test_dir)
clear_hidden_files(yolov5_labels_test_dir)

train_file = open(os.path.join(wd, "sampling-part/data/yolov5_train.txt"), 'w')
val_file = open(os.path.join(wd, "sampling-part/data/yolov5_val.txt"), 'w')
trainval_file = open(os.path.join(wd, "sampling-part/data/yolov5_trainval.txt"), 'w')
test_file = open(os.path.join(wd, "sampling-part/data/yolov5_test.txt"), 'w')
train_file.close()
val_file.close()
trainval_file.close()
test_file.close()

train_file = open(os.path.join(wd, "sampling-part/data/yolov5_train.txt"), 'a')
val_file = open(os.path.join(wd, "sampling-part/data/yolov5_val.txt"), 'a')
trainval_file = open(os.path.join(wd, "sampling-part/data/yolov5_trainval.txt"), 'a')
test_file = open(os.path.join(wd, "sampling-part/data/yolov5_test.txt"), 'a')

list_imgs = os.listdir(image_dir)  # list image files

# paths = [data_base_dir, work_sapce_dir, annotation_dir, image_dir, yolo_labels_dir, yolov5_labels_dir,
#          yolov5_labels_train_dir,
#          yolov5_labels_val_dir, yolov5_labels_test_dir, yolov5_images_dir, yolov5_images_train_dir,
#          yolov5_images_val_dir,
#          yolov5_images_test_dir]
#
# for path in paths:
#     path = path.replace('/', '\\')

# print(data_base_dir)
# print(work_sapce_dir)
# print(annotation_dir)
# print(image_dir)
# print(image_dir)
# print(yolo_labels_dir)
# print(yolov5_labels_test_dir)
# print(yolov5_labels_val_dir)
# print(yolov5_labels_test_dir)
#
# print(yolov5_images_test_dir)
# print(yolov5_images_val_dir)
# print(yolov5_images_train_dir)

# probo = random.randint(1, 100)
# print("Probobility: %d" % probo)

# trainval_percent = 0.9
# train_percent = 0.9

# trainval_percent = 0.25
# train_percent = 0.8

trainval_percent = 0.8
train_percent = 0.75

total_xml = os.listdir(annotation_dir)
num = len(total_xml)
list = range(num)

tv = int(num * trainval_percent) ## 训练集+验证集
tr = int(tv * train_percent) # 训练集

print('train+val',tv)
print('train',tr)
print('val',tv-tr)
print('test',num-tv)
# os.system("pause")

random.seed(1)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

print('train',len(train))
print('val',len(trainval)-len(train))
print('test',num-len(trainval))

# os.system("pause")

train_cnt = 0
val_cnt = 0
test_cnt = 0

for i in range(0, len(list_imgs)):
    path = os.path.join(image_dir, list_imgs[i])
    if os.path.isfile(path):
        image_path = image_dir + list_imgs[i]
        voc_path = list_imgs[i]
        print(image_path, voc_path)

        (nameWithoutExtention, extention) = os.path.splitext(os.path.basename(image_path))
        print(nameWithoutExtention, extention)
        (voc_nameWithoutExtention, voc_extention) = os.path.splitext(os.path.basename(voc_path))
        print(voc_nameWithoutExtention, voc_extention)

        annotation_name = nameWithoutExtention + '.xml'
        annotation_path = os.path.join(annotation_dir, annotation_name)

        print(annotation_path)

        label_name = nameWithoutExtention + '.txt'
        label_path = os.path.join(yolo_labels_dir, label_name)

        print(label_path)

        in_file_path = annotation_path
        out_file_path = label_path

    # probo = random.randint(1, 100)
    # print("Probobility: %d" % probo)

    # if (probo < 80):  # train dataset
    if i in trainval:
        trainval_file.write(image_path + '\n')
        if i in train:
            train_cnt+=1
            if os.path.exists(annotation_path):
                train_file.write(image_path + '\n')
                convert_annotation(nameWithoutExtention, in_file_path, out_file_path)  # convert label
                copyfile(image_path, yolov5_images_train_dir + voc_path)
                copyfile(label_path, yolov5_labels_train_dir + label_name)
        else:
            if os.path.exists(annotation_path):
                val_file.write(image_path + '\n')
                convert_annotation(nameWithoutExtention, in_file_path, out_file_path)  # convert label
                copyfile(image_path, yolov5_images_val_dir + voc_path)
                copyfile(label_path, yolov5_labels_val_dir + label_name)
                val_cnt += 1
    else:  # test dataset
        if os.path.exists(annotation_path):
            test_file.write(image_path + '\n')
            convert_annotation(nameWithoutExtention, in_file_path, out_file_path)  # convert label
            copyfile(image_path, yolov5_images_test_dir + voc_path)
            copyfile(label_path, yolov5_labels_test_dir + label_name)
            test_cnt += 1
train_file.close()
test_file.close()


print('train:',train_cnt)
print('val:',val_cnt)
print('test',test_cnt)
