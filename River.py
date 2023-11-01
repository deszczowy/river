#app
import sys

from PyQt5.QtWidgets import QApplication

from View import RMainWindow
from Controller import RController
from Engine import REngine

def main():
    app = QApplication(sys.argv)
    engine = REngine()
    view = RMainWindow()
    controller = RController(engine, view)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()