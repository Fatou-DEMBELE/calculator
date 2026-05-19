import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_calcu import Ui_MainWindow


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.zeroButton.clicked.connect(lambda: self.add("0"))
        self.ui.oneButton.clicked.connect(lambda: self.add("1"))
        self.ui.twoButton.clicked.connect(lambda: self.add("2"))
        self.ui.threeButton.clicked.connect(lambda: self.add("3"))
        self.ui.fourButton.clicked.connect(lambda: self.add("4"))
        self.ui.fiveButton.clicked.connect(lambda: self.add("5"))
        self.ui.sixButton.clicked.connect(lambda: self.add("6"))
        self.ui.sevenButton.clicked.connect(lambda: self.add("7"))
        self.ui.eightButton.clicked.connect(lambda: self.add("8"))
        self.ui.nineButton.clicked.connect(lambda: self.add("9"))

        self.ui.addButton.clicked.connect(lambda: self.add("+"))
        self.ui.minusButton.clicked.connect(lambda: self.add("-"))
        self.ui.multiplyButton.clicked.connect(lambda: self.add("*"))
        self.ui.divideButton.clicked.connect(lambda: self.add("/"))
        self.ui.decimalButton.clicked.connect(lambda: self.add("."))
        self.ui.percentButton.clicked.connect(lambda: self.add("%"))

        self.ui.equalButton.clicked.connect(self.equal)
        self.ui.clearButton.clicked.connect(self.clear)

    def add(self, value):
        current = self.ui.outputLabel.text()
        self.ui.outputLabel.setText(current + value)

    def equal(self):
        try:
            expression = self.ui.outputLabel.text()
            expression = expression.replace("%", "/100")
            result = str(eval(expression))
            self.ui.outputLabel.setText(result)
        except:
            self.ui.outputLabel.setText("Error")

    def clear(self):
        self.ui.outputLabel.setText("")


app = QApplication(sys.argv)
window = Calculator()
window.show()
sys.exit(app.exec())