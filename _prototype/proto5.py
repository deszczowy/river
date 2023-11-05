import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QPushButton, QLineEdit, QLabel, QFormLayout

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modal Dialog")
        self.setGeometry(200, 200, 400, 200)

        layout = QVBoxLayout()

        # Create widgets for input
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()

        self.age_label = QLabel("Age:")
        self.age_input = QLineEdit()

        form_layout = QFormLayout()
        form_layout.addRow(self.name_label, self.name_input)
        form_layout.addRow(self.age_label, self.age_input)

        button = QPushButton("OK")
        button.clicked.connect(self.accept)

        layout.addLayout(form_layout)
        layout.addWidget(button)

        self.setLayout(layout)

    def get_values(self):
        name = self.name_input.text()
        age = self.age_input.text()
        return name, age

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 600, 400)

        self.dialog = None  # Initialize the dialog instance

        button = QPushButton("Open Dialog")
        button.clicked.connect(self.show_modal_dialog)
        self.setCentralWidget(button)

    def show_modal_dialog(self):
        if self.dialog is None:
            self.dialog = MyDialog()

        result = self.dialog.exec_()  # Execute the dialog as a modal dialog

        if result == QDialog.Accepted:
            name, age = self.dialog.get_values()
            print("Name:", name)
            print("Age:", age)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
