import datetime
import sys
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QListWidgetItem


from purchase_list import Purchase

app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi('20181017_main_gui_modal.ui')

window.show()
"""
Get all positions
"""


def get_all_positions():
    purchase = Purchase()
    window.listWidget_purchase_list.clear()
    for purchase in purchase.get_all_positions():
        item = QListWidgetItem(f'{str(purchase["name"])} : {str(purchase["quantity"])} '
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


def validate_data(date_text):
    purchase_date = date_text
    try:
        datetime.datetime.strptime(purchase_date, '%Y/%m/%d')
        return True
    except Exception as e:
        return False


def line_edit_checking():
    valid_data = validate_data(window.lineEdit_purchase_date.text())
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
        pass  # TODO: добавить вывод ошибки в listWidget


window.pushButton_add_new_position.clicked.connect(add_new_position)
"""
Set new quantity or new date for 1 item
"""


def check_object():
    object_ = get_object_name()
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
        selected_object = purchase.get_all_positions()[selected_object_number]
        # print(str(selected_object_name))
        # print('*' * 10)
        return selected_object
    else:
        pass  # TODO: необходимо выделить объект для редактирования


def get_object_name():
    return get_object()['name']  # LifeHack!!!


window.listWidget_purchase_list.itemClicked.connect(get_object_name)


def set_quantity():
    # print('IN set_quantity')
    if check_object() and check_quantity():
        purchase2edit = get_object_name()
        # print(purchase2edit)
        new_quantity = window.lineEdit_set_quantity.text()
        purchase = Purchase()
        # print(new_quantity)
        purchase.set_quantity(purchase2edit, new_quantity)
    else:
        pass  # TODO: необходимо задать количество


window.pushButton_set_quantity.clicked.connect(set_quantity)


def set_purchase_date():
    # print('IN set_purchase_date')
    validated_data = validate_data(window.lineEdit_set_purchase_date.text())
    if check_object() and validated_data:
        purchase2edit = get_object_name()
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
    purchase2deleted = get_object_name()
    # print(purchase2deleted)
    purchase = Purchase()
    purchase.delete_position(purchase2deleted)
    get_all_positions()  # LifeHack!!! AutoUpdate)))

def set_status(status):
    # print('IN set_status1')
    purchase2set_status = get_object_name()
    # print(purchase2set_status)
    # status = 1
    purchase = Purchase()
    purchase.set_status(purchase2set_status, status)
    get_all_positions()

# Don't forget change contextMenuPolicy to CustomContextMenu on listWidget
window.listWidget_purchase_list.customContextMenuRequested.connect(right_click_function)

action = QtWidgets.QAction()
action.setObjectName('action_delete_position')
action.setText('Delete')

action1 = QtWidgets.QAction()
action1.setObjectName('action1_set_status')
action1.setText('Purchased')

action2 = QtWidgets.QAction()
action2.setObjectName('action2_set_status')
action2.setText('To buy')

window.listWidget_purchase_list.customMenu = QtWidgets.QMenu('Menu', window.listWidget_purchase_list)
window.listWidget_purchase_list.customMenu.addAction(action)
window.listWidget_purchase_list.customMenu.addAction(action1)
window.listWidget_purchase_list.customMenu.addAction(action2)


action.triggered.connect(delete_position)
action1.triggered.connect(lambda: set_status(status=1))  # lambda must have!!!)
action2.triggered.connect(lambda: set_status(status=0))
"""
2-click (LeftMouseButton) detail feature
"""


def get_detail():
    object_ = get_object()
    print(object_)
    window_detail = uic.loadUi('20181017_main_gui_dialog.ui')

    window_detail.label_name.setText(object_['name'])
    window_detail.label_quantity.setText(object_['quantity'])

    if object_['status'] == 1:
        window_detail.pushButton_to_buy.clicked.connect(lambda: set_status(status=0))
        window_detail.pushButton_to_buy.clicked.connect(window_detail.accept)
    else:
        window_detail.pushButton_to_buy.hide()

    # dialog.pushOk.clicked.connect(dialog.accept)  # Всё ОК
    # dialog.pushCancel.clicked.connect(dialog.reject)  # Для кнопки ОТМЕНА

    window_detail.exec()


window.listWidget_purchase_list.itemDoubleClicked.connect(get_detail)

sys.exit(app.exec_())
