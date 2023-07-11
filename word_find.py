from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(527, 418)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(140, 250, 131, 28))
        self.start.setObjectName("start")
        self.start.clicked.connect(self.Start)
        self.Check = QtWidgets.QPushButton(self.centralwidget)
        self.Check.setGeometry(QtCore.QRect(320, 190, 93, 28))
        self.Check.setObjectName("Check")
        self.Check.clicked.connect(self.check)
        self.Reset = QtWidgets.QPushButton(self.centralwidget)
        self.Reset.setGeometry(QtCore.QRect(292, 250, 121, 28))
        self.Reset.setObjectName("Reset")
        self.Reset.clicked.connect(self.reset)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, -10, 251, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("color: green")
        self.label.setObjectName("label")
        self.word = QtWidgets.QLabel(self.centralwidget)
        self.word.setGeometry(QtCore.QRect(150, 110, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.word.setFont(font)
        self.word.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.word.setStyleSheet("color: rgb(73, 155, 255);")
        self.word.setText("")
        self.word.setObjectName("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 190, 151, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 527, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start.setText(_translate("MainWindow", "START"))
        self.Check.setText(_translate("MainWindow", "Check"))
        self.Reset.setText(_translate("MainWindow", "Reset"))
        self.label.setText(_translate("MainWindow", "Word find "))

    def Start(self):
        self.word.clear()
        self.word.setStyleSheet('background-color: white')
        lst = ["word", "who", 'what', 'phone', 'number', 'mouse', 'school', 'find', 'pen']

        self.word = random.choice(lst)
        word = random.sample(self.word, len(self.word))
        word = ''.join(word)
        self.word.setText(word)

    def check(self):
        if self.word == self.lineEdit.text():
            self.word.setText('CORRECT')
            self.word.setStyleSheet('''
                color: green;
                background-color: lightgreen;
            ''')
        else:
            self.word.setText('INCCORRECT')
            self.word.setStyleSheet('''
                color: red;
                background-color: #ffcccb;
            ''')

    def reset(self):
        self.word.clear()
        self.word.setStyleSheet('background-color: white')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
