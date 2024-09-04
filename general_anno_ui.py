# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLCDNumber, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSlider, QSpinBox, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1085, 818)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.first_tab = QTabWidget(self.centralwidget)
        self.first_tab.setObjectName(u"first_tab")
        self.classification_tab = QWidget()
        self.classification_tab.setObjectName(u"classification_tab")
        self.verticalLayout_3 = QVBoxLayout(self.classification_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalTabWidget_2 = QTabWidget(self.classification_tab)
        self.horizontalTabWidget_2.setObjectName(u"horizontalTabWidget_2")
        self.cl_anno_tab = QWidget()
        self.cl_anno_tab.setObjectName(u"cl_anno_tab")
        self.horizontalLayout_3 = QHBoxLayout(self.cl_anno_tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cl_image_lbl = QLabel(self.cl_anno_tab)
        self.cl_image_lbl.setObjectName(u"cl_image_lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cl_image_lbl.sizePolicy().hasHeightForWidth())
        self.cl_image_lbl.setSizePolicy(sizePolicy)
        self.cl_image_lbl.setMaximumSize(QSize(1000, 800))
        self.cl_image_lbl.setPixmap(QPixmap(u"../../Users/PC/.designer/backup/no image.jpg"))
        self.cl_image_lbl.setScaledContents(True)
        self.cl_image_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.cl_image_lbl)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.cl_folder_open_btn = QPushButton(self.cl_anno_tab)
        self.cl_folder_open_btn.setObjectName(u"cl_folder_open_btn")

        self.verticalLayout_4.addWidget(self.cl_folder_open_btn)

        self.cl_save_btn = QPushButton(self.cl_anno_tab)
        self.cl_save_btn.setObjectName(u"cl_save_btn")

        self.verticalLayout_4.addWidget(self.cl_save_btn)

        self.cl_class_info_btn = QPushButton(self.cl_anno_tab)
        self.cl_class_info_btn.setObjectName(u"cl_class_info_btn")

        self.verticalLayout_4.addWidget(self.cl_class_info_btn)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.cl_current_num = QLCDNumber(self.cl_anno_tab)
        self.cl_current_num.setObjectName(u"cl_current_num")
        font = QFont()
        font.setFamilies([u"Agency FB"])
        font.setBold(True)
        font.setItalic(False)
        self.cl_current_num.setFont(font)
        self.cl_current_num.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.cl_current_num)

        self.label_2 = QLabel(self.cl_anno_tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.cl_total_num = QLCDNumber(self.cl_anno_tab)
        self.cl_total_num.setObjectName(u"cl_total_num")
        self.cl_total_num.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.cl_total_num)

        self.horizontalLayout_4.setStretch(0, 5)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 5)

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.file_list_table = QTableWidget(self.cl_anno_tab)
        if (self.file_list_table.columnCount() < 2):
            self.file_list_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.file_list_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.file_list_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.file_list_table.setObjectName(u"file_list_table")
        self.file_list_table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.file_list_table.setStyleSheet(u"QLCDNumber {\n"
"    color: red;              /* \uc22b\uc790\uc758 \uc0c9\uc0c1\uc744 \ube68\uac04\uc0c9\uc73c\ub85c \uc124\uc815 */\n"
"    background-color: black; /* \ubc30\uacbd \uc0c9\uc0c1\uc744 \uac80\uc740\uc0c9\uc73c\ub85c \uc124\uc815 */\n"
"}")
        self.file_list_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.verticalLayout_4.addWidget(self.file_list_table)

        self.class_choice_table = QTableWidget(self.cl_anno_tab)
        if (self.class_choice_table.columnCount() < 2):
            self.class_choice_table.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.class_choice_table.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.class_choice_table.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.class_choice_table.setObjectName(u"class_choice_table")
        self.class_choice_table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.class_choice_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.verticalLayout_4.addWidget(self.class_choice_table)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.setStretch(4, 6)
        self.verticalLayout_4.setStretch(5, 2)

        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalTabWidget_2.addTab(self.cl_anno_tab, "")
        self.cl_aug_tab = QWidget()
        self.cl_aug_tab.setObjectName(u"cl_aug_tab")
        self.horizontalLayout_7 = QHBoxLayout(self.cl_aug_tab)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.cl_aug_origin_img = QLabel(self.cl_aug_tab)
        self.cl_aug_origin_img.setObjectName(u"cl_aug_origin_img")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cl_aug_origin_img.sizePolicy().hasHeightForWidth())
        self.cl_aug_origin_img.setSizePolicy(sizePolicy1)
        self.cl_aug_origin_img.setMaximumSize(QSize(150, 150))
        self.cl_aug_origin_img.setPixmap(QPixmap(u"../../Users/PC/.designer/backup/no image.jpg"))
        self.cl_aug_origin_img.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.cl_aug_origin_img)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.cl_aug_text = QLabel(self.cl_aug_tab)
        self.cl_aug_text.setObjectName(u"cl_aug_text")

        self.verticalLayout_17.addWidget(self.cl_aug_text)


        self.horizontalLayout_8.addLayout(self.verticalLayout_17)

        self.horizontalLayout_8.setStretch(0, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.scrollArea = QScrollArea(self.cl_aug_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 20, 20))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.aug_image_grid = QGridLayout()
        self.aug_image_grid.setObjectName(u"aug_image_grid")

        self.gridLayout_2.addLayout(self.aug_image_grid, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 5)

        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalFrame_5 = QFrame(self.cl_aug_tab)
        self.verticalFrame_5.setObjectName(u"verticalFrame_5")
        self.verticalFrame_5.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.verticalLayout_9 = QVBoxLayout(self.verticalFrame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.cl_aug_folder_open = QPushButton(self.verticalFrame_5)
        self.cl_aug_folder_open.setObjectName(u"cl_aug_folder_open")

        self.verticalLayout_9.addWidget(self.cl_aug_folder_open)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.vf_check = QCheckBox(self.verticalFrame_5)
        self.vf_check.setObjectName(u"vf_check")

        self.horizontalLayout_15.addWidget(self.vf_check)

        self.hf_check = QCheckBox(self.verticalFrame_5)
        self.hf_check.setObjectName(u"hf_check")

        self.horizontalLayout_15.addWidget(self.hf_check)


        self.verticalLayout_10.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.ro_check = QCheckBox(self.verticalFrame_5)
        self.ro_check.setObjectName(u"ro_check")

        self.horizontalLayout_14.addWidget(self.ro_check)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_6 = QLabel(self.verticalFrame_5)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setMinimumSize(QSize(0, 10))

        self.verticalLayout_14.addWidget(self.label_6)

        self.angle_slider = QSlider(self.verticalFrame_5)
        self.angle_slider.setObjectName(u"angle_slider")
        self.angle_slider.setMinimum(1)
        self.angle_slider.setMaximum(359)
        self.angle_slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_14.addWidget(self.angle_slider)

        self.angle_entry = QLineEdit(self.verticalFrame_5)
        self.angle_entry.setObjectName(u"angle_entry")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.angle_entry.sizePolicy().hasHeightForWidth())
        self.angle_entry.setSizePolicy(sizePolicy3)
        self.angle_entry.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_14.addWidget(self.angle_entry)

        self.verticalLayout_14.setStretch(0, 1)
        self.verticalLayout_14.setStretch(1, 2)
        self.verticalLayout_14.setStretch(2, 2)

        self.horizontalLayout_14.addLayout(self.verticalLayout_14)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 3)

        self.verticalLayout_10.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.bl_check = QCheckBox(self.verticalFrame_5)
        self.bl_check.setObjectName(u"bl_check")

        self.horizontalLayout_13.addWidget(self.bl_check)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_7 = QLabel(self.verticalFrame_5)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)

        self.verticalLayout_11.addWidget(self.label_7)

        self.blur_slider = QSlider(self.verticalFrame_5)
        self.blur_slider.setObjectName(u"blur_slider")
        self.blur_slider.setMinimum(3)
        self.blur_slider.setMaximum(11)
        self.blur_slider.setSingleStep(2)
        self.blur_slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_11.addWidget(self.blur_slider)

        self.blur_entry = QLineEdit(self.verticalFrame_5)
        self.blur_entry.setObjectName(u"blur_entry")
        self.blur_entry.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_11.addWidget(self.blur_entry)

        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_11.setStretch(1, 2)
        self.verticalLayout_11.setStretch(2, 2)

        self.horizontalLayout_13.addLayout(self.verticalLayout_11)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 3)

        self.verticalLayout_10.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.br_check = QCheckBox(self.verticalFrame_5)
        self.br_check.setObjectName(u"br_check")

        self.horizontalLayout_12.addWidget(self.br_check)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_8 = QLabel(self.verticalFrame_5)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)

        self.verticalLayout_12.addWidget(self.label_8)

        self.bright_slider = QSlider(self.verticalFrame_5)
        self.bright_slider.setObjectName(u"bright_slider")
        self.bright_slider.setMinimum(-255)
        self.bright_slider.setMaximum(255)
        self.bright_slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_12.addWidget(self.bright_slider)

        self.bright_entry = QLineEdit(self.verticalFrame_5)
        self.bright_entry.setObjectName(u"bright_entry")
        self.bright_entry.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.bright_entry)


        self.horizontalLayout_12.addLayout(self.verticalLayout_12)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 3)

        self.verticalLayout_10.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.no_check = QCheckBox(self.verticalFrame_5)
        self.no_check.setObjectName(u"no_check")

        self.horizontalLayout_9.addWidget(self.no_check)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_9 = QLabel(self.verticalFrame_5)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)

        self.verticalLayout_13.addWidget(self.label_9)

        self.noise_slider = QSlider(self.verticalFrame_5)
        self.noise_slider.setObjectName(u"noise_slider")
        self.noise_slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_13.addWidget(self.noise_slider)

        self.noise_entry = QLineEdit(self.verticalFrame_5)
        self.noise_entry.setObjectName(u"noise_entry")
        self.noise_entry.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_13.addWidget(self.noise_entry)


        self.horizontalLayout_9.addLayout(self.verticalLayout_13)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 3)

        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.ra_check = QCheckBox(self.verticalFrame_5)
        self.ra_check.setObjectName(u"ra_check")

        self.horizontalLayout_11.addWidget(self.ra_check)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 1)
        self.verticalLayout_10.setStretch(2, 1)
        self.verticalLayout_10.setStretch(3, 1)
        self.verticalLayout_10.setStretch(4, 1)
        self.verticalLayout_10.setStretch(5, 1)

        self.verticalLayout_9.addLayout(self.verticalLayout_10)

        self.aug_preview = QPushButton(self.verticalFrame_5)
        self.aug_preview.setObjectName(u"aug_preview")

        self.verticalLayout_9.addWidget(self.aug_preview)

        self.cl_aug_save = QPushButton(self.verticalFrame_5)
        self.cl_aug_save.setObjectName(u"cl_aug_save")

        self.verticalLayout_9.addWidget(self.cl_aug_save)

        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 7)
        self.verticalLayout_9.setStretch(2, 1)
        self.verticalLayout_9.setStretch(3, 1)

        self.horizontalLayout_2.addWidget(self.verticalFrame_5)

        self.horizontalLayout_2.setStretch(0, 3)

        self.horizontalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalTabWidget_2.addTab(self.cl_aug_tab, "")

        self.verticalLayout_2.addWidget(self.horizontalTabWidget_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.first_tab.addTab(self.classification_tab, "")
        self.detection_tab = QWidget()
        self.detection_tab.setObjectName(u"detection_tab")
        self.verticalLayout_6 = QVBoxLayout(self.detection_tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.de_folder_open_btn = QPushButton(self.detection_tab)
        self.de_folder_open_btn.setObjectName(u"de_folder_open_btn")

        self.verticalLayout_5.addWidget(self.de_folder_open_btn)

        self.groupBox = QGroupBox(self.detection_tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setMaximumSize(QSize(16777215, 150))
        self.groupBox.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.groupBox.setAcceptDrops(True)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.de_rec = QRadioButton(self.groupBox)
        self.de_rec.setObjectName(u"de_rec")
        self.de_rec.setChecked(True)

        self.verticalLayout.addWidget(self.de_rec)

        self.de_circle = QRadioButton(self.groupBox)
        self.de_circle.setObjectName(u"de_circle")

        self.verticalLayout.addWidget(self.de_circle)

        self.de_Polygon = QRadioButton(self.groupBox)
        self.de_Polygon.setObjectName(u"Polygon")

        self.verticalLayout.addWidget(self.de_Polygon)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.detection_tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 15))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.label)

        self.de_class_choice = QSpinBox(self.groupBox_2)
        self.de_class_choice.setObjectName(u"de_class_choice")
        self.de_class_choice.setAcceptDrops(False)
        self.de_class_choice.setMaximum(9)

        self.verticalLayout_15.addWidget(self.de_class_choice)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.delete_row = QPushButton(self.detection_tab)
        self.delete_row.setObjectName(u"delete_row")

        self.verticalLayout_5.addWidget(self.delete_row)

        self.de_image_save = QPushButton(self.detection_tab)
        self.de_image_save.setObjectName(u"de_image_save")

        self.verticalLayout_5.addWidget(self.de_image_save)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.de_image_lbl = QLabel(self.detection_tab)
        self.de_image_lbl.setObjectName(u"de_image_lbl")
        self.de_image_lbl.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.de_image_lbl.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.de_image_lbl.setPixmap(QPixmap(u"no image.jpg"))
        self.de_image_lbl.setScaledContents(True)

        self.horizontalLayout.addWidget(self.de_image_lbl)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.de_list_table = QTableWidget(self.detection_tab)
        if (self.de_list_table.columnCount() < 1):
            self.de_list_table.setColumnCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.de_list_table.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        self.de_list_table.setObjectName(u"de_list_table")
        self.de_list_table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.de_list_table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.de_list_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.verticalLayout_8.addWidget(self.de_list_table)

        self.labeling_change_btn = QPushButton(self.detection_tab)
        self.labeling_change_btn.setObjectName(u"labeling_change_btn")

        self.verticalLayout_8.addWidget(self.labeling_change_btn)

        self.de_class_choice_table = QTableWidget(self.detection_tab)
        if (self.de_class_choice_table.columnCount() < 6):
            self.de_class_choice_table.setColumnCount(6)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.de_class_choice_table.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        font1 = QFont()
        font1.setPointSize(9)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem6.setFont(font1);
        self.de_class_choice_table.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.de_class_choice_table.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.de_class_choice_table.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.de_class_choice_table.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.de_class_choice_table.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        self.de_class_choice_table.setObjectName(u"de_class_choice_table")
        self.de_class_choice_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.de_class_choice_table.setColumnCount(6)
        self.de_class_choice_table.horizontalHeader().setCascadingSectionResizes(False)
        self.de_class_choice_table.horizontalHeader().setDefaultSectionSize(40)
        self.de_class_choice_table.verticalHeader().setCascadingSectionResizes(False)
        self.de_class_choice_table.verticalHeader().setDefaultSectionSize(29)

        self.verticalLayout_8.addWidget(self.de_class_choice_table)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_8)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 7)
        self.horizontalLayout.setStretch(2, 2)

        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.first_tab.addTab(self.detection_tab, "")

        self.horizontalLayout_5.addWidget(self.first_tab)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.first_tab.setCurrentIndex(1)
        self.horizontalTabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.cl_image_lbl.setText("")
        self.cl_folder_open_btn.setText(QCoreApplication.translate("MainWindow", u"Folder Open", None))
        self.cl_save_btn.setText(QCoreApplication.translate("MainWindow", u"Save Result", None))
        self.cl_class_info_btn.setText(QCoreApplication.translate("MainWindow", u"Class Info", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"/", None))
        ___qtablewidgetitem = self.file_list_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"filename", None));
        ___qtablewidgetitem1 = self.file_list_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"class", None));
        ___qtablewidgetitem2 = self.class_choice_table.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\ud074\ub798\uc2a4", None));
        ___qtablewidgetitem3 = self.class_choice_table.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\uc120\ud0dd", None));
        self.horizontalTabWidget_2.setTabText(self.horizontalTabWidget_2.indexOf(self.cl_anno_tab), QCoreApplication.translate("MainWindow", u"Annotation", None))
        self.cl_aug_origin_img.setText("")
        self.cl_aug_text.setText(QCoreApplication.translate("MainWindow", u"\uc6d0\ubcf8 \ud3f4\ub354 \uc774\ubbf8\uc9c0\uc218 : 3232\n"
"\ud604\uc7ac \uc99d\uac15\uc728 : 3x\n"
"\uc99d\uac15\ud3f4\ub354 \uc774\ubbf8\uc9c0 \uc218 : 9696\n"
"", None))
        self.cl_aug_folder_open.setText(QCoreApplication.translate("MainWindow", u"Folder Open", None))
        self.vf_check.setText(QCoreApplication.translate("MainWindow", u"Vertical Flip", None))
        self.hf_check.setText(QCoreApplication.translate("MainWindow", u"Horizontal Flip", None))
        self.ro_check.setText(QCoreApplication.translate("MainWindow", u"Rotation", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\ud68c\uc804\uac01\ub3c4(1 ~ 359)", None))
        self.bl_check.setText(QCoreApplication.translate("MainWindow", u"Blur", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\uc815\ub3c4( 3 ~ 11 )", None))
        self.br_check.setText(QCoreApplication.translate("MainWindow", u"Bright", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\uc815\ub3c4 (-255 ~ 255)", None))
        self.no_check.setText(QCoreApplication.translate("MainWindow", u"Noise", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\uc815\ub3c4 (0 ~ 100)", None))
        self.ra_check.setText(QCoreApplication.translate("MainWindow", u"Random Crop", None))
        self.aug_preview.setText(QCoreApplication.translate("MainWindow", u"\uc99d\uac15 \ubbf8\ub9ac\ubcf4\uae30", None))
        self.cl_aug_save.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \ubc0f \ub77c\ubca8\uc800\uc7a5", None))
        self.horizontalTabWidget_2.setTabText(self.horizontalTabWidget_2.indexOf(self.cl_aug_tab), QCoreApplication.translate("MainWindow", u"Augmentation", None))
        self.first_tab.setTabText(self.first_tab.indexOf(self.classification_tab), QCoreApplication.translate("MainWindow", u"Classification", None))
        self.de_folder_open_btn.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
#if QT_CONFIG(tooltip)
        self.groupBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.groupBox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Labelling Shape", None))
        self.de_rec.setText(QCoreApplication.translate("MainWindow", u"Rectangle", None))
        self.de_circle.setText(QCoreApplication.translate("MainWindow", u"Circle", None))
        self.de_Polygon.setText(QCoreApplication.translate("MainWindow", u"Polygon", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Choose Class", None))
        self.delete_row.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.de_image_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.de_image_lbl.setText("")
        ___qtablewidgetitem4 = self.de_list_table.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Filename", None));
        self.labeling_change_btn.setText(QCoreApplication.translate("MainWindow", u"Labelling Info", None))
        ___qtablewidgetitem5 = self.de_class_choice_table.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"type", None));
        ___qtablewidgetitem6 = self.de_class_choice_table.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"class", None));
        ___qtablewidgetitem7 = self.de_class_choice_table.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"x0", None));
        ___qtablewidgetitem8 = self.de_class_choice_table.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"y0", None));
        ___qtablewidgetitem9 = self.de_class_choice_table.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"x1", None));
        ___qtablewidgetitem10 = self.de_class_choice_table.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"y1", None));
        self.first_tab.setTabText(self.first_tab.indexOf(self.detection_tab), QCoreApplication.translate("MainWindow", u"Detection", None))
    # retranslateUi

