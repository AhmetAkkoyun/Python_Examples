# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kumpir_siparis.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 400)
        self.btn_siparis_tamamla = QtWidgets.QPushButton(Form)
        self.btn_siparis_tamamla.setGeometry(QtCore.QRect(270, 260, 110, 25))
        self.btn_siparis_tamamla.setObjectName("btn_siparis_tamamla")
        self.cmb_kumpir_secim = QtWidgets.QComboBox(Form)
        self.cmb_kumpir_secim.setGeometry(QtCore.QRect(110, 20, 120, 25))
        self.cmb_kumpir_secim.setObjectName("cmb_kumpir_secim")
        self.cmb_kumpir_secim.addItem("")
        self.cmb_kumpir_secim.setItemText(0, "")
        self.cmb_kumpir_secim.addItem("")
        self.cmb_kumpir_secim.addItem("")
        self.cmb_kumpir_secim.addItem("")
        self.edt_siparis_bilgisi = QtWidgets.QLineEdit(Form)
        self.edt_siparis_bilgisi.setGeometry(QtCore.QRect(20, 290, 360, 90))
        self.edt_siparis_bilgisi.setObjectName("edt_siparis_bilgisi")
        self.label_kumpir = QtWidgets.QLabel(Form)
        self.label_kumpir.setGeometry(QtCore.QRect(20, 20, 80, 25))
        self.label_kumpir.setObjectName("label_kumpir")
        self.label_cikolata = QtWidgets.QLabel(Form)
        self.label_cikolata.setGeometry(QtCore.QRect(20, 180, 80, 25))
        self.label_cikolata.setObjectName("label_cikolata")
        self.cmb_cikolata_secim = QtWidgets.QComboBox(Form)
        self.cmb_cikolata_secim.setGeometry(QtCore.QRect(110, 180, 120, 25))
        self.cmb_cikolata_secim.setObjectName("cmb_cikolata_secim")
        self.cmb_cikolata_secim.addItem("")
        self.cmb_cikolata_secim.setItemText(0, "")
        self.cmb_cikolata_secim.addItem("")
        self.cmb_cikolata_secim.addItem("")
        self.cmb_cikolata_secim.addItem("")
        self.label_susleme = QtWidgets.QLabel(Form)
        self.label_susleme.setGeometry(QtCore.QRect(20, 220, 80, 25))
        self.label_susleme.setObjectName("label_susleme")
        self.cmb_susleme_secim = QtWidgets.QComboBox(Form)
        self.cmb_susleme_secim.setGeometry(QtCore.QRect(110, 220, 120, 25))
        self.cmb_susleme_secim.setObjectName("cmb_susleme_secim")
        self.cmb_susleme_secim.addItem("")
        self.cmb_susleme_secim.setItemText(0, "")
        self.cmb_susleme_secim.addItem("")
        self.cmb_susleme_secim.addItem("")
        self.cmb_susleme_secim.addItem("")
        self.edt_kumpir = QtWidgets.QLineEdit(Form)
        self.edt_kumpir.setGeometry(QtCore.QRect(250, 20, 110, 25))
        self.edt_kumpir.setObjectName("edt_kumpir")
        self.edt_cikolata = QtWidgets.QLineEdit(Form)
        self.edt_cikolata.setGeometry(QtCore.QRect(250, 180, 110, 25))
        self.edt_cikolata.setObjectName("edt_cikolata")
        self.edt_susleme = QtWidgets.QLineEdit(Form)
        self.edt_susleme.setGeometry(QtCore.QRect(250, 220, 110, 25))
        self.edt_susleme.setObjectName("edt_susleme")
        self.cmb_kumpir_malz_1 = QtWidgets.QComboBox(Form)
        self.cmb_kumpir_malz_1.setGeometry(QtCore.QRect(110, 60, 90, 25))
        self.cmb_kumpir_malz_1.setObjectName("cmb_kumpir_malz_1")
        self.cmb_kumpir_malz_1.addItem("")
        self.cmb_kumpir_malz_1.setItemText(0, "")
        self.cmb_kumpir_malz_1.addItem("")
        self.cmb_kumpir_malz_1.addItem("")
        self.cmb_kumpir_malz_1.addItem("")
        self.cmb_kumpir_malz_1.addItem("")
        self.cmb_kumpir_malz_1.addItem("")
        self.cmb_kumpir_malz_1.addItem("")
        self.cmb_kumpir_malz_1.addItem("")
        self.edt_kumpir_malz_1 = QtWidgets.QLineEdit(Form)
        self.edt_kumpir_malz_1.setGeometry(QtCore.QRect(250, 60, 70, 25))
        self.edt_kumpir_malz_1.setObjectName("edt_kumpir_malz_1")
        self.edt_kumpir_malz_2 = QtWidgets.QLineEdit(Form)
        self.edt_kumpir_malz_2.setGeometry(QtCore.QRect(250, 100, 70, 25))
        self.edt_kumpir_malz_2.setObjectName("edt_kumpir_malz_2")
        self.edt_kumpir_malz_3 = QtWidgets.QLineEdit(Form)
        self.edt_kumpir_malz_3.setGeometry(QtCore.QRect(250, 140, 70, 25))
        self.edt_kumpir_malz_3.setObjectName("edt_kumpir_malz_3")
        self.label_karisik_secim1 = QtWidgets.QLabel(Form)
        self.label_karisik_secim1.setGeometry(QtCore.QRect(20, 60, 80, 25))
        self.label_karisik_secim1.setObjectName("label_karisik_secim1")
        self.label_karisik_secim_2 = QtWidgets.QLabel(Form)
        self.label_karisik_secim_2.setGeometry(QtCore.QRect(20, 100, 80, 25))
        self.label_karisik_secim_2.setObjectName("label_karisik_secim_2")
        self.label_karisik_secim_3 = QtWidgets.QLabel(Form)
        self.label_karisik_secim_3.setGeometry(QtCore.QRect(20, 140, 80, 25))
        self.label_karisik_secim_3.setObjectName("label_karisik_secim_3")
        self.cmb_kumpir_malz_2 = QtWidgets.QComboBox(Form)
        self.cmb_kumpir_malz_2.setGeometry(QtCore.QRect(110, 100, 90, 25))
        self.cmb_kumpir_malz_2.setObjectName("cmb_kumpir_malz_2")
        self.cmb_kumpir_malz_2.addItem("")
        self.cmb_kumpir_malz_2.setItemText(0, "")
        self.cmb_kumpir_malz_2.addItem("")
        self.cmb_kumpir_malz_2.addItem("")
        self.cmb_kumpir_malz_2.addItem("")
        self.cmb_kumpir_malz_2.addItem("")
        self.cmb_kumpir_malz_2.addItem("")
        self.cmb_kumpir_malz_2.addItem("")
        self.cmb_kumpir_malz_2.addItem("")
        self.cmb_kumpir_malz_3 = QtWidgets.QComboBox(Form)
        self.cmb_kumpir_malz_3.setGeometry(QtCore.QRect(110, 140, 90, 25))
        self.cmb_kumpir_malz_3.setObjectName("cmb_kumpir_malz_3")
        self.cmb_kumpir_malz_3.addItem("")
        self.cmb_kumpir_malz_3.setItemText(0, "")
        self.cmb_kumpir_malz_3.addItem("")
        self.cmb_kumpir_malz_3.addItem("")
        self.cmb_kumpir_malz_3.addItem("")
        self.cmb_kumpir_malz_3.addItem("")
        self.cmb_kumpir_malz_3.addItem("")
        self.cmb_kumpir_malz_3.addItem("")
        self.cmb_kumpir_malz_3.addItem("")
        
        self.cmb_kumpir_malz_1.setEnabled(False)
        self.cmb_kumpir_malz_2.setEnabled(False)
        self.cmb_kumpir_malz_3.setEnabled(False)
        self.cmb_cikolata_secim.setEnabled(False)
        self.cmb_susleme_secim.setEnabled(False)
        self.edt_kumpir.setEnabled(False)
        self.edt_kumpir_malz_1.setEnabled(False)
        self.edt_kumpir_malz_2.setEnabled(False)
        self.edt_kumpir_malz_3.setEnabled(False)
        self.edt_cikolata.setEnabled(False)
        self.edt_susleme.setEnabled(False)
        
        self.cmb_kumpir_secim.currentIndexChanged.connect(self.kumpir_secimi_doldur)
        self.cmb_kumpir_malz_1.currentIndexChanged.connect(self.karisik_malzeme_secimi_1_doldur)
        self.cmb_kumpir_malz_2.currentIndexChanged.connect(self.karisik_malzeme_secimi_2_doldur)
        self.cmb_kumpir_malz_3.currentIndexChanged.connect(self.karisik_malzeme_secimi_3_doldur)
        self.cmb_cikolata_secim.currentIndexChanged.connect(self.cikolata_secimi_doldur)
        self.cmb_susleme_secim.currentIndexChanged.connect(self.susleme_secimi_doldur)
        self.btn_siparis_tamamla.clicked.connect(self.siparisi_tamamla_clicked)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "KUMPİR EXPRES"))
        self.btn_siparis_tamamla.setText(_translate("Form", "Siparişi Tamamla"))
        self.cmb_kumpir_secim.setItemText(1, _translate("Form", "Sade Kumpir"))
        self.cmb_kumpir_secim.setItemText(2, _translate("Form", "Çift Kaşarlı Kumpir"))
        self.cmb_kumpir_secim.setItemText(3, _translate("Form", "Karışık Kumpir"))
        self.label_kumpir.setText(_translate("Form", "Kumpir Seçiniz"))
        self.label_cikolata.setText(_translate("Form", "Çikolata Seçiniz"))
        self.cmb_cikolata_secim.setItemText(1, _translate("Form", "Beyaz Çikolata"))
        self.cmb_cikolata_secim.setItemText(2, _translate("Form", "Sütlü Çikolata - Nutella"))
        self.cmb_cikolata_secim.setItemText(3, _translate("Form", "Franbuazlı Çikolata"))
        self.label_susleme.setText(_translate("Form", "Süsleme Seçiniz"))
        self.cmb_susleme_secim.setItemText(1, _translate("Form", "Hindistan Cevizi"))
        self.cmb_susleme_secim.setItemText(2, _translate("Form", "Damla Bitter Çikolata"))
        self.cmb_susleme_secim.setItemText(3, _translate("Form", "Bal"))
        self.cmb_kumpir_malz_1.setItemText(1, _translate("Form", "Kısır"))
        self.cmb_kumpir_malz_1.setItemText(2, _translate("Form", "Mısır"))
        self.cmb_kumpir_malz_1.setItemText(3, _translate("Form", "Rus Salatası"))
        self.cmb_kumpir_malz_1.setItemText(4, _translate("Form", "Siyah Zeytin"))
        self.cmb_kumpir_malz_1.setItemText(5, _translate("Form", "Sosis"))
        self.cmb_kumpir_malz_1.setItemText(6, _translate("Form", "Turşu"))
        self.cmb_kumpir_malz_1.setItemText(7, _translate("Form", "Yeşil Zeytin"))
        self.label_karisik_secim1.setText(_translate("Form", "Malzeme Seçiniz"))
        self.label_karisik_secim_2.setText(_translate("Form", "Malzeme Seçiniz"))
        self.label_karisik_secim_3.setText(_translate("Form", "Malzeme Seçiniz"))
        self.cmb_kumpir_malz_2.setItemText(1, _translate("Form", "Kısır"))
        self.cmb_kumpir_malz_2.setItemText(2, _translate("Form", "Mısır"))
        self.cmb_kumpir_malz_2.setItemText(3, _translate("Form", "Rus Salatası"))
        self.cmb_kumpir_malz_2.setItemText(4, _translate("Form", "Siyah Zeytin"))
        self.cmb_kumpir_malz_2.setItemText(5, _translate("Form", "Sosis"))
        self.cmb_kumpir_malz_2.setItemText(6, _translate("Form", "Turşu"))
        self.cmb_kumpir_malz_2.setItemText(7, _translate("Form", "Yeşil Zeytin"))
        self.cmb_kumpir_malz_3.setItemText(1, _translate("Form", "Kısır"))
        self.cmb_kumpir_malz_3.setItemText(2, _translate("Form", "Mısır"))
        self.cmb_kumpir_malz_3.setItemText(3, _translate("Form", "Rus Salatası"))
        self.cmb_kumpir_malz_3.setItemText(4, _translate("Form", "Siyah Zeytin"))
        self.cmb_kumpir_malz_3.setItemText(5, _translate("Form", "Sosis"))
        self.cmb_kumpir_malz_3.setItemText(6, _translate("Form", "Turşu"))
        self.cmb_kumpir_malz_3.setItemText(7, _translate("Form", "Yeşil Zeytin"))
        



    def kumpir_secimi_doldur(self):
        secilen = self.cmb_kumpir_secim.currentIndex()
        secim = self.cmb_kumpir_secim.currentText()
        
        if secilen <= 2:
            self.cmb_kumpir_malz_1.setEnabled(False)
            self.cmb_kumpir_malz_2.setEnabled(False)
            self.cmb_kumpir_malz_3.setEnabled(False)

        else:
            self.cmb_kumpir_malz_1.setEnabled(True)
            self.cmb_kumpir_malz_2.setEnabled(True)
            self.cmb_kumpir_malz_3.setEnabled(True)
            
        self.edt_kumpir.setText(secim)
        
        self.cmb_cikolata_secim.setEnabled(True) 
      
        
        
    def karisik_malzeme_secimi_1_doldur(self):
        secilen = self.cmb_kumpir_malz_1.currentText()
        self.edt_kumpir_malz_1.setText(secilen)

        
    def karisik_malzeme_secimi_2_doldur(self):
        secilen = self.cmb_kumpir_malz_2.currentText()
        self.edt_kumpir_malz_2.setText(secilen)

        
    def karisik_malzeme_secimi_3_doldur(self):
        secilen = self.cmb_kumpir_malz_3.currentText()
        self.edt_kumpir_malz_3.setText(secilen)

        
    def cikolata_secimi_doldur(self):
        secilen = self.cmb_cikolata_secim.currentText()
        self.edt_cikolata.setText(secilen)
        
        self.cmb_susleme_secim.setEnabled(True)        
        

                
    def susleme_secimi_doldur(self):
        secilen = self.cmb_susleme_secim.currentText()
        self.edt_susleme.setText(secilen)

    
    def siparisi_tamamla_clicked(self):
        
        siparis_ozeti_kumpir = []
        siparis_ozeti_tatli = []
        
        Kumpir_fiyat = 0
        
        if self.edt_kumpir.text() == "Sade Kumpir":
            Kumpir_fiyat = 10
            siparis_ozeti_kumpir = siparis_ozeti_kumpir + [self.edt_kumpir.text()]
        elif self.edt_kumpir.text() == "Çift Kaşarlı Kumpir":
            Kumpir_fiyat = 12
            siparis_ozeti_kumpir = siparis_ozeti_kumpir + [self.edt_kumpir.text()]
        elif self.edt_kumpir.text() == "Karışık Kumpir":
            Kumpir_fiyat = 10
            siparis_ozeti_kumpir = siparis_ozeti_kumpir + [self.edt_kumpir.text()]
        else:
            Kumpir_fiyat = 0
            
        Malz_1_fiyat = 0
            
        if self.edt_kumpir_malz_1.text() == "":
            Malz_1_fiyat = 0
        else:
            Malz_1_fiyat = 2
            siparis_ozeti_kumpir = siparis_ozeti_kumpir + [self.edt_kumpir_malz_1.text()]
            
        Malz_2_fiyat = 0
        
        if self.edt_kumpir_malz_2.text() == "":
            Malz_2_fiyat = 0
        else:
            Malz_2_fiyat = 2
            siparis_ozeti_kumpir = siparis_ozeti_kumpir + [self.edt_kumpir_malz_2.text()]
            
        Malz_3_fiyat = 0
            
        if self.edt_kumpir_malz_3.text() == "":
            Malz_3_fiyat = 0
        else:
            Malz_3_fiyat = 2
            siparis_ozeti_kumpir = siparis_ozeti_kumpir + [self.edt_kumpir_malz_3.text()]
        
        cikolata_fiyat = 0

        if self.edt_cikolata.text() == "":
            cikolata_fiyat = 0
        else:
            cikolata_fiyat = 5
            siparis_ozeti_tatli = siparis_ozeti_tatli + [self.edt_cikolata.text()]
            
        susleme_fiyat = 0
        
        if self.edt_susleme.text() == "":
            susleme_fiyat = 0
        else:
            susleme_fiyat = 2
            siparis_ozeti_tatli = siparis_ozeti_tatli + [self.edt_susleme.text()]
            
        Toplam_fiyat = Kumpir_fiyat + \
        Malz_1_fiyat + \
        Malz_2_fiyat + \
        Malz_3_fiyat + \
        cikolata_fiyat + \
        susleme_fiyat 
                       
        
        sonuc = str(siparis_ozeti_kumpir) + str(siparis_ozeti_tatli) + " - Ücret: " + str(Toplam_fiyat) + " TL"

        
        self.edt_siparis_bilgisi.setText(sonuc)
        
   




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

