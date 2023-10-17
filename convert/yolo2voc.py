# -*- coding: UTF-8 -*-
"""
@File    ：yolo2voc.py
@Author  ：Csy
@Date    ：2023-10-17 18:53 
@Bref    :
@Ref     :
"""

import os,shutil
import cv2
from meta.Dataset_Meta import Dataset_setting
import utils


class YOLO2VOC():
    def __init__(self, source_dir, dst_dir,
                 source_dataset_type='yolo', dst_datatset_type='voc',
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
            self.source_labels_dir_path = os.path.join(source_dir,
                                                       Dataset_setting[self.source_dataset_type]['dirs'][1])

        print('dst_dir struct:')
        utils.check_and_create_dir(self.dst_dataset_type, dst_dir)

        self.dst_images_dir_path = os.path.join(dst_dir, Dataset_setting[self.dst_dataset_type]['dirs']
        [0])
        self.dst_labels_dir_path = os.path.join(dst_dir, Dataset_setting[self.dst_dataset_type]['dirs']
        [1])

        if self.source_labels_txt_path is not None:
            self.class_name_to_id, self.class_id_to_name = utils.get_label_id_map_with_txt(
                self.source_labels_txt_path)

        print('src_dst struct')
        utils.print_dirs_info(source_dir)

        self.imgs_list, _ = utils.get_imgs(self.source_dir, dataset_type=self.source_dataset_type)
        self.anns_list, _ = utils.get_Anns(self.source_dir, dataset_type=self.source_dataset_type)

        if self.anns_list[0] == 'classes.txt':
            self.anns_list = self.anns_list[1:]

    def convert(self):
        for img_name, label_name in zip(self.imgs_list, self.anns_list):
            print(img_name)
            img_h, img_w, img_c = cv2.imread(self.source_images_dir_path + '/' + img_name).shape
            xml_objects = []
            with open(self.source_labels_dir_path + '/' + label_name) as yolo_file:
                for line in yolo_file.readlines():
                    class_id, xc, yc, w, h = [float(itm) for itm in line.split(' ')]
                    xml_object = utils.bbox_yolo2voc(xc, yc, w, h, img_w, img_h)
                    xml_objects.append([self.class_id_to_name[class_id]] + list(xml_object))
                yolo_file.close()

            with open(self.dst_labels_dir_path + '/' + label_name[:-4] + '.xml', 'w') as xml_file:
                xml_file.write('<annotation>\n')
                xml_file.write('    <folder>VOC2007</folder>\n')
                xml_file.write('    <filename>' + str(img_name) + '</filename>\n')
                xml_file.write('    <size>\n')
                xml_file.write('        <width>' + str(img_w) + '</width>\n')
                xml_file.write('        <height>' + str(img_h) + '</height>\n')
                xml_file.write('        <depth>' + str(img_c) + '</depth>\n')
                xml_file.write('    </size>\n')

                # write the region of image on xml file
                for class_name, xmin, ymin, xmax, ymax in xml_objects:
                    xml_file.write('    <object>\n')
                    xml_file.write('        <name>' + class_name + '</name>\n')
                    xml_file.write('        <pose>Unspecified</pose>\n')
                    xml_file.write('        <truncated>0</truncated>\n')
                    xml_file.write('        <difficult>0</difficult>\n')
                    xml_file.write('        <bndbox>\n')

                    xml_file.write('            <xmin>' + str(xmin) + '</xmin>\n')
                    xml_file.write('            <ymin>' + str(ymin) + '</ymin>\n')
                    xml_file.write('            <xmax>' + str(xmax) + '</xmax>\n')
                    xml_file.write('            <ymax>' + str(ymax) + '</ymax>\n')
                    xml_file.write('        </bndbox>\n')
                    xml_file.write('    </object>\n')

                xml_file.write('</annotation>')
                xml_file.close()
            shutil.copy(self.source_images_dir_path + "/" + img_name, self.dst_images_dir_path + "/" + img_name)
        shutil.copy(self.source_dir + "/" + 'classes.txt', self.dst_dir + "/" + 'classes.txt')

        print('done!')

if __name__ == '__main__':
    convertor = YOLO2VOC(source_dir='../exp_dataset/yolo',dst_dir='../exp_dataset/TDataset',
                         source_labels_txt_path='../exp_dataset/yolo/classes.txt')
    convertor.convert()