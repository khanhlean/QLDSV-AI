


from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc

import DBHelper
from DBHelper import *
from QuanLy_Layout import *
from SinhVien_Layout import *
from TB_Layout import *

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-BDENHI9;'
                      'Database=quanlydiem1_HTTM;'
                      'Trusted_connection=yes;')
# cur = conn.cursor()

class Ui_DialogMain(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(339, 200)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 30, 291, 221))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.TKLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.TKLabel.setObjectName("TKLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.TKLabel)
        self.TKLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.TKLineEdit.setSizeIncrement(QtCore.QSize(0, 0))
        self.TKLineEdit.setObjectName("TKLineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.TKLineEdit)
        self.MKLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.MKLabel.setObjectName("MKLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.MKLabel)
        self.MKLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.MKLineEdit.setObjectName("MKLineEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.MKLineEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")



        self.DNButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.DNButton.setObjectName("DNButton")
        self.horizontalLayout_2.addWidget(self.DNButton)
        self.DNButton.clicked.connect(self.nutDN)



        self.ThoatButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.ThoatButton.setObjectName("ThoatButton")
        self.horizontalLayout_2.addWidget(self.ThoatButton)
        self.formLayout_2.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.ThoatButton.clicked.connect(self.nutThoat)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.TKLineEdit.setText("SINHVIEN1")
        self.MKLineEdit.setText("123456")

    def layTaiKhoan(self, a,b):
        tk = self.TKLineEdit.text()
        mk = self.MKLineEdit.text()
        query1 = "SELECT MaTk FROM TaiKhoan where tentaikhoan= '" + a + "' and matkhau= '" + b + "'"
        # cur.execute(query1)
        for row in ketnoi().execute(query1):
            b = str(row).replace("(", "", 2)
            c = str(b).replace("'", "", 2)
            d = str(c).replace(",", "", 2)
            e = str(d).replace(")", "", 2)
            f = str(e).replace(" ", "", 2)
        return f

    def searchVaiTro(self, a,b):
        query1 = "SELECT MaVaiTro FROM TaiKhoan where tentaikhoan= '" + a + "' and matkhau= '" + b + "'"
        # cur.execute(query1)
        for row in ketnoi().execute(query1):
            b = str(row).replace("(", "", 2)
            c = str(b).replace("'", "", 2)
            d = str(c).replace(",", "", 2)
            e = str(d).replace(")", "", 2)
            f = str(e).replace(" ", "", 2)
        return f

    def nutDN(self):
        tk = self.TKLineEdit.text()
        mk = self.MKLineEdit.text()
        try:
            if str(self.searchVaiTro(tk,mk)) == "VT2":
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_DialogQL()
                self.ui.setup(self.window)
                self.window.show()
                DBHelper.matk=self.layTaiKhoan(tk, mk)

            if str(self.searchVaiTro(tk,mk)) == "VT3":
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_DialogSV()
                self.ui.setupUi(self.window)
                self.window.show()
                DBHelper.matk=self.layTaiKhoan(tk, mk)
            conn.commit()
            print("Ok")

        except:
            DBHelper.textThongBao = "Tài khoản hoặc mật khẩu sai."
            hienTB(self)
            print("Fail")

    def nutThoat(self):
        QtWidgets.QApplication.quit()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "QLDSV"))
        self.label.setText(_translate("Dialog", "ĐĂNG NHẬP"))
        self.TKLabel.setText(_translate("Dialog", "Tài khoản:"))
        self.MKLabel.setText(_translate("Dialog", "Mật khẩu:"))
        self.DNButton.setText(_translate("Dialog", "Đăng nhập"))
        self.ThoatButton.setText(_translate("Dialog", "Thoát"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_DialogMain()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

