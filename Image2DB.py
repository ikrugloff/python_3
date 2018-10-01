#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки.
from PIL.ImageQt import ImageQt

import sqlite3 as lite
import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap, QImage, qRgb


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        con = lite.connect('image.db')
        cur = con.cursor()

        file = open("big.jpg", "rb")

        img = file.read()

        print(img)

        file.close()

        binary = lite.Binary(img)

        cur.execute("INSERT INTO Images(Data) VALUES (?)", (binary,))

        con.commit()
        con.close()



        self.move(300, 200)
        self.setWindowTitle('Example')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())