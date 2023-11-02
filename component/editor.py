# Main editor for story flow

from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout

class REditor(QWidget):
    def __init__(self, parent):
        super(REditor, self).__init__(parent)
        self.setParent(parent)
        self.widget = QTextEdit()
        self.margin_width = 0
        layout = QVBoxLayout()
        layout.addWidget(self.widget)
        self.setLayout(layout)
        self.set_margins()

    def set_margins(self):
        margin = self.width() - 400
        margin = round(margin / 2)
        print(margin)

        if margin < 0:
            margin = 0
        if margin != self.margin_width:
            self.widget.setViewportMargins(margin, 20, margin, 20)
            self.margin_width = margin
            
    def resizeEvent(self, event):
        self.set_margins()

    def is_modified(self):
        return self.widget.document().isModified()
    
    def cool_down(self):
        self.widget.document().setModified(False)
    
    def get_content(self):
        return self.widget.document().toPlainText()
    
    def set_content(self, content):
        self.widget.document().setPlainText(content)