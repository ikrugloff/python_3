# Использование функции loadUi()
from PyQt5 import QtWidgets, uic
import sys
import time
from PyQt5.QtWidgets import QListWidget

import purchase_list
from PyQt5.uic.properties import QtCore

app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi('20181015_main_gui.ui')

# print(window.pushButton_launch)  # вывод в консоль инфы об объекте
# (<PyQt5.QtWidgets.QPushButton object at 0x7ff65bb42ca8>)

#########
# testing display of External items
# window.listWidget_satisfaction.addItem('listWidget_satisfaction_External_item1')
# window.listWidget_satisfaction.addItem('listWidget_satisfaction_External_item2')
#########

#########
# testing display of the content of the list
# ITEMS = ['First list element',
#          'Second list element',
#          'Third list element',
#          'Fourth list element',
#          'Fifth list element'
#          ]
# for item in ITEMS:
#     window.listWidget_satisfaction.addItem(item)
#########

#########
# testing display of the content of the range
# for i in range(6):
#     item = QtWidgets.QListWidgetItem(f'Item_{i}')
#     window.listWidget_satisfaction.addItem(item)
#########

#########
# def hello():  # обработчик события (что будет происходить при нажатии на кнопку)
#     window.listWidget_satisfaction.addItem('hello_internal_item1')
#     window.listWidget_satisfaction.addItem('hello_internal_item2')
# берём основное окно(window), кнопку на нём(objectName), событие(clicked(нажатие мыши)), вызов соответствующего
# обработчика события connect(hello)
# window.pushButton_launch.clicked.connect(hello)
#########

# show GUI window
window.show()
# window.listWidget_satisfaction.show()

window.comboBox_sex.addItem('Female')  # TODO: How do it in designer??? Right mouse button???
window.comboBox_sex.addItem('Male')

######
self.listWidget_extractedmeters.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
self.listWidget_extractedmeters.connect(self.listWidget_extractedmeters, QtCore.SIGNAL("customContextMenuRequested(QPoint)" ), self.listItemRightClicked)


def listItemRightClicked(self, QPos):
    self.listMenu= QtGui.QMenu()
    menu_item = self.listMenu.addAction("Remove Item")
    self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.menuItemClicked)
    parentPosition = self.listWidget_extractedmeters.mapToGlobal(QtCore.QPoint(0, 0))
    self.listMenu.move(parentPosition + QPos)
    self.listMenu.show()


def menuItemClicked(self):
    currentItemName=str(self.listWidget_extractedmeters.currentItem().text() )
    print(currentItemName)
######

#########
#  Why does session start before clicking the button??????
def interest_search():

    session = vk.AuthSession(app_id=MyVkData.APP_ID, user_login=MyVkData.LOGIN,
                             user_password=MyVkData.GET_PASSWORD())
    vkapi = vk.API(session, timeout=100)

    ######
    # INTERESTS = ['путешествия', 'фильмы']
    INTERESTS = window.lineEdit_for_1_interest.text()
    ######

    AGE_FROM = window.lineEdit_min_age.text()
    AGE_TO = window.lineEdit_max_age.text()

    ######
    sex = str(window.comboBox_sex.currentText())
    if sex == 'Female':
        SEX = 1
    else:
        SEX = 2
    ######

    CITY = 1  # Moscow

    def timeout(query):
        time.sleep(0.3)
        return query

    # Why does we need comma in "interests" when we use list as input??????
    users = vkapi.users.search(interests=''.join(INTERESTS), city=CITY, sex=SEX, age_from=AGE_FROM,
                               age_to=AGE_TO, fields='photo_big,domain', access_token=MyVkData.ACCESS_TOKEN_VK,
                               v=MyVkData.API_VERSION_VK)

    users = timeout(users)
    ITEMS = 'items'
    user_list = users[ITEMS]


    for user in user_list:
        window.listWidget_satisfaction.addItem(f'{str(user["id"])}, {str(user["first_name"])}, '
                                               f'{str(user["last_name"])}, {str(user["domain"])}')
        # window.listWidget_satisfaction.addItem(str(user))
    window.listWidget_satisfaction.addItem(INTERESTS)
###
window.pushButton_launch.clicked.connect(interest_search)
#########

# start GUI app
sys.exit(app.exec_())
