# Status bar, for static data show and messages

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout

class RStatusBar(QWidget):
    def __init__(self):
        super(RStatusBar, self).__init__()
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addSpacing(0)
        self.panels = dict([])
        self.setLayout(self.layout)
        self.setContentsMargins(0, 0, 0, 0)

    def set_content(self, panel_name, content):
        if panel_name in self.panels:
            self.panels[panel_name].setText(content)
        
    def load(self):
        for panel in self.panels:
            self.layout.addWidget(self.panels[panel])

    def add_panel(self, name, textAlign = 'L', width = 0):
        panel = QLabel("")
        panel.setObjectName("StatusPanel")
        
        if textAlign == 'L':
            panel.setAlignment(QtCore.Qt.AlignLeft)
        elif textAlign == 'R':
            panel.setAlignment(QtCore.Qt.AlignRight)
        elif textAlign == 'C':
            panel.setAlignment(QtCore.Qt.AlignCenter)
        else:
            panel.setAlignment(QtCore.Qt.AlignLeft)
            
        # width not implemented yet
        self.panels[name] = panel