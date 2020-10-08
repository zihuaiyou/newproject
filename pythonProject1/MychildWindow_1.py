import sys
from PyQt5.QtWidgets import *
import win_1, win_1_1, win_1_2, win_1_3, win_1_4
import os

i = 0


class MychildWindow_1(QMainWindow, win_1.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def new_file(self):
        pass

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
        content_4 = '单个孔眼直径： ' + list_perforation[0] + 'm\n'
        content_5 = '射入地层深度： ' + list_perforation[1] + 'm\n'
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
                # f.write(s)
                # for x, y in zip(list_ground, range(4 * i)):
                #     if (y + 1) % 4 == 0:
                #         a = x + '\t' + '\n'
                #     else:
                #         a = x + '\t'
                #     f.write(a)
                f.write(content)


class MychildWindow_1_1(QWidget, win_1_1.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        global list
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
            list_1 = [A, B, C, D]

        E = self.tableWidget.item(r, 0).text()
        F = self.tableWidget.item(r, 1).text()
        G = self.tableWidget.item(r, 2).text()
        H = self.tableWidget.item(r, 3).text()
        list_2 = [E, F, G, H]
        if self.tableWidget.item(r + 1, 0) != None:
            I = self.tableWidget.item(r + 1, 0).text()
            J = self.tableWidget.item(r + 1, 1).text()
            K = self.tableWidget.item(r + 1, 2).text()
            L = self.tableWidget.item(r + 1, 3).text()
            list_3 = [I, J, K, L]

    def input_data(self):
        global list_4
        a = self.lineEdit_1.text()
        b = self.lineEdit_2.text()
        c = self.lineEdit_3.text()
        d = self.lineEdit_4.text()
        list_4 = [a, b, c, d]

    def add(self):
        global i
        i += 1
        self.tableWidget.setRowCount(int(i))
        for l, m in zip(range(4), list_4):
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
        for l, m in zip(range(4), list_4):
            self.tableWidget.setItem(r, l, QTableWidgetItem(m))

    def up(self):
        for l, m in zip(range(4), list_2):
            self.tableWidget.setItem(r - 1, l, QTableWidgetItem(m))
        for x, y in zip(range(4), list_1):
            self.tableWidget.setItem(r, x, QTableWidgetItem(y))

    def down(self):
        for l, m in zip(range(4), list_3):
            self.tableWidget.setItem(r, l, QTableWidgetItem(m))
        for x, y in zip(range(4), list_2):
            self.tableWidget.setItem(r + 1, x, QTableWidgetItem(y))

    def input_data_1(self):
        global list_name, list_ground
        list_ground = []
        list_name = ['岩石种类名称', '弹性模量(GPa)', '泊松比', '抗拉强度(MPa)']
        for j in range(i):
            for k in range(4):
                value = self.tableWidget.item(j, k).text()
                list_ground.append(value)


class MychildWindow_1_2(QWidget, win_1_2.Ui_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def input_data_2(self):
        global list_s
        horizontal_Max_s = self.lineEdit_1.text()
        horizontal_Min_s = self.lineEdit_2.text()
        vertical_s = self.lineEdit_3.text()
        list_s = [horizontal_Max_s, horizontal_Min_s, vertical_s]


class MychildWindow_1_3(QWidget, win_1_3.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def input_data_3(self):
        global list_perforation
        diam = self.lineEdit_1.text()
        depth = self.lineEdit_2.text()
        intersection_angle = self.lineEdit_3.text()
        azimuth = self.lineEdit_4.text()
        list_perforation = [diam, depth, intersection_angle, azimuth]


class MychildWindow_1_4(QWidget, win_1_4.Ui_Form):
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
    w1 = MychildWindow_1()
    w1_1 = MychildWindow_1_1()
    w1_2 = MychildWindow_1_2()
    w1_3 = MychildWindow_1_3()
    w1_4 = MychildWindow_1_4()
    w1.show()


    def showWin_1():
        w1_1.show()


    def showWin_2():
        w1_2.show()


    def showWin_3():
        w1_3.show()


    def showWin_4():
        w1_4.show()


    w1.action_Ground.triggered.connect(showWin_1)
    w1.action_stress.triggered.connect(showWin_2)
    w1.action_perforation.triggered.connect(showWin_3)
    w1.action_construction.triggered.connect(showWin_4)

    app.exec_()
