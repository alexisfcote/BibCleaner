# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\alfoc\Desktop\Bibtex Cleaner\uiBibCleaner.ui'
#
# Created: Mon Sep 29 17:03:04 2014
#      by: PyQt4 UI code generator 4.9.6
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
        main.setEnabled(True)
        main.resize(528, 350)
        main.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("favicon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main.setWindowIcon(icon)
        main.setSizeGripEnabled(False)
        self.gridLayout = QtGui.QGridLayout(main)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(2, -1, 2, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.FileEdit = QtGui.QLineEdit(main)
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
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButto_reload = QtGui.QPushButton(main)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButto_reload.sizePolicy().hasHeightForWidth())
        self.pushButto_reload.setSizePolicy(sizePolicy)
        self.pushButto_reload.setObjectName(_fromUtf8("pushButto_reload"))
        self.horizontalLayout.addWidget(self.pushButto_reload)
        self.pushButton_load = QtGui.QPushButton(main)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_load.sizePolicy().hasHeightForWidth())
        self.pushButton_load.setSizePolicy(sizePolicy)
        self.pushButton_load.setToolTip(_fromUtf8(""))
        self.pushButton_load.setObjectName(_fromUtf8("pushButton_load"))
        self.horizontalLayout.addWidget(self.pushButton_load)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox_check = QtGui.QGroupBox(main)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_check.sizePolicy().hasHeightForWidth())
        self.groupBox_check.setSizePolicy(sizePolicy)
        self.groupBox_check.setObjectName(_fromUtf8("groupBox_check"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_check)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.checkBox_url = QtGui.QCheckBox(self.groupBox_check)
        self.checkBox_url.setChecked(True)
        self.checkBox_url.setObjectName(_fromUtf8("checkBox_url"))
        self.verticalLayout_2.addWidget(self.checkBox_url)
        self.checkBox_file_location = QtGui.QCheckBox(self.groupBox_check)
        self.checkBox_file_location.setChecked(True)
        self.checkBox_file_location.setObjectName(_fromUtf8("checkBox_file_location"))
        self.verticalLayout_2.addWidget(self.checkBox_file_location)
        self.checkBox_isbn = QtGui.QCheckBox(self.groupBox_check)
        self.checkBox_isbn.setChecked(True)
        self.checkBox_isbn.setObjectName(_fromUtf8("checkBox_isbn"))
        self.verticalLayout_2.addWidget(self.checkBox_isbn)
        self.checkBox_abstract = QtGui.QCheckBox(self.groupBox_check)
        self.checkBox_abstract.setChecked(True)
        self.checkBox_abstract.setObjectName(_fromUtf8("checkBox_abstract"))
        self.verticalLayout_2.addWidget(self.checkBox_abstract)
        self.verticalLayout.addWidget(self.groupBox_check)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(main)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)
        self.textEdit_bibtex = QtGui.QTextEdit(main)
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
        self.gridLayout.addWidget(self.textEdit_bibtex, 0, 0, 1, 1)

        self.retranslateUi(main)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), main.close)
        QtCore.QMetaObject.connectSlotsByName(main)
        main.setTabOrder(self.FileEdit, self.checkBox_url)
        main.setTabOrder(self.checkBox_url, self.checkBox_file_location)
        main.setTabOrder(self.checkBox_file_location, self.buttonBox)
        main.setTabOrder(self.buttonBox, self.textEdit_bibtex)

    def retranslateUi(self, main):
        main.setWindowTitle(_translate("main", "CleanBib", None))
        self.FileEdit.setPlaceholderText(_translate("main", "Location of the file", None))
        self.pushButto_reload.setText(_translate("main", "Reload", None))
        self.pushButton_load.setText(_translate("main", "Load", None))
        self.groupBox_check.setTitle(_translate("main", "Remove :", None))
        self.checkBox_url.setText(_translate("main", "url", None))
        self.checkBox_file_location.setText(_translate("main", "file", None))
        self.checkBox_isbn.setToolTip(_translate("main", "Remove ISDN, DOI, Article ID and ISSN", None))
        self.checkBox_isbn.setText(_translate("main", "ISBN, DOI and ...", None))
        self.checkBox_abstract.setToolTip(_translate("main", "Remove ISDN, DOI, Article ID and ISSN", None))
        self.checkBox_abstract.setText(_translate("main", "abstract", None))
        self.textEdit_bibtex.setHtml(_translate("main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))

