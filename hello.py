# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(457, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 300))
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalFrame = QtWidgets.QFrame(self.verticalWidget)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.horizontalFrame)
        self.verticalLayout_3.setContentsMargins(2, 2, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalFrame = QtWidgets.QFrame(self.horizontalFrame)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalFrame)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.text = QtWidgets.QTextBrowser(self.verticalFrame)
        self.text.setPlaceholderText("")
        self.text.setObjectName("text")
        self.verticalLayout_2.addWidget(self.text)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalFrame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout_3.addWidget(self.verticalFrame)
        self.in_push = QtWidgets.QPushButton(self.horizontalFrame)
        self.in_push.setObjectName("in_push")
        self.verticalLayout_3.addWidget(self.in_push)
        self.cancel = QtWidgets.QPushButton(self.horizontalFrame)
        self.cancel.setObjectName("cancel")
        self.verticalLayout_3.addWidget(self.cancel)
        self.verticalLayout.addWidget(self.horizontalFrame)
        self.gridLayout.addWidget(self.verticalWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 457, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.in_push.clicked.connect(self.text.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.text)
        MainWindow.setTabOrder(self.text, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.in_push)
        MainWindow.setTabOrder(self.in_push, self.cancel)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "爬虫"))
        self.lineEdit.setInputMask(_translate("MainWindow", "546456"))
        self.lineEdit.setText(_translate("MainWindow", "546456"))
        self.in_push.setText(_translate("MainWindow", "提交"))
        self.cancel.setText(_translate("MainWindow", "返回"))
