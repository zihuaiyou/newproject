# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(853, 721)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_2.addWidget(self.graphicsView)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 853, 23))
        self.menubar.setObjectName("menubar")
        self.menuwenjian = QtWidgets.QMenu(self.menubar)
        self.menuwenjian.setObjectName("menuwenjian")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionxinjian = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.actionxinjian.setFont(font)
        self.actionxinjian.setObjectName("actionxinjian")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionbaocun = QtWidgets.QAction(MainWindow)
        self.actionbaocun.setObjectName("actionbaocun")
        self.action_save_as = QtWidgets.QAction(MainWindow)
        self.action_save_as.setObjectName("action_save_as")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.action_Ground = QtWidgets.QAction(MainWindow)
        self.action_Ground.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.action_Ground.setFont(font)
        self.action_Ground.setObjectName("action_Ground")
        self.action_stress = QtWidgets.QAction(MainWindow)
        self.action_stress.setObjectName("action_stress")
        self.action_perforation = QtWidgets.QAction(MainWindow)
        self.action_perforation.setObjectName("action_perforation")
        self.action_construction = QtWidgets.QAction(MainWindow)
        self.action_construction.setObjectName("action_construction")
        self.actionsuanli = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.actionsuanli.setFont(font)
        self.actionsuanli.setObjectName("actionsuanli")
        self.menuwenjian.addAction(self.actionxinjian)
        self.menuwenjian.addAction(self.actionOpen)
        self.menuwenjian.addAction(self.actionbaocun)
        self.menuwenjian.addAction(self.action_save_as)
        self.menuwenjian.addSeparator()
        self.menuwenjian.addAction(self.actionExit)
        self.menu.addAction(self.action_Ground)
        self.menu.addAction(self.action_stress)
        self.menu.addAction(self.action_perforation)
        self.menu.addAction(self.action_construction)
        self.menu_2.addAction(self.actionsuanli)
        self.menubar.addAction(self.menuwenjian.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.actionOpen.triggered.connect(MainWindow.openFile)
        self.actionExit.triggered.connect(MainWindow.close)
        self.action_save_as.triggered.connect(MainWindow.save_as)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "单射孔模型压裂模拟程序"))
        self.groupBox.setTitle(_translate("MainWindow", "算例绘图区"))
        self.menuwenjian.setTitle(_translate("MainWindow", "文件"))
        self.menu.setTitle(_translate("MainWindow", "修改"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.actionxinjian.setText(_translate("MainWindow", "新建"))
        self.actionOpen.setText(_translate("MainWindow", "打开 "))
        self.actionbaocun.setText(_translate("MainWindow", "保存"))
        self.action_save_as.setText(_translate("MainWindow", "另存为"))
        self.actionExit.setText(_translate("MainWindow", "退出"))
        self.action_Ground.setText(_translate("MainWindow", "修改地层性质"))
        self.action_stress.setText(_translate("MainWindow", "修改地应力"))
        self.action_perforation.setText(_translate("MainWindow", "修改射孔参数 "))
        self.action_construction.setText(_translate("MainWindow", "修改施工参数"))
        self.actionsuanli.setText(_translate("MainWindow", "算例创建向导"))