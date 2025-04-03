from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QWidget
import cv2
from PyQt5.QtGui import QImage, QPixmap
import matplotlib.pyplot as plt
import numpy as np
import os
import ui.ui_equhist


def clahist(image):
    histogram = np.zeros(256)
    height, width, = image.shape
    for i in range(0, height):
        for j in range(0, width):
            histogram[image[i, j]] += 1
    return histogram


#直方图均衡自制函数
def equhist(orgin_image):
    change_image = orgin_image
    histogram = clahist(change_image)
    height, width, = change_image.shape
    pixel_count = height * width
    histogram = histogram / pixel_count
    f_his = np.empty_like(histogram)

    for i, count in enumerate(histogram):
        f_his[i] = np.sum(histogram[:i + 1])
    f_his = f_his * 255
    f_hiss = np.round(f_his)
    for i in range(0, height):
        for j in range(0, width):
            change_image[i, j] = f_hiss[change_image[i, j]]
    return change_image

#计算直方图
def calahist(image):

    b_channel, r_channel, g_channel = cv2.split(image)
    hist_red = clahist(r_channel)
    hist_green = clahist(g_channel)
    hist_blue = clahist(b_channel)

    # 创建一个Figure对象和一个子图
    fig, ax = plt.subplots(figsize=(8, 6))

    # 绘制红色通道的直方图
    ax.plot(hist_red, color='red', label='Red Channel')

    # 绘制绿色通道的直方图
    ax.plot(hist_green, color='green', label='Green Channel')

    # 绘制蓝色通道的直方图
    ax.plot(hist_blue, color='blue', label='Blue Channel')

    # 设置图例
    ax.legend()

    # 将Matplotlib的Figure对象转换为QImage
    canvas = plt.get_current_fig_manager().canvas
    canvas.draw()
    pil_image = canvas.tostring_rgb()
    width, height = canvas.get_width_height()
    qimage = QImage(pil_image, width, height, QImage.Format_RGB888)
    pixmap = QPixmap.fromImage(qimage)

    return pixmap

class equhistAct(QWidget,ui.ui_equhist.Ui_Form):
    def __init__(self):
        super(equhistAct,self).__init__()
        self.setupUi(self)


        self.pushButton.clicked.connect(self.openimg)
        self.pushButton_2.clicked.connect(self.motion)
        self.pushButton_3.clicked.connect(self.saveHSV)
        self.pushButton_4.clicked.connect(self.saveRGB)


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
            self.label_origin_hist.clear()
            self.label_HSV.clear()
            self.label_HSV_hist.clear()
            self.label_RGB.clear()
            self.label_RGB_hist.clear()

    def motion(self):

        image = cv2.imread(self.image_path)


        #初始图像直方图
        origin_hist = calahist(image)
        origin_hist = QtGui.QPixmap(origin_hist).scaled(self.label_origin.width(), self.label_origin.height())
        self.label_origin_hist.setPixmap(origin_hist)


        #进行hsv_v直方图均衡并输出

        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h_channel, s_channel, v_channel = cv2.split(hsv_image)
        v_channel = equhist(v_channel)
        equalized_hsv_image = cv2.merge([h_channel, s_channel, v_channel])
        equalized_hsv_image = cv2.cvtColor(equalized_hsv_image, cv2.COLOR_HSV2BGR)
        rgb_image = cv2.cvtColor(equalized_hsv_image, cv2.COLOR_BGR2RGB)
        height, width, channels = rgb_image.shape
        qimage = QImage(rgb_image.data, width, height, width * channels, QImage.Format_RGB888)
        self.image_hsv = qimage
        qimage = QtGui.QPixmap(qimage).scaled(self.label_HSV.width(), self.label_HSV.height())
        self.label_HSV.setPixmap(qimage)

        hsv_hist = calahist(equalized_hsv_image)
        hsv_hist = QtGui.QPixmap(hsv_hist).scaled(self.label_HSV_hist.width(), self.label_HSV_hist.height())
        self.label_HSV_hist.setPixmap(hsv_hist)

        #进行rgb直方图均衡
        b_channel, r_channel, g_channel = cv2.split(image)
        r_channel = equhist(r_channel)
        g_channel = equhist(g_channel)
        b_channel = equhist(b_channel)
        equalized_brg_image = cv2.merge([b_channel, g_channel, r_channel])
        equalized_rgb_image = cv2.cvtColor(equalized_brg_image, cv2.COLOR_BGR2RGB)
        height, width, channels = equalized_rgb_image.shape
        qimage = QImage(equalized_rgb_image.data, width, height, width * channels, QImage.Format_RGB888)
        self.image_RGB = qimage
        qimage = QtGui.QPixmap(qimage).scaled(self.label_RGB.width(), self.label_RGB.height())
        self.label_RGB.setPixmap(qimage)

        rbg_hist = calahist(equalized_brg_image)
        rbg_hist = QtGui.QPixmap(rbg_hist).scaled(self.label_RGB_hist.width(), self.label_RGB_hist.height())
        self.label_RGB_hist.setPixmap(rbg_hist)

    def saveHSV(self):
        if self.image_hsv:
            save_path, _ = QFileDialog.getSaveFileName(self, '保存图片文件', '', 'Images (*.png *.xpm *.jpg *.bmp)')
            self.image_hsv.save(save_path)

    def saveRGB(self):
        if self.image_RGB:
            save_path, _ = QFileDialog.getSaveFileName(self, '保存图片文件', '', 'Images (*.png *.xpm *.jpg *.bmp)')
            self.image_RGB.save(save_path)