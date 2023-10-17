from convert.labelimg2dota import Labelimg2Dota


def dota2voc():
    '''
    dota -> yolo -> voc
    '''
    print('data2data is not supported yet')

    pass


def dota2coco():
    '''
    dota -> yolo -> coco
    '''
    print('data2data is not supported yet')
    pass


def dota2yolo(souce_dir, dst_dir,
              source_dataset_type, dst_datatset_type,
              source_labels_txt_path=None,
              ann_image_together=False, test_size=0.1,
              val_size=0.11
              ):
    print('data2data is not supported yet')
    pass

def voc2dota():
    print('data2data is not supported yet')
    pass


def voc2coco():
    print('data2data is not supported yet')
    pass


def voc2yolo():
    print('data2data is not supported yet')
    pass



def coco2dota():
    '''
    coco -> yolo -> dota
    :return:
    '''
    print('data2data is not supported yet')
    pass


def coco2voc():
    print('data2data is not supported yet')
    pass


def coco2yolo(souce_dir, dst_dir, ann_img_together):
    print('data2data is not supported yet')
    pass


def yolo2dota(source_dir, dst_dir,
              source_dataset_type, dst_datatset_type,
              source_labels_txt_path=None,
              ann_image_together=False, test_size=0.1,
              val_size=0.11):
    print('data2data is not supported yet')
    pass


def yolo2voc():
    print('data2data is not supported yet')
    pass


def yolo2coco():
    print('data2data is not supported yet')
    pass


def labelimg2dota(source_dir, dst_dir, ann_image_together=True):
    Labelimg2Dota(source_dir, dst_dir, ann_image_together).convert()


def labelimg2yolo(source_dir, dst_dir, ann_image_together=True):
    print('labelimg2yolo is not supported yet')
    pass


def labelimg2voc(source_dir, dst_dir, ann_image_together=True):
    print('labelimg2voc is not supported yet')
    pass


def labelimg2coco(source_dir, dst_dir,
                  source_labels_txt_path,
                  ann_image_together=True,
                  test_size=0.1,
                  val_size=0.11
                  ):
    print('labelimg2coco is not supported yet')
    pass
