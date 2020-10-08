import sys
from PyQt5.QtWidgets import *
import win_3, win_3_1, win_3_2, win_3_3, win_3_4, win_3_5
import os

i = 0
n = 0
i_1 = 0
i_2 = 0
d1=0


class MychildWindow_3(QMainWindow, win_3.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def openFile(self):
        file = QFileDialog.getOpenFileName(self, "打开", ".")
        if file[0]:
            os.system(file[0])

    def save_as(self):
        list_rock = []
        list_rock2 = []
        list_name2 = []
        list_name3 = []
        list_name4 = []
        list_stress4 = []
        list_name5 = []
        list_c = []

        # win3_2 table
        for d in range(i):
            for g in list_name:
                list_name2.append(g)
        for x, y in zip(list_name2, list_ground):
            value = x + ': ' + y
            list_rock.append(value)

        # win3_3 table
        for d in range(i_2):
            for g in list_name_3:
                list_name3.append(g)
        for x, y in zip(list_name3, list_ground_3):
            value = x + ': ' + y
            list_rock2.append(value)

        # win3_4 table
        for d in range(n):
            for g in list_name_1:
                list_name4.append(g)
        for x, y in zip(list_name4, list_ground_1):
            value = x + ': ' + y
            list_stress4.append(value)

        # win3_5 table
        for d in range(i_1):
            for g in list_name_2:
                list_name5.append(g)
        for x, y in zip(list_name5, list_ground_2):
            value = x + ': ' + y
            list_c.append(value)

        # win3_1
        content_1 = '裂缝长度(m)： ' + list_crack[0] + 'm\n'
        content_2 = '裂缝高度(m)： ' + list_crack[1] + 'm\n'
        content_3 = '裂缝宽度： ' + list_crack[2] + 'm\n'
        content_4 = '裂缝形状： ' + str(list_crack[3]) + '\n'
        content_crack = content_1 + content_2 + content_3 + content_4

        # win3_3
        content_4 = '最大水平地应力方向： ' + direction_Max_s + 'm\n'
        content_5 = '最小水平地应力方向： ' + direction_Min_s + 'm\n'
        content_d = content_4 + content_5

        # win3_5
        content_v = '压裂液粘度： ' + viscosity + 'cp\n'

        file_save_as = QFileDialog.getSaveFileName(self, "另存为", ".", "(*.txt)")
        if file_save_as[0]:
            f = open(file_save_as[0], encoding='utf-8', mode='w')
            with f:
                # win3_1
                f.write(content_crack)

                # win3_2
                for z in list_rock:
                    content_rock = z + '\n'
                    f.write(content_rock)

                # win_3_3
                f.write(content_d)
                for z in list_rock2:
                    content_rock2 = z + '\n'
                    f.write(content_rock2)

                # win_3_4
                for z in list_stress4:
                    content_stress4 = z + '\n'
                    f.write(content_stress4)

                # win_3_5
                f.write(content_v)
                for z in list_c:
                    content_c = z + '\n'
                    f.write(content_c)


class MychildWindow_3_1(QWidget, win_3_1.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 当下拉索引发生改变时发射信号触发绑定的事件
        self.comboBox.currentIndexChanged[str].connect(self.print_value)


    def print_value(self):
        global d1
        d1 = self.comboBox.currentText()
        print(d1)
        return d1


    def input_data(self):
        global list_crack

        a = self.lineEdit_1.text()
        b = self.lineEdit_2.text()
        c = self.lineEdit_3.text()
        list_crack = [a, b, c, d1]


class MychildWindow_3_2(QWidget, win_3_2.Ui_Form):
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


class MychildWindow_3_3(QWidget, win_3_3.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 让表格内容不可编辑
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 让鼠标选中整行
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 单击获取单元格中的内容
        self.tableWidget.itemClicked.connect(self.outSelect)

        self.comboBox.currentIndexChanged[str].connect(self.print_value)
        self.comboBox_2.currentIndexChanged[str].connect(self.print_value)

    def print_value(self):
        global c2, d2
        c2 = self.comboBox.currentText()
        d2 = self.comboBox_2.currentText()
        return c2, d2

    def outSelect(self, Item=None):
        global r_3, list_1_2, list_2_2, list_3_2
        if Item == None:
            return
        r_3 = Item.row()
        if r_3 != 0:
            A = self.tableWidget.item(r_3 - 1, 0).text()
            B = self.tableWidget.item(r_3 - 1, 1).text()
            C = self.tableWidget.item(r_3 - 1, 2).text()
            D = self.tableWidget.item(r_3 - 1, 3).text()
            E = self.tableWidget.item(r_3 - 1, 4).text()

            list_1_2 = [A, B, C, D, E]

        A1 = self.tableWidget.item(r_3, 0).text()
        B1 = self.tableWidget.item(r_3, 1).text()
        C1 = self.tableWidget.item(r_3, 2).text()
        D1 = self.tableWidget.item(r_3, 3).text()
        E1 = self.tableWidget.item(r_3, 4).text()
        list_2_2 = [A1, B1, C1, D1, E1]

        if self.tableWidget.item(r_3 + 1, 0) != None:
            A2 = self.tableWidget.item(r_3 + 1, 0).text()
            B2 = self.tableWidget.item(r_3 + 1, 1).text()
            C2 = self.tableWidget.item(r_3 + 1, 2).text()
            D2 = self.tableWidget.item(r_3 + 1, 3).text()
            E2 = self.tableWidget.item(r_3 + 1, 4).text()
            list_3_2 = [A2, B2, C2, D2, E2]

    def input_data(self):
        global list_4_2
        a = self.lineEdit_3.text()
        b = self.lineEdit_4.text()
        e = self.lineEdit_5.text()

        list_4_2 = [a, b, c2, d2, e]

    def add(self):
        global i_2
        i_2 += 1
        self.tableWidget.setRowCount(int(i_2))
        for l, m in zip(range(5), list_4_2):
            self.tableWidget.setItem(i_2 - 1, l, QTableWidgetItem(m))
        return i_2

    def delete(self):
        global i_2
        i_2 -= 1
        if i_2 < 0:
            QMessageBox.warning(self, '警告', '行数必须大于0 ！',
                                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            self.tableWidget.setRowCount(int(i_2))
            return i_2

    def update_data(self):
        for l, m in zip(range(5), list_4_2):
            self.tableWidget.setItem(r_3, l, QTableWidgetItem(m))

    def up(self):
        for l, m in zip(range(5), list_2_2):
            self.tableWidget.setItem(r_3 - 1, l, QTableWidgetItem(m))
        for x, y in zip(range(5), list_1_2):
            self.tableWidget.setItem(r_3, x, QTableWidgetItem(y))

    def down(self):
        for l, m in zip(range(5), list_3_2):
            self.tableWidget.setItem(r_3, l, QTableWidgetItem(m))
        for x, y in zip(range(5), list_2_2):
            self.tableWidget.setItem(r_3 + 1, x, QTableWidgetItem(y))

    def input_data_1(self):
        global list_name_3, list_ground_3, direction_Max_s, direction_Min_s
        direction_Max_s = self.lineEdit_1.text()
        direction_Min_s = self.lineEdit_2.text()
        list_ground_3 = []
        list_name_3 = ['地层名称', '地层厚度(m)', '地层种类', '地层底面种类', '地层底面倾角(°)']
        for j in range(i_2):
            for k in range(5):
                value = self.tableWidget.item(j, k).text()
                list_ground_3.append(value)


class MychildWindow_3_4(QWidget, win_3_4.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 让表格内容不可编辑
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 让鼠标选中整行
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 单击获取单元格中的内容
        self.tableWidget.itemClicked.connect(self.outSelect)

    def outSelect(self, Item=None):
        global r_1
        if Item == None:
            return
        r_1 = Item.row()

    def add(self):
        global n
        n += 1
        self.tableWidget.setRowCount(int(n))
        for l, m in zip(range(3), list_stress):
            self.tableWidget.setItem(n - 1, l, QTableWidgetItem(m))
        return n

    def update_data(self):
        for l, m in zip(range(3), list_stress):
            self.tableWidget.setItem(r_1, l, QTableWidgetItem(m))

    def input_data(self):
        global list_stress
        a = self.lineEdit_1.text()
        b = self.lineEdit_2.text()
        c = self.lineEdit_3.text()

        list_stress = [a, b, c]

    def input_data_1(self):
        global list_name_1, list_ground_1
        list_ground_1 = []
        list_name_1 = ['水平最大地应力', '水平最小地应力', '垂向地应力']
        for j in range(n):
            for k in range(3):
                value = self.tableWidget.item(j, k).text()
                list_ground_1.append(value)


class MychildWindow_3_5(QWidget, win_3_5.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 让表格内容不可编辑
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 让鼠标选中整行
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 单击获取单元格中的内容
        self.tableWidget.itemClicked.connect(self.outSelect)

    def outSelect(self, Item=None):
        global r_2, list_1_1, list_2_1, list_3_1
        if Item == None:
            return
        r_2 = Item.row()
        if r_2 != 0:
            A = self.tableWidget.item(r_2 - 1, 0).text()
            B = self.tableWidget.item(r_2 - 1, 1).text()

            list_1_1 = [A, B]

        A1 = self.tableWidget.item(r_2, 0).text()
        B1 = self.tableWidget.item(r_2, 1).text()
        list_2_1 = [A1, B1]

        if self.tableWidget.item(r_2 + 1, 0) != None:
            A2 = self.tableWidget.item(r_2 + 1, 0).text()
            B2 = self.tableWidget.item(r_2 + 1, 1).text()
            list_3_1 = [A2, B2]

    def input_data(self):
        global list_4_1, viscosity
        a = self.lineEdit_1.text()
        b = self.lineEdit_2.text()
        viscosity = self.lineEdit.text()

        list_4_1 = [a, b]

    def add(self):
        global i_1
        i_1 += 1
        self.tableWidget.setRowCount(int(i_1))
        for l, m in zip(range(2), list_4_1):
            self.tableWidget.setItem(i_1 - 1, l, QTableWidgetItem(m))
        return i_1

    def delete(self):
        global i_1
        i_1 -= 1
        if i_1 < 0:
            QMessageBox.warning(self, '警告', '行数必须大于0 ！',
                                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            self.tableWidget.setRowCount(int(i_1))
            return i_1

    def update_data(self):
        for l, m in zip(range(2), list_4_1):
            self.tableWidget.setItem(r_2, l, QTableWidgetItem(m))

    def up(self):
        for l, m in zip(range(2), list_2_1):
            self.tableWidget.setItem(r_2 - 1, l, QTableWidgetItem(m))
        for x, y in zip(range(2), list_1_1):
            self.tableWidget.setItem(r_2, x, QTableWidgetItem(y))

    def down(self):
        for l, m in zip(range(2), list_3_1):
            self.tableWidget.setItem(r_2, l, QTableWidgetItem(m))
        for x, y in zip(range(2), list_2_1):
            self.tableWidget.setItem(r_2 + 1, x, QTableWidgetItem(y))

    def input_data_1(self):
        global list_name_2, list_ground_2
        list_ground_2 = []
        list_name_2 = ['排量（m³/min)', '注入时间(min)']
        for j in range(i_1):
            for k in range(2):
                value = self.tableWidget.item(j, k).text()
                list_ground_2.append(value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w3 = MychildWindow_3()
    w3_1 = MychildWindow_3_1()
    w3_2 = MychildWindow_3_2()
    w3_3 = MychildWindow_3_3()
    w3_4 = MychildWindow_3_4()
    w3_5 = MychildWindow_3_5()
    w3.show()


    def showWin_1():
        w3_1.show()


    def showWin_2():
        w3_2.show()


    def showWin_3():
        w3_3.show()


    def showWin_4():
        w3_4.show()


    def showWin_5():
        w3_5.show()


    w3.action_1.triggered.connect(showWin_1)
    w3.action_2.triggered.connect(showWin_2)
    w3.action_3.triggered.connect(showWin_3)
    w3.action_4.triggered.connect(showWin_4)
    w3.action_5.triggered.connect(showWin_5)

    app.exec_()
