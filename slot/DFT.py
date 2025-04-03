from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton, QDialog, QLabel
from PyQt5.QtGui import QImage, QPixmap
import matplotlib.pyplot as plt
import numpy as np
import math
from PIL import Image
import os
import ui.ui_DFT
import cv2

"离散傅氏正变换"
def ft(image):

    matrix = np.array(image, dtype=float)
    width, height = matrix.shape
    for x in range(0, width):
        for y in range(0, height):
            if (x+y) % 2 == 0:
                matrix[x, y] *= -1

    matrix_size = (width, width)
    a1 = np.empty(matrix_size, dtype=np.complex128)
    for u in range(0, width):
        for x in range(0, width):
            temp = -2 * math.pi * u * x / width
            t = complex(math.cos(temp), math.sin(temp))
            a1[u, x] = t

    matrix_size = (height, height)
    a2 = np.empty(matrix_size, dtype=np.complex128)
    for v in range(0, height):
        for y in range(0, height):
            temp = -2 * math.pi * v * y / height
            t = complex(math.cos(temp), math.sin(temp))
            a2[v, y] = t

    temp_matrix = np.dot(a1, matrix)
    result_matrix = np.dot(temp_matrix, a2)
    return result_matrix

"离散傅氏逆变换"
def ift(matrix):
    width, height = matrix.shape
    matrix_size = (width, width)
    a1 = np.empty(matrix_size, dtype=np.complex128)
    for u in range(0, width):
        for x in range(0, width):
            temp = 2 * math.pi * u * x / width
            t = complex(math.cos(temp), math.sin(temp))
            a1[u, x] = t
    matrix_size = (height, height)
    a2 = np.empty(matrix_size, dtype=np.complex128)
    for v in range(0, height):
        for y in range(0, height):
            temp = 2 * math.pi * v * y / height
            t = complex(math.cos(temp), math.sin(temp))
            a2[v, y] = t

    temp_matrix = np.dot(a1, matrix)
    result_matrix = np.dot(temp_matrix, a2)
    result_matrix = result_matrix/(width*height)
    for x in range(0, width):
        for y in range(0, height):
            if (x+y) % 2 == 0:
                result_matrix[x, y] *= -1
    result_matrix = np.abs(result_matrix)
    return result_matrix

"低通滤波器"
def fil(matrix, threshold):
    tempm = matrix
    width, height = tempm.shape
    center_x = width//2
    center_y = height//2
    t = threshold * width * height
    for x in range(width):
        for y in range(height):
            temp = (x-center_x)**2 + (y-center_y)**2
            if temp >= t:
                tempm[x, y] = 0
    return tempm



"离散傅氏变换可视"
def showft(matrix):

    plt.imshow(np.round(20 * np.log10(np.abs(matrix)+1)), cmap='gray')
    plt.axis('off')  # 去坐标轴
    plt.xticks([])  # 去刻度


    temp_file = 'temp.png'
    plt.savefig(temp_file, bbox_inches='tight', pad_inches=-0.1)  # 注意两个参数
    plt.close()


class ErrorDialogthreshold(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Error")
        self.setModal(True)

        self.label = QLabel("请输入阈值!", self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        self.setLayout(layout)

class DFTAct(QWidget,ui.ui_DFT.Ui_Form):
    def __init__(self):
        super(DFTAct,self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.openimg)
        self.pushButton_2.clicked.connect(self.motion)
        self.pushButton_3.clicked.connect(self.saveImage)
        self.pushButton_4.clicked.connect(self.saveFil)



    def openimg(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
        file_dialog.setViewMode(QFileDialog.Detail)
        file_path, _ = file_dialog.getOpenFileName(self, '选择图片文件', '', 'Images (*.png *.xpm *.jpg *.bmp)')

        # 如果选择了文件，则更新图像文件路径，并加载图片到标签
        if file_path:
            self.image_path = file_path
            img = QtGui.QPixmap(self.image_path).scaled(self.label_origin.width(), self.label_origin.height())
            self.label_origin.setPixmap(img)
            self.label_grey.clear()
            self.label_grey_cos.clear()
            self.label_filter.clear()
            self.label_filter_cos.clear()
            self.lineEdit_SNR.clear()
            self.lineEdit_CR.clear()
            self.lineEdit_threshold.clear()

    def motion(self):
        # 导入图片
        text = self.lineEdit_threshold.text()
        if not text:
            # 如果文本为空，弹出错误消息对话框
            error_dialog = ErrorDialogthreshold(self)
            if error_dialog.exec_() == QDialog.Rejected:
                # 如果用户点击了错误消息对话框的取消按钮，不继续执行后续程序
                return

        image = cv2.imread(self.image_path)
        # 转换为灰度图
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # 将灰度图转换为Qt格式的图像
        image = Image.open(self.image_path).convert('L')
        matrix = np.array(image, dtype=float)
        img = Image.fromarray(matrix).convert('L')
        qt_image = QImage(img.tobytes(), img.width, img.height, QImage.Format_Grayscale8)
        pixmap = QPixmap.fromImage(qt_image)
        pixmap = QtGui.QPixmap(pixmap).scaled(self.label_filter.width(), self.label_filter.height())
        self.label_grey.setPixmap(pixmap)

        image = Image.open(self.image_path).convert('L')
        "进行FT变换"
        ft_img = ft(image)
        showft(ft_img)
        temp_file = 'temp.png'
        pixmap = QPixmap(temp_file)
        pixmap = QtGui.QPixmap(pixmap).scaled(self.label_grey_cos.width(), self.label_grey_cos.height())
        self.label_grey_cos.setPixmap(pixmap)
        if (os.path.isfile("temp.png")):
            os.remove("temp.png")

        "进行低通滤波"
        threshold = float(self.lineEdit_threshold.text())
        ft_fil_img = fil(ft_img, threshold)
        showft(ft_fil_img)
        temp_file = 'temp.png'
        pixmap = QPixmap(temp_file)
        self.image_path_fil = pixmap
        pixmap = QtGui.QPixmap(pixmap).scaled(self.label_filter_cos.width(), self.label_filter_cos.height())
        self.label_filter_cos.setPixmap(pixmap)
        if (os.path.isfile("temp.png")):
            os.remove("temp.png")


        filter_img = ift(ft_fil_img)

        image = Image.fromarray(filter_img).convert('L')
        qt_image = QImage(image.tobytes(), image.width, image.height, QImage.Format_Grayscale8)
        pixmap = QPixmap.fromImage(qt_image)
        self.image_path_idct = pixmap
        pixmap = QtGui.QPixmap(pixmap).scaled(self.label_filter.width(), self.label_filter.height())
        self.label_filter.setPixmap(pixmap)


        "计算峰值信噪比PSNR评价图像压缩质量"

        mse = np.mean((gray_image - filter_img) ** 2)
        psnr = 20 * np.log10(255 / math.sqrt(mse))
        psnr = format(psnr, ".4f")
        self.lineEdit_SNR.setText(psnr)


        "计算压缩比cr"
        origin_img = self.label_grey.pixmap().toImage()
        origin_img.save("temp.png")
        origin_size = os.path.getsize('temp.png')
        if (os.path.isfile("temp.png")):
            os.remove("temp.png")
        filter_img = self.label_filter.pixmap().toImage()
        filter_img.save("temp.png")
        filter_size = os.path.getsize('temp.png')
        if (os.path.isfile("temp.png")):
            os.remove("temp.png")

        cr = (filter_size / origin_size) * 100
        cr = format(cr, ".4f")
        self.lineEdit_CR.setText(cr)

    def saveImage(self):
        if self.image_path_idct:
            save_path, _ = QFileDialog.getSaveFileName(self, '保存图片文件', '', 'Images (*.png *.xpm *.jpg *.bmp)')
            self.image_path_idct.save(save_path)


    def saveFil(self):
        if self.image_path_fil:
            save_path, _ = QFileDialog.getSaveFileName(self, '保存图片文件', '', 'Images (*.png *.xpm *.jpg *.bmp)')
            self.image_path_fil.save(save_path)