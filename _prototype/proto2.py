import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap, QIcon

class KeycapApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Keycap App")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        keycap_button = QPushButton()
        pixmap = QPixmap("keycap.png")  # Replace with your keycap image path
        icon = QIcon(pixmap)
        keycap_button.setIcon(icon)
        keycap_button.setIconSize(pixmap.rect().size())
        keycap_button.setText("Sample Keycap Description")

        layout.addWidget(keycap_button)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = KeycapApp()
    window.show()
    sys.exit(app.exec_())