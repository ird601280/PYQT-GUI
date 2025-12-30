import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("IITD EQUIP LAB")
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowIcon(QIcon("iitdelhilogo.jpg"))

        label = QLabel("TEMP & CURRENT MONITORING GUI", self)
        label.setFont(QFont("Arial", 15))
        label.setGeometry(0,0,1000,100)
        label.setStyleSheet("color:pitchblack ;"
                            "background-color:lightgrey;"
                            "font-weight:bold;")
        label.setAlignment(Qt.AlignCenter)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())  # Corrected to sys.exit(
    app.exec() 