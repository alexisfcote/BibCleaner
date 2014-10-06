#!/usr/bin/python3
#------------------------------------------------------------------------------
# Name:        CleanBib
# Purpose: Remove unwanted keys from a .bib file
#
# Author:      Alexis Fortin-Cote
#
# Created:     25/09/2014
# Copyright:   (c) Alexis Fortin-Cote 2014
# Licence:
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#------------------------------------------------------------------------------
import re
import os
import sys
from PyQt4.QtGui import QApplication, QMainWindow, QMessageBox
from PyQt4 import QtCore, QtGui
from BibCleaner.uiBibCleaner import Ui_main




def cleanDict(file, customDict=dict()):
    try:
        with open(file) as f:
            newf = open(file+'new','w')
            for line in f:
                if line[0]=='@':
                    lastAt = re.findall('@\w+',line)[0]

                found = re.findall('\w+\ =',line) # on trouve la clés
                if found:
                    cle = found[0].replace(' ', '')[:-1] # on enleve le = et l'espace
                    # si la cle dans customDict est à 1 et que ce n'est pas pour un type @misc on enlève
                    if customDict[cle] and not(lastAt == '@misc'):
                        print('removed : '+line)
                    else:
                        newf.write(line)
                else:
                    newf.write(line)

        newf.close()
        f.close()
        os.remove(file)
        os.renames(file+'new',file)
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))

class Startui(QMainWindow):
    def __init__(self, parent=None):
        # QT ui
        QMainWindow.__init__(self, parent)
        self.ui = Ui_main()
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('favicon.ico'))
        self.ui.setupUi(self)

        # Variables
        self.fname = ''
        # ui custom checkbox
        self.ui.cblist = []

        # Charge les checkbox cochés par défaut
        default = self.load_Default()
        self.cles = dict()
        for cle in default:
            self.cles[cle] = 1

        # Charge le last open file
        try:
            with open('config', 'r') as f:
                fname = f.read()
            if os.path.isfile(fname):
                self.fname = fname
                self.refresh()
        except IOError:
            print('No recent file')
            pass


        #Connection
        QtCore.QObject.connect(self.ui.pushButton_load,QtCore.SIGNAL("clicked()"), self.file_dialog)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Apply).clicked.connect(self.uiClean)
        #QtCore.QObject.connect(self.ui.buttonBox,QtCore.SIGNAL('clicked (QAbstractButton*)'), self.uiClean)


    def file_dialog(self):
        self.fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file','~')
        with open('config', 'w+') as f:
            f.write(self.fname)

        if os.path.isfile(self.fname):
            self.refresh()

    def uiClean(self):
        self.update_checkbox()
        if os.path.isfile(self.fname):
            cleanDict(self.fname, self.cles)
            print('Cleaned')
            self.refresh()
        else:
            msgBox = QMessageBox();
            msgBox.setWindowTitle('CleanBib');
            msgBox.setText("Invalid file selected.");
            msgBox.setIcon(QMessageBox.Warning);
            msgBox.exec_();

    def refresh(self):
        newcles = dict()
        with open(self.fname, 'r') as f:
            self.ui.textEdit_bibtex.setText(f.read()) # on rempli le textbox avec le fichier
            f.seek(0)
            for line in f:
                # on ajoute les clés manquant dans le dictionnaire
                if not line[0]=='@':
                    found = re.findall('\w+\ =',line) # on trouve les clés
                    if found:
                        cle = found[0].replace(' ', '')[:-1] # on enleve le = et l'espace
                        if not cle in newcles:
                            newcles[cle] = 0
        # on ajoute les nouvelles cles et on reprend conserve les anciennes si elles existents toujours
        for cle in newcles:
            if cle in self.cles:
                newcles[cle] = self.cles[cle]
        self.cles = newcles

        self.ui.FileEdit.setText(self.fname)

        for checkbox in self.ui.cblist:
            checkbox.deleteLater()

        self.ui.cblist = [];
        i=0
        # on crée les checkboxes des cles trouvés
        for cle in sorted(self.cles):
            self.ui.cblist.append(QtGui.QCheckBox(cle, self.ui.groupBox_custom))
            self.ui.cblist[i].setObjectName(cle)
            if self.cles[cle]:
                self.ui.cblist[i].setChecked(True)
            self.ui.verticalLayout_3.addWidget(self.ui.cblist[i])
            i = i+1


    def update_checkbox(self):
        i=0
        for cb in self.ui.cblist:
            if cb.checkState():
                self.cles[cb.objectName()] = 1
            i=i+1

    @staticmethod
    def load_Default():
        try:
            f = open('Default', 'r')
        except IOError:
            f = open('Default', 'w+')
            f.write('url\nisbn\nissn\nfile\ndoi\nabstract\nurldate')
            f.seek(0, 0)

        list = []
        for line in f:
            if re.findall('\w+', line):
                list.append(line.replace('\n', ''))
        f.close()
        return list









def main():
    app = QApplication(sys.argv)
    myapp = Startui()
    myapp.show()
    sys.exit(app.exec_())
    #    clean('My Collection.bib')

if __name__ == '__main__':
    main()
