# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created: Mon Aug  4 18:44:24 2008
#      by: PyQt4 UI code generator 4.4.3-snapshot-20080731
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        PreferencesDialog.setObjectName("PreferencesDialog")
        PreferencesDialog.resize(536, 373)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PreferencesDialog.sizePolicy().hasHeightForWidth())
        PreferencesDialog.setSizePolicy(sizePolicy)
        PreferencesDialog.setSizeGripEnabled(False)
        PreferencesDialog.setModal(True)
        self.tabWidget = QtGui.QTabWidget(PreferencesDialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 531, 311))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setGeometry(QtCore.QRect(0, 0, 527, 288))
        self.tab_6.setObjectName("tab_6")
        self.label_54 = QtGui.QLabel(self.tab_6)
        self.label_54.setGeometry(QtCore.QRect(10, 0, 161, 27))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.layoutWidget_10 = QtGui.QWidget(self.tab_6)
        self.layoutWidget_10.setGeometry(QtCore.QRect(50, 20, 211, 86))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self._25 = QtGui.QVBoxLayout(self.layoutWidget_10)
        self._25.setObjectName("_25")
        self.optionDownloadFolderAsk = QtGui.QRadioButton(self.layoutWidget_10)
        self.optionDownloadFolderAsk.setObjectName("optionDownloadFolderAsk")
        self._25.addWidget(self.optionDownloadFolderAsk)
        self.optionDownloadFolderSame = QtGui.QRadioButton(self.layoutWidget_10)
        self.optionDownloadFolderSame.setChecked(True)
        self.optionDownloadFolderSame.setObjectName("optionDownloadFolderSame")
        self._25.addWidget(self.optionDownloadFolderSame)
        self.optionDownloadFolderPredefined = QtGui.QRadioButton(self.layoutWidget_10)
        self.optionDownloadFolderPredefined.setObjectName("optionDownloadFolderPredefined")
        self._25.addWidget(self.optionDownloadFolderPredefined)
        self.optionPredefinedFolderText = QtGui.QLineEdit(self.tab_6)
        self.optionPredefinedFolderText.setGeometry(QtCore.QRect(210, 80, 221, 23))
        self.optionPredefinedFolderText.setReadOnly(True)
        self.optionPredefinedFolderText.setObjectName("optionPredefinedFolderText")
        self.label_53 = QtGui.QLabel(self.tab_6)
        self.label_53.setGeometry(QtCore.QRect(10, 140, 191, 27))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.line_8 = QtGui.QFrame(self.tab_6)
        self.line_8.setGeometry(QtCore.QRect(20, 120, 481, 16))
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.optionButtonChooseFolder = QtGui.QPushButton(self.tab_6)
        self.optionButtonChooseFolder.setGeometry(QtCore.QRect(440, 80, 75, 27))
        self.optionButtonChooseFolder.setObjectName("optionButtonChooseFolder")
        self.layoutWidget = QtGui.QWidget(self.tab_6)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 172, 473, 86))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.optionDownloadSameFilename = QtGui.QRadioButton(self.layoutWidget)
        self.optionDownloadSameFilename.setChecked(True)
        self.optionDownloadSameFilename.setObjectName("optionDownloadSameFilename")
        self.verticalLayout_2.addWidget(self.optionDownloadSameFilename)
        self.optionDownloadSameFilenamePlusLang = QtGui.QRadioButton(self.layoutWidget)
        self.optionDownloadSameFilenamePlusLang.setChecked(False)
        self.optionDownloadSameFilenamePlusLang.setObjectName("optionDownloadSameFilenamePlusLang")
        self.verticalLayout_2.addWidget(self.optionDownloadSameFilenamePlusLang)
        self.optionDownloadOnlineSubName = QtGui.QRadioButton(self.layoutWidget)
        self.optionDownloadOnlineSubName.setObjectName("optionDownloadOnlineSubName")
        self.verticalLayout_2.addWidget(self.optionDownloadOnlineSubName)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setGeometry(QtCore.QRect(0, 0, 527, 288))
        self.tab_8.setObjectName("tab_8")
        self.label_55 = QtGui.QLabel(self.tab_8)
        self.label_55.setGeometry(QtCore.QRect(20, 20, 301, 27))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.optionDefaultUploadLanguage = QtGui.QComboBox(self.tab_8)
        self.optionDefaultUploadLanguage.setGeometry(QtCore.QRect(330, 20, 161, 22))
        self.optionDefaultUploadLanguage.setObjectName("optionDefaultUploadLanguage")
        self.label_56 = QtGui.QLabel(self.tab_8)
        self.label_56.setGeometry(QtCore.QRect(20, 60, 271, 18))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.label_58 = QtGui.QLabel(self.tab_8)
        self.label_58.setGeometry(QtCore.QRect(37, 110, 68, 23))
        self.label_58.setObjectName("label_58")
        self.optionLoginUsername = QtGui.QLineEdit(self.tab_8)
        self.optionLoginUsername.setGeometry(QtCore.QRect(110, 80, 110, 23))
        self.optionLoginUsername.setObjectName("optionLoginUsername")
        self.label_57 = QtGui.QLabel(self.tab_8)
        self.label_57.setGeometry(QtCore.QRect(37, 80, 68, 23))
        self.label_57.setObjectName("label_57")
        self.optionLoginPassword = QtGui.QLineEdit(self.tab_8)
        self.optionLoginPassword.setGeometry(QtCore.QRect(110, 110, 110, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optionLoginPassword.sizePolicy().hasHeightForWidth())
        self.optionLoginPassword.setSizePolicy(sizePolicy)
        self.optionLoginPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.optionLoginPassword.setObjectName("optionLoginPassword")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setGeometry(QtCore.QRect(0, 0, 527, 288))
        self.tab_9.setObjectName("tab_9")
        self.label_52 = QtGui.QLabel(self.tab_9)
        self.label_52.setGeometry(QtCore.QRect(20, 10, 111, 18))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.optionProxyPort = QtGui.QSpinBox(self.tab_9)
        self.optionProxyPort.setGeometry(QtCore.QRect(90, 60, 71, 25))
        self.optionProxyPort.setMaximum(99999)
        self.optionProxyPort.setProperty("value", QtCore.QVariant(8080))
        self.optionProxyPort.setObjectName("optionProxyPort")
        self.optionProxyHost = QtGui.QLineEdit(self.tab_9)
        self.optionProxyHost.setGeometry(QtCore.QRect(90, 30, 141, 23))
        self.optionProxyHost.setObjectName("optionProxyHost")
        self.label_60 = QtGui.QLabel(self.tab_9)
        self.label_60.setGeometry(QtCore.QRect(31, 31, 44, 22))
        self.label_60.setObjectName("label_60")
        self.label_59 = QtGui.QLabel(self.tab_9)
        self.label_59.setGeometry(QtCore.QRect(31, 58, 44, 22))
        self.label_59.setObjectName("label_59")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setGeometry(QtCore.QRect(0, 0, 527, 288))
        self.tab_7.setObjectName("tab_7")
        self.optionInterfaceLanguage = QtGui.QComboBox(self.tab_7)
        self.optionInterfaceLanguage.setGeometry(QtCore.QRect(202, 3, 177, 22))
        self.optionInterfaceLanguage.setObjectName("optionInterfaceLanguage")
        self.label_61 = QtGui.QLabel(self.tab_7)
        self.label_61.setGeometry(QtCore.QRect(20, 0, 177, 29))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_61.setFont(font)
        self.label_61.setObjectName("label_61")
        self.label_62 = QtGui.QLabel(self.tab_7)
        self.label_62.setGeometry(QtCore.QRect(20, 30, 177, 29))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_62.setFont(font)
        self.label_62.setObjectName("label_62")
        self.label_63 = QtGui.QLabel(self.tab_7)
        self.label_63.setGeometry(QtCore.QRect(20, 80, 301, 18))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_63.setFont(font)
        self.label_63.setObjectName("label_63")
        self.optionVideoAppParams = QtGui.QLineEdit(self.tab_7)
        self.optionVideoAppParams.setGeometry(QtCore.QRect(128, 130, 261, 23))
        self.optionVideoAppParams.setObjectName("optionVideoAppParams")
        self.optionVideoAppChooseLocation = QtGui.QPushButton(self.tab_7)
        self.optionVideoAppChooseLocation.setGeometry(QtCore.QRect(399, 99, 83, 27))
        self.optionVideoAppChooseLocation.setObjectName("optionVideoAppChooseLocation")
        self.optionVideoAppLocation = QtGui.QLineEdit(self.tab_7)
        self.optionVideoAppLocation.setGeometry(QtCore.QRect(128, 100, 261, 23))
        self.optionVideoAppLocation.setObjectName("optionVideoAppLocation")
        self.label_65 = QtGui.QLabel(self.tab_7)
        self.label_65.setGeometry(QtCore.QRect(119, 159, 271, 18))
        self.label_65.setObjectName("label_65")
        self.label_66 = QtGui.QLabel(self.tab_7)
        self.label_66.setGeometry(QtCore.QRect(30, 130, 81, 23))
        self.label_66.setObjectName("label_66")
        self.label_67 = QtGui.QLabel(self.tab_7)
        self.label_67.setGeometry(QtCore.QRect(30, 100, 91, 23))
        self.label_67.setObjectName("label_67")
        self.optionIntegrationExplorer = QtGui.QCheckBox(self.tab_7)
        self.optionIntegrationExplorer.setEnabled(False)
        self.optionIntegrationExplorer.setGeometry(QtCore.QRect(50, 50, 277, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optionIntegrationExplorer.sizePolicy().hasHeightForWidth())
        self.optionIntegrationExplorer.setSizePolicy(sizePolicy)
        self.optionIntegrationExplorer.setMinimumSize(QtCore.QSize(0, 22))
        self.optionIntegrationExplorer.setObjectName("optionIntegrationExplorer")
        self.tabWidget.addTab(self.tab_7, "")
        self.layoutWidget1 = QtGui.QWidget(PreferencesDialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 330, 521, 38))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtGui.QSpacerItem(498, 36, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.optionsButtonApplyChanges = QtGui.QPushButton(self.layoutWidget1)
        self.optionsButtonApplyChanges.setObjectName("optionsButtonApplyChanges")
        self.horizontalLayout_3.addWidget(self.optionsButtonApplyChanges)
        self.optionsButtonCancel = QtGui.QPushButton(self.layoutWidget1)
        self.optionsButtonCancel.setObjectName("optionsButtonCancel")
        self.horizontalLayout_3.addWidget(self.optionsButtonCancel)

        self.retranslateUi(PreferencesDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PreferencesDialog)

    def retranslateUi(self, PreferencesDialog):
        PreferencesDialog.setWindowTitle(QtGui.QApplication.translate("PreferencesDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_54.setText(QtGui.QApplication.translate("PreferencesDialog", "Destination folder:", None, QtGui.QApplication.UnicodeUTF8))
        self.optionDownloadFolderAsk.setText(QtGui.QApplication.translate("PreferencesDialog", "Always ask user", None, QtGui.QApplication.UnicodeUTF8))
        self.optionDownloadFolderSame.setText(QtGui.QApplication.translate("PreferencesDialog", "Same folder as video file", None, QtGui.QApplication.UnicodeUTF8))
        self.optionDownloadFolderPredefined.setText(QtGui.QApplication.translate("PreferencesDialog", "Predefined folder:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_53.setText(QtGui.QApplication.translate("PreferencesDialog", "Filename of the Subtitle:", None, QtGui.QApplication.UnicodeUTF8))
        self.optionButtonChooseFolder.setText(QtGui.QApplication.translate("PreferencesDialog", "Choose...", None, QtGui.QApplication.UnicodeUTF8))
        self.optionDownloadSameFilename.setText(QtGui.QApplication.translate("PreferencesDialog", "Same name as video file", None, QtGui.QApplication.UnicodeUTF8))
        self.optionDownloadSameFilenamePlusLang.setText(QtGui.QApplication.translate("PreferencesDialog", "Same name as video file + language code (ex: StarwardsCD1.eng.srt)", None, QtGui.QApplication.UnicodeUTF8))
        self.optionDownloadOnlineSubName.setText(QtGui.QApplication.translate("PreferencesDialog", "Same name as the online subtitle", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QtGui.QApplication.translate("PreferencesDialog", "Downloads", None, QtGui.QApplication.UnicodeUTF8))
        self.label_55.setText(QtGui.QApplication.translate("PreferencesDialog", "Default language of uploaded subtitles", None, QtGui.QApplication.UnicodeUTF8))
        self.label_56.setText(QtGui.QApplication.translate("PreferencesDialog", "Upload files as OpenSubtitles user:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_58.setText(QtGui.QApplication.translate("PreferencesDialog", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_57.setText(QtGui.QApplication.translate("PreferencesDialog", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QtGui.QApplication.translate("PreferencesDialog", "Upload", None, QtGui.QApplication.UnicodeUTF8))
        self.label_52.setText(QtGui.QApplication.translate("PreferencesDialog", "Network Proxy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_60.setText(QtGui.QApplication.translate("PreferencesDialog", "Host:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_59.setText(QtGui.QApplication.translate("PreferencesDialog", "Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QtGui.QApplication.translate("PreferencesDialog", "Network", None, QtGui.QApplication.UnicodeUTF8))
        self.label_61.setText(QtGui.QApplication.translate("PreferencesDialog", "Interface Language:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_62.setText(QtGui.QApplication.translate("PreferencesDialog", "Context Menu:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_63.setText(QtGui.QApplication.translate("PreferencesDialog", "External application for video playback", None, QtGui.QApplication.UnicodeUTF8))
        self.optionVideoAppChooseLocation.setText(QtGui.QApplication.translate("PreferencesDialog", "Choose...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_65.setText(QtGui.QApplication.translate("PreferencesDialog", "{0} = video file path; {1} = subtitle path", None, QtGui.QApplication.UnicodeUTF8))
        self.label_66.setText(QtGui.QApplication.translate("PreferencesDialog", "Parameters:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_67.setText(QtGui.QApplication.translate("PreferencesDialog", "Video Player:", None, QtGui.QApplication.UnicodeUTF8))
        self.optionIntegrationExplorer.setText(QtGui.QApplication.translate("PreferencesDialog", "Enable in your explorer", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QtGui.QApplication.translate("PreferencesDialog", "Others", None, QtGui.QApplication.UnicodeUTF8))
        self.optionsButtonApplyChanges.setText(QtGui.QApplication.translate("PreferencesDialog", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.optionsButtonCancel.setText(QtGui.QApplication.translate("PreferencesDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
