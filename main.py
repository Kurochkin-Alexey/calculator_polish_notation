from PyQt6 import QtWidgets, uic
import sys
import subprocess

class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        uic.loadUi('calculator.ui', self)

        self.pushButton.clicked.connect(self.calculation_clicked)

    def calculation_clicked(self):
        data = self.lineEdit.text()
        result = subprocess.check_output(["python", "pn.py", data])
        self.label_3.setStyleSheet("font-size: 20px;")
        self.label_3.setText(str(result.decode("utf-8")))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())

