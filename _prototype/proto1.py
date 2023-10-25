import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)

        # Create the central widget (widget1)
        widget1 = QWidget(self)
        self.setCentralWidget(widget1)

        # Create the second widget (widget2)
        self.widget2 = QWidget(self)
        self.widget2.setGeometry(0, 0, 100, self.height())
        self.widget2.setStyleSheet("background-color: green")
        self.widget2.hide()

        self.widget3 = QWidget(self)
        self.widget3.setGeometry(self.width() - 200, 0, self.width() - 200, self.height())
        self.widget3.setStyleSheet("background-color: red")
        self.widget3.hide()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_F2:
            self.toggle_widget2()

        if event.key() == Qt.Key_F3:
            self.toggle_widget3()

    def toggle_widget2(self):
        if self.widget2.isHidden():
            self.widget2.show()
        else:
            self.widget2.hide()

    def toggle_widget3(self):
        if self.widget3.isHidden():
            self.widget3.show()
        else:
            self.widget3.hide()

    def resizeEvent(self, event):
        self.widget2.setGeometry(0, 0, 100, self.height())

def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()