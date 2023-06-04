# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quiz.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(425, 120)
        self.ak_buyuk_harf = QtWidgets.QPushButton(Dialog)
        self.ak_buyuk_harf.setGeometry(QtCore.QRect(160, 10, 100, 30))
        self.ak_buyuk_harf.setObjectName("ak_buyuk_harf")
        self.ak_karakter_say = QtWidgets.QPushButton(Dialog)
        self.ak_karakter_say.setGeometry(QtCore.QRect(160, 80, 100, 30))
        self.ak_karakter_say.setObjectName("ak_karakter_say")
        self.ak_giris = QtWidgets.QLineEdit(Dialog)
        self.ak_giris.setGeometry(QtCore.QRect(10, 50, 200, 20))
        self.ak_giris.setObjectName("ak_giris")
        self.ak_cikis = QtWidgets.QLineEdit(Dialog)
        self.ak_cikis.setGeometry(QtCore.QRect(215, 50, 200, 20))
        self.ak_cikis.setObjectName("ak_cikis")
        
        self.ak_karakter_say.clicked.connect(self.ak_karakter_say_clicked)
        self.ak_buyuk_harf.clicked.connect(self.ak_buyuk_harf_clicked)
        
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Quiz"))
        self.ak_buyuk_harf.setText(_translate("Dialog", "Büyük Harf Yap"))
        self.ak_karakter_say.setText(_translate("Dialog", "Karakter Sayısı Ver"))

    def ak_karakter_say_clicked(self):
        okunan_yazi= self.ak_giris.text()
        yazilan_yazi= str(len(okunan_yazi))
        self.ak_cikis.setText(yazilan_yazi)
 
    def ak_buyuk_harf_clicked(self):
        okunan_yazi= self.ak_giris.text()
        yazilan_yazi= okunan_yazi.upper()
        self.ak_cikis.setText(yazilan_yazi)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

