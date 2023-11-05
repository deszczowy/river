#app
import sys

from PyQt5.QtWidgets import QApplication

from Core import RConfig
from View import RMainWindowConnector
from Controller import RController
from Engine import REngine

def main():
    app = QApplication(sys.argv)
    config = RConfig()
    engine = REngine()
    view = RMainWindowConnector()
    controller = RController(engine, view, config)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()