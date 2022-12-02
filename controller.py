from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    """
    This function establishes class global variables to be utilized by the initialization of the Controller

    """

    global MIN_VOLUME
    global MAX_VOLUME
    global MIN_CHANNEL
    global MAX_CHANNEL

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, *args, **kwargs):
        """
        This function initializes a controller with default values associated with the global variables for private
        variables __volume and __channel and initializing boolean values of False for __status and __muted

        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.volumeOff.setVisible(False)
        self.volumeOn.setVisible(True)
        self.__status = False
        self.__muted = False
        self.__volume = MIN_VOLUME
        self.__channel = MIN_CHANNEL
        self.tv_status.setText('Off')
        self.powerButton.clicked.connect(lambda: self.power())
        self.muteButton.clicked.connect(lambda: self.mute())
        self.channelUp.clicked.connect(lambda: self.channel_up())
        self.channelDown.clicked.connect(lambda: self.channel_down())
        self.volumeUp.clicked.connect(lambda: self.volume_up())
        self.volumeDown.clicked.connect(lambda: self.volume_down())

    def power(self):
        """
        Function taking a clicked action on 'powerButton' and turning the '__status' to True or False depending on
        status when the button was clicked and outputting the current 'tv_status'

        :return:
        """

        if self.__status == False:
            self.__status = True
            self.tv_status.setText(f'Power: On\nVolume: {self.__volume}\nChannel: {self.__channel}\nMuted: {self.__muted}')
        else:
            self.__status = False
            self.__volume = MIN_VOLUME
            self.__channel = MIN_CHANNEL
            self.tv_status.setText('Power: Off')



    def mute(self):
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
                self.tv_status.setText(f'Power: On\nVolume: 0\nChannel: {self.__channel}\nMuted: {self.__muted}')
                self.volumeOff.setVisible(True)
                self.volumeOn.setVisible(False)
            elif self.__muted == True:
                self.__muted = False
                self.tv_status.setText(f'Power: On\nVolume: {self.__volume}\nChannel: {self.__channel}\nMuted: {self.__muted}')
                self.volumeOff.setVisible(False)
                self.volumeOn.setVisible(True)

    def channel_up(self):
        if self.__status == True:
            if self.__channel == MAX_CHANNEL:
                self.__channel = MIN_CHANNEL
                self.tv_status.setText(f'Power: On\nVolume: {self.__volume}\nChannel: {self.__channel}\nMuted: {self.__muted}')
            else:
                self.__channel = self.__channel + 1
                self.tv_status.setText(f'Power: On\nVolume: {self.__volume}\nChannel: {self.__channel}\nMuted: {self.__muted}')

    def channel_down(self):
        if self.__status == True:
            if self.__channel == MIN_CHANNEL:
                self.__channel = MAX_CHANNEL
                self.tv_status.setText(f'Power: On\nVolume: {self.__volume}\nChannel: {self.__channel}\nMuted: {self.__muted}')
            else:
                self.__channel = self.__channel - 1
                self.tv_status.setText(f'Power: On\nVolume: {self.__volume}\nChannel: {self.__channel}\nMuted: {self.__muted}')

    def volume_up(self):
        if self.__status == True:
            if self.__volume < MAX_VOLUME:
                self.__volume = self.__volume + 1
                self.tv_status.setText(f'Power: On\nVolume: {self.__volume}\nChannel: {self.__channel}\nMuted: {self.__muted}')

    def volume_down(self):
        if self.__status == True:
            if self.__volume > MIN_VOLUME:
                self.__volume = self.__volume - 1
                self.tv_status.setText(f'Power: On\nVolume: {self.__volume}\nChannel: {self.__channel}\nMuted: {self.__muted}')




