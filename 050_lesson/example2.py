import sys

from PyQt5.QtWidgets import QListWidget, QApplication


class myListWidget(QListWidget):

    def Clicked(self, item):
        QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())


def main():
    app = QApplication(sys.argv)
    listWidget = myListWidget()

    # Resize width and height
    listWidget.resize(300, 120)

    listWidget.addItem("Item 1");
    listWidget.addItem("Item 2");
    listWidget.addItem("Item 3");
    listWidget.addItem("Item 4");

    listWidget.setWindowTitle('PyQT QListwidget Demo')
    listWidget.itemClicked.connect(listWidget.Clicked)

    listWidget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()





######
# self.listWidget_extractedmeters.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
# self.listWidget_extractedmeters.connect(self.listWidget_extractedmeters, QtCore.SIGNAL("customContextMenuRequested(QPoint)" ), self.listItemRightClicked)
#
#
# def listItemRightClicked(self, QPos):
#     self.listMenu= QtGui.QMenu()
#     menu_item = self.listMenu.addAction("Remove Item")
#     self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.menuItemClicked)
#     parentPosition = self.listWidget_extractedmeters.mapToGlobal(QtCore.QPoint(0, 0))
#     self.listMenu.move(parentPosition + QPos)
#     self.listMenu.show()
#
#
# def menuItemClicked(self):
#     currentItemName=str(self.listWidget_extractedmeters.currentItem().text() )
#     print(currentItemName)
######