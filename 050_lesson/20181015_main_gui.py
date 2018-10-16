import datetime

from PyQt5 import QtWidgets, uic
import sys
import time
from PyQt5.QtWidgets import QListWidget

from purchase_list import Purchase
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


window.show()

# window.comboBox_sex.addItem('Female')  # TODO: How do it in designer??? Right mouse button???
# window.comboBox_sex.addItem('Male')
# purchase = Purchase()
######
"""
Get all positions
"""
# purchase_list = purchase.get_all_positions()


def get_all_positions():
    purchase = Purchase()
    window.listWidget_purchase_list.clear()
    for purchase in purchase.get_all_positions():
        window.listWidget_purchase_list.addItem(f'{str(purchase["name"])} : {str(purchase["quantity"])} '
                                                f'{str(purchase["unit_of_measurement"])} (Purchased date: '
                                                f'{str(purchase["purchase_date"])})')


window.pushButton_refresh_purchase_list.clicked.connect(get_all_positions)
######
"""
Add new position
"""


def validate_data():
    purchase_date = window.lineEdit_purchase_date.text()
    try:
        datetime.datetime.strptime(purchase_date, '%Y/%m/%d')
        return True
    except Exception as e:
        return False


def line_edit_checking():
    valid_data = validate_data()
    if valid_data:
        if window.lineEdit_name.text() is not None \
                and window.lineEdit_quantity.text() is not None \
                and window.lineEdit_unit_of_measurement.text() is not None \
                and window.lineEdit_purchase_date.text() is not None:
            return True
        else:
            return False
    else:
        return False


def add_new_position():
    check = line_edit_checking()
    purchase = Purchase()
    if check:
        my_dict = {
            "name": window.lineEdit_name.text(),
            "quantity": window.lineEdit_quantity.text(),
            "unit_of_measurement": window.lineEdit_unit_of_measurement.text(),
            "purchase_date": window.lineEdit_purchase_date.text(),
            "status": 0
        }
        purchase.add_new_position(my_dict)
    else:
        pass


window.pushButton_add_new_position.clicked.connect(add_new_position)
######
"""
Set new quantity or new date for 1 item
"""
# #########
# #  Why does session start before clicking the button??????
# def interest_search():
#
#     session = vk.AuthSession(app_id=MyVkData.APP_ID, user_login=MyVkData.LOGIN,
#                              user_password=MyVkData.GET_PASSWORD())
#     vkapi = vk.API(session, timeout=100)
#
#     ######
#     # INTERESTS = ['путешествия', 'фильмы']
#     INTERESTS = window.lineEdit_for_1_interest.text()
#     ######
#
#     AGE_FROM = window.lineEdit_min_age.text()
#     AGE_TO = window.lineEdit_max_age.text()
#
#     ######
#     sex = str(window.comboBox_sex.currentText())
#     if sex == 'Female':
#         SEX = 1
#     else:
#         SEX = 2
#     ######
#
#     CITY = 1  # Moscow
#
#     def timeout(query):
#         time.sleep(0.3)
#         return query
#
#     # Why does we need comma in "interests" when we use list as input??????
#     users = vkapi.users.search(interests=''.join(INTERESTS), city=CITY, sex=SEX, age_from=AGE_FROM,
#                                age_to=AGE_TO, fields='photo_big,domain', access_token=MyVkData.ACCESS_TOKEN_VK,
#                                v=MyVkData.API_VERSION_VK)
#
#     users = timeout(users)
#     ITEMS = 'items'
#     user_list = users[ITEMS]
#
#
#     for user in user_list:
#         window.listWidget_satisfaction.addItem(f'{str(user["id"])}, {str(user["first_name"])}, '
#                                                f'{str(user["last_name"])}, {str(user["domain"])}')
#         # window.listWidget_satisfaction.addItem(str(user))
#     window.listWidget_satisfaction.addItem(INTERESTS)  # check for entered interest
# ###
# window.pushButton_launch.clicked.connect(interest_search)
# #########

# start GUI app
sys.exit(app.exec_())
