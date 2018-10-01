#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки.
from PIL.ImageQt import ImageQt

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap, QImage, qRgb


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        imageFile = "big.jpg"
        # imageFile = "small.png"

        image = Image.open(imageFile)

        # выравнивание по ширине (image.size[0])
        width = 800
        # высоту нужно определить (image.size[1])
        height = int(width * image.size[1] / image.size[0])

        # указываем конечные размеры (без сохранения соотношения)
        # width = 800
        # height = 800

        image = image.resize((width, height), Image.ANTIALIAS)

        draw = ImageDraw.Draw(image)

        img_tmp = ImageQt(image.convert('RGBA'))

        hbox = QHBoxLayout(self)
        pixmap = QPixmap.fromImage(img_tmp)

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Example')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())