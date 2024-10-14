# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui\ui\AgingAnalysis.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(779, 545)
        MainWindow.setMinimumSize(QtCore.QSize(779, 545))
        MainWindow.setMaximumSize(QtCore.QSize(779, 545))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEditLog = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEditLog.setGeometry(QtCore.QRect(9, 120, 761, 401))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.textEditLog.setFont(font)
        self.textEditLog.setStyleSheet("")
        self.textEditLog.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEditLog.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textEditLog.setReadOnly(True)
        self.textEditLog.setMaximumBlockCount(0)
        self.textEditLog.setBackgroundVisible(False)
        self.textEditLog.setCenterOnScroll(False)
        self.textEditLog.setObjectName("textEditLog")
        self.button_add_enterprise = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_enterprise.setGeometry(QtCore.QRect(40, 40, 91, 51))
        self.button_add_enterprise.setObjectName("button_add_enterprise")
        self.button_add_data = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_data.setGeometry(QtCore.QRect(300, 40, 81, 51))
        self.button_add_data.setObjectName("button_add_data")
        self.button_start_analysis = QtWidgets.QPushButton(self.centralwidget)
        self.button_start_analysis.setGeometry(QtCore.QRect(420, 40, 81, 51))
        self.button_start_analysis.setObjectName("button_start_analysis")
        self.button_export_excel = QtWidgets.QPushButton(self.centralwidget)
        self.button_export_excel.setGeometry(QtCore.QRect(540, 40, 81, 51))
        self.button_export_excel.setObjectName("button_export_excel")
        self.button_click_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.button_click_refresh.setGeometry(QtCore.QRect(660, 40, 81, 51))
        self.button_click_refresh.setObjectName("button_click_refresh")
        self.button_add_enterprise_batch = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_enterprise_batch.setGeometry(QtCore.QRect(170, 40, 91, 51))
        self.button_add_enterprise_batch.setObjectName("button_add_enterprise_batch")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "账龄分析"))
        self.button_add_enterprise.setText(_translate("MainWindow", "添加企业"))
        self.button_add_data.setText(_translate("MainWindow", "添加数据"))
        self.button_start_analysis.setText(_translate("MainWindow", "开始分析"))
        self.button_export_excel.setText(_translate("MainWindow", "导出Excel"))
        self.button_click_refresh.setText(_translate("MainWindow", "一键清空"))
        self.button_add_enterprise_batch.setText(_translate("MainWindow", "批量添加"))
