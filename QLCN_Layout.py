# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QLCN_Layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import pyodbc
from PyQt5 import QtCore, QtGui, QtWidgets
from DBHelper import *

class Ui_Dialog3(object):
    def setup(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(691, 639)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(120, 160, 331, 30))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pushButton_17 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_5.addWidget(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_5.addWidget(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_5.addWidget(self.pushButton_19)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(40, 260, 610, 361))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(170, 90, 231, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.mGVLabel_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.mGVLabel_3.setObjectName("mGVLabel_3")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.mGVLabel_3)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.HTLabel_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.HTLabel_3.setObjectName("HTLabel_3")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.HTLabel_3)
        self.HTLineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.HTLineEdit_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.HTLineEdit_3.setObjectName("HTLineEdit_3")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.HTLineEdit_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayout_4.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_5)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(170, 20, 351, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_21 = QtWidgets.QPushButton(Dialog)
        self.pushButton_21.setGeometry(QtCore.QRect(440, 161, 93, 28))
        self.pushButton_21.setObjectName("pushButton_21")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Tải dữ liệu cho Table, cho chọn dòng, bắt trỏ chuột.
        self.loaddataTable()
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableWidget.clicked.connect(self.tableClick)

        self.label_3.setText(self.taoMaLTC())
        # Nút Thêm
        self.pushButton_17.clicked.connect(self.nutThem)
        # Nút Xóa
        self.pushButton_18.clicked.connect(self.nutXoa)
        # Nút Sửa
        self.pushButton_19.clicked.connect(self.nutSua)
        # Nút Làm Mới
        self.pushButton_21.clicked.connect(self.nutLamMoi)

        self.pushButton_18.setEnabled(False)
        self.pushButton_19.setEnabled(False)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "QLDSV"))
        self.pushButton_17.setText(_translate("Dialog", "Thêm"))
        self.pushButton_18.setText(_translate("Dialog", "Xóa"))
        self.pushButton_19.setText(_translate("Dialog", "Sửa"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Mã CN"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Tên CN"))
        self.mGVLabel_3.setText(_translate("Dialog", "Mã CN:"))
        self.label_3.setText(_translate("Dialog", "CN1"))
        self.HTLabel_3.setText(_translate("Dialog", "Tên CN:"))
        self.label_4.setText(_translate("Dialog", "QUẢN LÝ CHUYÊN NGÀNH"))
        self.pushButton_21.setText(_translate("Dialog", "Làm mới"))


    # Hàm tải dữ liệu lên cho table
    def loaddataTable(self):
        sqlquery = "select * from chuyennganh order by cast(substring(MaCN,3,10) as int)"
        self.tableWidget.setRowCount(50)
        tablerow = 0
        # đặt số cột, và dữ liệu ở mỗi cột
        for row in ketnoi().execute(sqlquery):
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            tablerow += 1
        self.tableWidget.setRowCount(tablerow)
        self.tableWidget.setColumnWidth(1, 300)
        # Khong cho edit
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

    # Hàm bắt event table click tải dữ liệu lên ô để sửa
    def tableClick(self):
        self.pushButton_17.setEnabled(False)
        self.pushButton_18.setEnabled(True)
        self.pushButton_19.setEnabled(True)
        row = self.tableWidget.currentRow()
        self.label_3.setText(self.tableWidget.item(row, 0).text())
        self.HTLineEdit_3.setText(self.tableWidget.item(row, 1).text())

    # Hàm tìm ra CN lớn nhất -> đưa vào lable CN
    def taoMaLTC(self):
        sqlquery = "select maCN from chuyennganh"
        max=0
        for row in ketnoi().execute(sqlquery):
            b = str(row).replace("(", "", 2)
            c = str(b).replace("'", "", 2)
            d = str(c).replace(",", "", 2)
            e = str(d).replace(")", "", 2)
            ma = int((str(e)[2:4]))
            if ma>max:
                max=ma
        return "CN"+str(max+1)

    # Nút Thêm
    def nutThem(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-BDENHI9;'
                              'Database=quanlydiem1_HTTM;'
                              'Trusted_connection=yes;')
        cur = conn.cursor()

        a=self.label_3.text()
        b=self.HTLineEdit_3.text()

        query="insert into chuyennganh values('"+a+"',N'"+b+"')"
        print(query)
        try:
            cur.execute(query)
            conn.commit()
            self.label_3.setText(self.taoMaLTC())
            DBHelper.textThongBao = "         Thêm thành công."
            hienTB(self)
            print("Ok")
        except:
            print("Fail")
        self.nutLamMoi()

    # Nút Xóa
    def nutXoa(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-BDENHI9;'
                              'Database=quanlydiem1_HTTM;'
                              'Trusted_connection=yes;')
        cur = conn.cursor()
        a = self.label_3.text()
        print(a)
        query = "delete from chuyennganh where macn='" + a + "'"
        try:
            if a=="CN00":
                print("Không thể xóa CN này.")
                DBHelper.textThongBao = "Không thể xóa CN này."
                hienTB(self)
            else:
                cur.execute(query)
                conn.commit()
                print("Ok")
                DBHelper.textThongBao = "         Xóa thành công."
                hienTB(self)
        except:
            print("Fail")
        self.nutLamMoi()

    # Nút Sửa
    def nutSua(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-BDENHI9;'
                              'Database=quanlydiem1_HTTM;'
                              'Trusted_connection=yes;')
        cur = conn.cursor()

        a = self.label_3.text()
        b = self.HTLineEdit_3.text()

        query = "update chuyennganh set [TenCN]=N'" + b + "' where macn = '" + a + "'"
        print(query)
        try:
            cur.execute(query)
            conn.commit()
            DBHelper.textThongBao = "         Sửa thành công."
            hienTB(self)
            print("Ok")
        except:
            print("Fail")
        self.nutLamMoi()

    # Nút Làm Mới
    def nutLamMoi(self):
        self.loaddataTable()
        self.tableWidget.clearSelection()
        self.label_3.setText(self.taoMaLTC())
        self.HTLineEdit_3.setText("")
        self.pushButton_17.setEnabled(True)
        self.pushButton_18.setEnabled(False)
        self.pushButton_19.setEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog3()
    ui.setup(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
