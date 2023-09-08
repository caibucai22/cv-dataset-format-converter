# -*- coding: UTF-8 -*-
"""
@File    ：labelme2yolo.py
@Author  ：Csy
@Date    ：2023-09-07 21:28 
@Bref    :
@Ref     :
"""
import utils

class Labelme2YOLO():

    def __init__(self,source_dir,dst_dir):
        self.program_dir = source_dir
        # 打印 文件夹下 目录情况
        utils.print_dirs_info(source_dir)
        _, self.imgs_list = utils.get_imgs(self.program_dir,dataset_type='labelme')