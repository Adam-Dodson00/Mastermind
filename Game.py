# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_MainWindow(object):

    def __init__(self):
        self.guessnum = 0
        self.submit_clicks = 0
        self.ans = random.sample(range(0, 10), 4)
        print(self.ans)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 603)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(260, 20, 251, 81))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(28)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 130, 291, 391))
        self.groupBox.setObjectName("groupBox")
        self.Guess1_label = QtWidgets.QLabel(self.groupBox)
        self.Guess1_label.setGeometry(QtCore.QRect(20, 30, 55, 16))
        self.Guess1_label.setObjectName("Guess1_label")
        self.Guess1_label.setText("")
        self.Guess2_label = QtWidgets.QLabel(self.groupBox)
        self.Guess2_label.setGeometry(QtCore.QRect(20, 50, 55, 16))
        self.Guess2_label.setObjectName("Guess2_label")
        self.Guess2_label.setText("")
        self.Guess3_label = QtWidgets.QLabel(self.groupBox)
        self.Guess3_label.setGeometry(QtCore.QRect(20, 70, 55, 16))
        self.Guess3_label.setObjectName("Guess3_label")
        self.Guess3_label.setText("")
        self.Guess4_label = QtWidgets.QLabel(self.groupBox)
        self.Guess4_label.setGeometry(QtCore.QRect(20, 90, 55, 16))
        self.Guess4_label.setObjectName("Guess4_label")
        self.Guess4_label.setText("")
        self.Guess5_label = QtWidgets.QLabel(self.groupBox)
        self.Guess5_label.setGeometry(QtCore.QRect(20, 110, 55, 16))
        self.Guess5_label.setObjectName("Guess5_label")
        self.Guess5_label.setText("")
        self.Guess6_label = QtWidgets.QLabel(self.groupBox)
        self.Guess6_label.setGeometry(QtCore.QRect(20, 130, 55, 16))
        self.Guess6_label.setObjectName("Guess6_label")
        self.Guess6_label.setText("")
        self.Guess7_label = QtWidgets.QLabel(self.groupBox)
        self.Guess7_label.setGeometry(QtCore.QRect(20, 150, 55, 16))
        self.Guess7_label.setObjectName("Guess7_label")
        self.Guess7_label.setText("")
        self.Guess8_label = QtWidgets.QLabel(self.groupBox)
        self.Guess8_label.setGeometry(QtCore.QRect(20, 170, 55, 16))
        self.Guess8_label.setObjectName("Guess8_label")
        self.Guess8_label.setText("")
        self.Guess9_label = QtWidgets.QLabel(self.groupBox)
        self.Guess9_label.setGeometry(QtCore.QRect(20, 190, 55, 16))
        self.Guess9_label.setObjectName("Guess9_label")
        self.Guess9_label.setText("")
        self.Guess10_label = QtWidgets.QLabel(self.groupBox)
        self.Guess10_label.setGeometry(QtCore.QRect(20, 210, 55, 16))
        self.Guess10_label.setObjectName("Guess10_label")
        self.Guess10_label.setText("")
        self.Guess11_label = QtWidgets.QLabel(self.groupBox)
        self.Guess11_label.setGeometry(QtCore.QRect(20, 230, 55, 16))
        self.Guess11_label.setObjectName("Guess11_label")
        self.Guess11_label.setText("")
        self.Guess12_label = QtWidgets.QLabel(self.groupBox)
        self.Guess12_label.setGeometry(QtCore.QRect(20, 250, 55, 16))
        self.Guess12_label.setObjectName("Guess12_label")
        self.Guess12_label.setText("")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(20, 270, 55, 16))
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.Guess13_label = QtWidgets.QLabel(self.groupBox)
        self.Guess13_label.setGeometry(QtCore.QRect(20, 270, 55, 16))
        self.Guess13_label.setObjectName("Guess13_label")
        self.Guess13_label.setText("")
        self.Guess14_label = QtWidgets.QLabel(self.groupBox)
        self.Guess14_label.setGeometry(QtCore.QRect(20, 290, 55, 16))
        self.Guess14_label.setObjectName("Guess14_label")
        self.Guess14_label.setText("")
        self.Guess15_label = QtWidgets.QLabel(self.groupBox)
        self.Guess15_label.setGeometry(QtCore.QRect(20, 310, 55, 16))
        self.Guess15_label.setObjectName("Guess15_label")
        self.Guess15_label.setText("")
        self.Guess1inpt = QtWidgets.QLabel(self.groupBox)
        self.Guess1inpt.setGeometry(QtCore.QRect(100, 30, 61, 16))
        self.Guess1inpt.setText("")
        self.Guess1inpt.setObjectName("Guess1inpt")
        self.Results_guess_2 = QtWidgets.QLabel(self.groupBox)
        self.Results_guess_2.setGeometry(QtCore.QRect(190, 50, 55, 16))
        self.Results_guess_2.setText("")
        self.Results_guess_2.setObjectName("Results_guess_2")
        self.Guess2inpt = QtWidgets.QLabel(self.groupBox)
        self.Guess2inpt.setGeometry(QtCore.QRect(100, 50, 61, 16))
        self.Guess2inpt.setText("")
        self.Guess2inpt.setObjectName("Guess2inpt")
        self.Results_guess_3 = QtWidgets.QLabel(self.groupBox)
        self.Results_guess_3.setGeometry(QtCore.QRect(190, 70, 55, 16))
        self.Results_guess_3.setText("")
        self.Results_guess_3.setObjectName("Results_guess_3")
        self.Guess3inpt = QtWidgets.QLabel(self.groupBox)
        self.Guess3inpt.setGeometry(QtCore.QRect(100, 70, 61, 16))
        self.Guess3inpt.setText("")
        self.Guess3inpt.setObjectName("Guess3inpt")
        self.Results_guess_4 = QtWidgets.QLabel(self.groupBox)
        self.Results_guess_4.setGeometry(QtCore.QRect(190, 90, 55, 16))
        self.Results_guess_4.setText("")
        self.Results_guess_4.setObjectName("Results_guess_4")
        self.Guess4inpt = QtWidgets.QLabel(self.groupBox)
        self.Guess4inpt.setGeometry(QtCore.QRect(100, 90, 61, 16))
        self.Guess4inpt.setText("")
        self.Guess4inpt.setObjectName("Guess4inpt")
        self.Guess5inpt = QtWidgets.QLabel(self.groupBox)
        self.Guess5inpt.setGeometry(QtCore.QRect(100, 110, 61, 16))
        self.Guess5inpt.setText("")
        self.Guess5inpt.setObjectName("Guess5inpt")
        self.Results_guess_6 = QtWidgets.QLabel(self.groupBox)
        self.Results_guess_6.setGeometry(QtCore.QRect(190, 130, 55, 16))
        self.Results_guess_6.setText("")
        self.Results_guess_6.setObjectName("Results_guess_6")
        self.Guess6inpt = QtWidgets.QLabel(self.groupBox)
        self.Guess6inpt.setGeometry(QtCore.QRect(100, 130, 61, 16))
        self.Guess6inpt.setText("")
        self.Guess6inpt.setObjectName("Guess6inpt")
        self.Results_guess_7 = QtWidgets.QLabel(self.groupBox)
        self.Results_guess_7.setGeometry(QtCore.QRect(190, 150, 55, 16))
        self.Results_guess_7.setText("")
        self.Results_guess_7.setObjectName("Results_guess_7")
        self.Guess7inpt = QtWidgets.QLabel(self.groupBox)
        self.Guess7inpt.setGeometry(QtCore.QRect(100, 150, 61, 16))
        self.Guess7inpt.setText("")
        self.Guess7inpt.setObjectName("Guess7inpt")
        self.Guess8inpt = QtWidgets.QLabel(self.groupBox)
        self.Guess8inpt.setGeometry(QtCore.QRect(100, 170, 61, 16))
        self.Guess8inpt.setText("")
        self.Guess8inpt.setObjectName("Guess8inpt")
        self.Results_guess_9 = QtWidgets.QLabel(self.groupBox)
        self.Results_guess_9.setGeometry(QtCore.QRect(190, 190, 55, 16))
        self.Results_guess_9.setText("")
        self.Results_guess_9.setObjectName("Results_guess_9")
        self.Guess9inpt = QtWidgets.QLabel(self.groupBox)
        self.Guess9inpt.setGeometry(QtCore.QRect(100, 190, 61, 16))
        self.Guess9inpt.setText("")
        self.Guess9inpt.setObjectName("Guess9inpt")
        self.Results_guess_10 = QtWidgets.QLabel(self.groupBox)
        self.Results_guess_10.setGeometry(QtCore.QRect(190, 210, 55, 16))
        self.Results_guess_10.setText("")
        self.Results_guess_10.setObjectName("Results_guess_10")
        self.Guess10inpt = QtWidgets.QLabel(self.groupBox)
        self.Guess10inpt.setGeometry(QtCore.QRect(100, 210, 61, 16))
        self.Guess10inpt.setText("")
        self.Guess10inpt.setObjectName("Guess10inpt")
        self.Results_guess_11 = QtWidgets.QLabel(self.groupBox)
        self.Results_guess_11.setGeometry(QtCore.QRect(190, 230, 55, 16))
        self.Results_guess_11.setText("")
        self.Results_guess_11.setObjectName("Results_guess_11")
        self.Guess11inpt = QtWidgets.QLabel(self.groupBox)
        self.Guess11inpt.setGeometry(QtCore.QRect(100, 230, 61, 16))
        self.Guess11inpt.setText("")
        self.Guess11inpt.setObjectName("Guess11inpt")
        self.Results_guess_12 = QtWidgets.QLabel(self.groupBox)
        self.Results_guess_12.setGeometry(QtCore.QRect(190, 250, 55, 16))
        self.Results_guess_12.setText("")
        self.Results_guess_12.setObjectName("Results_guess_12")
        self.Guess12inpt = QtWidgets.QLabel(self.groupBox)
        self.Guess12inpt.setGeometry(QtCore.QRect(100, 250, 61, 16))
        self.Guess12inpt.setText("")
        self.Guess12inpt.setObjectName("Guess12inpt")
        self.Results_guess_13 = QtWidgets.QLabel(self.groupBox)
        self.Results_guess_13.setGeometry(QtCore.QRect(190, 270, 55, 16))
        self.Results_guess_13.setText("")
        self.Results_guess_13.setObjectName("Results_guess_13")
        self.Guess13inpt = QtWidgets.QLabel(self.groupBox)
        self.Guess13inpt.setGeometry(QtCore.QRect(100, 270, 61, 16))
        self.Guess13inpt.setText("")
        self.Guess13inpt.setObjectName("Guess13inpt")
        self.Results_guess_14 = QtWidgets.QLabel(self.groupBox)
        self.Results_guess_14.setGeometry(QtCore.QRect(190, 290, 55, 16))
        self.Results_guess_14.setText("")
        self.Results_guess_14.setObjectName("Results_guess_14")
        self.Guess14inpt = QtWidgets.QLabel(self.groupBox)
        self.Guess14inpt.setGeometry(QtCore.QRect(100, 290, 61, 16))
        self.Guess14inpt.setText("")
        self.Guess14inpt.setObjectName("Guess14inpt")
        self.Results_guess_15 = QtWidgets.QLabel(self.groupBox)
        self.Results_guess_15.setGeometry(QtCore.QRect(190, 310, 55, 16))
        self.Results_guess_15.setText("")
        self.Results_guess_15.setObjectName("Results_guess_15")
        self.Guess15inpt = QtWidgets.QLabel(self.groupBox)
        self.Guess15inpt.setGeometry(QtCore.QRect(100, 310, 61, 16))
        self.Guess15inpt.setText("")
        self.Guess15inpt.setObjectName("Guess15inpt")
        self.Results_guess_1 = QtWidgets.QLabel(self.groupBox)
        self.Results_guess_1.setGeometry(QtCore.QRect(190, 30, 55, 16))
        self.Results_guess_1.setText("")
        self.Results_guess_1.setObjectName("Results_guess_1")
        self.Results_guess_8 = QtWidgets.QLabel(self.groupBox)
        self.Results_guess_8.setGeometry(QtCore.QRect(190, 170, 55, 16))
        self.Results_guess_8.setText("")
        self.Results_guess_8.setObjectName("Results_guess_8")
        self.Results_guess_5 = QtWidgets.QLabel(self.groupBox)
        self.Results_guess_5.setGeometry(QtCore.QRect(190, 110, 55, 16))
        self.Results_guess_5.setText("")
        self.Results_guess_5.setObjectName("Results_guess_5")
        self.input_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.input_1.setGeometry(QtCore.QRect(380, 250, 71, 41))
        self.input_1.setMaximum(10)
        self.input_1.setObjectName("input_1")
        self.input_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.input_2.setGeometry(QtCore.QRect(470, 250, 71, 41))
        self.input_2.setMaximum(10)
        self.input_2.setObjectName("input_2")
        self.input_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.input_3.setGeometry(QtCore.QRect(560, 250, 71, 41))
        self.input_3.setMaximum(10)
        self.input_3.setObjectName("input_3")
        self.input_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.input_4.setGeometry(QtCore.QRect(650, 250, 71, 41))
        self.input_4.setMaximum(10)
        self.input_4.setObjectName("input_4")
        self.Result_Output = QtWidgets.QLabel(self.centralwidget)
        self.Result_Output.setGeometry(QtCore.QRect(420, 430, 131, 51))
        self.Result_Output.setObjectName("Result_Output")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 330, 201, 51))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 130, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 170, 341, 21))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Game = QtWidgets.QAction(MainWindow)
        self.actionNew_Game.setObjectName("actionNew_Game")

        self.pushButton.clicked.connect(self.Test_Input)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "Mastermind!"))
        self.groupBox.setTitle(_translate("MainWindow", "Guess History"))
        self.Guess1_label.setText(_translate("MainWindow", "Guess 1"))
        self.Guess2_label.setText(_translate("MainWindow", "Guess 2"))
        self.Guess3_label.setText(_translate("MainWindow", "Guess 3"))
        self.Guess4_label.setText(_translate("MainWindow", "Guess 4"))
        self.Guess5_label.setText(_translate("MainWindow", "Guess 5"))
        self.Guess6_label.setText(_translate("MainWindow", "Guess 6"))
        self.Guess7_label.setText(_translate("MainWindow", "Guess 7"))
        self.Guess8_label.setText(_translate("MainWindow", "Guess 8"))
        self.Guess9_label.setText(_translate("MainWindow", "Guess 9"))
        self.Guess10_label.setText(_translate("MainWindow", "Guess 10"))
        self.Guess11_label.setText(_translate("MainWindow", "Guess 11"))
        self.Guess12_label.setText(_translate("MainWindow", "Guess 12"))
        self.Guess13_label.setText(_translate("MainWindow", "Guess 13"))
        self.Guess14_label.setText(_translate("MainWindow", "Guess 14"))
        self.Guess15_label.setText(_translate("MainWindow", "Guess 15"))
        self.Result_Output.setText(_translate("MainWindow", "Result"))
        self.pushButton.setText(_translate("MainWindow", "Submit!"))
        self.label.setText(_translate("MainWindow", "A random 4 digit code has been created! "))
        self.label_2.setText(_translate("MainWindow", "Put 4 numbers in the boxes bellow and read the result!! "))
        self.actionNew_Game.setText(_translate("MainWindow", "New Game"))
        self.actionNew_Game.setStatusTip(_translate("MainWindow", "Start a new game?"))
        self.actionNew_Game.setShortcut(_translate("MainWindow", "Ctrl+N"))

    def Test_Input(self):
        pos_1 = int(self.input_1.value())
        pos_2 = int(self.input_2.value())
        pos_3 = int(self.input_3.value())
        pos_4 = int(self.input_4.value())
        ans_1 = self.ans[0]
        ans_2 = self.ans[1]
        ans_3 = self.ans[2]
        ans_4 = self.ans[3]
        self.numcorrect = 0
        self.poscorrect = 0
        self.user_input = [pos_1, pos_2, pos_3, pos_4]
        self.guess = str(self.input_1.value()) + str(self.input_2.value()) + str(self.input_3.value()) + str(self.input_4.value())
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

        if self.guessnum == 1:
            self.Results_guess_1.setText(str(self.numcorrect) + ' #|' + str(self.poscorrect) + ' Pos')
            self.Results_guess_1.adjustSize()
        if self.guessnum == 2:
            self.Results_guess_2.setText(str(self.numcorrect) + ' #|' + str(self.poscorrect) + ' Pos')
            self.Results_guess_2.adjustSize()
        if self.guessnum == 3:
            self.Results_guess_3.setText(str(self.numcorrect) + ' #|' + str(self.poscorrect) + ' Pos')
            self.Results_guess_3.adjustSize()
        if self.guessnum == 4:
            self.Results_guess_4.setText(str(self.numcorrect) + ' #|' + str(self.poscorrect) + ' Pos')
            self.Results_guess_4.adjustSize()
        if self.guessnum == 5:
            self.Results_guess_5.setText(str(self.numcorrect) + ' #|' + str(self.poscorrect) + ' Pos')
            self.Results_guess_5.adjustSize()
        if self.guessnum == 6:
            self.Results_guess_6.setText(str(self.numcorrect) + ' #|' + str(self.poscorrect) + ' Pos')
            self.Results_guess_6.adjustSize()
        if self.guessnum == 7:
            self.Results_guess_7.setText(str(self.numcorrect) + ' #|' + str(self.poscorrect) + ' Pos')
            self.Results_guess_7.adjustSize()
        if self.guessnum == 8:
            self.Results_guess_8.setText(str(self.numcorrect) + ' #|' + str(self.poscorrect) + ' Pos')
            self.Results_guess_8.adjustSize()
        if self.guessnum == 9:
            self.Results_guess_9.setText(str(self.numcorrect) + ' #|' + str(self.poscorrect) + ' Pos')
            self.Results_guess_9.adjustSize()
        if self.guessnum == 10:
            self.Results_guess_10.setText(str(self.numcorrect) + ' #|' + str(self.poscorrect) + ' Pos')
            self.Results_guess_10.adjustSize()
        if self.guessnum == 11:
            self.Results_guess_11.setText(str(self.numcorrect) + ' #|' + str(self.poscorrect) + ' Pos')
            self.Results_guess_11.adjustSize()
        if self.guessnum == 12:
            self.Results_guess_12.setText(str(self.numcorrect) + ' #|' + str(self.poscorrect) + ' Pos')
            self.Results_guess_12.adjustSize()
        if self.guessnum == 13:
            self.Results_guess_13.setText(str(self.numcorrect) + ' #|' + str(self.poscorrect) + ' Pos')
            self.Results_guess_13.adjustSize()
        if self.guessnum == 14:
            self.Results_guess_14.setText(str(self.numcorrect) + ' #|' + str(self.poscorrect) + ' Pos')
            self.Results_guess_14.adjustSize()
        if self.guessnum == 15:
            self.Results_guess_15.setText(str(self.numcorrect) + ' #|' + str(self.poscorrect) + ' Pos')
            self.Results_guess_15.adjustSize()

        if self.guessnum == 1:
            self.Guess1inpt.setText(str(self.guess))
        if self.guessnum == 2:
            self.Guess2inpt.setText(str(self.guess))
        if self.guessnum == 3:
            self.Guess3inpt.setText(str(self.guess))
        if self.guessnum == 4:
            self.Guess4inpt.setText(str(self.guess))
        if self.guessnum == 5:
            self.Guess5inpt.setText(str(self.guess))
        if self.guessnum == 6:
            self.Guess6inpt.setText(str(self.guess))
        if self.guessnum == 7:
            self.Guess7inpt.setText(str(self.guess))
        if self.guessnum == 8:
            self.Guess8inpt.setText(str(self.guess))
        if self.guessnum == 9:
            self.Guess9inpt.setText(str(self.guess))
        if self.guessnum == 10:
            self.Guess10inpt.setText(str(self.guess))
        if self.guessnum == 11:
            self.Guess11inpt.setText(str(self.guess))
        if self.guessnum == 12:
            self.Guess12inpt.setText(str(self.guess))
        if self.guessnum == 13:
            self.Guess13inpt.setText(str(self.guess))
        if self.guessnum == 14:
            self.Guess14inpt.setText(str(self.guess))
        if self.guessnum == 15:
            self.Guess15inpt.setText(str(self.guess))

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
