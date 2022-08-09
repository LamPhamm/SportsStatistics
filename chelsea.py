# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chelsea.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import ChelseaInfo

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(689, 516)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.TitleLabel.setGeometry(QtCore.QRect(180, 0, 361, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.TitleLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(48)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setAutoFillBackground(False)
        self.TitleLabel.setObjectName("TitleLabel")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 50, 701, 471))
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap("chelseaBackground.jpg"))
        self.Background.setScaledContents(True)
        self.Background.setObjectName("Background")
        self.playerStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.playerStatusLabel.setGeometry(QtCore.QRect(10, 440, 221, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.playerStatusLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.playerStatusLabel.setFont(font)
        self.playerStatusLabel.setText("")
        self.playerStatusLabel.setObjectName("playerStatusLabel")
        self.playerStatComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.playerStatComboBox.setGeometry(QtCore.QRect(140, 360, 201, 22))
        self.playerStatComboBox.setObjectName("playerStatComboBox")
        self.playerStatComboBox.addItem("")
        self.playerStatComboBox.addItem("")
        self.playerStatComboBox.addItem("")
        self.playerStatComboBox.addItem("")
        self.playerStatComboBox.addItem("")
        self.playerStatComboBox.addItem("")
        self.playerComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.playerComboBox.setGeometry(QtCore.QRect(130, 320, 131, 22))
        self.playerComboBox.setObjectName("playerComboBox")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.playerComboBox.addItem("")
        self.trophyComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.trophyComboBox.setGeometry(QtCore.QRect(570, 330, 111, 22))
        self.trophyComboBox.setObjectName("trophyComboBox")
        self.trophyComboBox.addItem("")
        self.trophyComboBox.addItem("")
        self.trophyComboBox.addItem("")
        self.trophyComboBox.addItem("")
        self.trophyComboBox.addItem("")
        self.trophyComboBox.addItem("")
        self.trophyComboBox.addItem("")
        self.trophyComboBox.addItem("")
        self.seasonStatComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.seasonStatComboBox.setGeometry(QtCore.QRect(570, 370, 111, 22))
        self.seasonStatComboBox.setObjectName("seasonStatComboBox")
        self.seasonStatComboBox.addItem("")
        self.seasonStatComboBox.addItem("")
        self.seasonStatComboBox.addItem("")
        self.seasonStatComboBox.addItem("")
        self.seasonStatComboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 310, 131, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 350, 131, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 360, 191, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 320, 131, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.seasonStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.seasonStatusLabel.setGeometry(QtCore.QRect(300, 440, 381, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.seasonStatusLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.seasonStatusLabel.setFont(font)
        self.seasonStatusLabel.setText("")
        self.seasonStatusLabel.setObjectName("seasonStatusLabel")
        self.james = QtWidgets.QLabel(self.centralwidget)
        self.james.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.james.setText("")
        self.james.setPixmap(QtGui.QPixmap("james.jpg"))
        self.james.setScaledContents(True)
        self.james.setObjectName("james")
        self.Kai = QtWidgets.QLabel(self.centralwidget)
        self.Kai.setGeometry(QtCore.QRect(50, 0, 51, 51))
        self.Kai.setText("")
        self.Kai.setPixmap(QtGui.QPixmap("kai.jpg"))
        self.Kai.setScaledContents(True)
        self.Kai.setObjectName("Kai")
        self.Ngolo = QtWidgets.QLabel(self.centralwidget)
        self.Ngolo.setGeometry(QtCore.QRect(100, 0, 51, 51))
        self.Ngolo.setText("")
        self.Ngolo.setPixmap(QtGui.QPixmap("ngolo.webp"))
        self.Ngolo.setScaledContents(True)
        self.Ngolo.setObjectName("Ngolo")
        self.pulisic = QtWidgets.QLabel(self.centralwidget)
        self.pulisic.setGeometry(QtCore.QRect(540, 0, 51, 51))
        self.pulisic.setText("")
        self.pulisic.setPixmap(QtGui.QPixmap("pulisic.jpeg"))
        self.pulisic.setScaledContents(True)
        self.pulisic.setObjectName("pulisic")
        self.mount = QtWidgets.QLabel(self.centralwidget)
        self.mount.setGeometry(QtCore.QRect(590, 0, 51, 51))
        self.mount.setText("")
        self.mount.setPixmap(QtGui.QPixmap("mount.webp"))
        self.mount.setScaledContents(True)
        self.mount.setObjectName("mount")
        self.hazard = QtWidgets.QLabel(self.centralwidget)
        self.hazard.setGeometry(QtCore.QRect(640, 0, 51, 51))
        self.hazard.setText("")
        self.hazard.setPixmap(QtGui.QPixmap("hazard2.jpg"))
        self.hazard.setScaledContents(True)
        self.hazard.setObjectName("hazard")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Combobox handlers
        self.trophyComboBox.activated.connect(self.changeSeasonStatusLabel)
        self.seasonStatComboBox.activated.connect(self.changeSeasonStatusLabel2)
        self.playerStatComboBox.activated.connect(self.changePlayerStatusLabel)
        self.playerComboBox.activated.connect(self.changePlayerStatComboBox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chelsea FC Stat Robot by Lam Pham"))
        self.TitleLabel.setText(_translate("MainWindow", "Chelsea FC Stat Robot"))
        self.playerStatComboBox.setItemText(0, _translate("MainWindow", "Appearances"))
        self.playerStatComboBox.setItemText(1, _translate("MainWindow", "Nationality"))
        self.playerStatComboBox.setItemText(2, _translate("MainWindow", "Clean Sheets"))
        self.playerStatComboBox.setItemText(3, _translate("MainWindow", "Goals(Defender)"))
        self.playerStatComboBox.setItemText(4, _translate("MainWindow", "Goals(Midfielder/Attacker)"))
        self.playerStatComboBox.setItemText(5, _translate("MainWindow", "Assists"))
        self.playerComboBox.setItemText(0, _translate("MainWindow", "Kepa"))
        self.playerComboBox.setItemText(1, _translate("MainWindow", "Mendy"))
        self.playerComboBox.setItemText(2, _translate("MainWindow", "Alonso"))
        self.playerComboBox.setItemText(3, _translate("MainWindow", "Silva"))
        self.playerComboBox.setItemText(4, _translate("MainWindow", "Koulibaly"))
        self.playerComboBox.setItemText(5, _translate("MainWindow", "Chilwell"))
        self.playerComboBox.setItemText(6, _translate("MainWindow", "James"))
        self.playerComboBox.setItemText(7, _translate("MainWindow", "Azpilicueta"))
        self.playerComboBox.setItemText(8, _translate("MainWindow", "Cucurella"))
        self.playerComboBox.setItemText(9, _translate("MainWindow", "Chalobah"))
        self.playerComboBox.setItemText(10, _translate("MainWindow", "Sarr"))
        self.playerComboBox.setItemText(11, _translate("MainWindow", "Jorginho"))
        self.playerComboBox.setItemText(12, _translate("MainWindow", "Kanté"))
        self.playerComboBox.setItemText(13, _translate("MainWindow", "Pulisic"))
        self.playerComboBox.setItemText(14, _translate("MainWindow", "Kovacic"))
        self.playerComboBox.setItemText(15, _translate("MainWindow", "Mount"))
        self.playerComboBox.setItemText(16, _translate("MainWindow", "Ziyech"))
        self.playerComboBox.setItemText(17, _translate("MainWindow", "Havertz"))
        self.playerComboBox.setItemText(18, _translate("MainWindow", "Loftus-Cheek"))
        self.playerComboBox.setItemText(19, _translate("MainWindow", "Chukwuemeka"))
        self.playerComboBox.setItemText(20, _translate("MainWindow", "Gallagher"))
        self.playerComboBox.setItemText(21, _translate("MainWindow", "Barkley"))
        self.playerComboBox.setItemText(22, _translate("MainWindow", "Hudson-Odoi"))
        self.playerComboBox.setItemText(23, _translate("MainWindow", "Sterling"))
        self.playerComboBox.setItemText(24, _translate("MainWindow", "Broja"))
        self.trophyComboBox.setItemText(0, _translate("MainWindow", "Premier League"))
        self.trophyComboBox.setItemText(1, _translate("MainWindow", "Champions League"))
        self.trophyComboBox.setItemText(2, _translate("MainWindow", "Europa League"))
        self.trophyComboBox.setItemText(3, _translate("MainWindow", "FA Cup"))
        self.trophyComboBox.setItemText(4, _translate("MainWindow", "League Cup"))
        self.trophyComboBox.setItemText(5, _translate("MainWindow", "Super Cup"))
        self.trophyComboBox.setItemText(6, _translate("MainWindow", "Club World Cup"))
        self.trophyComboBox.setItemText(7, _translate("MainWindow", "Community Shield"))
        self.seasonStatComboBox.setItemText(0, _translate("MainWindow", "Record"))
        self.seasonStatComboBox.setItemText(1, _translate("MainWindow", "Points"))
        self.seasonStatComboBox.setItemText(2, _translate("MainWindow", "Position"))
        self.seasonStatComboBox.setItemText(3, _translate("MainWindow", "Goals"))
        self.seasonStatComboBox.setItemText(4, _translate("MainWindow", "Goals Conceded"))
        self.label.setText(_translate("MainWindow", "Choose a Player:"))
        self.label_2.setText(_translate("MainWindow", "Choose a Statistic:"))
        self.label_3.setText(_translate("MainWindow", "Choose a Season Statistic:"))
        self.label_4.setText(_translate("MainWindow", "Choose a Trophy:"))

    def changeSeasonStatusLabel(self):
        #Determine the type of trophy to be displayed
        titles,titlesYears="",""
        trophy_type=self.trophyComboBox.currentText()
        
        if trophy_type=="Premier League":
            titles,titlesYears=ChelseaInfo.getLeagueTitles();
        elif trophy_type=="Champions League":
            titles,titlesYears=ChelseaInfo.getChampionsLeagueTitles();
        elif trophy_type=="Europa League":
            titles,titlesYears=ChelseaInfo.getEuropaLeagues();
        elif trophy_type=="Club World Cup":
            titles,titlesYears=ChelseaInfo.getClubWorldCups();
        elif trophy_type=="FA CUP":
            titles,titlesYears=ChelseaInfo.getFACups();
        elif trophy_type=="League Cup":
            titles,titlesYears=ChelseaInfo.getLeagueCups();
        elif trophy_type=="Super Cup":
            titles,titlesYears=ChelseaInfo.getSuperCups();
        else:
            titles,titlesYears=ChelseaInfo.getCommunityShields();

        #Change the status label
        self.seasonStatusLabel.setText("Times Won: "+titles+"\nYears: "+titlesYears)
    
    def changeSeasonStatusLabel2(self):
        #Determine the season statistic to be displayed
        season_stat=self.seasonStatComboBox.currentText()

        stat=""
        if season_stat=="Record":
            stat="Record: " + ChelseaInfo.getRecord()
        elif season_stat=="Points":
            stat=ChelseaInfo.getPoints()
        elif season_stat=="Position":
            stat="Position: " + ChelseaInfo.getPosition()
        elif season_stat=="Goals":
            stat="Goals Scored: " + ChelseaInfo.getGoals()
        else:
            stat="Goals Conceded: " + ChelseaInfo.getGoalsConceded()

        #Change the status label
        self.seasonStatusLabel.setText(stat)

    def changePlayerStatusLabel(self):
        #Get the player and the stat to be displayed for the player
        player=self.playerComboBox.currentText()
        player_stat=self.playerStatComboBox.currentText()

        stat=""
        if player_stat=="Appearances":
            stat="Appearances: " + ChelseaInfo.getAppearances(player)
        elif player_stat=="Nationality":
            stat="Nationality: " + ChelseaInfo.getNationality(player)
        elif player_stat=="Clean Sheets":
            stat="Clean Sheets: " + ChelseaInfo.getCleanSheets(player)
        elif player_stat=="Goals(Defender)":
            stat="Goals: " + ChelseaInfo.getGoalsForDefender(player)
        elif player_stat=="Goals(Midfielder/Attacker)":
            stat="Goals: " + ChelseaInfo.getGoalsForAttacker(player)
        else:
            stat="Assists: " + ChelseaInfo.getAssists(player)
        
        #Change the status label
        self.playerStatusLabel.setText(stat)
    
    def changePlayerStatComboBox(self):
        #Unhide any hidden rows
        self.playerStatComboBox.view().setRowHidden(2,False)
        self.playerStatComboBox.view().setRowHidden(3,False)
        self.playerStatComboBox.view().setRowHidden(4,False)
        self.playerStatComboBox.view().setRowHidden(5,False)

        #List of defenders and list of goalkeeprs
        defenders=["Alonso","Koulibaly","Silva","Chilwell","James","Azpilicueta","Chalobah","Sarr","Cucurella"]
        goalkeepers=["Kepa","Mendy"]

        #If the player selected is a goalkeeper, hide the irrelevant rows
        if self.playerComboBox.currentText() in goalkeepers:
            self.playerStatComboBox.view().setRowHidden(3,True)
            self.playerStatComboBox.view().setRowHidden(4,True)
            self.playerStatComboBox.view().setRowHidden(5,True)

        #If the player selected is a defender, hide the irrelevant rows
        elif self.playerComboBox.currentText() in defenders:
            self.playerStatComboBox.view().setRowHidden(4,True)
            self.playerStatComboBox.view().setRowHidden(5,True)

        #If the player selected is a attacker, hide the irrelevant rows
        else:
            self.playerStatComboBox.view().setRowHidden(2,True)
            self.playerStatComboBox.view().setRowHidden(3,True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

