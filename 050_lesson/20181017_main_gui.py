import datetime
import sys
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QListWidgetItem


from purchase_list import Purchase

app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi('20181017_main_gui.ui')

window.show()
"""
Get all positions
"""


def get_all_positions():
    purchase = Purchase()
    window.listWidget_purchase_list.clear()
    for purchase in purchase.get_all_positions():
        item = QListWidgetItem(f'{str(purchase["name"])} : {str(purchase["quantity"])}'
                               f'{str(purchase["unit_of_measurement"])} (Purchased date: '
                               f'{str(purchase["purchase_date"])}) : '
                               f'Status: {str(purchase["status"])}')
        if str(purchase["status"]) == '1':
            item.setBackground(QColor('#7fc97f'))
            window.listWidget_purchase_list.addItem(item)
        else:
            window.listWidget_purchase_list.addItem(item)


window.pushButton_refresh_purchase_list.clicked.connect(get_all_positions)

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
"""
Set new quantity or new date for 1 item
"""


def check_object():
    object_ = get_object()
    # print(f'Object: {object_}')
    if object_:
        return True
    else:
        return False


def check_quantity():
    quantity = window.lineEdit_set_quantity.text()
    # print(f'Quantity: {quantity}')
    if quantity:
        return True
    else:
        return False


def get_object():
    selected_object_number = window.listWidget_purchase_list.currentRow()
    if selected_object_number >= 0:
        # print(selected_object_number)
        # print(window.listWidget_purchase_list.currentItem().text())
        purchase = Purchase()
        selected_object_name = purchase.get_all_positions()[selected_object_number]['name']
        # print(str(selected_object_name))
        # print('*' * 10)
        return selected_object_name
    else:
        pass


window.listWidget_purchase_list.itemClicked.connect(get_object)


def set_quantity():
    # print('IN set_quantity')
    if check_object() and check_quantity():
        purchase2edit = get_object()
        print(purchase2edit)
        new_quantity = window.lineEdit_set_quantity.text()
        purchase = Purchase()
        print(new_quantity)
        purchase.set_quantity(purchase2edit, new_quantity)
    else:
        pass


window.pushButton_set_quantity.clicked.connect(set_quantity)


def valid_data():
    purchase_date = window.lineEdit_set_purchase_date.text()
    try:
        datetime.datetime.strptime(purchase_date, '%Y/%m/%d')
        return True
    except Exception as e:
        return False


def set_purchase_date():
    # print('IN set_purchase_date')
    validated_data = valid_data()
    if check_object() and validated_data:
        purchase2edit = get_object()
        # print(purchase2edit)
        new_date = window.lineEdit_set_purchase_date.text()
        purchase = Purchase()
        # print(new_date)
        purchase.set_purchase_date(purchase2edit, new_date)
    else:
        pass


window.pushButton_set_purchase_date.clicked.connect(set_purchase_date)
"""
Right-click item menu with options:
1. Delete_position
2. Set_status
"""


def right_click_function():
    window.listWidget_purchase_list.customMenu.popup(QtGui.QCursor.pos())


def delete_position():
    # print('IN delete_position')
    purchase2deleted = get_object()
    # print(purchase2deleted)
    purchase = Purchase()
    purchase.delete_position(purchase2deleted)


def set_status1():
    # print('IN set_status1')
    purchase2set_status = get_object()
    # print(purchase2set_status)
    status = 1
    purchase = Purchase()
    purchase.set_status(purchase2set_status, status)


def set_status0():
    # print('IN set_status0')
    purchase2set_status = get_object()
    # print(purchase2set_status)
    status = 0
    purchase = Purchase()
    purchase.set_status(purchase2set_status, status)


window.listWidget_purchase_list.customContextMenuRequested.connect(right_click_function)

window.action = QtWidgets.QAction()
window.action.setObjectName('action_delete_position')
window.action.setText('Delete')

window.action1 = QtWidgets.QAction()
window.action1.setObjectName('action1_set_status')
window.action1.setText('Purchased')

window.action2 = QtWidgets.QAction()
window.action2.setObjectName('action2_set_status')
window.action2.setText('To buy')

window.listWidget_purchase_list.customMenu = QtWidgets.QMenu('Menu', window.listWidget_purchase_list)
window.listWidget_purchase_list.customMenu.addAction(window.action)
window.listWidget_purchase_list.customMenu.addAction(window.action1)
window.listWidget_purchase_list.customMenu.addAction(window.action2)


window.action.triggered.connect(delete_position)
window.action1.triggered.connect(set_status1)
window.action2.triggered.connect(set_status0)

sys.exit(app.exec_())
