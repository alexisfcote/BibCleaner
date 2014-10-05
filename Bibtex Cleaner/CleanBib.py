#------------------------------------------------------------------------------
# Name:        CleanBib
# Purpose:
#
# Author:      alfoc
#
# Created:     25/09/2014
# Copyright:   (c) alfoc 2014
# Licence:     <your licence>
#------------------------------------------------------------------------------
import re
import os
import sys
from PyQt4.QtGui import QApplication, QDialog, QWidget, QMessageBox
from PyQt4 import QtCore, QtGui
from uiBibCleaner import Ui_main


lastAt = ''

def clean(file, url=False, fileR=False, isbn=False, abstract=False):
    toRemove = [] # Liste des choses à enlever
    if url:
        toRemove.append('url =')
    if fileR:
        toRemove.append('file ')
    if isbn:
        toRemove.append('isbn ')
        toRemove.append('issn ')
        toRemove.append('artic') # article id
        toRemove.append('doi =')
    if abstract:
        toRemove.append('abstr')

    try:
        with open(file) as f:
            newf = open(file+'new','w')
            for line in f:
                if line[0]=='@':
                    lastAt = re.findall('@\w+',line)[0]

                lineStart = line[0:5]
                # si le début de la ligne commence par ce qui est dans
                # la liste toRemove et que ce n'est pas pour un type @misc on enlève
                if lineStart in toRemove and not(lastAt == '@misc'):
                    print('removed : '+line)
                else:
                    newf.write(line)

        newf.close()
        f.close()
        os.remove(file)
        os.renames(file+'new',file)
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))

class Startui(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_main()
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('favicon.ico'))
        self.ui.setupUi(self)
        self.fname = ''
        QtCore.QObject.connect(self.ui.pushButton_load,QtCore.SIGNAL("clicked()"), self.file_dialog)
        QtCore.QObject.connect(self.ui.buttonBox,QtCore.SIGNAL('accepted()'), self.uiClean)


    def file_dialog(self):
        self.fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file','~')
        if os.path.isfile(self.fname):
            self.refresh()

    def uiClean(self):
        if os.path.isfile(self.fname):
            clean(self.fname,
            url=self.ui.checkBox_url.checkState(),
            fileR=self.ui.checkBox_file_location.checkState(),
            isbn=self.ui.checkBox_isbn.checkState(),
            abstract=self.ui.checkBox_abstract.checkState()
            )
            print('Cleaned')
            self.refresh()
        else:
            msgBox = QMessageBox();
            msgBox.setWindowTitle('CleanBib');
            msgBox.setText("Invalid file selected.");
            msgBox.setIcon(QMessageBox.Warning);
            msgBox.exec_();

    def refresh(self):
        f = open(self.fname, 'r')
        self.ui.textEdit_bibtex.setText(f.read())
        f.close()
        self.ui.FileEdit.setText(self.fname)





def main():
    app = QApplication(sys.argv)
    myapp = Startui()
    myapp.show()
    sys.exit(app.exec_())
    #    clean('My Collection.bib')

if __name__ == '__main__':
    main()
