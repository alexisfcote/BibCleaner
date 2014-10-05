# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './uiBibCleaner.ui'
#
# Created: Sun Oct  5 11:32:52 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName(_fromUtf8("main"))
        main.resize(630, 455)
        self.centralwidget = QtGui.QWidget(main)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.textEdit_bibtex = QtGui.QTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_bibtex.sizePolicy().hasHeightForWidth())
        self.textEdit_bibtex.setSizePolicy(sizePolicy)
        self.textEdit_bibtex.setMinimumSize(QtCore.QSize(300, 0))
        self.textEdit_bibtex.setStyleSheet(_fromUtf8(""))
        self.textEdit_bibtex.setReadOnly(True)
        self.textEdit_bibtex.setAcceptRichText(True)
        self.textEdit_bibtex.setObjectName(_fromUtf8("textEdit_bibtex"))
        self.horizontalLayout.addWidget(self.textEdit_bibtex)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(2, -1, 2, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.FileEdit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FileEdit.sizePolicy().hasHeightForWidth())
        self.FileEdit.setSizePolicy(sizePolicy)
        self.FileEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.FileEdit.setInputMask(_fromUtf8(""))
        self.FileEdit.setReadOnly(True)
        self.FileEdit.setObjectName(_fromUtf8("FileEdit"))
        self.verticalLayout.addWidget(self.FileEdit)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButto_reload = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButto_reload.sizePolicy().hasHeightForWidth())
        self.pushButto_reload.setSizePolicy(sizePolicy)
        self.pushButto_reload.setObjectName(_fromUtf8("pushButto_reload"))
        self.horizontalLayout_2.addWidget(self.pushButto_reload)
        self.pushButton_load = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_load.sizePolicy().hasHeightForWidth())
        self.pushButton_load.setSizePolicy(sizePolicy)
        self.pushButton_load.setToolTip(_fromUtf8(""))
        self.pushButton_load.setObjectName(_fromUtf8("pushButton_load"))
        self.horizontalLayout_2.addWidget(self.pushButton_load)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setBaseSize(QtCore.QSize(0, 0))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 198, 336))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.groupBox_custom = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_custom.sizePolicy().hasHeightForWidth())
        self.groupBox_custom.setSizePolicy(sizePolicy)
        self.groupBox_custom.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_custom.setObjectName(_fromUtf8("groupBox_custom"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_custom)
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3.addWidget(self.groupBox_custom)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.buttonBox = QtGui.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        main.setCentralWidget(self.centralwidget)

        self.retranslateUi(main)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), main.close)
        QtCore.QMetaObject.connectSlotsByName(main)
        main.setTabOrder(self.pushButton_load, self.buttonBox)
        main.setTabOrder(self.buttonBox, self.textEdit_bibtex)
        main.setTabOrder(self.textEdit_bibtex, self.FileEdit)
        main.setTabOrder(self.FileEdit, self.pushButto_reload)

    def retranslateUi(self, main):
        main.setWindowTitle(_translate("main", "MainWindow", None))
        self.textEdit_bibtex.setHtml(_translate("main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><br /></p></body></html>", None))
        self.FileEdit.setPlaceholderText(_translate("main", "Location of the file", None))
        self.pushButto_reload.setText(_translate("main", "Reload", None))
        self.pushButton_load.setText(_translate("main", "Load", None))
        self.groupBox_custom.setTitle(_translate("main", "Keys to remove:", None))

