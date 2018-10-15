#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
from PIL import Image, ImageDraw  # Подключим необходимые библиотеки.
from PIL.ImageQt import ImageQt

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
                             QLabel, QApplication)
from PyQt5.QtGui import QPixmap, QImage, qRgb


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        imageFile = "dark_elf.jpg"

        image = Image.open(imageFile)

        print(image.size)
        cx, cy = image.size[0]/2, image.size[1]/2
        d = 50

        #image = image.crop((cx-d, cy-d, cx+d, cy+d))

        image = image.crop((50, 50, 150, 150))  # 50, 50 - x,y start coordinate; 150, 150 - final size

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
