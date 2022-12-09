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
    MAX_VOLUME = 3
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
        self.espnLabel.setVisible(False)
        self.cnnLabel.setVisible(False)
        self.nickLabel.setVisible(False)
        self.hgtvLabel.setVisible(False)
        self.volumeDashOne.setVisible(False)
        self.volumeDashTwo.setVisible(False)
        self.volumeDashThree.setVisible(False)
        self.volumeDotOne.setVisible(False)
        self.volumeDotTwo.setVisible(False)
        self.volumeDotThree.setVisible(False)
        self.volumeLevel.setVisible(False)
        self.volumeUpDisabled.setVisible(False)
        self.volumeDownDisabled.setVisible(False)
        self.currentChannel.setVisible(False)
        self.statusOn.setVisible(False)
        self.statusOff.setVisible(True)
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
            self.currentChannel.setVisible(True)
            self.statusOn.setVisible(True)
            self.statusOff.setVisible(False)
            self.channel_display()
            self.volume_display()
        else:
            self.__status = False
            self.__muted = False
            self.espnLabel.setVisible(False)
            self.cnnLabel.setVisible(False)
            self.nickLabel.setVisible(False)
            self.hgtvLabel.setVisible(False)
            self.currentChannel.setVisible(False)
            self.volumeDashOne.setVisible(False)
            self.volumeDashTwo.setVisible(False)
            self.volumeDashThree.setVisible(False)
            self.volumeDotOne.setVisible(False)
            self.volumeDotTwo.setVisible(False)
            self.volumeDotThree.setVisible(False)
            self.volumeLevel.setVisible(False)
            self.currentChannel.setVisible(False)
            self.statusOn.setVisible(False)
            self.statusOff.setVisible(True)
            self.volumeOff.setVisible(False)
            self.volumeOn.setVisible(True)
            self.volumeUpDisabled.setVisible(False)
            self.volumeDownDisabled.setVisible(False)
            self.volumeUp.setVisible(True)
            self.volumeDown.setVisible(True)





    def mute(self):
        """
        Function taking a clicked action on 'muteButton' and switching the '__muted' status from True to False or False
        to True depending on initial status

        :return:
        """
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
                self.volume_display()
                self.volumeOff.setVisible(True)
                self.volumeOn.setVisible(False)
            elif self.__muted == True:
                self.__muted = False
                self.volume_display()
                self.volumeOff.setVisible(False)
                self.volumeOn.setVisible(True)

    def channel_up(self):
        """
        Function taking a clicked action on 'channelUp' and incrementing the channel up to 2 and cycling back to 0
        if the channel is already at 2

        :return:
        """
        if self.__status == True:
            if self.__channel == MAX_CHANNEL:
                self.__channel = MIN_CHANNEL
                self.channel_display()
            else:
                self.__channel = self.__channel + 1
                self.channel_display()


    def channel_down(self):
        """
        Function taking a clicked action on 'channelDown' and decreasing the channel down to 0 and cycling back to 2
        if the channel is already at 0

        :return:
        """
        if self.__status == True:
            if self.__channel == MIN_CHANNEL:
                self.__channel = MAX_CHANNEL
                self.channel_display()
            else:
                self.__channel = self.__channel - 1
                self.channel_display()

    def volume_up(self):
        """
        Function taking a clicked action on 'volumeUp' and increasing the volume to a max of 2. If the value is already
        at 2 the volume will not increase further.

        :return:
        """
        if self.__status == True:
            if self.__volume < MAX_VOLUME:
                self.__volume = self.__volume + 1
                self.volume_display()


    def volume_down(self):
        """
        Function taking a clicked action on 'volumeDown' and decreasing the volume to a minimum of 0. If the value is
        already at 0, the volume will not decrease further.
        :return:
        """
        if self.__status == True:
            if self.__volume > MIN_VOLUME:
                self.__volume = self.__volume - 1
                self.volume_display()
            else:
                self.volume_display()

    def channel_display(self):
        if self.__channel == 0:
            self.espnLabel.setVisible(True)
            self.cnnLabel.setVisible(False)
            self.nickLabel.setVisible(False)
            self.hgtvLabel.setVisible(False)
            self.currentChannel.setText('0')
        elif self.__channel == 1:
            self.espnLabel.setVisible(False)
            self.cnnLabel.setVisible(True)
            self.nickLabel.setVisible(False)
            self.hgtvLabel.setVisible(False)
            self.currentChannel.setText('1')
        elif self.__channel == 2:
            self.espnLabel.setVisible(False)
            self.cnnLabel.setVisible(False)
            self.nickLabel.setVisible(True)
            self.hgtvLabel.setVisible(False)
            self.currentChannel.setText('2')
        elif self.__channel == 3:
            self.espnLabel.setVisible(False)
            self.cnnLabel.setVisible(False)
            self.nickLabel.setVisible(False)
            self.hgtvLabel.setVisible(True)
            self.currentChannel.setText('3')

    def volume_display(self):

        if self.__muted == False:

            self.volumeUpDisabled.setVisible(False)
            self.volumeDownDisabled.setVisible(False)
            self.volumeUp.setVisible(True)
            self.volumeDown.setVisible(True)

            if self.__volume == 0:
                self.volumeDashOne.setVisible(False)
                self.volumeDashTwo.setVisible(False)
                self.volumeDashThree.setVisible(False)
                self.volumeDotOne.setVisible(True)
                self.volumeDotTwo.setVisible(True)
                self.volumeDotThree.setVisible(True)
                self.volumeLevel.setVisible(True)
                self.volumeLevel.setText('MIN')


            elif self.__volume == 1:
                self.volumeDashOne.setVisible(True)
                self.volumeDashTwo.setVisible(False)
                self.volumeDashThree.setVisible(False)
                self.volumeDotOne.setVisible(False)
                self.volumeDotTwo.setVisible(True)
                self.volumeDotThree.setVisible(True)
                self.volumeLevel.setVisible(True)
                self.volumeLevel.setText('1')


            elif self.__volume == 2:
                self.volumeDashOne.setVisible(True)
                self.volumeDashTwo.setVisible(True)
                self.volumeDashThree.setVisible(False)
                self.volumeDotOne.setVisible(False)
                self.volumeDotTwo.setVisible(False)
                self.volumeDotThree.setVisible(True)
                self.volumeLevel.setVisible(True)
                self.volumeLevel.setText('2')


            elif self.__volume == 3:
                self.volumeDashOne.setVisible(True)
                self.volumeDashTwo.setVisible(True)
                self.volumeDashThree.setVisible(True)
                self.volumeDotOne.setVisible(False)
                self.volumeDotTwo.setVisible(False)
                self.volumeDotThree.setVisible(False)
                self.volumeLevel.setVisible(True)
                self.volumeLevel.setText('MAX')

        else:
            self.volumeDashOne.setVisible(False)
            self.volumeDashTwo.setVisible(False)
            self.volumeDashThree.setVisible(False)
            self.volumeDotOne.setVisible(True)
            self.volumeDotTwo.setVisible(True)
            self.volumeDotThree.setVisible(True)
            self.volumeLevel.setVisible(True)
            self.volumeUpDisabled.setVisible(True)
            self.volumeDownDisabled.setVisible(True)
            self.volumeUp.setVisible(False)
            self.volumeDown.setVisible(False)
            self.volumeLevel.setText('MUTED')






