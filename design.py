# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Htran = QtWidgets.QLabel(self.centralwidget)
        self.Htran.setGeometry(QtCore.QRect(290, 70, 16, 16))
        self.Htran.setObjectName("Htran")
        self.Vtran = QtWidgets.QLabel(self.centralwidget)
        self.Vtran.setGeometry(QtCore.QRect(290, 110, 16, 16))
        self.Vtran.setObjectName("Vtran")
        self.Mtran = QtWidgets.QLabel(self.centralwidget)
        self.Mtran.setGeometry(QtCore.QRect(290, 180, 16, 16))
        self.Mtran.setObjectName("Mtran")
        self.Ptran = QtWidgets.QLabel(self.centralwidget)
        self.Ptran.setGeometry(QtCore.QRect(290, 140, 16, 16))
        self.Ptran.setObjectName("Ptran")
        self.Hrec = QtWidgets.QLabel(self.centralwidget)
        self.Hrec.setGeometry(QtCore.QRect(340, 40, 16, 16))
        self.Hrec.setObjectName("Hrec")
        self.Mrec = QtWidgets.QLabel(self.centralwidget)
        self.Mrec.setGeometry(QtCore.QRect(580, 40, 16, 16))
        self.Mrec.setObjectName("Mrec")
        self.Prec = QtWidgets.QLabel(self.centralwidget)
        self.Prec.setGeometry(QtCore.QRect(510, 40, 16, 16))
        self.Prec.setObjectName("Prec")
        self.Vrec = QtWidgets.QLabel(self.centralwidget)
        self.Vrec.setGeometry(QtCore.QRect(430, 40, 16, 16))
        self.Vrec.setObjectName("Vrec")
        self.calculate = QtWidgets.QPushButton(self.centralwidget)
        self.calculate.setGeometry(QtCore.QRect(70, 500, 151, 51))
        self.calculate.setObjectName("calculate")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 50, 59, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 140, 59, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 100, 59, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 180, 59, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 230, 59, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 290, 59, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(178, 120, 91, 20))
        self.label_15.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_15.setObjectName("label_15")
        self.T = QtWidgets.QLabel(self.centralwidget)
        self.T.setGeometry(QtCore.QRect(80, 380, 21, 16))
        self.T.setObjectName("T")
        self.S0R = QtWidgets.QLineEdit(self.centralwidget)
        self.S0R.setGeometry(QtCore.QRect(100, 50, 71, 21))
        self.S0R.setObjectName("S0R")
        self.HH = QtWidgets.QLineEdit(self.centralwidget)
        self.HH.setGeometry(QtCore.QRect(310, 60, 71, 31))
        self.HH.setObjectName("HH")
        self.VH = QtWidgets.QLineEdit(self.centralwidget)
        self.VH.setGeometry(QtCore.QRect(310, 100, 71, 31))
        self.VH.setObjectName("VH")
        self.PH = QtWidgets.QLineEdit(self.centralwidget)
        self.PH.setGeometry(QtCore.QRect(310, 140, 71, 31))
        self.PH.setObjectName("PH")
        self.MH = QtWidgets.QLineEdit(self.centralwidget)
        self.MH.setGeometry(QtCore.QRect(310, 180, 71, 31))
        self.MH.setObjectName("MH")
        self.HV = QtWidgets.QLineEdit(self.centralwidget)
        self.HV.setGeometry(QtCore.QRect(390, 60, 71, 31))
        self.HV.setObjectName("HV")
        self.VV = QtWidgets.QLineEdit(self.centralwidget)
        self.VV.setGeometry(QtCore.QRect(390, 100, 71, 31))
        self.VV.setObjectName("VV")
        self.PV = QtWidgets.QLineEdit(self.centralwidget)
        self.PV.setGeometry(QtCore.QRect(390, 140, 71, 31))
        self.PV.setObjectName("PV")
        self.MV = QtWidgets.QLineEdit(self.centralwidget)
        self.MV.setGeometry(QtCore.QRect(390, 180, 71, 31))
        self.MV.setObjectName("MV")
        self.HP = QtWidgets.QLineEdit(self.centralwidget)
        self.HP.setGeometry(QtCore.QRect(470, 60, 71, 31))
        self.HP.setObjectName("HP")
        self.VP = QtWidgets.QLineEdit(self.centralwidget)
        self.VP.setGeometry(QtCore.QRect(470, 100, 71, 31))
        self.VP.setObjectName("VP")
        self.PP = QtWidgets.QLineEdit(self.centralwidget)
        self.PP.setGeometry(QtCore.QRect(470, 140, 71, 31))
        self.PP.setObjectName("PP")
        self.MP = QtWidgets.QLineEdit(self.centralwidget)
        self.MP.setGeometry(QtCore.QRect(470, 180, 71, 31))
        self.MP.setObjectName("MP")
        self.HM = QtWidgets.QLineEdit(self.centralwidget)
        self.HM.setGeometry(QtCore.QRect(550, 60, 71, 31))
        self.HM.setObjectName("HM")
        self.VM = QtWidgets.QLineEdit(self.centralwidget)
        self.VM.setGeometry(QtCore.QRect(550, 100, 71, 31))
        self.VM.setObjectName("VM")
        self.PM = QtWidgets.QLineEdit(self.centralwidget)
        self.PM.setGeometry(QtCore.QRect(550, 140, 71, 31))
        self.PM.setObjectName("PM")
        self.MM = QtWidgets.QLineEdit(self.centralwidget)
        self.MM.setGeometry(QtCore.QRect(550, 180, 71, 31))
        self.MM.setObjectName("MM")
        self.S0H = QtWidgets.QLineEdit(self.centralwidget)
        self.S0H.setGeometry(QtCore.QRect(100, 290, 71, 21))
        self.S0H.setObjectName("S0H")
        self.S0V = QtWidgets.QLineEdit(self.centralwidget)
        self.S0V.setGeometry(QtCore.QRect(100, 230, 71, 21))
        self.S0V.setObjectName("S0V")
        self.S0P = QtWidgets.QLineEdit(self.centralwidget)
        self.S0P.setGeometry(QtCore.QRect(100, 180, 71, 21))
        self.S0P.setObjectName("S0P")
        self.S0M = QtWidgets.QLineEdit(self.centralwidget)
        self.S0M.setGeometry(QtCore.QRect(100, 140, 71, 21))
        self.S0M.setObjectName("S0M")
        self.S0L = QtWidgets.QLineEdit(self.centralwidget)
        self.S0L.setGeometry(QtCore.QRect(100, 100, 71, 21))
        self.S0L.setObjectName("S0L")
        self.PL = QtWidgets.QLineEdit(self.centralwidget)
        self.PL.setGeometry(QtCore.QRect(630, 140, 71, 31))
        self.PL.setObjectName("PL")
        self.VL = QtWidgets.QLineEdit(self.centralwidget)
        self.VL.setGeometry(QtCore.QRect(630, 100, 71, 31))
        self.VL.setObjectName("VL")
        self.ML = QtWidgets.QLineEdit(self.centralwidget)
        self.ML.setGeometry(QtCore.QRect(630, 180, 71, 31))
        self.ML.setObjectName("ML")
        self.HL = QtWidgets.QLineEdit(self.centralwidget)
        self.HL.setGeometry(QtCore.QRect(630, 60, 71, 31))
        self.HL.setObjectName("HL")
        self.PR = QtWidgets.QLineEdit(self.centralwidget)
        self.PR.setGeometry(QtCore.QRect(710, 140, 71, 31))
        self.PR.setObjectName("PR")
        self.VR = QtWidgets.QLineEdit(self.centralwidget)
        self.VR.setGeometry(QtCore.QRect(710, 100, 71, 31))
        self.VR.setObjectName("VR")
        self.MR = QtWidgets.QLineEdit(self.centralwidget)
        self.MR.setGeometry(QtCore.QRect(710, 180, 71, 31))
        self.MR.setObjectName("MR")
        self.HR = QtWidgets.QLineEdit(self.centralwidget)
        self.HR.setGeometry(QtCore.QRect(710, 60, 71, 31))
        self.HR.setObjectName("HR")
        self.LR = QtWidgets.QLineEdit(self.centralwidget)
        self.LR.setGeometry(QtCore.QRect(710, 220, 71, 31))
        self.LR.setObjectName("LR")
        self.LH = QtWidgets.QLineEdit(self.centralwidget)
        self.LH.setGeometry(QtCore.QRect(310, 220, 71, 31))
        self.LH.setObjectName("LH")
        self.LV = QtWidgets.QLineEdit(self.centralwidget)
        self.LV.setGeometry(QtCore.QRect(390, 220, 71, 31))
        self.LV.setObjectName("LV")
        self.LM = QtWidgets.QLineEdit(self.centralwidget)
        self.LM.setGeometry(QtCore.QRect(550, 220, 71, 31))
        self.LM.setObjectName("LM")
        self.LL = QtWidgets.QLineEdit(self.centralwidget)
        self.LL.setGeometry(QtCore.QRect(630, 220, 71, 31))
        self.LL.setObjectName("LL")
        self.LP = QtWidgets.QLineEdit(self.centralwidget)
        self.LP.setGeometry(QtCore.QRect(470, 220, 71, 31))
        self.LP.setObjectName("LP")
        self.RR = QtWidgets.QLineEdit(self.centralwidget)
        self.RR.setGeometry(QtCore.QRect(710, 260, 71, 31))
        self.RR.setObjectName("RR")
        self.RH = QtWidgets.QLineEdit(self.centralwidget)
        self.RH.setGeometry(QtCore.QRect(310, 260, 71, 31))
        self.RH.setObjectName("RH")
        self.RV = QtWidgets.QLineEdit(self.centralwidget)
        self.RV.setGeometry(QtCore.QRect(390, 260, 71, 31))
        self.RV.setObjectName("RV")
        self.RM = QtWidgets.QLineEdit(self.centralwidget)
        self.RM.setGeometry(QtCore.QRect(550, 260, 71, 31))
        self.RM.setObjectName("RM")
        self.RL = QtWidgets.QLineEdit(self.centralwidget)
        self.RL.setGeometry(QtCore.QRect(630, 260, 71, 31))
        self.RL.setObjectName("RL")
        self.RP = QtWidgets.QLineEdit(self.centralwidget)
        self.RP.setGeometry(QtCore.QRect(470, 260, 71, 31))
        self.RP.setObjectName("RP")
        self.Ltrans = QtWidgets.QLabel(self.centralwidget)
        self.Ltrans.setGeometry(QtCore.QRect(290, 220, 16, 16))
        self.Ltrans.setObjectName("Ltrans")
        self.Rtrans = QtWidgets.QLabel(self.centralwidget)
        self.Rtrans.setGeometry(QtCore.QRect(290, 270, 16, 16))
        self.Rtrans.setObjectName("Rtrans")
        self.Lrec = QtWidgets.QLabel(self.centralwidget)
        self.Lrec.setGeometry(QtCore.QRect(660, 40, 16, 16))
        self.Lrec.setObjectName("Lrec")
        self.Rrec = QtWidgets.QLabel(self.centralwidget)
        self.Rrec.setGeometry(QtCore.QRect(740, 40, 16, 16))
        self.Rrec.setObjectName("Rrec")
        self.m00 = QtWidgets.QLabel(self.centralwidget)
        self.m00.setGeometry(QtCore.QRect(460, 390, 51, 31))
        self.m00.setFrameShape(QtWidgets.QFrame.Box)
        self.m00.setFrameShadow(QtWidgets.QFrame.Plain)
        self.m00.setLineWidth(2)
        self.m00.setText("")
        self.m00.setObjectName("m00")
        self.m01 = QtWidgets.QLabel(self.centralwidget)
        self.m01.setGeometry(QtCore.QRect(510, 390, 51, 31))
        self.m01.setFrameShape(QtWidgets.QFrame.Box)
        self.m01.setFrameShadow(QtWidgets.QFrame.Plain)
        self.m01.setLineWidth(2)
        self.m01.setText("")
        self.m01.setObjectName("m01")
        self.m02 = QtWidgets.QLabel(self.centralwidget)
        self.m02.setGeometry(QtCore.QRect(560, 390, 51, 31))
        self.m02.setFrameShape(QtWidgets.QFrame.Box)
        self.m02.setFrameShadow(QtWidgets.QFrame.Plain)
        self.m02.setLineWidth(2)
        self.m02.setText("")
        self.m02.setObjectName("m02")
        self.m03 = QtWidgets.QLabel(self.centralwidget)
        self.m03.setGeometry(QtCore.QRect(610, 390, 51, 31))
        self.m03.setFrameShape(QtWidgets.QFrame.Box)
        self.m03.setFrameShadow(QtWidgets.QFrame.Plain)
        self.m03.setLineWidth(2)
        self.m03.setText("")
        self.m03.setObjectName("m03")
        self.m12 = QtWidgets.QLabel(self.centralwidget)
        self.m12.setGeometry(QtCore.QRect(560, 420, 51, 31))
        self.m12.setFrameShape(QtWidgets.QFrame.Box)
        self.m12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.m12.setLineWidth(2)
        self.m12.setText("")
        self.m12.setObjectName("m12")
        self.m11 = QtWidgets.QLabel(self.centralwidget)
        self.m11.setGeometry(QtCore.QRect(510, 420, 51, 31))
        self.m11.setFrameShape(QtWidgets.QFrame.Box)
        self.m11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.m11.setLineWidth(2)
        self.m11.setText("")
        self.m11.setObjectName("m11")
        self.m10 = QtWidgets.QLabel(self.centralwidget)
        self.m10.setGeometry(QtCore.QRect(460, 420, 51, 31))
        self.m10.setFrameShape(QtWidgets.QFrame.Box)
        self.m10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.m10.setLineWidth(2)
        self.m10.setText("")
        self.m10.setObjectName("m10")
        self.m13 = QtWidgets.QLabel(self.centralwidget)
        self.m13.setGeometry(QtCore.QRect(610, 420, 51, 31))
        self.m13.setFrameShape(QtWidgets.QFrame.Box)
        self.m13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.m13.setLineWidth(2)
        self.m13.setText("")
        self.m13.setObjectName("m13")
        self.m22 = QtWidgets.QLabel(self.centralwidget)
        self.m22.setGeometry(QtCore.QRect(560, 450, 51, 31))
        self.m22.setFrameShape(QtWidgets.QFrame.Box)
        self.m22.setFrameShadow(QtWidgets.QFrame.Plain)
        self.m22.setLineWidth(2)
        self.m22.setText("")
        self.m22.setObjectName("m22")
        self.m21 = QtWidgets.QLabel(self.centralwidget)
        self.m21.setGeometry(QtCore.QRect(510, 450, 51, 31))
        self.m21.setFrameShape(QtWidgets.QFrame.Box)
        self.m21.setFrameShadow(QtWidgets.QFrame.Plain)
        self.m21.setLineWidth(2)
        self.m21.setText("")
        self.m21.setObjectName("m21")
        self.m20 = QtWidgets.QLabel(self.centralwidget)
        self.m20.setGeometry(QtCore.QRect(460, 450, 51, 31))
        self.m20.setFrameShape(QtWidgets.QFrame.Box)
        self.m20.setFrameShadow(QtWidgets.QFrame.Plain)
        self.m20.setLineWidth(2)
        self.m20.setText("")
        self.m20.setObjectName("m20")
        self.m23 = QtWidgets.QLabel(self.centralwidget)
        self.m23.setGeometry(QtCore.QRect(610, 450, 51, 31))
        self.m23.setFrameShape(QtWidgets.QFrame.Box)
        self.m23.setFrameShadow(QtWidgets.QFrame.Plain)
        self.m23.setLineWidth(2)
        self.m23.setText("")
        self.m23.setObjectName("m23")
        self.m32 = QtWidgets.QLabel(self.centralwidget)
        self.m32.setGeometry(QtCore.QRect(560, 480, 51, 31))
        self.m32.setFrameShape(QtWidgets.QFrame.Box)
        self.m32.setFrameShadow(QtWidgets.QFrame.Plain)
        self.m32.setLineWidth(2)
        self.m32.setText("")
        self.m32.setObjectName("m32")
        self.m31 = QtWidgets.QLabel(self.centralwidget)
        self.m31.setGeometry(QtCore.QRect(510, 480, 51, 31))
        self.m31.setFrameShape(QtWidgets.QFrame.Box)
        self.m31.setFrameShadow(QtWidgets.QFrame.Plain)
        self.m31.setLineWidth(2)
        self.m31.setText("")
        self.m31.setObjectName("m31")
        self.m30 = QtWidgets.QLabel(self.centralwidget)
        self.m30.setGeometry(QtCore.QRect(460, 480, 51, 31))
        self.m30.setFrameShape(QtWidgets.QFrame.Box)
        self.m30.setFrameShadow(QtWidgets.QFrame.Plain)
        self.m30.setLineWidth(2)
        self.m30.setText("")
        self.m30.setObjectName("m30")
        self.m33 = QtWidgets.QLabel(self.centralwidget)
        self.m33.setGeometry(QtCore.QRect(610, 480, 51, 31))
        self.m33.setFrameShape(QtWidgets.QFrame.Box)
        self.m33.setFrameShadow(QtWidgets.QFrame.Plain)
        self.m33.setLineWidth(2)
        self.m33.setText("")
        self.m33.setObjectName("m33")
        self.TT = QtWidgets.QLineEdit(self.centralwidget)
        self.TT.setGeometry(QtCore.QRect(100, 380, 71, 21))
        self.TT.setObjectName("TT")
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Htran.setText(_translate("MainWindow", "H "))
        self.Vtran.setText(_translate("MainWindow", "V"))
        self.Mtran.setText(_translate("MainWindow", "M"))
        self.Ptran.setText(_translate("MainWindow", "P"))
        self.Hrec.setText(_translate("MainWindow", "H "))
        self.Mrec.setText(_translate("MainWindow", "M"))
        self.Prec.setText(_translate("MainWindow", "P"))
        self.Vrec.setText(_translate("MainWindow", "V"))
        self.calculate.setText(_translate("MainWindow", "Calculate"))
        self.label_9.setText(_translate("MainWindow", "S0R"))
        self.label_10.setText(_translate("MainWindow", "S0M"))
        self.label_11.setText(_translate("MainWindow", "S0L"))
        self.label_12.setText(_translate("MainWindow", "S0P"))
        self.label_13.setText(_translate("MainWindow", "S0V"))
        self.label_14.setText(_translate("MainWindow", "S0H"))
        self.label_15.setText(_translate("MainWindow", "Transmittance"))
        self.T.setText(_translate("MainWindow", "T"))
        self.Ltrans.setText(_translate("MainWindow", "L"))
        self.Rtrans.setText(_translate("MainWindow", "R"))
        self.Lrec.setText(_translate("MainWindow", "L"))
        self.Rrec.setText(_translate("MainWindow", "R"))
