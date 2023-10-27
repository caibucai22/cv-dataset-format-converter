from convert.coco2yolo import COCO2YOLO
from convert.dota2yolo import DOTA2YOLO
from convert.labelme2coco import Labelme2COCO
from convert.labelme2dota import Labelme2DOTA
from convert.labelme2yolo import Labelme2YOLO
from convert.voc2yolo import VOC2YOLO
from convert.yolo2coco import YOLO2COCO
from convert.yolo2dota import YOLO2DOTA
from convert.yolo2voc import YOLO2VOC

from meta.Dataset_Meta import *


def dota2labelme():
    pass


def voc2labelme():
    pass


def coco2labelme():
    pass


def yolo2labelme():
    pass


def dota2voc(source_dir, dst_dir,
             source_dataset_type, dst_datatset_type,
             source_labels_txt_path=None,
             ann_image_together=False, test_size=0.1,
             val_size=0.11):
    '''
    dota -> yolo -> voc
    '''
    print('data2data is not supported yet')
    dota2yolo = DOTA2YOLO(source_dir, TDATASET_PATH,
                          source_dataset_type='dota', dst_datatset_type='yolo',
                          source_labels_txt_path=source_dir)
    yolo2voc = YOLO2VOC(TDATASET_PATH, dst_dir,
                        source_dataset_type='yolo', dst_datatset_type='voc',
                        source_labels_txt_path=TDATASET_PATH)

    dota2yolo.convert()
    yolo2voc.convert()


def dota2coco(source_dir, dst_dir,
              source_dataset_type, dst_datatset_type,
              source_labels_txt_path=None,
              ann_image_together=False, test_size=0.1,
              val_size=0.11):
    '''
    dota -> yolo -> coco
    '''

    dota2yolo = DOTA2YOLO(source_dir, TDATASET_PATH,
                          source_dataset_type='dota', dst_datatset_type='yolo',
                          source_labels_txt_path=source_dir)
    yolo2coco = YOLO2COCO(TDATASET_PATH, dst_dir,
                          source_dataset_type='yolo', dst_datatset_type='coco',
                          source_labels_txt_path=TDATASET_PATH)

    dota2yolo.convert()
    yolo2coco.convert()


def dota2yolo(source_dir, dst_dir,
              source_dataset_type='dota', dst_datatset_type='yolo',
              source_labels_txt_path=None,
              ann_image_together=False, test_size=0.1,
              val_size=0.11
              ):
    dota2yolo = DOTA2YOLO(source_dir, dst_dir,
                          source_dataset_type='dota', dst_datatset_type='yolo',
                          source_labels_txt_path=source_dir + '/classes.txt')
    dota2yolo.convert()


def voc2dota(source_dir, dst_dir,
             source_dataset_type, dst_datatset_type,
             source_labels_txt_path=None,
             ann_image_together=False, test_size=0.1,
             val_size=0.11):
    '''
    voc -> yolo -> dota
    '''
    voc2yolo = VOC2YOLO(source_dir, TDATASET_PATH,
                        source_dataset_type='voc', dst_datatset_type='yolo',
                        source_labels_txt_path=source_dir)

    yolo2dota = YOLO2DOTA(TDATASET_PATH, dst_dir,
                          source_dataset_type='yolo', dst_datatset_type='dota',
                          source_labels_txt_path=TDATASET_PATH + '/classes.txt'
                          )
    voc2yolo.convert()
    yolo2dota.convert()


def voc2coco(source_dir, dst_dir,
             source_dataset_type, dst_datatset_type,
             source_labels_txt_path=None,
             ann_image_together=False, test_size=0.1,
             val_size=0.11):
    '''
    voc -> yolo -> coco
    :return:
    '''
    voc2yolo = VOC2YOLO(source_dir, TDATASET_PATH,
                        source_dataset_type='voc', dst_datatset_type='yolo',
                        source_labels_txt_path=source_dir)
    yolo2coco = YOLO2COCO(TDATASET_PATH, dst_dir,
                          source_dataset_type='yolo', dst_datatset_type='coco',
                          source_labels_txt_path=TDATASET_PATH)
    voc2yolo.convert()
    yolo2coco.convert()


def voc2yolo(source_dir, dst_dir,
             source_dataset_type='voc', dst_datatset_type='yolo',
             source_labels_txt_path=None,
             ann_image_together=False, test_size=0.1,
             val_size=0.11):
    voc2yolo = VOC2YOLO(source_dir, dst_dir,
                        source_dataset_type='voc', dst_datatset_type='yolo',
                        source_labels_txt_path=source_dir + '/classes.txt')
    voc2yolo.convert()


def coco2dota(source_dir, dst_dir,
              source_dataset_type, dst_datatset_type,
              source_labels_txt_path=None,
              ann_image_together=False, test_size=0.1,
              val_size=0.11):
    '''
    coco -> yolo -> dota
    :return:
    '''
    coco2yolo = COCO2YOLO(source_dir, TDATASET_PATH,
                          source_dataset_type='coco', dst_datatset_type='yolo',
                          source_labels_txt_path=source_dir)

    yolo2dota = YOLO2DOTA(TDATASET_PATH, dst_dir,
                          source_dataset_type='yolo', dst_datatset_type='dota',
                          source_labels_txt_path=source_dir
                          )

    coco2yolo.convert()
    yolo2dota.convert()


def coco2voc(source_dir, dst_dir,
             source_dataset_type, dst_datatset_type,
             source_labels_txt_path=None,
             ann_image_together=False, test_size=0.1,
             val_size=0.11):
    coco2yolo = COCO2YOLO(source_dir, TDATASET_PATH,
                          source_dataset_type='coco', dst_dataset_type='yolo',
                          source_labels_txt_path=source_dir + 'classes.txt')
    yolo2voc = YOLO2VOC(TDATASET_PATH, dst_dir)

    coco2yolo.convert()
    yolo2voc.convert()


def coco2yolo(source_dir, dst_dir, ann_image_together=False):
    coco2yolo = COCO2YOLO(source_dir, dst_dir, ann_image_together,
                          source_dataset_type='coco', dst_dataset_type='yolo',
                          source_labels_txt_path=source_dir + '/' + 'classes.txt')
    coco2yolo.convert()


def yolo2dota(source_dir, dst_dir,
              source_dataset_type, dst_datatset_type,
              source_labels_txt_path=None,
              ann_image_together=False, test_size=0.1,
              val_size=0.11):
    yolo2dota = YOLO2DOTA(source_dir, dst_dir,
                          source_dataset_type='yolo', dst_datatset_type='dota',
                          source_labels_txt_path=source_dir
                          )
    yolo2dota.convert()


def yolo2voc(source_dir, dst_dir,
             source_dataset_type='yolo', dst_dataset_type='voc',
             source_labels_txt_path=None,
             ann_image_together=False, test_size=0.1,
             val_size=0.11):
    yolo2voc = YOLO2VOC(source_dir, dst_dir,
                        source_labels_txt_path=source_dir + '/classes.txt')
    yolo2voc.convert()


def yolo2coco(source_dir, dst_dir,
              source_dataset_type='yolo', dst_datatset_type='coco',
              source_labels_txt_path=None,
              ann_image_together=False, test_size=0.1,
              val_size=0.11):
    yolo2coco = YOLO2COCO(source_dir, dst_dir,
                          source_labels_txt_path=source_dir + '/classes.txt')
    yolo2coco.convert()


def labelme2dota(source_dir, dst_dir,
                 source_dataset_type, dst_datatset_type,
                 source_labels_txt_path=None,
                 ann_image_together=False, test_size=0.1,
                 val_size=0.11):
    Labelme2DOTA(source_dir, dst_dir, ann_image_together).convert()


def labelme2yolo(source_dir, dst_dir,
                 source_dataset_type='labelme', dst_datatset_type='yolo',
                 source_labels_txt_path=None,
                 ann_image_together=False, test_size=0.1,
                 val_size=0.11):
    labelme2yolo = Labelme2YOLO(source_dir, dst_dir, ann_image_together=True,
                                source_labels_txt_path=source_dir + '/' + 'classes.txt')
    labelme2yolo.convert()


def labelme2voc(source_dir, dst_dir,
                source_dataset_type, dst_datatset_type,
                source_labels_txt_path=None,
                ann_image_together=False, test_size=0.1,
                val_size=0.11):
    labelimg2yolo = Labelme2YOLO(source_dir, dst_dir,
                                 source_dataset_type='labelme', dst_datatset_type='coco',
                                 source_labels_txt_path=source_dir)

    labelme2coco.convert()


def labelme2coco(source_dir, dst_dir,
                 source_dataset_type, dst_datatset_type,
                 source_labels_txt_path=None,
                 ann_image_together=False, test_size=0.1,
                 val_size=0.11
                 ):
    labelimg2coco = Labelme2COCO(source_dir, dst_dir,
                                 source_dataset_type='labelme', dst_datatset_type='coco',
                                 source_labels_txt_path=source_dir)
    labelimg2coco.convert()
