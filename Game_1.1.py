

from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_MainWindow(object):

    def __init__(self):
        self.guessnum = -1
        self.submit_clicks = 0
        self.ans = random.sample(range(0, 10), 4)
        # print(self.ans)

    def setupUi(self, MainWindow):
        MainWindow.resize(766, 603)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(260, 20, 251, 81))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(28)
        self.Title.setFont(font)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 130, 291, 391))

        self.Guess_label = [QtWidgets.QLabel(self.groupBox) for num in range(16)]
        for x in self.Guess_label:
            i = 30 + (20 * self.Guess_label.index(x))
            x.setGeometry(QtCore.QRect(20, i, 55, 16))
        self.Guessinpt = [QtWidgets.QLabel(self.groupBox) for num in range(16)]
        for x in self.Guessinpt:
            i = 30 + (20 * self.Guessinpt.index(x))
            x.setGeometry(QtCore.QRect(100, i, 61, 16))
        self.Results_guess = [QtWidgets.QLabel(self.groupBox) for num in range(16)]
        for x in self.Results_guess:
            i = 30 + (20 * self.Results_guess.index(x))
            x.setGeometry(QtCore.QRect(190, i, 55, 16))
        self.input = [QtWidgets.QSpinBox(self.centralwidget) for num in range(4)]
        for x in self.input:
            i = 380 + (90 * self.input.index(x))
            x.setGeometry(QtCore.QRect( i, 250, 71, 41))
        for x in self.input:
            x.setMaximum(10)

        self.Result_Output = QtWidgets.QLabel(self.centralwidget)
        self.Result_Output.setGeometry(QtCore.QRect(420, 430, 131, 51))
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 330, 201, 51))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 130, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 170, 341, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Game = QtWidgets.QAction(MainWindow)

        self.pushButton.clicked.connect(self.Test_Input)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "Mastermind!"))
        self.groupBox.setTitle(_translate("MainWindow", "Guess History"))
        for x in self.Guess_label:
            x.setText((_translate('Mainwindow', 'Guess ' + str(self.Guess_label.index(x) + 1))))
        self.Result_Output.setText(_translate("MainWindow", "Result"))
        self.pushButton.setText(_translate("MainWindow", "Submit!"))
        self.label.setText(_translate("MainWindow", "A random 4 digit code has been created! "))
        self.label_2.setText(_translate("MainWindow", "Put 4 numbers in the boxes bellow and read the result!! "))
        self.actionNew_Game.setText(_translate("MainWindow", "New Game"))
        self.actionNew_Game.setStatusTip(_translate("MainWindow", "Start a new game?"))
        self.actionNew_Game.setShortcut(_translate("MainWindow", "Ctrl+N"))

    def Test_Input(self):
        pos_1 = int(self.input[0].value())
        pos_2 = int(self.input[1].value())
        pos_3 = int(self.input[2].value())
        pos_4 = int(self.input[3].value())
        ans_1 = self.ans[0]
        ans_2 = self.ans[1]
        ans_3 = self.ans[2]
        ans_4 = self.ans[3]
        self.numcorrect = 0
        self.poscorrect = 0
        self.user_input = [pos_1, pos_2, pos_3, pos_4]
        if pos_1 in self.ans:
            if pos_1 == ans_1:
                self.poscorrect += 1
            elif pos_1 in self.user_input:
                self.numcorrect += 1

        if pos_2 in self.ans:
            if pos_2 == ans_2:
                self.poscorrect += 1
            elif pos_2 in self.user_input:
                self.numcorrect += 1

        if pos_3 in self.ans:
            if pos_3 == ans_3:
                self.poscorrect += 1
            elif pos_3 in self.user_input:
                self.numcorrect += 1

        if pos_4 in self.ans:
            if pos_4 == ans_4:
                self.poscorrect += 1
            elif pos_4 in self.user_input:
                self.numcorrect += 1

        self.guessnum += 1
        self.Result_Output.setText(str(self.numcorrect) + ' Numbers are in the code but in the wrong place!' + '\n' + str(self.poscorrect) + ' Numbers are correct!')
        self.Result_Output.adjustSize()

        if self.guessnum == 15:
            self.Title.setText('You Lose!')
            self.Result_Output.setText('You Lose')
        if self.poscorrect == 4:
            self.Result_Output.setText('You Win')
            self.Title.setText('You Win')

        self.Results_guess[self.guessnum].setText(str(self.numcorrect) + ' #|' + str(self.poscorrect) + ' Pos')
        self.Results_guess[self.guessnum].adjustSize()
        self.Guessinpt[self.guessnum].setText(str(self.user_input))



        # print(self.guess)
        # print(self.guessnum)
        # print(self.poscorrect)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
