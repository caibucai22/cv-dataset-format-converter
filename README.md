思路
从用户提供的数据集中 提取信息 得到一个中间格式
然后由中间格式 再转换为目标格式

数据源
1. 来自 labelimg 
2. 来自 labelme
3. 来自已经构建好的数据集
    1. coco
    2. yolo
    3. dota
    4. voc


labelimg/labelme
1. json文件和图像文件在同一个文件夹下
2. json文件和图像文件不在同一个文件夹下


各类数据集格式如下

coco
- annotations
- train
- val
- test

yolo
- 


任务类型
- 检测
- 分割
