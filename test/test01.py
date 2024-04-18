# -*- coding: UTF-8 -*-
"""
@File    ：test01.py.py
@Author  ：Csy
@Date    ：2023-11-10 16:23 
@Bref    :
@Ref     :
"""

import os

source_dir = '../exp_dataset/coco'

for root,dirs,files in os.walk(source_dir):
    print(root)
    for dir in dirs:
        print('\t',dir)
    for file in files:
        print('\t',file)


from utils import util

img_list = util.getImageListFromMulti(source_dir,dataset_type='coco')
for img in img_list:
    print(img)