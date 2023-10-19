# -*- coding: utf-8 -*-
"""
# @file name : split_dataset.py
# @author    : Csy
# @date      : 2023-07-04 19:18
# @brief     : 此种划分方式 可以较灵活针对数据集要求格式 注意修改上面的配置即可
"""

import os, shutil, random
import time

from tqdm import *
from PIL import Image
from sklearn.model_selection import train_test_split

random.seed(0)
val_size = 0.1
# test_size = 0.2
test_size = 0.1

imgpath = r'E:\01-LabProjects\800\scratch\raw\new_ScratchDataset\images'
labelpath = r'E:\01-LabProjects\800\scratch\raw\new_ScratchDataset\labels'
# postfixs = ['.png', '_instance_color_RGB.png', '_instance_id_RGB.png']

postfixs = ['.png', '.txt']

dst_path = r'E:\01-LabProjects\800\scratch\raw\new_ScratchDataset\new_ScratchDataset'

# mode 1
# save_dirs = ['train', 'val', 'test']
# save_subdirs = ['images', 'labels']

# mode 2
save_dirs = ['images', 'labels']
save_subdirs = ['train', 'val', 'test']

mode = 3

# mkdir
if not os.path.exists(os.path.join(dst_path)):
    print("创建数据集文件夹")
    os.mkdir(os.path.join(dst_path))

# mk subdir
for dir in save_dirs:
    for subdir in save_subdirs:
        if not os.path.exists(os.path.join(dst_path, dir, subdir)):
            os.makedirs(os.path.join(dst_path, dir, subdir))

listdir = [name for name in os.listdir(imgpath)]

# convert img format bmp-> png
convert = False
if convert:
    for name in listdir:
        if name.endswith('bmp'):
            basename = os.path.splitext(name)[0]
            im = Image.open(imgpath + "/" + name)
            im.save(imgpath + "/" + basename + '.png')

    raise Exception("转换完成 请重新执行程序")
else:
    pass

listdir = [name for name in os.listdir(imgpath) if name.endswith(postfixs[0])]

print("共", len(listdir), "张照片")

train, test = train_test_split(listdir, test_size=test_size, shuffle=True, random_state=0)
train, val = train_test_split(train, test_size=val_size, shuffle=True, random_state=0)

# train, val = train_test_split(listdir, test_size=val_size, shuffle=True, random_state=0)


print('train: ', len(train))
print('val  : ', len(val))
print('test : ', len(test))


if mode == 1:
    for i in train:
        # print(i[:-4])
        shutil.copy('{}/{}{}'.format(imgpath, i[:-4], postfixs[0]),
                    '{}/{}/{}/{}{}'.format(dst_path, save_dirs[0], save_subdirs[0], i[:-4], postfixs[0]))
        # shutil.copy('{}/{}{}'.format(imgpath, i[:-4], postfixs[1]), '{}/{}/{}/{}{}'.format(dst_path,save_dirs[0],save_subdirs[0],i[:-4], postfixs[1]))
        # shutil.copy('{}/{}{}'.format(imgpath, i[:-4], postfixs[2]), '{}/{}/{}/{}{}'.format(dst_path,save_dirs[0],save_subdirs[0],i[:-4], postfixs[2]))

        shutil.copy('{}/{}{}'.format(labelpath, i[:-4], postfixs[1]),
                    '{}/{}/{}/{}{}'.format(dst_path, save_dirs[0], save_subdirs[1], i[:-4], postfixs[1]))

    for i in val:
        shutil.copy('{}/{}{}'.format(imgpath, i[:-4], postfixs[0]),
                    '{}/{}/{}/{}{}'.format(dst_path, save_dirs[1], save_subdirs[0], i[:-4], postfixs[0]))
        # shutil.copy('{}/{}{}'.format(imgpath, i[:-4], postfixs[1]),'{}/{}/{}/{}{}'.format(dst_path, save_dirs[1], save_subdirs[0], i[:-4], postfixs[1]))
        # shutil.copy('{}/{}{}'.format(imgpath, i[:-4], postfixs[2]),'{}/{}/{}/{}{}'.format(dst_path, save_dirs[1], save_subdirs[0], i[:-4], postfixs[2]))

        shutil.copy('{}/{}{}'.format(labelpath, i[:-4], postfixs[1]),
                    '{}/{}/{}/{}{}'.format(dst_path, save_dirs[1], save_subdirs[1], i[:-4], postfixs[1]))

    for i in test:
        shutil.copy('{}/{}{}'.format(imgpath, i[:-4], postfixs[0]),
                    '{}/{}/{}/{}{}'.format(dst_path, save_dirs[2], save_subdirs[0], i[:-4], postfixs[0]))
        # shutil.copy('{}/{}{}'.format(imgpath, i[:-4], postfixs[1]),'{}/{}/{}/{}{}'.format(dst_path, save_dirs[2], save_subdirs[0], i[:-4], postfixs[1]))
        # shutil.copy('{}/{}{}'.format(imgpath, i[:-4], postfixs[2]),'{}/{}/{}/{}{}'.format(dst_path, save_dirs[2], save_subdirs[0], i[:-4], postfixs[2]))
        shutil.copy('{}/{}{}'.format(labelpath, i[:-4], postfixs[1]),
                    '{}/{}/{}/{}{}'.format(dst_path, save_dirs[2], save_subdirs[1], i[:-4], postfixs[1]))
elif mode == 2:
    for i in train:
        # print(i[:-4])
        shutil.copy('{}/{}{}'.format(imgpath, i[:-4], postfixs[0]),
                    '{}/{}/{}/{}{}'.format(dst_path, save_dirs[0], save_subdirs[0], i[:-4], postfixs[0]))
        # shutil.copy('{}/{}{}'.format(imgpath, i[:-4], postfixs[1]), '{}/{}/{}/{}{}'.format(dst_path,save_dirs[0],save_subdirs[0],i[:-4], postfixs[1]))
        # shutil.copy('{}/{}{}'.format(imgpath, i[:-4], postfixs[2]), '{}/{}/{}/{}{}'.format(dst_path,save_dirs[0],save_subdirs[0],i[:-4], postfixs[2]))

        shutil.copy('{}/{}{}'.format(labelpath, i[:-4], postfixs[1]),
                    '{}/{}/{}/{}{}'.format(dst_path, save_dirs[1], save_subdirs[0], i[:-4], postfixs[1]))

    for i in val:
        shutil.copy('{}/{}{}'.format(imgpath, i[:-4], postfixs[0]),
                    '{}/{}/{}/{}{}'.format(dst_path, save_dirs[0], save_subdirs[1], i[:-4], postfixs[0]))
        # shutil.copy('{}/{}{}'.format(imgpath, i[:-4], postfixs[1]),'{}/{}/{}/{}{}'.format(dst_path, save_dirs[1], save_subdirs[0], i[:-4], postfixs[1]))
        # shutil.copy('{}/{}{}'.format(imgpath, i[:-4], postfixs[2]),'{}/{}/{}/{}{}'.format(dst_path, save_dirs[1], save_subdirs[0], i[:-4], postfixs[2]))

        shutil.copy('{}/{}{}'.format(labelpath, i[:-4], postfixs[1]),
                    '{}/{}/{}/{}{}'.format(dst_path, save_dirs[1], save_subdirs[1], i[:-4], postfixs[1]))

    for i in test:
        shutil.copy('{}/{}{}'.format(imgpath, i[:-4], postfixs[0]),
                    '{}/{}/{}/{}{}'.format(dst_path, save_dirs[0], save_subdirs[2], i[:-4], postfixs[0]))
        # shutil.copy('{}/{}{}'.format(imgpath, i[:-4], postfixs[1]),'{}/{}/{}/{}{}'.format(dst_path, save_dirs[2], save_subdirs[0], i[:-4], postfixs[1]))
        # shutil.copy('{}/{}{}'.format(imgpath, i[:-4], postfixs[2]),'{}/{}/{}/{}{}'.format(dst_path, save_dirs[2], save_subdirs[0], i[:-4], postfixs[2]))
        shutil.copy('{}/{}{}'.format(labelpath, i[:-4], postfixs[1]),
                    '{}/{}/{}/{}{}'.format(dst_path, save_dirs[1], save_subdirs[2], i[:-4], postfixs[1]))

print('done')
