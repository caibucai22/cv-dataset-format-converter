# -*- coding: UTF-8 -*-
"""
@File    ：BaseConverter.py
@Author  ：Csy
@Date    ：2024/4/26 20:18 
@Bref    :
@Ref     :
TODO     :
         :
"""

class BaseConverter(object):

    def __init__(self,source_dir,dst_dir,
                 source_dataset_type,dst_dataset_type,
                 source_labels_txt_path):
        self.source_dir = source_dir
