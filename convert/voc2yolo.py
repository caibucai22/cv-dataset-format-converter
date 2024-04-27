# -*- coding: UTF-8 -*-
"""
@File    ：voc2yolo.py
@Author  ：Csy
@Date    ：2023-10-08 19:41 
@Bref    : VOC 转 YOLO
@Ref     :
"""

import xml.etree.ElementTree as ET
import os,shutil
from meta.Dataset_Meta import Dataset_setting
import utils



class VOC2YOLO():

    def __init__(self, source_dir, dst_dir,
                 source_dataset_type, dst_datatset_type,
                 source_labels_txt_path=None,
                 ann_img_together=False,
                 test_size=0.2,
                 val_size=0.5):
        self.source_dir = source_dir
        self.dst_dir = dst_dir

        self.source_dataset_type = source_dataset_type
        self.dst_dataset_type = dst_datatset_type

        self.test_size = test_size
        self.val_size = val_size

        self.source_images_dir_path = os.path.join(source_dir, Dataset_setting[self.source_dataset_type]['dirs'][0])
        self.source_labels_dir_path = self.source_images_dir_path
        self.source_labels_txt_path = source_labels_txt_path
        if not ann_img_together:
            self.source_labels_dir_path = os.path.join(source_dir, Dataset_setting[self.source_dataset_type]['dirs'][1])

        print('dst_dir struct:')
        utils.check_and_create_dir(self.dst_dataset_type, dst_dir)

        self.dst_images_dir_path = os.path.join(dst_dir, Dataset_setting[self.dst_dataset_type]['dirs']
        [0])
        self.dst_labels_dir_path = os.path.join(dst_dir, Dataset_setting[self.dst_dataset_type]['dirs']
        [1])

        if self.source_labels_txt_path is not None:
            self.class_name_to_id, self.class_id_to_name = utils.get_label_id_map_with_txt(self.source_labels_txt_path)

        print('src_dst struct')
        utils.print_dirs_info(source_dir)

        self.imgs_list, _ = utils.get_imgs(self.source_dir, dataset_type=self.source_dataset_type)
        self.anns_list, _ = utils.get_Anns(self.source_dir, dataset_type=self.source_dataset_type)

        if self.anns_list[0] == 'classes.txt':
            self.anns_list = self.anns_list[1:]
    def convert(self):
        for img_name, label_name in zip(self.imgs_list, self.anns_list):
            print(img_name)

            yolo_lines = []
            with open(self.source_labels_dir_path + '/' + label_name, ) as f:
                tree = ET.parse(f)
                root = tree.getroot()
                size_obj = root.find('size')
                img_w, img_h = int(size_obj.find('width').text), int(size_obj.find('height').text)

                for obj in root.iter('object'):
                    difficult = obj.find('difficult').text
                    cls = obj.find('name').text
                    if cls not in self.class_name_to_id.keys() or int(difficult) == 1:
                        continue
                    cls_id = self.class_name_to_id[cls]
                    xmlbox = obj.find('bndbox')
                    b = (
                        float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text),
                        float(xmlbox.find('ymin').text),
                        float(xmlbox.find('ymax').text))
                    xc, yc, w, h = utils.bbox_voc2yolo((img_w, img_h), b)
                    yolo_line = ''
                    for itm in [cls_id, xc, yc, w, h]:
                        yolo_line += ' ' + str(round(itm,7))
                    yolo_lines.append(yolo_line.strip())
                f.close()

            dst_label_name = label_name[:-4]+Dataset_setting[self.dst_dataset_type]['anno_type']
            with open(self.dst_labels_dir_path + '/' + dst_label_name, 'w') as f:
                for line in yolo_lines:
                    f.write(line + '\n')
                f.close()
            shutil.copy(self.source_images_dir_path + "/" + img_name, self.dst_images_dir_path + "/" + img_name)
        shutil.copy(self.source_dir + "/" + 'classes.txt', self.dst_dir + "/" + 'classes.txt')
        print('done')


if __name__ == '__main__':
    convertor = VOC2YOLO(source_dir='../exp_dataset/voc',dst_dir='../exp_dataset/TDataset',
                        source_labels_txt_path='../exp_dataset/voc/classes.txt' ,
                        source_dataset_type='voc',dst_datatset_type='yolo')
    convertor.convert()



