import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel

class HoverWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.label = QLabel('One', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background-color: lightblue; font-size: 24px;")
        self.label.setGeometry(100, 100, 200, 100)

    def enterEvent(self, event):
        # When the mouse enters the widget, bring it to the front
        self.raise_()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Hovering Widget Example')

        # Create the hovering widget
        self.hover_widget = HoverWidget(self)
        self.hover_widget.setGeometry(100, 100, 400, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
