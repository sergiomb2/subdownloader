# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created: Thu Aug 28 01:09:51 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        PreferencesDialog.setObjectName("PreferencesDialog")
        PreferencesDialog.setWindowModality(QtCore.Qt.WindowModal)
        PreferencesDialog.resize(560, 369)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PreferencesDialog.sizePolicy().hasHeightForWidth())
        PreferencesDialog.setSizePolicy(sizePolicy)
        PreferencesDialog.setSizeGripEnabled(False)
        PreferencesDialog.setModal(True)
        self.verticalLayout_5 = QtGui.QVBoxLayout(PreferencesDialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtGui.QTabWidget(PreferencesDialog)
        self.tabWidget.setWindowModality(QtCore.Qt.NonModal)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setGeometry(QtCore.QRect(0, 0, 540, 279))
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_56 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.verticalLayout_4.addWidget(self.label_56)
        self.scrollArea = QtGui.QScrollArea(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 150))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 526, 241))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.optionFilterLangLayout_1 = QtGui.QVBoxLayout()
        self.optionFilterLangLayout_1.setSpacing(5)
        self.optionFilterLangLayout_1.setObjectName("optionFilterLangLayout_1")
        self.horizontalLayout_2.addLayout(self.optionFilterLangLayout_1)
        self.optionFilterLangLayout_2 = QtGui.QVBoxLayout()
        self.optionFilterLangLayout_2.setSpacing(5)
        self.optionFilterLangLayout_2.setObjectName("optionFilterLangLayout_2")
        self.horizontalLayout_2.addLayout(self.optionFilterLangLayout_2)
        self.optionFilterLangLayout_3 = QtGui.QVBoxLayout()
        self.optionFilterLangLayout_3.setSpacing(5)
        self.optionFilterLangLayout_3.setObjectName("optionFilterLangLayout_3")
        self.horizontalLayout_2.addLayout(self.optionFilterLangLayout_3)
        self.optionFilterLangLayout_4 = QtGui.QVBoxLayout()
        self.optionFilterLangLayout_4.setSpacing(5)
        self.optionFilterLangLayout_4.setObjectName("optionFilterLangLayout_4")
        self.horizontalLayout_2.addLayout(self.optionFilterLangLayout_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.tab, "")
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setGeometry(QtCore.QRect(0, 0, 540, 279))
        self.tab_6.setObjectName("tab_6")
        self.label_54 = QtGui.QLabel(self.tab_6)
        self.label_54.setGeometry(QtCore.QRect(10, 0, 161, 27))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.layoutWidget_10 = QtGui.QWidget(self.tab_6)
        self.layoutWidget_10.setGeometry(QtCore.QRect(20, 20, 211, 86))
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
        self.optionPredefinedFolderText.setGeometry(QtCore.QRect(190, 80, 241, 23))
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
        self.layoutWidget.setGeometry(QtCore.QRect(20, 170, 514, 86))
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
        self.tab_8.setGeometry(QtCore.QRect(0, 0, 540, 279))
        self.tab_8.setObjectName("tab_8")
        self.label_55 = QtGui.QLabel(self.tab_8)
        self.label_55.setGeometry(QtCore.QRect(10, 20, 311, 27))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.optionDefaultUploadLanguage = QtGui.QComboBox(self.tab_8)
        self.optionDefaultUploadLanguage.setGeometry(QtCore.QRect(330, 20, 161, 22))
        self.optionDefaultUploadLanguage.setObjectName("optionDefaultUploadLanguage")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setGeometry(QtCore.QRect(0, 0, 540, 279))
        self.tab_9.setObjectName("tab_9")
        self.label_52 = QtGui.QLabel(self.tab_9)
        self.label_52.setGeometry(QtCore.QRect(20, 10, 131, 18))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.optionProxyPort = QtGui.QSpinBox(self.tab_9)
        self.optionProxyPort.setGeometry(QtCore.QRect(90, 60, 71, 31))
        self.optionProxyPort.setMaximum(99999)
        self.optionProxyPort.setProperty("value", QtCore.QVariant(8080))
        self.optionProxyPort.setObjectName("optionProxyPort")
        self.optionProxyHost = QtGui.QLineEdit(self.tab_9)
        self.optionProxyHost.setGeometry(QtCore.QRect(90, 30, 221, 31))
        self.optionProxyHost.setObjectName("optionProxyHost")
        self.label_60 = QtGui.QLabel(self.tab_9)
        self.label_60.setGeometry(QtCore.QRect(31, 31, 44, 22))
        self.label_60.setObjectName("label_60")
        self.label_59 = QtGui.QLabel(self.tab_9)
        self.label_59.setGeometry(QtCore.QRect(31, 58, 44, 22))
        self.label_59.setObjectName("label_59")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setGeometry(QtCore.QRect(0, 0, 540, 279))
        self.tab_7.setObjectName("tab_7")
        self.optionInterfaceLanguage = QtGui.QComboBox(self.tab_7)
        self.optionInterfaceLanguage.setGeometry(QtCore.QRect(202, 3, 177, 31))
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
        self.label_63.setGeometry(QtCore.QRect(20, 80, 311, 18))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_63.setFont(font)
        self.label_63.setObjectName("label_63")
        self.optionVideoAppParams = QtGui.QLineEdit(self.tab_7)
        self.optionVideoAppParams.setGeometry(QtCore.QRect(128, 130, 261, 31))
        self.optionVideoAppParams.setObjectName("optionVideoAppParams")
        self.optionVideoAppChooseLocation = QtGui.QPushButton(self.tab_7)
        self.optionVideoAppChooseLocation.setGeometry(QtCore.QRect(399, 99, 83, 31))
        self.optionVideoAppChooseLocation.setObjectName("optionVideoAppChooseLocation")
        self.optionVideoAppLocation = QtGui.QLineEdit(self.tab_7)
        self.optionVideoAppLocation.setGeometry(QtCore.QRect(128, 100, 261, 31))
        self.optionVideoAppLocation.setObjectName("optionVideoAppLocation")
        self.label_65 = QtGui.QLabel(self.tab_7)
        self.label_65.setGeometry(QtCore.QRect(119, 159, 301, 18))
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
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtGui.QSpacerItem(498, 36, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.optionsButtonApplyChanges = QtGui.QPushButton(PreferencesDialog)
        self.optionsButtonApplyChanges.setObjectName("optionsButtonApplyChanges")
        self.horizontalLayout_3.addWidget(self.optionsButtonApplyChanges)
        self.optionsButtonCancel = QtGui.QPushButton(PreferencesDialog)
        self.optionsButtonCancel.setObjectName("optionsButtonCancel")
        self.horizontalLayout_3.addWidget(self.optionsButtonCancel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.retranslateUi(PreferencesDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PreferencesDialog)

    def retranslateUi(self, PreferencesDialog):
        PreferencesDialog.setWindowTitle(QtGui.QApplication.translate("PreferencesDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_56.setText(QtGui.QApplication.translate("PreferencesDialog", "Filter search results by these languages:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("PreferencesDialog", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.label_54.setText(QtGui.QApplication.translate("PreferencesDialog", "Destination folder:", None, QtGui.QApplication.UnicodeUTF8))
        self.optionDownloadFolderAsk.setText(QtGui.QApplication.translate("PreferencesDialog", "Always ask user", None, QtGui.QApplication.UnicodeUTF8))
        self.optionDownloadFolderSame.setText(QtGui.QApplication.translate("PreferencesDialog", "Same folder as video file", None, QtGui.QApplication.UnicodeUTF8))
        self.optionDownloadFolderPredefined.setText(QtGui.QApplication.translate("PreferencesDialog", "Predefined folder:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_53.setText(QtGui.QApplication.translate("PreferencesDialog", "Filename of the Subtitle:", None, QtGui.QApplication.UnicodeUTF8))
        self.optionButtonChooseFolder.setText(QtGui.QApplication.translate("PreferencesDialog", "Choose...", None, QtGui.QApplication.UnicodeUTF8))
        self.optionDownloadSameFilename.setText(QtGui.QApplication.translate("PreferencesDialog", "Same name as video file", None, QtGui.QApplication.UnicodeUTF8))
        self.optionDownloadSameFilenamePlusLang.setText(QtGui.QApplication.translate("PreferencesDialog", "Same name as video file + language code (ex: StarwardsCD1.eng.srt)", None, QtGui.QApplication.UnicodeUTF8))
        self.optionDownloadOnlineSubName.setText(QtGui.QApplication.translate("PreferencesDialog", "Same name as the online subtitle", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QtGui.QApplication.translate("PreferencesDialog", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.label_55.setText(QtGui.QApplication.translate("PreferencesDialog", "Default language of uploaded subtitles", None, QtGui.QApplication.UnicodeUTF8))
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
