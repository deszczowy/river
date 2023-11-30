from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout

class REditor(QWidget):
    """
    Component. Main flow editor.
    Main class for UI building.
    """

    def __init__(self, parent):
        super(REditor, self).__init__(parent)
        self.setParent(parent)
        self.build_ui()

    def build_ui(self):
        self.editor = QTextEdit()
        self.margin_width = 0
        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        self.setLayout(layout)
        self.set_margins()

    def set_margins(self):
        margin = self.width() - 400
        margin = round(margin / 2)
        print(margin)

        if margin < 0:
            margin = 0
        if margin != self.margin_width:
            self.editor.setViewportMargins(margin, 0, margin, 20)
            self.margin_width = margin
            
    def resizeEvent(self, event):
        self.set_margins()

class REditorConnector(REditor):
    """
    Connector. Interaction with editor component.
    """

    def __init__(self, parent):
        super(REditorConnector, self).__init__(parent)

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