from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QVBoxLayout,QTabWidget,QHBoxLayout
from döviz import Doviz
from altin import Altin
from kripto import Kripto
from hisse import Hisse

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tabs.resize(500, 400)

        self.tabs.addTab(self.tab1, "Döviz")
        self.tabs.addTab(self.tab2, "Altın")
        self.tabs.addTab(self.tab3, "Kripto")
        self.tabs.addTab(self.tab4, "Hisseler")

        self.doviz_verileri_goster()
        self.altin_verileri_goster()
        self.kripto_Verileri_Goster()
        self.hisse_Verileri_Goster()



        h_box = QHBoxLayout(self)
        label = QLabel("Döviz Programına Hoşgeldiniz.")
        h_box.addWidget(label)

        self.layout.addLayout(h_box)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        self.setWindowTitle("Currency Pal")
        self.setFixedSize(400, 400)
        self.show()

    def doviz_verileri_goster(self):
        doviz = Doviz()
        doviz_veriler = doviz.verileri_Getir()

        self.topLayout = QVBoxLayout()
        self.label2 = QLabel("Döviz                                Alış       Satış    Değişim    Saat")
        self.topLayout.addWidget(self.label2)
        self.hLayout = QHBoxLayout()
        for titles in doviz_veriler:
            self.vLayout = QVBoxLayout()
            for each in titles:
                self.label1 = QLabel(str(each))
                self.vLayout.addWidget(self.label1)
            self.vLayout.addStretch()
            self.hLayout.addLayout(self.vLayout)
        self.hLayout.addStretch()
        self.topLayout.addLayout(self.hLayout)
        self.tab1.setLayout(self.topLayout)

    def altin_verileri_goster(self):
        altin = Altin()
        altin_veriler = altin.verileri_Getir()

        self.topLayout = QVBoxLayout()
        self.label2 = QLabel("Döviz                            Alış         Satış       Değişim    Saat")
        self.topLayout.addWidget(self.label2)
        self.hLayout = QHBoxLayout()
        for titles in altin_veriler:
            self.vLayout = QVBoxLayout()
            for each in titles:
                self.label1 = QLabel(str(each))
                self.vLayout.addWidget(self.label1)
            self.vLayout.addStretch()
            self.hLayout.addLayout(self.vLayout)
        self.hLayout.addStretch()
        self.topLayout.addLayout(self.hLayout)
        self.tab2.setLayout(self.topLayout)

    def kripto_Verileri_Goster(self):
        kripto = Kripto()
        kripto_veriler = kripto.verileri_Getir()

        self.topLayout = QVBoxLayout()
        self.label2 = QLabel("İsim        Piyasa değeri  Koin sayısı  İşlem hacmi")
        self.topLayout.addWidget(self.label2)
        self.hLayout = QHBoxLayout()
        for titles in kripto_veriler:
            self.vLayout = QVBoxLayout()
            for each in titles:
                self.label1 = QLabel(str(each))
                self.vLayout.addWidget(self.label1)
            self.vLayout.addStretch()
            self.hLayout.addLayout(self.vLayout)
        self.hLayout.addStretch()
        self.topLayout.addLayout(self.hLayout)
        self.tab3.setLayout(self.topLayout)

    def hisse_Verileri_Goster(self):
        hisse = Hisse()
        hisse_Veriler = hisse.verileri_Getir()

        self.topLayout = QVBoxLayout()
        self.label2 = QLabel("İsim    Alış     Satış  Hacim(TL)")
        self.topLayout.addWidget(self.label2)
        self.hLayout = QHBoxLayout()
        for titles in hisse_Veriler:
            self.vLayout = QVBoxLayout()
            for each in titles:
                self.label1 = QLabel(str(each))
                self.vLayout.addWidget(self.label1)
            self.vLayout.addStretch()
            self.hLayout.addLayout(self.vLayout)
        self.hLayout.addStretch()
        self.topLayout.addLayout(self.hLayout)
        self.tab4.setLayout(self.topLayout)
import sys
app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())