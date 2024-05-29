from PyQt5 import QtCore, QtGui, QtWidgets
from SVXemDiem_Layout import *
from SVXemTTSV_Layout import *
from SVXemCT_Layout import *
from DBHelper import *
import DBHelper

class Ui_DialogSV(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 204)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 20, 281, 161))
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
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.formLayout_2.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.ThoatButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.ThoatButton.setObjectName("ThoatButton")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ThoatButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.ThoatButton.clicked.connect(self.nutXemTTSV)
        self.DNButton.clicked.connect(self.nutXemDSV)
        self.pushButton.clicked.connect(self.nutXemCT)

        # # Tải dữ liệu cho Table, cho chọn dòng, bắt trỏ chuột.
        # self.loaddataTable()
        # self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        # self.tableWidget.clicked.connect(self.tableClick)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "QLDSV"))
        self.label.setText(_translate("Dialog", "                  SINH VIÊN"))
        self.DNButton.setText(_translate("Dialog", "Xem điểm"))
        self.pushButton.setText(_translate("Dialog", "Xem công ty phù hợp"))
        self.ThoatButton.setText(_translate("Dialog", "Thông tin sinh viên"))

    def nutXemDSV(self):
        print(DBHelper.matk)
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_DialogSVXD()
        self.ui.setup(self.window)
        self.window.show()

    def nutXemTTSV(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_DialogSVXemTTSV()
        self.ui.setup(self.window)
        self.window.show()

    def nutXemCT(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_DialogSVXemCT()
        self.ui.setup(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_DialogSV()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())