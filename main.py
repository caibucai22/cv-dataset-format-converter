# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
                               QLineEdit, QMainWindow, QProgressBar, QPushButton,
                               QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setCheckable(True)
        self.radioButton_2.setChecked(False)

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.verticalLayout_2.addWidget(self.widget)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.comboBox = QComboBox(self.widget_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox_2 = QComboBox(self.widget_3)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_2.addWidget(self.comboBox_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 2)

        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.radioButton_3 = QRadioButton(self.widget_4)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_3.addWidget(self.radioButton_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.radioButton_4 = QRadioButton(self.widget_4)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_3.addWidget(self.radioButton_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.radioButton_5 = QRadioButton(self.widget_4)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.horizontalLayout_3.addWidget(self.radioButton_5)

        self.lineEdit = QLineEdit(self.widget_4)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.radioButton_6 = QRadioButton(self.widget_4)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.horizontalLayout_3.addWidget(self.radioButton_6)

        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_8 = QWidget(self.centralwidget)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.widget_8)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.widget_8)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setDragEnabled(False)
        self.lineEdit_3.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.lineEdit_3)

        self.label_5 = QLabel(self.widget_8)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.lineEdit_2 = QLineEdit(self.widget_8)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.lineEdit_2)

        self.verticalLayout_2.addWidget(self.widget_8)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_2 = QPushButton(self.widget_7)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.widget_7)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.verticalLayout_3.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_3 = QPushButton(self.widget_6)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_5.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget_6)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_5.addWidget(self.pushButton_4)

        self.verticalLayout_3.addWidget(self.widget_6)

        self.verticalLayout_2.addWidget(self.widget_2)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_2.addWidget(self.progressBar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8f6c\u6362  ", None))
        self.radioButton_2.setText(
            QCoreApplication.translate("MainWindow", u"\u6570\u636e\u96c6\u8f6c\u6362\u4e0e\u5212\u5206", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6e90\u6837\u5f0f", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"VOC", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"COCO", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"YOLO", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Data Labelme", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u6837\u5f0f", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"VOC", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"COCO", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"YOLO", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Data Labelme", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5212\u5206\u6bd4\u4f8b", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"8 : 1 : 1", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"6 : 2 : 2", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u5212\u5206", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6e90\u8def\u5f84  ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u8def\u5f84", None))
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6e90\u6587\u4ef6/\u6587\u4ef6\u5939", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4fdd\u5b58\u8def\u5f84", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8f6c\u6362", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u7ed3\u679c", None))
    # retranslateUi


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec())
