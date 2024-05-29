import pyodbc
import Treeeeeee
from TB_Layout import *
from Treeeeeee import *
def ketnoi():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-BDENHI9;'
                          'Database=quanlydiem1_HTTM;'
                          'Trusted_connection=yes;')
    cur = conn.cursor()
    return cur

def hienTB(self):
    self.window=QtWidgets.QMainWindow()
    self.ui=Ui_DialogTB()
    self.ui.setup(self.window)
    self.window.show()

matk="SV2"
masv_formnl=""
textThongBao=""