思路
从用户提供的数据集中 提取信息 得到一个中间格式
然后由中间格式 再转换为目标格式
## 进度
2023.09.11 已实现 labelme2yolo, labelme2dota

## 支持数据源
1. 来自 labelimg 
2. 来自 labelme
3. 来自已经构建好的数据集
    1. coco
    2. yolo
    3. dota
    4. voc

### 数据源格式
labelimg/labelme
1. json文件和图像文件在同一个文件夹下
2. json文件和图像文件不在同一个文件夹下

标注信息的文件数量
1. 单个 json文件 , coco 【保存的信息 比较完善 需要的用户提供的额外信息少】
2. 多个 json/txt/xml 文件 , labelimg , labelme , yolo , dota, voc 【保存了核心的标注信息, 需要用户额外提供 类别信息、】

各类数据集格式如下

coco
- annotations
- train
- val
- test

labelimg 【取消该类型】
- images ...
- labels ...

labelme
- images ...
- labels ...


yolo
- images
  - train/test/val
- labels
  - train/test/val

dota

voc

任务类型
- 检测
- 分割

思路：
1. 先根据meta获取到所有信息 -> 构建 TDatast -> 根据TDataset和目标meta 生成目标数据集
2. labelme 标注是 多个 .json 文件 -> 只生成一个 annotations.json  数据集；
   labelme 先划分 然后再去各自生成 子数据集


## 待实现功能
做 图像预处理增强 集成 包括 图像切片 ...

UI
添加 ann_img_together 按钮