import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent

class Menu(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.parent = parent
        lay = QVBoxLayout()
        label = QLabel('One', self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("background-color: lightblue; font-size: 24px;")
        self.setGeometry(0, 0, 100, self.parent.height())
        self.setStyleSheet("background-color: green; border: 1px dotted red;")
        lay.addWidget(label)
        self.setLayout(lay)
        self.hide()
        
    def resizeEvent(self, event):
        print(event)
        self.setGeometry(0, 0, 100, self.parent.height())

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)

        # Create the central widget (widget1)
        widget1 = QWidget(self)
        self.setCentralWidget(widget1)

        self.widget2 = Menu(self)

        # Create the second widget (widget2)
        #self.widget2 = Menu(self)
        #self.widget2.setGeometry(0, 0, 100, self.height())
        

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
        self.widget2.resizeEvent(event)


def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()