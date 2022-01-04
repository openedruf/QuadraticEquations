from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from math import sqrt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.005, y1:1, x2:1, y2:0, stop:0 rgba(22, 212, 255, 255), stop:1 rgba(255, 143, 143, 255));")
        MainWindow.setWindowTitle("Quadratic Equations")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 200, 60, 16))
        font = QtGui.QFont()
        font.setFamily(".SF NS Mono")
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label.setText("Answer:")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(42, 90, 110, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(195, 90, 110, 21))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(347, 90, 110, 21))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(195, 150, 110, 32))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 10px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("solve!")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 160, 16))
        font = QtGui.QFont()
        font.setFamily(".SF NS Mono")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_2.setText("quadratic equations")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 230, 160, 20))
        font = QtGui.QFont()
        font.setFamily(".SF NS Mono")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 260, 160, 20))
        font = QtGui.QFont()
        font.setFamily(".SF NS Mono")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.add_functions()

    def add_functions(self):
        self.pushButton.clicked.connect(self.solve)

    def solve(self):
        a = self.lineEdit.text()
        b = self.lineEdit_2.text()
        c = self.lineEdit_3.text()

        is_adv_digit = lambda x: x.isdigit() if x[:1] != '-' else x[1:].isdigit()

        if (is_adv_digit(a) and is_adv_digit(b) and is_adv_digit(c)):
            a = int(a)
            b = int(b)
            c = int(c)
            discriminant = (b*b) - (4*a*c)
            if (discriminant > 0):
                x1 = (b*(-1) + sqrt(discriminant)) / (2*a)
                x2 = (b*(-1) - sqrt(discriminant)) / (2*a)
                self.label_3.setText(str(x1))
                self.label_4.setText(str(x2))
            else:
                error = QMessageBox()
                error.setWindowTitle("Warning")
                error.setText("Invalid Discriminant")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)
                error.exec_()
        else:
            error = QMessageBox()
            error.setWindowTitle("Warning")
            error.setText("Invalid Value")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
