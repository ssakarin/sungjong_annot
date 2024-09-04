from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QMainWindow, QDialog, QMessageBox, QFileDialog, QTableWidgetItem, QTextEdit, QVBoxLayout, QPushButton, QLabel, QWidget, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QTableWidget
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QImage, QColor, QPixmap, QPainter, QPen, QColor, QBrush
from general_anno_ui import Ui_MainWindow

import sys, os, shutil
import pandas as pd
import cv2
import random
import numpy as np

class TextEditDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit(self)
        self.saveButton = QPushButton('Save', self)
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.saveButton)
        self.setLayout(layout)
        self.setWindowTitle('Edit Text')
        self.setGeometry(300, 300, 400, 300)
        self.saveButton.clicked.connect(self.saveText)
        self.loadText() 

    def loadText(self):
        try:
            with open('class_list.txt', 'r', encoding='utf-8') as file:
                self.textEdit.setText(file.read())
        except FileNotFoundError:
            self.textEdit.setPlainText("File not found. A new file will be created.")

    def saveText(self):
        text = self.textEdit.toPlainText()
        with open('class_list.txt', 'w', encoding='utf-8') as file:
            file.write(text)

        self.close()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('통합 라벨링 프로그램')
        self.selected_dir = None
        self.aug_dir = None
        self.df = None
        self.selected_dir_de = None
        self.aug_dir_de = None
        self.df_de = None
        self.item_list = []
        self.item_list_de = []
        self.status_bar = self.statusBar()  # 스태이터스바 추가
                
        self.past_pos = None # 마우스 이벤트 시작값
        self.end_pos = None # 마우스 이벤트 종료값
        self.class_choice_table.setRowCount(0)
        self.drawing = False # 그림 그리는 중인가?
        self.imge_rgb = None 
        self.current_image = None
        self.image_pos = None
        self.poly_pos = []

        ######################agumentation변수##################
        self.aug_ratio = 1
        self.aug_num_images = 0
        self.sample_img = None
        self.grid_images = []
        self.aug_file_list = []
        self.save_img_list = []
        ######################detection변수##################
        self.Object_detection_info = []
        self.detection_info = []
        self.de_img_folder = None
        self.de_txt_folder = None
        self.line_color_list = [(255, 255, 0), (0, 255, 255),(0, 255, 0), (255, 0, 0),(0, 0, 255), (255, 0, 255),(255, 128, 0),(128, 0, 255),(0, 128, 128),(128, 128, 0)]
        # self.point_list = []

        with open('class_list.txt', "r") as inp:
            self.class_choice_table.setRowCount(len(list(inp)))

        with open('class_list.txt', "r") as inp:
            for i, linestr in enumerate(inp):
                self.class_choice_table.setItem(i, 0, QTableWidgetItem(linestr.replace("\n","")))
                self.class_choice_table.setItem(i, 1, QTableWidgetItem('0'))
                self.item_list.append(linestr.replace("\n",""))

        ###################################       함수 바인딩       #######################################

        self.cl_folder_open_btn.clicked.connect(self.select_dir)
        self.file_list_table.clicked.connect(self.file_list_click)
        self.cl_class_info_btn.clicked.connect(self.class_file_change)
        self.cl_save_btn.clicked.connect(self.save_result)
        self.cl_aug_folder_open.clicked.connect(self.open_aug_folder)
        self.aug_preview.clicked.connect(self.show_grid_images)
        self.cl_aug_save.clicked.connect(self.image_save_result)
        self.de_folder_open_btn.clicked.connect(self.detection_open)
        self.de_list_table.clicked.connect(self.de_file_list_click)
        self.de_class_choice_table.itemSelectionChanged.connect(self.de_show_image)
        self.delete_row.clicked.connect(self.de_delete_row)
        self.de_image_save.clicked.connect(self.de_Image_Save)
        #self.Square.clicked.connect(self.mousePressEvent)

        self.angle_entry.textChanged.connect(self.on_angle_text_changed)
        self.angle_slider.valueChanged.connect(self.on_angle_slider_changed)
        self.blur_entry.textChanged.connect(self.on_blur_text_changed)
        self.blur_slider.valueChanged.connect(self.on_blur_slider_changed)
        self.bright_entry.textChanged.connect(self.on_bright_text_changed)
        self.bright_slider.valueChanged.connect(self.on_bright_slider_changed)
        self.noise_entry.textChanged.connect(self.on_noise_text_changed)
        self.noise_slider.valueChanged.connect(self.on_noise_slider_changed)


    def init_df(self):
        col_listForDF = ['id']
        col_listForDF.extend(self.item_list)
        self.df = pd.DataFrame(columns=col_listForDF)

    def set_count(self): 
        row_sum = self.df[self.item_list].sum(axis = 1)
        total_count = len(self.df)
        labeled_count = total_count - (row_sum == 0).sum()
        self.cl_current_num.display(labeled_count)
        self.cl_total_num.display(total_count)

    def select_dir(self):
        selected_dir = QFileDialog.getExistingDirectory(self, '디렉토리 선택')

        self.init_df()

        if selected_dir != '':
            self.current_dir = selected_dir

            file_list_table = [f for f in os.listdir(self.current_dir) if f.endswith(".bmp") or f.endswith(".jpg") or f.endswith(".JPG") or f.endswith(".png")]
            if len(file_list_table) < 1:
                self.select_dir()
            else:
                if 'result.csv' in os.listdir(self.current_dir):
                    if sorted(self.df.columns) == sorted(pd.read_csv(self.current_dir + '/result.csv').columns):
                        self.df = pd.concat([self.df, pd.read_csv(self.current_dir + '/result.csv')])
                        self.file_list_table.setRowCount(0)
                        self.file_list_table.setRowCount(len(self.df))
                        self.file_list_table.setCurrentCell(0, 0)
                    else:
                        QMessageBox.warning(self, '클래스 정보 불일치', "클래스 정보가 불일치 합니다. \n새로운 데이터프레임을 생성합니다.")
                        self.df['id']=file_list_table
                        self.df = self.df.fillna(0)
                        self.file_list_table.setRowCount(0)
                        self.file_list_table.setRowCount(len(self.df))
                        self.file_list_table.setCurrentCell(0, 0)
                else:
                    self.df['id']=file_list_table
                    self.df = self.df.fillna(0)
                    self.file_list_table.setRowCount(0)
                    self.file_list_table.setRowCount(len(self.df))
                    self.file_list_table.setCurrentCell(0, 0)

                for rows in self.df.itertuples():
                    self.file_list_table.setItem(rows.Index, 0, QTableWidgetItem(str(rows.id)))
                    detatil = [getattr(rows, x) for x in self.item_list]
                    if 1 in detatil:
                        index = detatil.index(1)  # 1의 위치 찾기
                        attribute_name = self.item_list[index]  # 해당 속성 이름
                    else:
                        attribute_name = 'unKnown'
                    

                    self.file_list_table.setItem(rows.Index, 1, QTableWidgetItem(str(attribute_name)))
                    self.file_list_table.setRowHeight(rows.Index, 20)
                    self.set_filetable_color(rows.Index, sum(detatil))
        else:
            return 0
        #리셋
        self.set_count()
        self.show_image() 

    def show_image(self):
        row = self.file_list_table.currentRow()
        
        try:
            image_name = self.file_list_table.item(row, 0).text()
        except:
            return 0
        
        image_origin_path = f'{self.current_dir}/{image_name}'
        image_cv2 = cv2.imread(image_origin_path)
        self.image_rgb = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)

        height, width, _ = image_cv2.shape
        bytesPerLine = 3 * width 
        image_w = QImage(self.image_rgb.data, width, height, bytesPerLine, QImage.Format_RGB888)

        pixmap_b = QtGui.QPixmap.fromImage(image_w)

        image_b_resize = pixmap_b.scaled(800, 800, Qt.KeepAspectRatio)

        self.cl_image_lbl.setPixmap(image_b_resize)

        self.repair_key_event

    def repair_key_event(self):
        self.repair_keyevent.setFocus()

    def file_list_click(self):
        row = self.file_list_table.currentRow()
        detatil = [self.df.loc[row, x] for x in self.item_list]

        for i in range(len(detatil)):
            if detatil[i]:
                cell = QTableWidgetItem(str(detatil[i]))
                cell.setBackground(QColor('green'))
                self.class_choice_table.setItem(i, 1, cell)
            else:
                cell = QTableWidgetItem(str(detatil[i]))
                cell.setBackground(QColor(Qt.transparent))
                self.class_choice_table.setItem(i, 1, cell)

        self.show_image()

    def class_click(self):
        text = self.class_choice_table.item(self.class_choice_table.currentRow(), 0).text()
        row = self.file_list_table.currentRow()
        shout = 1 if self.df.loc[row, text] == 0 else 0

        self.df.loc[row, text] = shout
        detatil = [self.df.loc[row, x] for x in self.item_list]
        if 1 in detatil:
            index = detatil.index(1)  # 1의 위치 찾기
            attribute_name = self.item_list[index]  # 해당 속성 이름
        else:
            attribute_name = 'unKnown'
        self.file_list_table.setItem(row, 1, QTableWidgetItem(str(attribute_name)))
        if shout:
            cell = QTableWidgetItem(str(shout))
            cell.setBackground(QColor('green'))
            self.class_choice_table.setItem(self.class_choice_table.currentRow(), 1, cell)
        else:
            cell = QTableWidgetItem(str(shout))
            cell.setBackground(QColor(Qt.transparent))
            self.class_choice_table.setItem(self.class_choice_table.currentRow(), 1, cell)

        self.set_filetable_color(row, sum(detatil))
        self.set_count()
        del cell

    def number_key_press_event(self, e):
        if self.first_tab.currentIndex() == 0:
            press_key_num = int(e.text())
            # 0번은 10번으로 바꿈
            if press_key_num == 0:
                press_key_num = 10
            else:
                press_key_num = press_key_num

            if press_key_num <= len(self.item_list):
                self.class_choice_table.setCurrentCell(press_key_num - 1, 0)
                self.class_click()
        elif self.first_tab.currentIndex() == 1:
            print("dddddd")
            # press_key_num = int(e.text())
            # # 0번은 10번으로 바꿈
            # if press_key_num == 0:
            #     press_key_num = 10
            # else:
            #     press_key_num = press_key_num

            # if press_key_num <= len(self.item_list):4
            #     self.class_choice_table.setCurrentCell(press_key_num - 1, 0)
            #     self.class_click()


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_1:
            self.number_key_press_event(e)
        elif e.key() == Qt.Key_2:
            self.number_key_press_event(e)
        elif e.key() == Qt.Key_3:
            self.number_key_press_event(e)
        elif e.key() == Qt.Key_4:
            self.number_key_press_event(e)
        elif e.key() == Qt.Key_5:
            self.number_key_press_event(e)
        elif e.key() == Qt.Key_6:
            self.number_key_press_event(e)
        elif e.key() == Qt.Key_7:
            self.number_key_press_event(e)
        elif e.key() == Qt.Key_8:
            self.number_key_press_event(e)
        elif e.key() == Qt.Key_9:
            self.number_key_press_event(e)
        elif e.key() == Qt.Key_0:
            self.number_key_press_event(e)

        elif e.key() in (Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right):
            e.ignore()

        elif e.key() in (Qt.Key_A, Qt.Key_W):
            if self.first_tab.currentIndex() == 0:
                current_row = self.file_list_table.currentRow()
                if current_row <= 0:
                    row_count = self.file_list_table.rowCount()
                    self.file_list_table.setCurrentCell(row_count - 1, 0)
                    self.file_list_click()
                else:
                    self.file_list_table.setCurrentCell(current_row - 1, 0)
                    self.file_list_click()
            elif self.first_tab.currentIndex() == 1:
                current_row = self.de_list_table.currentRow()
                if current_row <= 0:
                    row_count = self.de_list_table.rowCount()
                    self.de_list_table.setCurrentCell(row_count - 1, 0)
                    self.de_file_list_click()
                else:
                    self.de_list_table.setCurrentCell(current_row - 1, 0)
                    self.de_file_list_click()

        elif e.key() == Qt.Key_D or e.key() == Qt.Key_S:
            if self.first_tab.currentIndex() == 0:
                current_row = self.file_list_table.currentRow()
                row_count = self.file_list_table.rowCount()
                if current_row >= row_count - 1:
                    self.file_list_table.setCurrentCell(0, 0)
                    self.file_list_click()
                else:
                    self.file_list_table.setCurrentCell(current_row + 1, 0)
                    self.file_list_click()
            elif self.first_tab.currentIndex() == 1:
                current_row = self.de_list_table.currentRow()
                row_count = self.de_list_table.rowCount()
                if current_row >= row_count - 1:
                    self.de_list_table.setCurrentCell(0, 0)
                    self.de_file_list_click()
                else:
                    self.de_list_table.setCurrentCell(current_row + 1, 0)
                    self.de_file_list_click()

    def save_result(self):
        self.df.to_csv(self.current_dir + '/result.csv', index= False)

    def set_filetable_color(self, current_row, count):
        fn = QTableWidgetItem(self.file_list_table.item(current_row, 0).text())
        is_labeled_color = QColor(10, 255, 10) if count > 0 else QColor(Qt.transparent)
        fn.setBackground(is_labeled_color)
        self.file_list_table.setItem(current_row, 0, fn)
        fn2 = QTableWidgetItem(self.file_list_table.item(current_row, 1).text())
        fn2.setBackground(is_labeled_color)
        self.file_list_table.setItem(current_row, 1, fn2)

    def class_file_change(self):
        dialog = TextEditDialog(self)
        dialog.exec()

        self.class_choice_table.setRowCount(0)
        self.item_list.clear()  

        with open('class_list.txt', "r") as inp:
            self.class_choice_table.setRowCount(len(list(inp)))

        with open('class_list.txt', "r") as inp:
            for i, linestr in enumerate(inp):
                self.class_choice_table.setItem(i, 0, QTableWidgetItem(linestr.replace("\n","")))
                self.class_choice_table.setItem(i, 1, QTableWidgetItem('0'))
                self.item_list.append(linestr.replace("\n",""))


        #######################################################################################
    def open_aug_folder(self):
        selected_dir = QFileDialog.getExistingDirectory(self, '디렉토리 선택')
        file_list_table = [f for f in os.listdir(selected_dir) if f.endswith(".bmp") or f.endswith(".jpg") or f.endswith(".JPG") or f.endswith(".png")]
        num_images = len(file_list_table)
        self.aug_dir = selected_dir
        self.aug_file_list = file_list_table
        self.aug_num_images = num_images
        randnum = random.randint(1,num_images)
        
        self.show_aug_sample_img(selected_dir, file_list_table[randnum - 1])
        self.set_claug_text()

    def show_aug_sample_img(self, current_dir, image_name):
        image_origin_path = f'{current_dir}/{image_name}'
        image_cv2 = cv2.imread(image_origin_path)
        self.image_rgb = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)
        self.image_rgb = cv2.resize(self.image_rgb, (150,150))
        self.sample_img = self.image_rgb

        height, width, _ = self.image_rgb.shape
        bytesPerLine = 3 * width
        image_w = QImage(self.image_rgb.data, width, height, bytesPerLine, QImage.Format_RGB888)

        pixmap_b = QtGui.QPixmap.fromImage(image_w)

        image_b_resize = pixmap_b.scaled(150, 150, Qt.KeepAspectRatio)

        self.cl_aug_origin_img.setPixmap(image_b_resize)

    def set_claug_text(self):
        text = f'원본 폴더 이미지수 : {self.aug_num_images}\n현재 증강율 : {self.aug_ratio}x\n증강폴더 이미지 수 : {self.aug_num_images * self.aug_ratio}\n'
        self.cl_aug_text.setText(text)

    def flip_method(self, is_save = False, img = None):
        if is_save:
            if self.vf_check.isChecked():
                vflipped_image = cv2.flip(img, 0)
                self.save_img_list.append(vflipped_image)
            if self.hf_check.isChecked():
                hflipped_image = cv2.flip(img, 1)
                self.save_img_list.append(hflipped_image)
            if self.vf_check.isChecked() and self.hf_check.isChecked():
                vhflipped_image = cv2.flip(img, -1)
                self.save_img_list.append(vhflipped_image)
        else:
            if self.vf_check.isChecked():
                vflipped_image = cv2.flip(self.sample_img, 0)
                self.grid_images.append(vflipped_image)
            if self.hf_check.isChecked():
                hflipped_image = cv2.flip(self.sample_img, 1)
                self.grid_images.append(hflipped_image)
            if self.vf_check.isChecked() and self.hf_check.isChecked():
                vhflipped_image = cv2.flip(self.sample_img, -1)
                self.grid_images.append(vhflipped_image)

    def Rotaion_method(self, is_save = False, img = None):
        if self.ro_check.isChecked():
            if is_save:
                angle = int(self.angle_entry.text())
                (height, width) = img.shape[:2]
                center = (width // 2, height // 2)
                temp_list = []
                for imgssss in self.save_img_list:
                    for a in range(0 + angle, 360, angle):
                        rotation_matrix = cv2.getRotationMatrix2D(center, a, 1.0)
                        img_rotated = cv2.warpAffine(imgssss, rotation_matrix, (width, height))
                        temp_list.append(img_rotated)

                self.save_img_list.extend(temp_list)
            else:
                angle = int(self.angle_entry.text())
                (height, width) = self.sample_img.shape[:2]
                center = (width // 2, height // 2)
                temp_list = []
                for imgssss in self.grid_images:
                    for a in range(0 + angle, 360, angle):
                        rotation_matrix = cv2.getRotationMatrix2D(center, a, 1.0)
                        img_rotated = cv2.warpAffine(imgssss, rotation_matrix, (width, height))
                        temp_list.append(img_rotated)
    
                self.grid_images.extend(temp_list)

    def Blur_method(self, is_save = False, img = None):
        if self.bl_check.isChecked():
            if is_save:
                ksize = int(self.blur_entry.text())
                temp_list = []
                for imgssss in self.save_img_list:
                    blurred_image = cv2.blur(imgssss, (ksize, ksize))
                    temp_list.append(blurred_image)

                self.save_img_list.extend(temp_list)
            else:
                ksize = int(self.blur_entry.text())
                temp_list = []
                for imgssss in self.grid_images:
                    blurred_image = cv2.blur(imgssss, (ksize, ksize))
                    temp_list.append(blurred_image)

                self.grid_images.extend(temp_list)
            
    def Bright_method(self, is_save = False, img = None):
        if self.br_check.isChecked():
            if is_save:
                value = int(self.bright_entry.text())
                temp_list = []
                for imgssss in self.save_img_list:
                    if value >= 0:
                        brighter_image = cv2.add(imgssss, np.full(imgssss.shape, value, dtype=np.uint8))
                    else:
                        brighter_image = cv2.subtract(imgssss, np.full(imgssss.shape, value, dtype=np.uint8))
                    temp_list.append(brighter_image)

                self.save_img_list.extend(temp_list)
            else:
                value = int(self.bright_entry.text())
                temp_list = []
                for imgssss in self.grid_images:
                    if value >= 0:
                        brighter_image = cv2.add(imgssss, np.full(imgssss.shape, value, dtype=np.uint8))
                    else:
                        brighter_image = cv2.subtract(imgssss, np.full(imgssss.shape, value, dtype=np.uint8))
                    temp_list.append(brighter_image)

                self.grid_images.extend(temp_list)

    def Noise_method(self, is_save = False, img = None):
        if self.no_check.isChecked():
            if is_save:
                var = int(self.noise_entry.text())
                temp_list = []
                mean = 0
                sigma = var ** 0.5

                for imgssss in self.save_img_list:
                    height, width, _ = imgssss.shape
                    gaussian = np.random.normal(mean, sigma, (height, width, 3))
                    noisy_image = np.zeros(imgssss.shape, np.float32)
                    if len(imgssss.shape) == 2:
                        noisy_image = imgssss + gaussian
                    else:
                        noisy_image[:, :, 0] = imgssss[:, :, 0] + gaussian[:, :, 0]
                        noisy_image[:, :, 1] = imgssss[:, :, 1] + gaussian[:, :, 1]
                        noisy_image[:, :, 2] = imgssss[:, :, 2] + gaussian[:, :, 2]
                    cv2.normalize(noisy_image, noisy_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
                    noisy_image = noisy_image.astype(np.uint8)
                    temp_list.append(noisy_image)
                self.save_img_list.extend(temp_list)
            else:
                var = int(self.noise_entry.text())
                temp_list = []
                mean = 0
                sigma = var ** 0.5

                for imgssss in self.grid_images:
                    height, width, _ = imgssss.shape
                    gaussian = np.random.normal(mean, sigma, (height, width, 3))
                    noisy_image = np.zeros(imgssss.shape, np.float32)
                    if len(imgssss.shape) == 2:
                        noisy_image = imgssss + gaussian
                    else:
                        noisy_image[:, :, 0] = imgssss[:, :, 0] + gaussian[:, :, 0]
                        noisy_image[:, :, 1] = imgssss[:, :, 1] + gaussian[:, :, 1]
                        noisy_image[:, :, 2] = imgssss[:, :, 2] + gaussian[:, :, 2]
                    cv2.normalize(noisy_image, noisy_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
                    noisy_image = noisy_image.astype(np.uint8)
                    temp_list.append(noisy_image)
                self.grid_images.extend(temp_list)

    def RandomCrop_method(self, is_save = False, img = None):
            if self.ra_check.isChecked():
                if is_save:
                    temp_list = []

                    for imgssss in self.save_img_list:
                        height, width, _ = imgssss.shape
                        crop_size = int(min(height, width) * 0.7)
                        if crop_size < 10:
                            crop_size = 10  # 최소 크롭 크기를 10로 설정

                        # 랜덤으로 크롭 시작점 설정
                        start_x0 = np.random.randint(0, width - crop_size + 1)
                        start_y0 = np.random.randint(0, height - crop_size + 1)
                        start_x1 = start_x0 + crop_size
                        start_y1 = start_y0 + crop_size

                        cropped_image = imgssss[start_y0:start_y1, start_x0:start_x1]
                        cropped_image = cv2.resize(cropped_image, (150, 150))

                        temp_list.append(cropped_image)
                    self.save_img_list.extend(temp_list)

                else:
                    temp_list = []

                    for imgssss in self.grid_images:
                        height, width, _ = imgssss.shape
                        crop_size = int(min(height, width) * 0.7)
                        if crop_size < 10:
                            crop_size = 10  # 최소 크롭 크기를 10로 설정

                        # 랜덤으로 크롭 시작점 설정
                        start_x0 = np.random.randint(0, width - crop_size + 1)
                        start_y0 = np.random.randint(0, height - crop_size + 1)
                        start_x1 = start_x0 + crop_size
                        start_y1 = start_y0 + crop_size

                        cropped_image = imgssss[start_y0:start_y1, start_x0:start_x1]
                        cropped_image = cv2.resize(cropped_image, (150,150))

                        temp_list.append(cropped_image)
                    self.grid_images.extend(temp_list)

    def show_grid_images(self):
        self.resetGridLayout()
        self.aug_ratio = 1
        self.grid_images = []
        self.grid_images.append(self.sample_img)

        self.flip_method()
        self.Rotaion_method()
        self.Blur_method()
        self.Bright_method()
        self.Noise_method()
        self.RandomCrop_method()

        positions = [(i // 5, i % 5) for i in range(len(self.grid_images))]
        for position, image_path in zip(positions, self.grid_images):
            
            height, width, _ = image_path.shape
            bytesPerLine = 3 * width
            image_w = QImage(image_path.data, width, height, bytesPerLine, QImage.Format_RGB888)

            pixmap_b = QtGui.QPixmap.fromImage(image_w)

            image_b_resize = pixmap_b.scaled(150, 150, Qt.KeepAspectRatio)

            label = QLabel()
            label.setPixmap(image_b_resize)
            self.aug_image_grid.addWidget(label, *position)

        for i in range(len(self.grid_images), 5):
            label = QLabel()
            label.setFixedSize(150, 150)
            self.aug_image_grid.addWidget(label, 0, i)

        self.aug_ratio = len(self.grid_images)
        self.set_claug_text()

    def image_save_result(self):
        for files in self.aug_file_list:
            self.save_img_list = []
            image_origin_path = f'{self.aug_dir}/{files}'
            image_cv2 = cv2.imread(image_origin_path)
            self.image_rgb = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)
            self.image_rgb = cv2.resize(self.image_rgb, (640, 640))
            self.save_img_list.append(self.image_rgb)

            self.flip_method(is_save=True, img=self.image_rgb)
            self.Rotaion_method(is_save=True, img=self.image_rgb)
            self.Blur_method(is_save=True, img=self.image_rgb)
            self.Bright_method(is_save=True, img=self.image_rgb)
            self.Noise_method(is_save=True, img=self.image_rgb)
            self.RandomCrop_method(is_save=True, img=self.image_rgb)

            for i, simg in enumerate(self.save_img_list):
                if not os.path.isdir(f'{self.aug_dir}/augmented'):
                    os.makedirs(os.path.join(f'{self.aug_dir}/augmented'))
                save_pathss = f'{self.aug_dir}/augmented/aug_{i}_{files}'
                cv2.imwrite(save_pathss, simg)


    def resetGridLayout(self):
        # 그리드 레이아웃을 가져옴
        layout = self.aug_image_grid
        
        # 레이아웃에서 위젯을 제거하는 반복문
        while layout.count():
            item = layout.takeAt(0)  # 첫 번째 아이템을 가져옴
            if item.widget():
                widget = item.widget()
                layout.removeWidget(widget)  # 레이아웃에서 위젯 제거
                widget.deleteLater()  # 위젯 객체 삭제

    ################################################################################

    def detection_open(self):
        # 폴더 선택 대화상자 열기
        detection_dir = QFileDialog.getExistingDirectory(None, 'Select Image Folder')

        if detection_dir:
            # 폴더 내 이미지 파일 필터링
            parent_dir = os.path.dirname(detection_dir)  # 상위 디렉토리 경로
            folder_name = os.path.basename(detection_dir)  # 선택한 폴더 이름
            new_folder_name = folder_name + "_txt"  # "_txt" 추가한 새 폴더 이름
            new_folder_path = os.path.join(parent_dir, new_folder_name)  # 새 폴더 경로
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)  # 새 폴더 생성
            self.de_img_folder = folder_name
            self.de_txt_folder = new_folder_path
            de_image_files = [f for f in os.listdir(detection_dir) if f.lower().endswith(('.bmp', '.jpg', '.jpeg', '.png'))]
            self.de_list_table.setRowCount(0)
            for filename in de_image_files:
                txt_file_path = os.path.join(new_folder_path, f'{os.path.splitext(filename)[0]}.txt')
                if not os.path.isfile(txt_file_path):  ##이미 txt가 있는경우
                    with open(txt_file_path, 'w') as txt_file:
                        txt_file.write('')  # 현재는 빈 파일로 생성
                row_position = self.de_list_table.rowCount()
                self.de_list_table.insertRow(row_position)
                # "Filename" 열에 파일 이름 추가
                self.de_list_table.setItem(row_position, 0, QTableWidgetItem(filename))    
            
            if self.de_list_table.rowCount() != 0: # 첫번째 이미지 출력
                self.de_list_table.setCurrentCell(0,0)
                self.de_file_list_click()

    def mousePressEvent(self, event): # 마우스 좌클릭시 좌표
        if event.buttons() and Qt.LeftButton and self.de_image_lbl.isVisible() and self.de_list_table.rowCount()>0:
            self.past_pos = event.globalPos()-QPoint(10,31)  #보정
            self.image_pos = self.mapToGlobal(self.de_image_lbl.pos())
            image_pos = self.mapToGlobal(self.de_image_lbl.pos())
            if self.past_pos.x()>= image_pos.x() and self.past_pos.y()>= image_pos.y() :
                self.drawing = True
                if self.de_Polygon.isChecked():  
                    self.setMouseTracking(True) 
                    self.first_tab.setMouseTracking(True)
                    self.detection_tab.setMouseTracking(True)
                    self.de_image_lbl.setMouseTracking(True)  
                    self.poly_pos.append(event.globalPos()-QPoint(10,31))
                    self.temp_image = self.current_image.copy()  # 원본 이미지를 복사하z여 임시 이미지로 사용
                    self.draw_Poly(self.temp_image)
                    self.update_image_display(self.temp_image)  
                    self.past_pos = event.globalPos()-QPoint(10,31)  #보정              

    def mouseReleaseEvent(self,event):  # 마우스 좌눌렀다 뗄때 좌표
        if self.de_image_lbl.isVisible() and self.de_Polygon.isChecked() == False and self.de_list_table.rowCount()>0:
            self.end_pos = event.globalPos()- QPoint(10,31)  #보정
            self.present_pos = event.globalPos()- QPoint(10,31)  #보정

            # 마우스 클릭, 릴리즈 위치가 이미지 안인지 확인    
            if self.past_pos.x()>= self.image_pos.x() and self.past_pos.y()>= self.image_pos.y() and self.end_pos.x() <= (self.image_pos.x()+self.de_image_lbl.width()) \
                and self.end_pos.y() <= (self.image_pos.y()+self.de_image_lbl.height()) and self.de_image_lbl.isVisible() :

                self.de_class_choice_table.insertRow(self.de_class_choice_table.rowCount())
                # 마우스 클릭, 릴리즈 상대위치 받아오기
                start_pos_x = (self.past_pos.x()-self.image_pos.x())/self.de_image_lbl.width()
                start_pos_y = (self.past_pos.y()-self.image_pos.y())/self.de_image_lbl.height()
                end_pos_x = (self.end_pos.x()-self.image_pos.x())/self.de_image_lbl.width()
                end_pos_y = (self.end_pos.y()-self.image_pos.y())/self.de_image_lbl.height()
                #소숫점 두자리까지 반올림 후 상대위치 저장
                if self.de_rec.isChecked():
                    self.de_class_choice_table.setItem(self.de_class_choice_table.rowCount()-1, 0, QTableWidgetItem(str(0))) #rect 0 
                elif self.de_circle.isChecked():
                    self.de_class_choice_table.setItem(self.de_class_choice_table.rowCount()-1, 0, QTableWidgetItem(str(1))) #circle 1
                self.de_class_choice_table.setItem(self.de_class_choice_table.rowCount()-1, 1, QTableWidgetItem(f"{self.de_class_choice.value()}"))                     
                self.de_class_choice_table.setItem(self.de_class_choice_table.rowCount()-1, 2, QTableWidgetItem(str(round(start_pos_x,2))))
                self.de_class_choice_table.setItem(self.de_class_choice_table.rowCount()-1, 3, QTableWidgetItem(str(round(start_pos_y,2))))
                self.de_class_choice_table.setItem(self.de_class_choice_table.rowCount()-1, 4, QTableWidgetItem(str(round(end_pos_x,2))))
                self.de_class_choice_table.setItem(self.de_class_choice_table.rowCount()-1, 5, QTableWidgetItem(str(round(end_pos_y,2))))
                #파일로 저장
                self.de_class_file_save()
                self.de_show_image() # 새로 클릭한 좌표 그려주기

    def mouseMoveEvent(self, event):
        if self.drawing and self.past_pos is not None and self.de_Polygon.isChecked() == False:
            self.end_pos = event.globalPos() - QPoint(10,31)  #
            mouse_pt = "Mouse Point : x={0},y={1}".format(self.end_pos.x(), self.end_pos.y())
            self.status_bar.showMessage(mouse_pt)
            start_pos_x = (self.past_pos.x()-self.image_pos.x())/self.de_image_lbl.width()
            start_pos_y = (self.past_pos.y()-self.image_pos.y())/self.de_image_lbl.height()
            end_pos_x = (self.end_pos.x()-self.image_pos.x())/self.de_image_lbl.width()
            end_pos_y = (self.end_pos.y()-self.image_pos.y())/self.de_image_lbl.height()            
            self.temp_image = self.current_image.copy()  # 원본 이미지를 복사하여 임시 이미지로 사용
            self.draw_shape(self.temp_image,start_pos_x,start_pos_y,end_pos_x,end_pos_y)
            self.update_image_display(self.temp_image)    

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete and self.drawing and self.de_Polygon.isChecked() :
            if(self.poly_pos):
                self.poly_pos.pop()
            self.temp_image = self.current_image.copy() 
            self.draw_Poly(self.temp_image)
            self.update_image_display(self.temp_image)  
        if event.key() == Qt.Key_Return and self.drawing and self.de_Polygon.isChecked() :
            self.de_class_choice_table.insertRow(self.de_class_choice_table.rowCount())
            self.de_class_choice_table.setItem(self.de_class_choice_table.rowCount()-1, 0, QTableWidgetItem(str(2))) #polygon 2
            self.de_class_choice_table.setItem(self.de_class_choice_table.rowCount()-1, 1, QTableWidgetItem(f"{self.de_class_choice.value()}"))   
            self.de_class_choice_table.setItem(self.de_class_choice_table.rowCount()-1, 2, QTableWidgetItem(str(len(self.poly_pos)))) # 몇각형 인지 저장
            pos_str = ''
            for pos in self.poly_pos :
                pos_str += str(round((pos.x()-self.image_pos.x())/self.de_image_lbl.width(),2))
                pos_str +=',' 
                pos_str += str(round((pos.y()-self.image_pos.y())/self.de_image_lbl.height(),2))
                pos_str +=','
            self.de_class_choice_table.setItem(self.de_class_choice_table.rowCount()-1, 3, QTableWidgetItem(pos_str))
            self.de_class_file_save()
            self.de_show_image() # 새로 클릭한 좌표 그려주기
            self.poly_pos.clear()


    def update_image_display(self, image):
        if image is not None:
            h, w, ch = image.shape
            qt_image = QImage(image.data, w, h, w * ch, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qt_image)
            self.de_image_lbl.setPixmap(
                pixmap.scaled(self.de_image_lbl.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def draw_shape(self, image, start_x, start_y, end_x, end_y):
        if image is not None and self.past_pos and self.end_pos:
            if self.de_rec.isChecked() : #method == 'rec' :
                height, width = image.shape[:2]  
                px1 = int(start_x * width)
                py1 = int(start_y * height)
                px2 = int(end_x * width)
                py2 = int(end_y * height)      
                cv2.rectangle(image, (px1,py1),(px2,py2),(0, 0, 255), 2)   
            elif self.de_circle.isChecked() :       
                height, width = image.shape[:2]  
                px1 = int(start_x * width)
                py1 = int(start_y * height)
                px2 = int(end_x * width)
                py2 = int(end_y * height)      
                cv2.circle(image, (int((px1+px2)/2),int((py1+py2)/2)), int((np.sqrt((px1-px2)*(px1-px2)+(py1-py2)*(py1-py2)))/2),(0, 0, 255),2)    
            # else:
            #     height, width = image.shape[:2]  
            #     px1 = int(start_x * width)
            #     py1 = int(start_y * height)
            #     px2 = int(end_x * width)
            #     py2 = int(end_y * height)      
            #     cv2.line(image, (px1,py1),(px2,py2),(0, 0, 255), 2)   

    def draw_Poly(self, image):
        height, width = image.shape[:2]  
        if len(self.poly_pos) > 1:
            for i in range(len(self.poly_pos)-1) :
                px1 = int((self.poly_pos[i].x()-self.image_pos.x())/self.de_image_lbl.width()*width)
                py1 = int((self.poly_pos[i].y()-self.image_pos.y())/self.de_image_lbl.height()*height)
                px2 = int((self.poly_pos[i+1].x()-self.image_pos.x())/self.de_image_lbl.width()*width)
                py2 = int((self.poly_pos[i+1].y()-self.image_pos.y())/self.de_image_lbl.height()*height)     
                cv2.line(image, (px1,py1),(px2,py2),(255, 120, 120), 2)  
                if i == len(self.poly_pos)-2 :
                    px1 = int((self.poly_pos[0].x()-self.image_pos.x())/self.de_image_lbl.width()*width)
                    py1 = int((self.poly_pos[0].y()-self.image_pos.y())/self.de_image_lbl.height()*height)
                    cv2.line(image, (px1,py1),(px2,py2),(0, 255, 0), 1)  

    def de_class_file_save(self) :
        row = self.de_list_table.currentRow()
        image_name = self.de_list_table.item(row, 0)
        txt_name = ".".join(image_name.text().split(".")[:-1]) + '.txt'
        with open(os.path.join(self.de_txt_folder, txt_name), 'w') as txt_file:
            for row_index in range(self.de_class_choice_table.rowCount()):
                line = ''
                for col_index in range(self.de_class_choice_table.columnCount()):
                    item = self.de_class_choice_table.item(row_index, col_index)
                    if item: 
                       line += item.text() 
                    if col_index < self.de_class_choice_table.columnCount()-1:
                        line += ' '
                    else :
                        line +='\n'
                txt_file.write(line)    

    ##################################
    def de_file_list_click(self):
        self.de_class_choice_table.clearSelection()
        self.de_class_choice_table.selectionModel().clearCurrentIndex()
        row = self.de_list_table.currentRow()
        image_name = self.de_list_table.item(row, 0)
        txt_name = ".".join(image_name.text().split(".")[:-1]) + '.txt'

        with open(os.path.join(self.de_txt_folder, txt_name), 'r') as txt_file:
            data = txt_file.readlines()
            self.de_class_choice_table.setRowCount(len(data))
            if data:
                self.de_class_choice_table.setColumnCount(len(data[0].strip().split()))

            for row_index, line in enumerate(data):
                # 줄바꿈 문자 제거 및 공백으로 분리
                values = line.strip().split()
                for column_index, value in enumerate(values):
                    # QTableWidgetItem 객체 생성
                    item = QTableWidgetItem(value)
                    # 테이블에 아이템 설정
                    self.de_class_choice_table.setItem(row_index, column_index, item)

        self.de_show_image() 

    def de_show_image(self):
        self.drawing = False
        row = self.de_list_table.currentRow()
        
        try:
            image_name = self.de_list_table.item(row, 0).text()
        except:
            return 0
        
        image_origin_path = f'{self.de_img_folder}/{image_name}'
        image_cv2 = cv2.imread(image_origin_path)
        self.image_rgb = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)
        self.current_image = self.image_rgb.copy()  # 현재 이미지를 저장
        rows = self.de_class_choice_table.rowCount()
        cols = self.de_class_choice_table.columnCount()
            
        #테이블에서 정보 읽어오는 코드임
        table_data = []
        for row in range(rows):
            row_data = []
            for col in range(cols):
                item = self.de_class_choice_table.item(row, col)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append(0.0)  # 빈 셀의 경우 빈 문자열로 처리
            table_data.append(row_data)

        #정보대로 그리는 함수
        processed_image = self.draw_area(self.image_rgb, table_data)
        height, width, _ = processed_image.shape
        bytesPerLine = 3 * width 
        image_w = QImage(processed_image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap_b = QtGui.QPixmap.fromImage(image_w)
        image_b_resize = pixmap_b.scaled(700, 700, Qt.KeepAspectRatio)
        self.de_image_lbl.setPixmap(image_b_resize)
        self.repair_key_event

    def draw_area(self, image,coord_list, method = 'rec'):        
        row = self.de_class_choice_table.currentRow()
        height, width = image.shape[:2]            
        for idx, coord in enumerate(coord_list):
            type, color, x1, y1, x2, y2 = coord
            if int(type) == 0  : # rec
                # 좌표를 픽셀 값으로 변환
                px1 = int(float(x1) * width)
                py1 = int(float(y1) * height)
                px2 = int(float(x2) * width)
                py2 = int(float(y2) * height)          
                if idx != row :
                    cv2.rectangle(image, (px1, py1), (px2, py2), self.line_color_list[int(color)], 2)
                else :
                    cv2.rectangle(image, (px1, py1), (px2, py2), (255,120,120), 5)
            elif int(type) == 1 : # circle
                # 좌표를 픽셀 값으로 변환
                px1 = int(float(x1) * width)
                py1 = int(float(y1) * height)
                px2 = int(float(x2) * width)
                py2 = int(float(y2) * height)    
                if idx != row :
                    cv2.circle(image, (int((px1+px2)/2),int((py1+py2)/2)), int((np.sqrt((px1-px2)*(px1-px2)+(py1-py2)*(py1-py2)))/2), self.line_color_list[int(color)],2)
                else :
                    cv2.circle(image, (int((px1+px2)/2),int((py1+py2)/2)), int((np.sqrt((px1-px2)*(px1-px2)+(py1-py2)*(py1-py2)))/2), (255,120,120),5)
            else: #polygon
                point = y1.split(',')
                for i in range (int(x1)-1):
                    px1 = int(float(point[2*i]) * width)
                    py1 = int(float(point[2*i+1]) * height)
                    px2 = int(float(point[2*i+2]) * width)
                    py2 = int(float(point[2*i+3]) * height)
                    if idx != row :
                        cv2.line(image, (px1,py1),(px2,py2),self.line_color_list[int(color)], 2) 
                    else :
                        cv2.line(image, (px1,py1),(px2,py2), (255,120,120),5) 
                px1 = int(float(point[0]) * width)
                py1 = int(float(point[1]) * height)
                px2 = int(float(point[2*(int(x1)-1)]) * width)
                py2 = int(float(point[2*(int(x1)-1)+1]) * height)
                if idx != row :
                    cv2.line(image, (px1,py1),(px2,py2),self.line_color_list[int(color)], 2) 
                else:
                    cv2.line(image, (px1,py1),(px2,py2), (255,120,120),5)

        return image  # 수정된 이미지 반환
    
    def de_delete_row(self):
        row = self.de_class_choice_table.currentRow()
        if row >=0 and row < self.de_class_choice_table.rowCount() :
            self.de_class_choice_table.removeRow(row)
            self.de_class_file_save()
            self.de_show_image() 
    
    def de_Image_Save(self) :  
        # self.de_class_choice_table.clearSelection()
        # self.de_class_choice_table.selectionModel().clearCurrentIndex()
        # for class_idx in range (10) :#class 갯수, label된 이미지 저장용 폴더
        #     new_folder_path = f'./image_class_{class_idx}/'
        #     if not os.path.exists(new_folder_path):
        #         os.makedirs(new_folder_path)  
        #     else :
        #         for file in os.scandir(new_folder_path) :
        #             os.remove(file.path) 
        # for img_idx in range (self.de_list_table.rowCount()):
        #     image_name = self.de_list_table.item(img_idx, 0).text()
        #     image_origin_path = f'{self.de_img_folder}/{image_name}'
        #     #label 정보 읽어오기
        #     txt_name = ".".join(image_name.split(".")[:-1]) + '.txt'
        #     with open(os.path.join(self.de_txt_folder, txt_name), 'r') as txt_file:
        #         data = txt_file.readlines()
        #         for class_idx in range (10) :
        #             table_data = []
        #             image_cv2 = cv2.imread(image_origin_path)
        #             self.image_rgb = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)
        #             new_folder_path = f'./image_class_{class_idx}/'
        #             for values in data :
        #                 value = values.strip().split()
        #                 if int(value[0]) == class_idx :
        #                     table_data.append(list(map(float, value)))   

        #             #정보대로 그리는 함수
        #             if table_data != [] :
        #                 processed_image = self.draw_area(self.image_rgb, table_data)
        #                 height, width, _ = processed_image.shape
        #                 bytesPerLine = 3 * width 
        #                 image_w = QImage(processed_image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        #                 pixmap_b = QtGui.QPixmap.fromImage(image_w)
        #                 image_b_resize = pixmap_b.scaled(700, 700, Qt.KeepAspectRatio)
        #                 self.de_image_lbl.setPixmap(image_b_resize)
        #                 image_file_path = f'{new_folder_path}{image_name}_class_{class_idx}.png'
        #                 image_b_resize.save(image_file_path)
        #self.de_show_image()  
        QMessageBox.information(self, 'Class', '저장완료')       
        self.repair_key_event      

#################################################################################
    def on_angle_text_changed(self, text):
        # 텍스트 입력이 유효한지 확인하고 슬라이더 값을 업데이트
        if text.isdigit():
            value = int(text)
            if 0 <= value <= 360:
                self.angle_slider.setValue(value)

    def on_angle_slider_changed(self, value):
        # 슬라이더 값이 변경되면 QLineEdit을 업데이트
        self.angle_entry.setText(str(value))

    def on_blur_text_changed(self, text):
        # 텍스트 입력이 유효한지 확인하고 슬라이더 값을 업데이트
        if text.isdigit():
            value = int(text)
            if 3 <= value <= 11:
                self.blur_slider.setValue(value)

    def on_blur_slider_changed(self, value):
        # 슬라이더 값이 변경되면 QLineEdit을 업데이트
        self.blur_entry.setText(str(value))

    def on_bright_text_changed(self, text):
        # 텍스트 입력이 유효한지 확인하고 슬라이더 값을 업데이트
        if text.isdigit():
            value = int(text)
            if -255 <= value <= 255:
                self.bright_slider.setValue(value)

    def on_bright_slider_changed(self, value):
        # 슬라이더 값이 변경되면 QLineEdit을 업데이트
        self.bright_entry.setText(str(value))

    def on_noise_text_changed(self, text):
        # 텍스트 입력이 유효한지 확인하고 슬라이더 값을 업데이트
        if text.isdigit():
            value = int(text)
            if  0 <= value <= 100:
                self.noise_slider.setValue(value)

    def on_noise_slider_changed(self, value):
        # 슬라이더 값이 변경되면 QLineEdit을 업데이트
        self.noise_entry.setText(str(value))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())