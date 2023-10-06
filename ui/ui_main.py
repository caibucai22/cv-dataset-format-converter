from enum import Enum

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt, QUrl)
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import (QComboBox, QHBoxLayout, QLabel,
                               QLineEdit, QProgressBar, QPushButton,
                               QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
                               QWidget, QFileDialog)

from convert.all_convert import *


class Ui_Main_UserInput:
    class Dataset_Format(Enum):
        DOTA = 'DOTA'
        VOC = 'VOC'
        COCO = 'COCO'
        YOLO = 'YOLO'
        DATA_LABELME = 'Data Labelme'

    class Operation_Type(Enum):
        FILE = 1
        DATASET = 2

    def __init__(self, file_operation_type: Operation_Type,
                 src_format: Dataset_Format,
                 dst_format: Dataset_Format,
                 divide_proportion: str,
                 src_path: str,
                 dst_path: str):
        self.file_operation_type = file_operation_type
        self.src_format = src_format
        self.dst_format = dst_format
        self.divide_proportion = divide_proportion
        self.src_path = src_path
        self.dst_path = dst_path


class Ui_Main(object):
    def __init__(self, parent: QWidget):
        self.parent = parent
        self.file_conversion_radioButton = None
        self.horizontalLayout = None
        self.file_operation_type_widget = None
        self.verticalLayout_2 = None
        self.centralwidget = None

    def setupUi(self, MainWindow):
        # 设置UI界面
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.file_operation_type_widget = QWidget(self.centralwidget)
        self.file_operation_type_widget.setObjectName(u"file_operation_type_widget")
        self.horizontalLayout = QHBoxLayout(self.file_operation_type_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.file_conversion_radioButton = QRadioButton(self.file_operation_type_widget)
        self.file_conversion_radioButton.setObjectName(u"file_conversion_radioButton")
        self.file_conversion_radioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.file_conversion_radioButton)

        self.dataset_conversion_radioButton = QRadioButton(self.file_operation_type_widget)
        self.dataset_conversion_radioButton.setObjectName(u"dataset_conversion_radioButton")
        self.dataset_conversion_radioButton.setCheckable(True)
        self.dataset_conversion_radioButton.setChecked(False)

        self.horizontalLayout.addWidget(self.dataset_conversion_radioButton)

        self.verticalLayout_2.addWidget(self.file_operation_type_widget)

        self.format_select_widget = QWidget(self.centralwidget)
        self.format_select_widget.setObjectName(u"format_select_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.format_select_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.src_format_label = QLabel(self.format_select_widget)
        self.src_format_label.setObjectName(u"src_format_label")
        self.src_format_label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.src_format_label)

        self.src_format_comboBox = QComboBox(self.format_select_widget)
        self.src_format_comboBox.addItem("")
        self.src_format_comboBox.addItem("")
        self.src_format_comboBox.addItem("")
        self.src_format_comboBox.addItem("")
        self.src_format_comboBox.addItem("")
        self.src_format_comboBox.setObjectName(u"src_format_comboBox")

        self.horizontalLayout_2.addWidget(self.src_format_comboBox)

        self.dst_format_label = QLabel(self.format_select_widget)
        self.dst_format_label.setObjectName(u"dst_format_label")
        self.dst_format_label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.dst_format_label)

        self.dst_format_comboBox = QComboBox(self.format_select_widget)
        self.dst_format_comboBox.addItem("")
        self.dst_format_comboBox.addItem("")
        self.dst_format_comboBox.addItem("")
        self.dst_format_comboBox.addItem("")
        self.dst_format_comboBox.addItem("")
        self.dst_format_comboBox.setObjectName(u"dst_format_comboBox")

        self.horizontalLayout_2.addWidget(self.dst_format_comboBox)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 2)

        self.verticalLayout_2.addWidget(self.format_select_widget)

        self.divide_proportion_widget = QWidget(self.centralwidget)
        self.divide_proportion_widget.setObjectName(u"divide_proportion_widget")
        self.horizontalLayout_3 = QHBoxLayout(self.divide_proportion_widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.divide_proportion_label = QLabel(self.divide_proportion_widget)
        self.divide_proportion_label.setObjectName(u"divide_proportion_label")

        self.horizontalLayout_3.addWidget(self.divide_proportion_label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self._8_1_1_radioButton = QRadioButton(self.divide_proportion_widget)
        self._8_1_1_radioButton.setObjectName(u"_8_1_1_radioButton")

        self.horizontalLayout_3.addWidget(self._8_1_1_radioButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self._6_2_2_radioButton = QRadioButton(self.divide_proportion_widget)
        self._6_2_2_radioButton.setObjectName(u"_6_2_2_radioButton")

        self.horizontalLayout_3.addWidget(self._6_2_2_radioButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self._no_divide_radioButton = QRadioButton(self.divide_proportion_widget)
        self._no_divide_radioButton.setObjectName(u"_no_divide_radioButton")
        self._no_divide_radioButton.setChecked(True)

        self.horizontalLayout_3.addWidget(self._no_divide_radioButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self._custom_radioButton = QRadioButton(self.divide_proportion_widget)
        self._custom_radioButton.setObjectName(u"_custom_radioButton")

        self.horizontalLayout_3.addWidget(self._custom_radioButton)

        self.divide_custom_lineEdit = QLineEdit(self.divide_proportion_widget)
        self.divide_custom_lineEdit.setObjectName(u"divide_custom_lineEdit")

        self.horizontalLayout_3.addWidget(self.divide_custom_lineEdit)

        self.verticalLayout_2.addWidget(self.divide_proportion_widget)

        self.file_path_widget = QWidget(self.centralwidget)
        self.file_path_widget.setObjectName(u"file_path_widget")
        self.horizontalLayout_6 = QHBoxLayout(self.file_path_widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.src_path_label = QLabel(self.file_path_widget)
        self.src_path_label.setObjectName(u"src_path_label")

        self.horizontalLayout_6.addWidget(self.src_path_label)

        self.src_path_lineEdit = QLineEdit(self.file_path_widget)
        self.src_path_lineEdit.setObjectName(u"src_path_lineEdit")
        self.src_path_lineEdit.setDragEnabled(False)
        self.src_path_lineEdit.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.src_path_lineEdit)

        self.dst_path_label = QLabel(self.file_path_widget)
        self.dst_path_label.setObjectName(u"dst_path_label")

        self.horizontalLayout_6.addWidget(self.dst_path_label)

        self.dst_path_lineEdit = QLineEdit(self.file_path_widget)
        self.dst_path_lineEdit.setObjectName(u"dst_path_lineEdit")
        self.dst_path_lineEdit.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.dst_path_lineEdit)

        self.verticalLayout_2.addWidget(self.file_path_widget)

        self.buttons_widget = QWidget(self.centralwidget)
        self.buttons_widget.setObjectName(u"buttons_widget")
        self.verticalLayout_3 = QVBoxLayout(self.buttons_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_7 = QWidget(self.buttons_widget)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.select_src_path_pushButton = QPushButton(self.widget_7)
        self.select_src_path_pushButton.setObjectName(u"select_src_path_pushButton")

        self.horizontalLayout_4.addWidget(self.select_src_path_pushButton)

        self.select_dst_path_pushButton = QPushButton(self.widget_7)
        self.select_dst_path_pushButton.setObjectName(u"select_dst_path_pushButton")

        self.horizontalLayout_4.addWidget(self.select_dst_path_pushButton)

        self.verticalLayout_3.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.buttons_widget)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.start_conversion_pushButton = QPushButton(self.widget_6)
        self.start_conversion_pushButton.setObjectName(u"start_conversion_pushButton")

        self.horizontalLayout_5.addWidget(self.start_conversion_pushButton)

        self.view_result_pushButton = QPushButton(self.widget_6)
        self.view_result_pushButton.setObjectName(u"view_result_pushButton")

        self.horizontalLayout_5.addWidget(self.view_result_pushButton)

        self.verticalLayout_3.addWidget(self.widget_6)

        self.verticalLayout_2.addWidget(self.buttons_widget)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_2.addWidget(self.progressBar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        # 给按钮绑定事件
        self.set_buttons_clicked()

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.file_conversion_radioButton.setText(
            QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8f6c\u6362  ", None))
        self.dataset_conversion_radioButton.setText(
            QCoreApplication.translate("MainWindow", u"\u6570\u636e\u96c6\u8f6c\u6362\u4e0e\u5212\u5206", None))
        self.src_format_label.setText(QCoreApplication.translate("MainWindow", u"\u6e90\u6837\u5f0f", None))
        self.src_format_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"DOTA", None))
        self.src_format_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"VOC", None))
        self.src_format_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"COCO", None))
        self.src_format_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"YOLO", None))
        self.src_format_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Data Labelme", None))

        self.dst_format_label.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u6837\u5f0f", None))
        self.dst_format_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"DOTA", None))
        self.dst_format_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"VOC", None))
        self.dst_format_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"COCO", None))
        self.dst_format_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"YOLO", None))
        self.dst_format_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Data Labelme", None))

        self.divide_proportion_label.setText(
            QCoreApplication.translate("MainWindow", u"\u5212\u5206\u6bd4\u4f8b", None))
        self._8_1_1_radioButton.setText(QCoreApplication.translate("MainWindow", u"8 : 1 : 1", None))
        self._6_2_2_radioButton.setText(QCoreApplication.translate("MainWindow", u"6 : 2 : 2", None))
        self._no_divide_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u5212\u5206", None))
        self._custom_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49", None))
        self.src_path_label.setText(QCoreApplication.translate("MainWindow", u"\u6e90\u8def\u5f84  ", None))
        self.dst_path_label.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u8def\u5f84", None))
        self.select_src_path_pushButton.setText(
            QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6e90\u6587\u4ef6/\u6587\u4ef6\u5939", None))
        self.select_dst_path_pushButton.setText(
            QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4fdd\u5b58\u8def\u5f84", None))
        self.start_conversion_pushButton.setText(
            QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8f6c\u6362", None))
        self.view_result_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u7ed3\u679c", None))

    def set_buttons_clicked(self):
        self.start_conversion_pushButton.clicked.connect(self.on_start_conversion_clicked)
        self.view_result_pushButton.clicked.connect(self.on_view_result_clicked)
        self.select_src_path_pushButton.clicked.connect(self.on_select_src_path_clicked)
        self.select_dst_path_pushButton.clicked.connect(self.on_select_dst_path_clicked)

    def on_start_conversion_clicked(self):
        print("开始转换按钮被点击")

        user_input = self.get_all_input()
        if user_input.file_operation_type == Ui_Main_UserInput.Operation_Type.FILE:
            print("文件转换")
        elif user_input.file_operation_type == Ui_Main_UserInput.Operation_Type.DATASET:
            print("数据集转换")
            format_funcs = {
                (Ui_Main_UserInput.Dataset_Format.DOTA, Ui_Main_UserInput.Dataset_Format.VOC): dota2voc,
                (Ui_Main_UserInput.Dataset_Format.DOTA, Ui_Main_UserInput.Dataset_Format.COCO): dota2coco,
                (Ui_Main_UserInput.Dataset_Format.DOTA, Ui_Main_UserInput.Dataset_Format.YOLO): dota2yolo,
                (Ui_Main_UserInput.Dataset_Format.DOTA, Ui_Main_UserInput.Dataset_Format.DATA_LABELME): dota2labelme,
                (Ui_Main_UserInput.Dataset_Format.VOC, Ui_Main_UserInput.Dataset_Format.COCO): voc2coco,
                (Ui_Main_UserInput.Dataset_Format.VOC, Ui_Main_UserInput.Dataset_Format.DATA_LABELME): voc2labelme,
                (Ui_Main_UserInput.Dataset_Format.VOC, Ui_Main_UserInput.Dataset_Format.YOLO): voc2yolo,
                (Ui_Main_UserInput.Dataset_Format.VOC, Ui_Main_UserInput.Dataset_Format.DOTA): voc2dota,
                (Ui_Main_UserInput.Dataset_Format.COCO, Ui_Main_UserInput.Dataset_Format.YOLO): coco2yolo,
                (Ui_Main_UserInput.Dataset_Format.COCO, Ui_Main_UserInput.Dataset_Format.DATA_LABELME): coco2labelme,
                (Ui_Main_UserInput.Dataset_Format.COCO, Ui_Main_UserInput.Dataset_Format.VOC): coco2voc,
                (Ui_Main_UserInput.Dataset_Format.COCO, Ui_Main_UserInput.Dataset_Format.DOTA): coco2dota,
                (Ui_Main_UserInput.Dataset_Format.YOLO, Ui_Main_UserInput.Dataset_Format.VOC): yolo2voc,
                (Ui_Main_UserInput.Dataset_Format.YOLO, Ui_Main_UserInput.Dataset_Format.DATA_LABELME): yolo2labelme,
                (Ui_Main_UserInput.Dataset_Format.YOLO, Ui_Main_UserInput.Dataset_Format.COCO): yolo2coco,
                (Ui_Main_UserInput.Dataset_Format.YOLO, Ui_Main_UserInput.Dataset_Format.DOTA): yolo2dota,
                (Ui_Main_UserInput.Dataset_Format.DATA_LABELME, Ui_Main_UserInput.Dataset_Format.VOC): labelme2voc,
                (Ui_Main_UserInput.Dataset_Format.DATA_LABELME, Ui_Main_UserInput.Dataset_Format.COCO): labelme2coco,
                (Ui_Main_UserInput.Dataset_Format.DATA_LABELME, Ui_Main_UserInput.Dataset_Format.YOLO): labelme2yolo,
                (Ui_Main_UserInput.Dataset_Format.DATA_LABELME, Ui_Main_UserInput.Dataset_Format.DOTA): labelme2dota,
            }

            func = format_funcs.get((user_input.src_format, user_input.dst_format))
            if func:
                print("开始转换")
                func(user_input.src_path, user_input.dst_path)
            else:
                print("不支持的格式转换")

    def on_view_result_clicked(self):
        print("查看结果按钮被点击")
        folder_path = self.dst_path_lineEdit.text()
        url = QUrl.fromLocalFile(folder_path)
        QDesktopServices.openUrl(url)

    def on_select_src_path_clicked(self):
        file_name = QFileDialog.getExistingDirectory(self.parent, '选择源文件夹')
        self.src_path_lineEdit.setText(file_name)

    def on_select_dst_path_clicked(self):
        file_name = QFileDialog.getExistingDirectory(self.parent, '选择目标文件夹')
        self.dst_path_lineEdit.setText(file_name)

    def get_all_input(self) -> Ui_Main_UserInput:
        file_operation_type = Ui_Main_UserInput.Operation_Type.FILE \
            if self.file_conversion_radioButton.isChecked() else Ui_Main_UserInput.Operation_Type.DATASET

        # 获取src格式
        src_format = Ui_Main_UserInput.Dataset_Format(self.src_format_comboBox.currentText())

        # 获取dst格式
        dst_format = Ui_Main_UserInput.Dataset_Format(self.dst_format_comboBox.currentText())

        divide_proportion = ''
        if self._8_1_1_radioButton.isChecked():
            divide_proportion = "8:1:1"
        elif self._6_2_2_radioButton.isChecked():
            divide_proportion = "6:2:2"
        elif self._no_divide_radioButton.isChecked():
            divide_proportion = "No divide"
        elif self._custom_radioButton.isChecked():
            divide_proportion = self.divide_custom_lineEdit.text()

        src_path = self.src_path_lineEdit.text()
        dst_path = self.dst_path_lineEdit.text()

        return Ui_Main_UserInput(file_operation_type=file_operation_type,
                                 src_format=src_format,
                                 dst_format=dst_format,
                                 divide_proportion=divide_proportion,
                                 src_path=src_path,
                                 dst_path=dst_path)
