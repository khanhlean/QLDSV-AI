# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SVXemCT_Layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import DBHelper
from DBHelper import *

class Ui_DialogSVXemCT(object):
    def setup(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(649, 450)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 160, 631, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(120, 122, 168, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.tNSVLabel = QtWidgets.QLabel(Dialog)
        self.tNSVLabel.setGeometry(QtCore.QRect(19, 60, 70, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tNSVLabel.setFont(font)
        self.tNSVLabel.setObjectName("tNSVLabel")
        self.mSSVLabel = QtWidgets.QLabel(Dialog)
        self.mSSVLabel.setGeometry(QtCore.QRect(19, 91, 56, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mSSVLabel.setFont(font)
        self.mSSVLabel.setObjectName("mSSVLabel")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 91, 148, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.mSSVLabel_5 = QtWidgets.QLabel(Dialog)
        self.mSSVLabel_5.setGeometry(QtCore.QRect(19, 122, 87, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mSSVLabel_5.setFont(font)
        self.mSSVLabel_5.setObjectName("mSSVLabel_5")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 60, 148, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(240, 20, 231, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Tải dữ liệu
        self.loaddata()
        self.loaddataTable()
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "QLDSV"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Mã Công Ty"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Tên Công Ty"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Địa Chỉ"))
        self.label_16.setText(_translate("Dialog", "Gioi"))
        self.tNSVLabel.setText(_translate("Dialog", "Tên SV:"))
        self.mSSVLabel.setText(_translate("Dialog", "MSSV:"))
        self.label_3.setText(_translate("Dialog", "SV2"))
        self.mSSVLabel_5.setText(_translate("Dialog", "Đánh giá:"))
        self.label_2.setText(_translate("Dialog", "Nguyễn Văn Tèo"))
        self.label_4.setText(_translate("Dialog", "CÔNG TY PHÙ HỢP"))

    # Hàm tải dữ liệu
    def loaddata(self):
        sqlquery = "select HoTen,MaSV,DanhGia from sinhvien where masv='" + DBHelper.matk + "'"
        # đặt số cột, và dữ liệu ở mỗi cột
        for row in ketnoi().execute(sqlquery):
            self.label_2.setText(row[0])
            self.label_3.setText(row[1])
            a=str(row[2])
            if a=="None":
                self.label_16.setText("Chưa có")
            else:
                self.label_16.setText(row[2])


    # Hàm tải dữ liệu lên cho table
    def loaddataTable(self):
        a=self.label_16.text()
        if self.label_16.text()=="Chưa có":
            a="Không"
        sqlquery = "select * from congty where yeucau='"+a+"' order by cast(substring(MaCT,3,10) as int)"
        self.tableWidget.setRowCount(50)
        tablerow = 0
        # đặt số cột, và dữ liệu ở mỗi cột
        for row in ketnoi().execute(sqlquery):
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            tablerow += 1
        self.tableWidget.setRowCount(tablerow)

        # Khong cho edit
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        #Sửa kích cỡ cột
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 220)
        self.tableWidget.setColumnWidth(2, 220)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_DialogSVXemCT()
    ui.setup(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
