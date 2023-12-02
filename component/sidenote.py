from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout

class RSideNote(QWidget):
    """
    Component. Static side notes editor.
    Main class for UI building.
    """

    def __init__(self, parent):
        super(RSideNote, self).__init__(parent)
        self.max_width = 300
        self.parent = parent
        self.build_ui()

    def build_ui(self):
        self.editor = QTextEdit()
        self.editor.setViewportMargins(5, 0, 5, 20)
        self.calculate_and_set_geometry()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addSpacing(0)
        layout.addWidget(self.editor)
        self.setLayout(layout)
        self.hide()

    def resizeEvent(self, event):
        self.calculate_and_set_geometry()

    def calculate_and_set_geometry(self):
        x0 = self.parent.width() - self.max_width
        y0 = self.parent.header.height()
        x1 = self.max_width
        y1 = self.parent.tabs.height()
        self.setGeometry(x0, y0, x1, y1)

class RSideNoteConnector(RSideNote):
    """
    Connector. Interaction with side note component.
    """

    def __init__(self, parent):
        super(RSideNoteConnector, self).__init__(parent)

    def set_focus(self):
        self.editor.setFocus()
    
    def is_focused(self):
        return self.editor.hasFocus()

    def is_modified(self):
        return self.editor.document().isModified()
    
    def cool_down(self):
        self.editor.document().setModified(False)
    
    def get_content(self):
        return self.editor.document().toPlainText()
    
    def set_content(self, content):
        self.editor.document().setPlainText(content)
        self.cool_down()