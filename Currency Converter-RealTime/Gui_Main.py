from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import data
import time as tm
class Ui_MainWindow(object):
    
    def setupUi(self,MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(925, 346)
        MainWindow.setWindowIcon(QtGui.QIcon("cc.png"))
        font = QtGui.QFont()
        font.setPointSize(18)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:rgb(173, 173, 173)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.UpdateprogressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.UpdateprogressBar.setGeometry(QtCore.QRect(560, 270, 118, 31))
        self.UpdateprogressBar.setProperty("value", 0)
        self.UpdateprogressBar.setObjectName("UpdateprogressBar")
        self.From = QtWidgets.QLabel(self.centralwidget)
        self.From.setGeometry(QtCore.QRect(0, 10, 111, 51))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(24)
        self.From.setFont(font)
        self.From.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.From.setStyleSheet("color:rgb(24, 155, 255)")
        self.From.setAlignment(QtCore.Qt.AlignCenter)
        self.From.setObjectName("From")
        self.To = QtWidgets.QLabel(self.centralwidget)
        self.To.setGeometry(QtCore.QRect(10, 70, 91, 41))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(24)
        self.To.setFont(font)
        self.To.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.To.setStyleSheet("color:rgb(92, 255, 157)")
        self.To.setAlignment(QtCore.Qt.AlignCenter)
        self.To.setObjectName("To")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 130, 511, 51))

        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.radioButtondot1 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtondot1.setGeometry(QtCore.QRect(40, 20, 91, 21))
   
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButtondot1.setFont(font)
        self.radioButtondot1.setObjectName("radioButtondot1")
        self.radioButtondot1.toggled.connect(self.radioBtn1)

        self.radioButton1000 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton1000.setGeometry(QtCore.QRect(220, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton1000.setFont(font)
        self.radioButton1000.setObjectName("radioButton1000")
        self.radioButton1000.toggled.connect(self.radioBtn1k)
        
        self.radioButton1M = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton1M.setGeometry(QtCore.QRect(400, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton1M.setFont(font)
        self.radioButton1M.setObjectName("radioButton1M")
        self.radioButton1M.toggled.connect(self.radioBtn1M)

        self.getlabel = QtWidgets.QLabel(self.centralwidget)
        self.getlabel.setGeometry(QtCore.QRect(50, 210, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Harrington")
        font.setPointSize(30)
        self.getlabel.setFont(font)
        self.getlabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.getlabel.setStyleSheet("color:rgb(249, 197, 5)")
        self.getlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.getlabel.setObjectName("getlabel")
        self.getAmount = QtWidgets.QLabel(self.centralwidget)
        self.getAmount.setGeometry(QtCore.QRect(180, 210, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(26)
        self.getAmount.setFont(font)
        self.getAmount.setStyleSheet("color:rgb(249, 197, 5)")
        self.getAmount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.getAmount.setObjectName("getAmount")
        self.getAmountUnit = QtWidgets.QLabel(self.centralwidget)
        self.getAmountUnit.setGeometry(QtCore.QRect(460, 210, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(26)
        self.getAmountUnit.setFont(font)
        self.getAmountUnit.setStyleSheet("color:rgb(249, 197, 5)")
        self.getAmountUnit.setAlignment(QtCore.Qt.AlignCenter)
        self.getAmountUnit.setObjectName("getAmountUnit")
        self.receive_time = QtWidgets.QLabel(self.centralwidget)
        self.receive_time.setGeometry(QtCore.QRect(50, 270, 411, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.receive_time.setFont(font)
        self.receive_time.setObjectName("receive_time")
        self.label_latest = QtWidgets.QLabel(self.centralwidget)
        self.label_latest.setGeometry(QtCore.QRect(480, 270, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_latest.setFont(font)
        self.label_latest.setStyleSheet("color:rgb(255, 18, 1)")
        self.label_latest.setObjectName("label_latest")
        self.label_latest.setVisible(False)
        self.reverse = QtWidgets.QPushButton(self.centralwidget)
        self.reverse.setGeometry(QtCore.QRect(390, 10, 111, 111))
        self.reverse.setStyleSheet("border-color: black;\n"
"background-color:white;\n"
"  border-width: 3px;        \n"
"  border-style: solid;\n"
"  border-radius: 25px;\n"
"  margin:30px;\n"
"  padding:30px;")
        self.reverse.setIcon(QtGui.QIcon("reverse.png"))
        self.reverse.setObjectName("reverse")
        self.reverse.clicked.connect(self.doReverse)
        self.convert = QtWidgets.QPushButton(self.centralwidget)
        self.convert.setGeometry(QtCore.QRect(690, 150, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Pristina")
        font.setPointSize(35)
        font.setKerning(True)
        self.convert.setFont(font)
        self.convert.setStyleSheet("background-color: orange;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.convert.setObjectName("convert")        
        self.convert.clicked.connect(self.doConvert)

        self.update = QtWidgets.QPushButton(self.centralwidget)
        self.update.setGeometry(QtCore.QRect(740, 240, 141, 51))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.update.setFont(font)
        self.update.setStyleSheet("background-color: brown;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"color:white")
        self.update.setObjectName("update")
        self.update.clicked.connect(self.doUpdation)
        self.Fromcombo = QtWidgets.QComboBox(self.centralwidget)
        self.Fromcombo.setGeometry(QtCore.QRect(110, 20, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(12)
        self.Fromcombo.setFont(font)
        self.Fromcombo.setStyleSheet("background-color:white;\n")
        self.Fromcombo.setObjectName("Fromcombo")   
        self.Tocombo = QtWidgets.QComboBox(self.centralwidget)
        self.Tocombo.setGeometry(QtCore.QRect(110, 70, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(12)
        self.Tocombo.setFont(font)
        self.Tocombo.setStyleSheet("background-color:white;\n")
        self.Tocombo.setObjectName("Tocombo")
        self.Fromcombo.clear()    
        self.Tocombo.clear()
        global Ccodej
        for k,v in Ccodej.items():
            self.Fromcombo.addItem(str(k)+"--"+str(v))     
            self.Tocombo.addItem(str(k)+"--"+str(v))

        self.Input = QtWidgets.QLabel(self.centralwidget)
        self.Input.setGeometry(QtCore.QRect(540, -10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(21)
        self.Input.setFont(font)
        self.Input.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Input.setStyleSheet("color:rgb(24, 155, 255)")
        self.Input.setAlignment(QtCore.Qt.AlignCenter)
        self.Input.setObjectName("Input")
        self.Inputbox=QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Inputbox.setGeometry(QtCore.QRect(550, 41, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(24)
        self.Inputbox.setFont(font)
        self.Inputbox.setStyleSheet("background-color:white;\n")
        self.Inputbox.setRange(0,1000000000000)
        self.Inputbox.setObjectName("Inputbox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 925, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Currency-Converter"))
        self.From.setText(_translate("MainWindow", "From"))
        self.To.setText(_translate("MainWindow", "To"))
        self.groupBox.setTitle(_translate("MainWindow", "Multiple"))
        self.radioButtondot1.setText(_translate("MainWindow", "1.0"))
        self.radioButton1000.setText(_translate("MainWindow", "x1000"))
        self.radioButton1M.setText(_translate("MainWindow", "x1M"))
        self.getlabel.setText(_translate("MainWindow", "Get"))
        self.getAmount.setText(_translate("MainWindow", "0.0"))
        self.getAmountUnit.setText(_translate("MainWindow", "***"))
        global Cjson, time
        timestamp = Cjson['timestamp']
        date_time = datetime.fromtimestamp(timestamp)
        time=date_time.strftime("%m/%d/%Y, %H:%M:%S")
        self.receive_time.setText(_translate("MainWindow", "Data Received At: "+time))
        self.label_latest.setText(_translate("MainWindow", "Latest!"))
        self.convert.setText(_translate("MainWindow", "Convert!"))
        self.update.setText(_translate("MainWindow", "Update"))
        self.Fromcombo.setItemText(0, _translate("MainWindow", ""))
        self.Fromcombo.setItemText(1, _translate("MainWindow", ""))
        self.Tocombo.setItemText(0, _translate("MainWindow", ""))
        self.Tocombo.setItemText(1, _translate("MainWindow", ""))
        self.Input.setText(_translate("MainWindow", "Amount:"))
        self.Inputbox.setAlignment(QtCore.Qt.AlignRight)
        
    def doConvert(self):
            if self.Fromcombo.currentText()=="" or self.Tocombo.currentText()=="" or self.Inputbox.value==0.0:
                return False           
            global Cjson
            global rate
            a=False#From
            b=False#To
            fromb=self.Fromcombo.currentText()[0:3]
            tob=self.Tocombo.currentText()[0:3]
            for k,v in Cjson['rates'].items():
                if fromb==str(k):
                    a=v
                if tob==str(k) :
                    b=v
                if a!=False and b!=False:
                    break
            rate=b/a
            print(rate)
            print(str(round((float(self.Inputbox.value())*rate),2)))
            self.getAmount.setText(str(round((float(self.Inputbox.value())*rate),2)))
            self.getAmountUnit.setText(self.Tocombo.currentText()[0:3])

    def radioBtn1k(self):
        self.Inputbox.setValue(self.Inputbox.value()*1000)
    def radioBtn1M(self):
        self.Inputbox.setValue(self.Inputbox.value()*1000000)    
    def radioBtn1(self):
        self.Inputbox.setValue(1.0)
    def doReverse(self):
        ftext=self.Fromcombo.currentText()
        ttext=self.Tocombo.currentText()
        self.Fromcombo.setCurrentText(ttext)
        self.Tocombo.setCurrentText(ftext)
    def doUpdation(self):
        global Cjson,time
        Cjson=data.Data.getCurrencyJson()
        timestamp = Cjson['timestamp']
        date_time = datetime.fromtimestamp(timestamp)
        time=date_time.strftime("%m/%d/%Y, %H:%M:%S")
        self.receive_time.setText("Data Received At: "+time)
        self.label_latest.setVisible(True)
        QtCore.QTimer.singleShot(3000, self.onTimeout)
    def onTimeout(self):
        self.label_latest.setVisible(False)
    def groupB(self):
        if self.rdbGroup.buttons(1).isChecked():
            self.Inputbox.setValue(1.00)      
        if self.rdbGroup.buttons(2).isChecked():
            value=self.Inputbox.value()*1000
            self.Inputbox.setValue(round(value,2))
        if self.rdbGroup.buttons(3).isChecked():
            value=self.Inputbox.value()*1000000
            self.Inputbox.setValue(round(value,2))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    splash_pix = QtGui.QPixmap('splash.png')
    splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.show();
    QtCore.QTimer.singleShot(3000,splash.close)
    
    Cjson=data.Data.getCurrencyJson()
    Ccodej=data.Data.getCurrencyCodeJson()
    if  'CNH' in Ccodej:
        Ccodej.pop('CNH')
    rate=0
    time=0
    tm.sleep(3.5)
    MainWindow = QtWidgets.QMainWindow()       
    ui = Ui_MainWindow() 
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
