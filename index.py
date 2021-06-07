import sys
from PyQt5.QtWidgets import QApplication

from window import Pencere

app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())