from PyQt5 import QtCore, QtGui, QtWidgets

import DBHelper
import Dangnhap_Layout
from QLGV_Layout import *
from QLSV_Layout import *
from QLLTC_Layout import *
from QLCN_Layout import *
from QLMH_Layout import *
from Dangnhap_Layout import *
from QLDiem_Layout import *
from DBHelper import *
from TB_Layout import *
from QLCT_Layout import *


class Ui_DialogQL(object):
    def setup(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(358, 347)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 30, 281, 301))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.DNButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.DNButton.setObjectName("DNButton")
        self.verticalLayout.addWidget(self.DNButton)
        self.ThoatButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.ThoatButton.setObjectName("ThoatButton")
        self.verticalLayout.addWidget(self.ThoatButton)
        self.DNButton_2 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.DNButton_2.setObjectName("DNButton_2")
        self.verticalLayout.addWidget(self.DNButton_2)
        self.DNButton_3 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.DNButton_3.setObjectName("DNButton_3")
        self.verticalLayout.addWidget(self.DNButton_3)
        self.DNButton_4 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.DNButton_4.setObjectName("DNButton_4")
        self.verticalLayout.addWidget(self.DNButton_4)
        self.DNButton_5 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.DNButton_5.setObjectName("DNButton_5")
        self.verticalLayout.addWidget(self.DNButton_5)
        self.DNButton_6 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.DNButton_6.setObjectName("DNButton_6")
        self.verticalLayout.addWidget(self.DNButton_6)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout_2.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # #Nút Thoát
        # self.pushButton.clicked.connect(self.nutThoat)

        # Nút QLGV
        self.DNButton.clicked.connect(self.nutQLGV)
        # Nút QLSV
        self.ThoatButton.clicked.connect(self.nutQLSV)
        # Nút QLCN
        self.DNButton_2.clicked.connect(self.nutQLCN)
        # Nút QLLTC
        self.DNButton_3.clicked.connect(self.nutQLLTC)
        # Nút QLMH
        self.DNButton_4.clicked.connect(self.nutQLMH)
        # Nút QLDiem
        self.DNButton_5.clicked.connect(self.nutQLDiem)
        # Nút QLCT
        self.DNButton_6.clicked.connect(self.nutQLCT)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "QLDSV"))
        self.label.setText(_translate("Dialog", "                  QUẢN LÝ"))
        self.DNButton.setText(_translate("Dialog", "Quản lý giảng viên"))
        self.ThoatButton.setText(_translate("Dialog", "Quản lý sinh viên"))
        self.DNButton_2.setText(_translate("Dialog", "Quản lý chuyên ngành"))
        self.DNButton_3.setText(_translate("Dialog", "Quản lý lớp tín chỉ"))
        self.DNButton_4.setText(_translate("Dialog", "Quản lý môn học"))
        self.DNButton_5.setText(_translate("Dialog", "Quản lý điểm số"))
        self.DNButton_6.setText(_translate("Dialog", "Quản lý công ty"))
        # self.pushButton.setText(_translate("Dialog", "Thoát"))




    def hienTB(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_DialogTB()
        self.ui.setup(self.window)
        self.window.show()
    def nutQLGV(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Dialog0()
        self.ui.setup(self.window)
        self.window.show()
    def nutQLSV(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Dialog1()
        self.ui.setup(self.window)
        self.window.show()
    def nutQLCN(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Dialog3()
        self.ui.setup(self.window)
        self.window.show()
    def nutQLLTC(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Dialog4()
        self.ui.setup(self.window)
        self.window.show()
    def nutQLMH(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Dialog5()
        self.ui.setup(self.window)
        self.window.show()
    def nutQLDiem(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Dialog6()
        self.ui.setup(self.window)
        self.window.show()

    def nutQLCT(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Dialog7()
        self.ui.setup(self.window)
        self.window.show()

    def nutThoat(self):
        print(DBHelper.matk)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_DialogQL()
    ui.setup(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
