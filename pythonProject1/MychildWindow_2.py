import sys
from PyQt5.QtWidgets import *
import win_2, win_2_1, win_2_2, win_2_3, win_2_4, win_2_5
import os
i = 0

class MychildWindow_2(QMainWindow, win_2.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def openFile(self):
        file = QFileDialog.getOpenFileName(self, "打开", ".")
        if file[0]:
            os.system(file[0])

    def save_as(self):
        list_rock = []
        list_name_2 = []
        for d in range(i):
            for g in list_name:
                list_name_2.append(g)
        for x, y in zip(list_name_2, list_ground):
            value = x + ': ' + y
            list_rock.append(value)
        # s = list_name[0] + '\t' + list_name[1] + '\t' + list_name[2] + '\t' + list_name[3]
        content_1 = '水平最大地应力： ' + list_s[0] + 'MPa\n'
        content_2 = '水平最小地应力： ' + list_s[1] + 'MPa\n'
        content_3 = '垂向地应力： ' + list_s[2] + 'MPa\n'
        content_s = content_1 + content_2 + content_3
        content_4 = '射孔区长度： ' + list_perforation[0] + 'm\n'
        content_5 = '孔密度： ' + list_perforation[1] + '个/m\n'
        content_6 = '水平井身与最小地应力方向交角： ' + list_perforation[2] + '度\n'
        content_7 = '射孔方位角： ' + list_perforation[3] + '度\n'
        content_perforation = content_4 + content_5 + content_6 + content_7
        content_8 = '排量： ' + list_construction[0] + 'm/min\n'
        content_9 = '压裂液粘度： ' + list_construction[1] + 'cp\n'
        content_construction = content_8 + content_9
        content = content_s + content_perforation + content_construction
        file_save_as = QFileDialog.getSaveFileName(self, "另存为", ".", "(*.txt)")
        if file_save_as[0]:
            f = open(file_save_as[0], encoding='utf-8', mode='w')
            with f:
                for z in list_rock:
                    content_rock = z + '\n'
                    f.write(content_rock)
                f.write(content)


class MychildWindow_2_1(QWidget, win_2_1.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MychildWindow_2_2(QWidget, win_2_2.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #     global list
        # 让表格内容不可编辑
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 让鼠标选中整行
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 单击获取单元格中的内容
        self.tableWidget.itemClicked.connect(self.outSelect)

    def outSelect(self, Item=None):
        global r, list_1, list_2, list_3
        if Item == None:
            return
        r = Item.row()
        if r != 0:
            A = self.tableWidget.item(r - 1, 0).text()
            B = self.tableWidget.item(r - 1, 1).text()
            C = self.tableWidget.item(r - 1, 2).text()
            D = self.tableWidget.item(r - 1, 3).text()
            E = self.tableWidget.item(r - 1, 4).text()
            F = self.tableWidget.item(r - 1, 5).text()
            G = self.tableWidget.item(r - 1, 6).text()
            H = self.tableWidget.item(r - 1, 7).text()

            list_1 = [A, B, C, D, E, F, G, H]

        A1 = self.tableWidget.item(r, 0).text()
        B1 = self.tableWidget.item(r, 1).text()
        C1 = self.tableWidget.item(r, 2).text()
        D1 = self.tableWidget.item(r, 3).text()
        E1 = self.tableWidget.item(r, 4).text()
        F1 = self.tableWidget.item(r, 5).text()
        G1 = self.tableWidget.item(r, 6).text()
        H1 = self.tableWidget.item(r, 7).text()
        list_2 = [A1, B1, C1, D1, E1, F1, G1, H1]

        if self.tableWidget.item(r + 1, 0) != None:
            A2 = self.tableWidget.item(r + 1, 0).text()
            B2 = self.tableWidget.item(r + 1, 1).text()
            C2 = self.tableWidget.item(r + 1, 2).text()
            D2 = self.tableWidget.item(r + 1, 3).text()
            E2 = self.tableWidget.item(r + 1, 4).text()
            F2 = self.tableWidget.item(r + 1, 5).text()
            G2 = self.tableWidget.item(r + 1, 6).text()
            H2 = self.tableWidget.item(r + 1, 7).text()
            list_3 = [A2, B2, C2, D2, E2, F2, G2, H2]

    def input_data(self):
        global list_4
        if self.CheckBox.isChecked() == True:
            g = '是'
        else:
            g = '否'
        a = self.lineEdit_1.text()
        b = self.lineEdit_2.text()
        c = self.lineEdit_3.text()
        d = self.lineEdit_4.text()
        e = self.lineEdit_5.text()
        f = self.lineEdit_6.text()
        h = self.lineEdit_7.text()

        list_4 = [a, b, c, d, e, f, g, h]

    def add(self):
        global i
        i += 1
        self.tableWidget.setRowCount(int(i))
        for l, m in zip(range(8), list_4):
            self.tableWidget.setItem(i - 1, l, QTableWidgetItem(m))
        return i

    def delete(self):
        global i
        i -= 1
        if i < 0:
            QMessageBox.warning(self, '警告', '行数必须大于0 ！',
                                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            self.tableWidget.setRowCount(int(i))
            return i

    def update_data(self):
        for l, m in zip(range(8), list_4):
            self.tableWidget.setItem(r, l, QTableWidgetItem(m))

    def up(self):
        for l, m in zip(range(8), list_2):
            self.tableWidget.setItem(r - 1, l, QTableWidgetItem(m))
        for x, y in zip(range(8), list_1):
            self.tableWidget.setItem(r, x, QTableWidgetItem(y))

    def down(self):
        for l, m in zip(range(8), list_3):
            self.tableWidget.setItem(r, l, QTableWidgetItem(m))
        for x, y in zip(range(8), list_2):
            self.tableWidget.setItem(r + 1, x, QTableWidgetItem(y))

    def input_data_1(self):
        global list_name, list_ground
        list_ground = []
        list_name = ['岩石种类名称', '弹性模量(GPa)', '泊松比', '抗拉强度(MPa)', '孔隙度(%)',
                     '渗透率(mD)', '是否界面层', '界面抗剪强度(MPa)']
        for j in range(i):
            for k in range(8):
                value = self.tableWidget.item(j, k).text()
                list_ground.append(value)
        # self.StatusBar = QStatusBar()
        # self.setStatusBar(self.StatusBar)
        # self.StatusBar.showMessage('已保存',5000)



class MychildWindow_2_3(QWidget, win_2_3.Ui_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def input_data_2(self):
        global list_s
        horizontal_Max_s = self.lineEdit_1.text()
        horizontal_Min_s = self.lineEdit_2.text()
        vertical_s = self.lineEdit_3.text()
        list_s = [horizontal_Max_s, horizontal_Min_s, vertical_s]


class MychildWindow_2_4(QWidget, win_2_4.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def input_data_3(self):
        global list_perforation
        length = self.lineEdit_1.text()
        density = self.lineEdit_2.text()
        intersection_angle = self.lineEdit_3.text()
        azimuth = self.lineEdit_4.text()
        list_perforation = [length, density, intersection_angle, azimuth]


class MychildWindow_2_5(QWidget, win_2_5.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def input_data_4(self):
        global list_construction
        Q = self.lineEdit_1.text()
        viscosity = self.lineEdit_2.text()
        list_construction = [Q, viscosity]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w2 = MychildWindow_2()
    w2_1 = MychildWindow_2_1()
    w2_2 = MychildWindow_2_2()
    w2_3 = MychildWindow_2_3()
    w2_4 = MychildWindow_2_4()
    w2_5 = MychildWindow_2_5()
    w2.show()


    def showWin_1():
        w2_1.show()


    def showWin_2():
        w2_2.show()


    def showWin_3():
        w2_3.show()


    def showWin_4():
        w2_4.show()


    def showWin_5():
        w2_5.show()


    w2.action_1.triggered.connect(showWin_1)
    w2.action_2.triggered.connect(showWin_2)
    w2.action_3.triggered.connect(showWin_3)
    w2.action_4.triggered.connect(showWin_4)
    w2.action_5.triggered.connect(showWin_5)

    app.exec_()
