# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 750)
        MainWindow.setMinimumSize(QtCore.QSize(300, 750))
        MainWindow.setMaximumSize(QtCore.QSize(300, 750))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 96, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 96, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 96, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 96, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.powerButton = QtWidgets.QPushButton(self.centralwidget)
        self.powerButton.setGeometry(QtCore.QRect(120, 30, 61, 61))
        self.powerButton.setText("")
        self.powerButton.setAutoDefault(False)
        self.powerButton.setFlat(True)
        self.powerButton.setObjectName("powerButton")
        self.channelUp = QtWidgets.QPushButton(self.centralwidget)
        self.channelUp.setGeometry(QtCore.QRect(50, 105, 61, 61))
        self.channelUp.setText("")
        self.channelUp.setFlat(True)
        self.channelUp.setObjectName("channelUp")
        self.channelDown = QtWidgets.QPushButton(self.centralwidget)
        self.channelDown.setGeometry(QtCore.QRect(50, 203, 61, 61))
        self.channelDown.setText("")
        self.channelDown.setFlat(True)
        self.channelDown.setObjectName("channelDown")
        self.volumeUp = QtWidgets.QPushButton(self.centralwidget)
        self.volumeUp.setGeometry(QtCore.QRect(190, 105, 61, 61))
        self.volumeUp.setText("")
        self.volumeUp.setFlat(True)
        self.volumeUp.setObjectName("volumeUp")
        self.volumeDown = QtWidgets.QPushButton(self.centralwidget)
        self.volumeDown.setGeometry(QtCore.QRect(190, 201, 61, 61))
        self.volumeDown.setText("")
        self.volumeDown.setFlat(True)
        self.volumeDown.setObjectName("volumeDown")
        self.channelUpImage = QtWidgets.QLabel(self.centralwidget)
        self.channelUpImage.setGeometry(QtCore.QRect(40, 100, 81, 71))
        self.channelUpImage.setText("")
        self.channelUpImage.setPixmap(QtGui.QPixmap("../Channel Up.png"))
        self.channelUpImage.setScaledContents(True)
        self.channelUpImage.setObjectName("channelUpImage")
        self.volumeUpImage = QtWidgets.QLabel(self.centralwidget)
        self.volumeUpImage.setGeometry(QtCore.QRect(180, 97, 81, 81))
        self.volumeUpImage.setText("")
        self.volumeUpImage.setPixmap(QtGui.QPixmap("../Volume Up Final.png"))
        self.volumeUpImage.setScaledContents(True)
        self.volumeUpImage.setObjectName("volumeUpImage")
        self.volumeDownImage = QtWidgets.QLabel(self.centralwidget)
        self.volumeDownImage.setGeometry(QtCore.QRect(180, 192, 81, 81))
        self.volumeDownImage.setText("")
        self.volumeDownImage.setPixmap(QtGui.QPixmap("../Volume Down Final.png"))
        self.volumeDownImage.setScaledContents(True)
        self.volumeDownImage.setObjectName("volumeDownImage")
        self.powerImage = QtWidgets.QLabel(self.centralwidget)
        self.powerImage.setGeometry(QtCore.QRect(116, 28, 71, 71))
        self.powerImage.setText("")
        self.powerImage.setPixmap(QtGui.QPixmap("../Power Final.png"))
        self.powerImage.setScaledContents(True)
        self.powerImage.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.powerImage.setObjectName("powerImage")
        self.muteButton = QtWidgets.QPushButton(self.centralwidget)
        self.muteButton.setGeometry(QtCore.QRect(123, 320, 61, 61))
        self.muteButton.setText("")
        self.muteButton.setFlat(True)
        self.muteButton.setObjectName("muteButton")
        self.tv_status = QtWidgets.QLabel(self.centralwidget)
        self.tv_status.setGeometry(QtCore.QRect(-20, 487, 341, 241))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tv_status.setPalette(palette)
        self.tv_status.setAutoFillBackground(True)
        self.tv_status.setFrameShape(QtWidgets.QFrame.Box)
        self.tv_status.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tv_status.setLineWidth(3)
        self.tv_status.setText("")
        self.tv_status.setAlignment(QtCore.Qt.AlignCenter)
        self.tv_status.setObjectName("tv_status")
        self.volumeOn = QtWidgets.QLabel(self.centralwidget)
        self.volumeOn.setGeometry(QtCore.QRect(113, 310, 81, 81))
        self.volumeOn.setText("")
        self.volumeOn.setPixmap(QtGui.QPixmap("../Mute Volume Final.png"))
        self.volumeOn.setScaledContents(True)
        self.volumeOn.setObjectName("volumeOn")
        self.volumeOff = QtWidgets.QLabel(self.centralwidget)
        self.volumeOff.setGeometry(QtCore.QRect(113, 310, 81, 81))
        self.volumeOff.setText("")
        self.volumeOff.setPixmap(QtGui.QPixmap("../Muted Final.png"))
        self.volumeOff.setScaledContents(True)
        self.volumeOff.setObjectName("volumeOff")
        self.espnLabel = QtWidgets.QLabel(self.centralwidget)
        self.espnLabel.setGeometry(QtCore.QRect(50, 520, 201, 161))
        self.espnLabel.setText("")
        self.espnLabel.setPixmap(QtGui.QPixmap("../ESPN.jpg"))
        self.espnLabel.setScaledContents(True)
        self.espnLabel.setObjectName("espnLabel")
        self.cnnLabel = QtWidgets.QLabel(self.centralwidget)
        self.cnnLabel.setGeometry(QtCore.QRect(50, 520, 201, 161))
        self.cnnLabel.setText("")
        self.cnnLabel.setPixmap(QtGui.QPixmap("../CNN.jpg"))
        self.cnnLabel.setScaledContents(True)
        self.cnnLabel.setObjectName("cnnLabel")
        self.nickLabel = QtWidgets.QLabel(self.centralwidget)
        self.nickLabel.setGeometry(QtCore.QRect(50, 520, 201, 161))
        self.nickLabel.setText("")
        self.nickLabel.setPixmap(QtGui.QPixmap("../Nick.jpg"))
        self.nickLabel.setScaledContents(True)
        self.nickLabel.setObjectName("nickLabel")
        self.hgtvLabel = QtWidgets.QLabel(self.centralwidget)
        self.hgtvLabel.setGeometry(QtCore.QRect(50, 520, 201, 161))
        self.hgtvLabel.setText("")
        self.hgtvLabel.setPixmap(QtGui.QPixmap("../HGTV.png"))
        self.hgtvLabel.setScaledContents(True)
        self.hgtvLabel.setObjectName("hgtvLabel")
        self.currentChannel = QtWidgets.QLabel(self.centralwidget)
        self.currentChannel.setGeometry(QtCore.QRect(250, 490, 47, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.currentChannel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.currentChannel.setFont(font)
        self.currentChannel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentChannel.setObjectName("currentChannel")
        self.channelDownImage = QtWidgets.QLabel(self.centralwidget)
        self.channelDownImage.setGeometry(QtCore.QRect(40, 200, 81, 71))
        self.channelDownImage.setText("")
        self.channelDownImage.setPixmap(QtGui.QPixmap("../Channel Down Final.png"))
        self.channelDownImage.setScaledContents(True)
        self.channelDownImage.setObjectName("channelDownImage")
        self.volumeDashThree = QtWidgets.QLabel(self.centralwidget)
        self.volumeDashThree.setGeometry(QtCore.QRect(10, 540, 31, 31))
        self.volumeDashThree.setText("")
        self.volumeDashThree.setPixmap(QtGui.QPixmap("../Dash Final.png"))
        self.volumeDashThree.setScaledContents(True)
        self.volumeDashThree.setObjectName("volumeDashThree")
        self.volumeDashTwo = QtWidgets.QLabel(self.centralwidget)
        self.volumeDashTwo.setGeometry(QtCore.QRect(10, 570, 31, 31))
        self.volumeDashTwo.setText("")
        self.volumeDashTwo.setPixmap(QtGui.QPixmap("../Dash Final.png"))
        self.volumeDashTwo.setScaledContents(True)
        self.volumeDashTwo.setObjectName("volumeDashTwo")
        self.volumeDashOne = QtWidgets.QLabel(self.centralwidget)
        self.volumeDashOne.setGeometry(QtCore.QRect(10, 600, 31, 31))
        self.volumeDashOne.setText("")
        self.volumeDashOne.setPixmap(QtGui.QPixmap("../Dash Final.png"))
        self.volumeDashOne.setScaledContents(True)
        self.volumeDashOne.setObjectName("volumeDashOne")
        self.volumeDotThree = QtWidgets.QLabel(self.centralwidget)
        self.volumeDotThree.setGeometry(QtCore.QRect(10, 540, 31, 31))
        self.volumeDotThree.setText("")
        self.volumeDotThree.setPixmap(QtGui.QPixmap("../Dot Final.png"))
        self.volumeDotThree.setScaledContents(True)
        self.volumeDotThree.setObjectName("volumeDotThree")
        self.volumeDotTwo = QtWidgets.QLabel(self.centralwidget)
        self.volumeDotTwo.setGeometry(QtCore.QRect(10, 570, 31, 31))
        self.volumeDotTwo.setText("")
        self.volumeDotTwo.setPixmap(QtGui.QPixmap("../Dot Final.png"))
        self.volumeDotTwo.setScaledContents(True)
        self.volumeDotTwo.setObjectName("volumeDotTwo")
        self.volumeDotOne = QtWidgets.QLabel(self.centralwidget)
        self.volumeDotOne.setGeometry(QtCore.QRect(10, 600, 31, 31))
        self.volumeDotOne.setText("")
        self.volumeDotOne.setPixmap(QtGui.QPixmap("../Dot Final.png"))
        self.volumeDotOne.setScaledContents(True)
        self.volumeDotOne.setObjectName("volumeDotOne")
        self.volumeLevel = QtWidgets.QLabel(self.centralwidget)
        self.volumeLevel.setGeometry(QtCore.QRect(2, 620, 47, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.volumeLevel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.volumeLevel.setFont(font)
        self.volumeLevel.setAlignment(QtCore.Qt.AlignCenter)
        self.volumeLevel.setObjectName("volumeLevel")
        self.statusOn = QtWidgets.QLabel(self.centralwidget)
        self.statusOn.setGeometry(QtCore.QRect(172, -84, 201, 211))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.statusOn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.statusOn.setFont(font)
        self.statusOn.setText("")
        self.statusOn.setPixmap(QtGui.QPixmap("../Status On.png"))
        self.statusOn.setScaledContents(True)
        self.statusOn.setAlignment(QtCore.Qt.AlignCenter)
        self.statusOn.setObjectName("statusOn")
        self.currentChannel_3 = QtWidgets.QLabel(self.centralwidget)
        self.currentChannel_3.setGeometry(QtCore.QRect(270, 110, 201, 211))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.currentChannel_3.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.currentChannel_3.setFont(font)
        self.currentChannel_3.setText("")
        self.currentChannel_3.setPixmap(QtGui.QPixmap("../Status Off.png"))
        self.currentChannel_3.setScaledContents(True)
        self.currentChannel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.currentChannel_3.setObjectName("currentChannel_3")
        self.statusOff = QtWidgets.QLabel(self.centralwidget)
        self.statusOff.setGeometry(QtCore.QRect(172, -84, 201, 211))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.statusOff.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.statusOff.setFont(font)
        self.statusOff.setText("")
        self.statusOff.setPixmap(QtGui.QPixmap("../Status Off.png"))
        self.statusOff.setScaledContents(True)
        self.statusOff.setAlignment(QtCore.Qt.AlignCenter)
        self.statusOff.setObjectName("statusOff")
        self.volumeUpDisabled = QtWidgets.QLabel(self.centralwidget)
        self.volumeUpDisabled.setGeometry(QtCore.QRect(180, 97, 81, 81))
        self.volumeUpDisabled.setText("")
        self.volumeUpDisabled.setPixmap(QtGui.QPixmap("../Volume Up Disabled.png"))
        self.volumeUpDisabled.setScaledContents(True)
        self.volumeUpDisabled.setObjectName("volumeUpDisabled")
        self.volumeDownDisabled = QtWidgets.QLabel(self.centralwidget)
        self.volumeDownDisabled.setGeometry(QtCore.QRect(180, 192, 81, 81))
        self.volumeDownDisabled.setText("")
        self.volumeDownDisabled.setPixmap(QtGui.QPixmap("../Volume Down Disabled.png"))
        self.volumeDownDisabled.setScaledContents(True)
        self.volumeDownDisabled.setObjectName("volumeDownDisabled")
        self.volumeDownImage.raise_()
        self.volumeUpImage.raise_()
        self.volumeDownDisabled.raise_()
        self.volumeUpDisabled.raise_()
        self.volumeDown.raise_()
        self.volumeUp.raise_()
        self.statusOff.raise_()
        self.statusOn.raise_()
        self.volumeOff.raise_()
        self.volumeOn.raise_()
        self.muteButton.raise_()
        self.channelDownImage.raise_()
        self.channelUpImage.raise_()
        self.powerImage.raise_()
        self.channelDown.raise_()
        self.channelUp.raise_()
        self.powerButton.raise_()
        self.tv_status.raise_()
        self.espnLabel.raise_()
        self.nickLabel.raise_()
        self.hgtvLabel.raise_()
        self.cnnLabel.raise_()
        self.currentChannel.raise_()
        self.volumeDashThree.raise_()
        self.volumeDashTwo.raise_()
        self.volumeDashOne.raise_()
        self.volumeDotThree.raise_()
        self.volumeDotTwo.raise_()
        self.volumeDotOne.raise_()
        self.volumeLevel.raise_()
        self.currentChannel_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Remote Control"))
        self.currentChannel.setText(_translate("MainWindow", "0"))
        self.volumeLevel.setText(_translate("MainWindow", "MUTED"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
