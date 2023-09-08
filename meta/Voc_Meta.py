# -*- coding: UTF-8 -*-
"""
@File    ：Voc_Meta.py
@Author  ：Csy
@Date    ：2023-08-30 19:27 
@Bref    :
@Ref     :
"""
'''
voc 是xml格式 这里以dict(json)形式表示

<annotation>
	<folder>Pictures</folder>
	<filename>01.jpg</filename>
	<path>C:\Users\Csy\Pictures\01.jpg</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>512</width>
		<height>512</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>bump</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>54</xmin>
			<ymin>257</ymin>
			<xmax>136</xmax>
			<ymax>493</ymax>
		</bndbox>
	</object>
	<object>
		<name>bump</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>221</xmin>
			<ymin>127</ymin>
			<xmax>317</xmax>
			<ymax>379</ymax>
		</bndbox>
	</object>
	<object>
		<name>rust</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>377</xmin>
			<ymin>178</ymin>
			<xmax>456</xmax>
			<ymax>422</ymax>
		</bndbox>
	</object>
</annotation>
'''

Voc_Meta = {
    "annotation": {}
}

annotation_meta = {
    "folder": "",
    "filename": "",
    "path": "",
    "source": {},
    "size": {},
    "segmented": 0,
    "object": []
}

source_meta = {
    "database": ""
}

size_meta = {
    "width": "",
    "height": "",
    "depth": ""
}
object_meta = {
    "name": "",
    "pose": "",
    "truncated": 0,
    "diffcult": 0,
    "bndbox": []
}

bndbox_meta = {
    "xmin": -1,
    "ymin": -1,
    "xmax": -1,
    "ymax": -1
}
