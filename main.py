import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
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

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

widget = QLabel("TEMP & CURRENT MONITORING GUI")
font = widget.font()
font.setPointSize(30)
widget.setFont(font)
widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

self.setCentralWidget(widget)

widget = QLabel("1")  # The label is created with the text 1.
widget.setText("2")   # The label now shows 2.

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("IITD EQUIP LAB")

        widget = QLabel("TEMP & CURRENT MONITORING GUI")
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec() 