# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(260, 110)
        self.edt_mesaj = QtWidgets.QLineEdit(dialog)
        self.edt_mesaj.setGeometry(QtCore.QRect(30, 60, 200, 20))
        self.edt_mesaj.setObjectName("edt_mesaj")
        self.ak_merhaba_yaz = QtWidgets.QPushButton(dialog)
        self.ak_merhaba_yaz.setGeometry(QtCore.QRect(30, 20, 100, 20))
        self.ak_merhaba_yaz.setObjectName("ak_merhaba_yaz_2")

        # aşağada eklediğimiz fonksiyonu burada bağlayacağız
        
        self.ak_merhaba_yaz.clicked.connect(self.ak_merhaba_yaz_clicked)


        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Merhaba"))
        self.ak_merhaba_yaz.setText(_translate("dialog", "MERHABA YAZ"))


    # yeni bir fonk ekleyeceğiz
    def ak_merhaba_yaz_clicked(self):
        self.edt_mesaj.setText("Merhaba Yüce Efendimiz Ahmet")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())

