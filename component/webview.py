# pip install PyQtWebEngine

import sys
import os

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

class CustomWebPage(QWebEnginePage):
    def acceptNavigationRequest(self, url, _type, isMainFrame):
        if _type == QWebEnginePage.NavigationTypeLinkClicked:
            return False
        return super().acceptNavigationRequest(url, _type, isMainFrame)
        
class RHtmlViewer(QWidget):
    def __init__(self, parent):
        super(RHtmlViewer, self).__init__(parent)
        self.setParent(parent)
        self.browser = QWebEngineView(self)
        self.browser.setPage(CustomWebPage(self))
        viewer_layout = QVBoxLayout()
        viewer_layout.setContentsMargins(0, 0, 0, 0)
        viewer_layout.addSpacing(0)
        viewer_layout.addWidget(self.browser)
        self.setLayout(viewer_layout)
    
    def load(self, path):
        file_path = os.path.abspath(path)
        url = QUrl.fromLocalFile(file_path)
        self.browser.setUrl(url)