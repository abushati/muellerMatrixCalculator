from PyQt5 import QtGui,QtCore,QtWidgets
import sys
from design import Ui_MainWindow
from calculations import look
from decimal import Decimal


def getInput():
	

	S0H = float(ui.S0H.text())
	S0V = float(ui.S0V.text())
	S0P = float(ui.S0P.text())
	S0M = float(ui.S0M.text())
	S0L = float(ui.S0L.text())
	S0R = float(ui.S0R.text())
	#ValueError: invalid literal for int() with base 10: '1 1' 
	Htrans = [float(ui.HH.text()),float(ui.HV.text()),float(ui.HP.text()),float(ui.HM.text()),float(ui.HL.text()),float(ui.HR.text())]
	HH,HV,HP,HM,HL,HR = normalizeComponents(Htrans, S0H)

	Vtrans = [float(ui.VH.text()),float(ui.VV.text()),float(ui.VP.text()),float(ui.VM.text()),float(ui.VL.text()),float(ui.VR.text())]
	VH,VV,VP,VM,VL,VR  = normalizeComponents(Vtrans, S0V)

	Ptrans = [float(ui.PH.text()),float(ui.PV.text()),float(ui.PP.text()),float(ui.PM.text()),float(ui.PL.text()),float(ui.PR.text())]
	PH,PV,PP,PM,PL,PR = normalizeComponents(Ptrans, S0P)

	Mtrans = [float(ui.MH.text()),float(ui.MV.text()),float(ui.MP.text()),float(ui.MM.text()),float(ui.ML.text()),float(ui.MR.text())]
	MH,MV,MP,MM,ML,MR = normalizeComponents(Mtrans,S0M)

	Ltrans = [float(ui.LH.text()),float(ui.LV.text()),float(ui.LP.text()),float(ui.LM.text()),float(ui.LL.text()),float(ui.LR.text())]
	LH,LV,LP,LM,LL,LR = normalizeComponents(Ltrans,S0L)

	Rtrans = [float(ui.RH.text()),float(ui.RV.text()),float(ui.RP.text()),float(ui.RM.text()),float(ui.RL.text()),float(ui.RR.text())]
	RH,RV,RP,RM,RL,RR = normalizeComponents(Rtrans,S0R)

	listOfComponents = dict(HH =HH,HV=HV,HP=HP,HM=HM,HL=HL,HR=HR,VH=VH,VV=VV,VP=VP,
							VM=VM,VL=VL,VR=VR,PH=PH,PV=PV,PP=PP,PM=PM,PL=PL,PR=PR,
							MH=MH,MV=MV,MP=MP,MM=MM,ML=ML,MR=MR,LH=LH,LV=LV,LP=LP,
							LM=LM,LL=LL,LR=LR,RH=RH,RV=RV,RP=RP,RM=RM,RL=RL,RR=RR)
	dics = look(listOfComponents)
	updated= preOutput(dics)

	outputDic = {}
	print(updated["m00"])
	M00 =updated["m00"]
	for box, value in updated.items():
		outputDic.update({f'{box}':round(Decimal(value/M00),3)})


	output(outputDic)



def normalizeComponents(listTran,normalizer):
	normalizedList = []
	for element in listTran:
		normalizeValue = element/normalizer
		normalizedList.append(normalizeValue)
	return normalizedList

def preOutput(dicsd):
	t = float(ui.TT.text())
	updatedDics = {}
	for key,value in dicsd.items():
		updatedDics.update({f"{key}":float(value)/t})

	return updatedDics

def output(dicsd):

	for box,value in dicsd.items():
		label = gui.findChild(QtWidgets.QLabel,f'{box}')
		label.setText(str(value))

	
	'''
	for keys, values in dics:
		print(f"this the coordinate {keys} and the is the value at that coordinate{values}") 
	'''

	

	

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	gui = QtWidgets.QDialog()
	ui = Ui_MainWindow()
	ui.setupUi(gui)
	ui.calculate.clicked.connect(getInput)
	
	gui.show()
	sys.exit(app.exec_())