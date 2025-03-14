# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui\ui\confirm_excel_name.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon

from utils.my_utils import get_icon


class Ui_ExcelNameDialog(object):
    def setupUi(self, ExcelNameDialog):
        ExcelNameDialog.setObjectName("ExcelNameDialog")
        ExcelNameDialog.resize(400, 228)
        ExcelNameDialog.setWindowIcon(QIcon(get_icon()))  # 设置图标
        self.label = QtWidgets.QLabel(ExcelNameDialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 101, 51))

        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(ExcelNameDialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 60, 281, 31))

        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(ExcelNameDialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 160, 81, 41))

        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(ExcelNameDialog)
        QtCore.QMetaObject.connectSlotsByName(ExcelNameDialog)

    def retranslateUi(self, ExcelNameDialog):
        _translate = QtCore.QCoreApplication.translate
        ExcelNameDialog.setWindowTitle(_translate("ExcelNameDialog", "填写表名"))
        self.label.setText(_translate("ExcelNameDialog", "导出表格名称:"))
        self.pushButton.setText(_translate("ExcelNameDialog", "确认"))
