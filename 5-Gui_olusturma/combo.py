# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'combo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(353, 85)
        self.cmb_programlama_dili = QtWidgets.QComboBox(Form)
        self.cmb_programlama_dili.setGeometry(QtCore.QRect(20, 40, 141, 22))
        self.cmb_programlama_dili.setObjectName("cmb_programlama_dili")
        self.cmb_programlama_dili.addItem("")
        self.cmb_programlama_dili.addItem("")
        self.edt_sonuc = QtWidgets.QLineEdit(Form)
        self.edt_sonuc.setGeometry(QtCore.QRect(180, 40, 151, 20))
        self.edt_sonuc.setObjectName("edt_sonuc")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(10)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(10)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        # designerda eklemeyi unuttuğumuz combobox seçeneklerini
        # aşağıdagöründüğü gibi buradan manuel olarak ekleyebiliriz 
        
        self.cmb_programlama_dili.addItems(["c#"])
        self.cmb_programlama_dili.addItems(["java", "javascript", "asp.net", "c"])

        # kendi bağlantılarımızı yapalım
        
        self.cmb_programlama_dili.currentIndexChanged.connect(self.sonuc_kutucugunu_doldur)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Combo box kullanımı"))
        self.cmb_programlama_dili.setItemText(0, _translate("Form", "python"))
        self.cmb_programlama_dili.setItemText(1, _translate("Form", "c++"))
        self.label.setText(_translate("Form", "Programlama Dili Seçiniz"))
        self.label_2.setText(_translate("Form", "Seçtiğiniz Programlama Dili:"))

    def sonuc_kutucugunu_doldur(self):
        secilen = self.cmb_programlama_dili.currentText()
        self.edt_sonuc.setText(secilen)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

