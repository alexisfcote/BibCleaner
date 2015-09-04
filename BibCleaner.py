#!/usr/bin/python3
# ------------------------------------------------------------------------------
# Name:        CleanBib
# Purpose: Remove unwanted keys from a .bib file
#
# Author:      Alexis Fortin-Cote
#
# Created:     25/09/2014
# Copyright:   (c) Alexis Fortin-Cote 2014
# Licence:
# This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
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
import time
from threading import Thread
from PyQt4.QtGui import QApplication, QMainWindow, QMessageBox
from PyQt4 import QtCore, QtGui
from uiBibCleaner import Ui_main


def cleandict(file, customdict=None):
    """ Function that removes lines from a given file for which the starting word is contained in the passed dict
    :param file: Filename of the .bib to modify
    :param customdict: Dictionary of the tags to remove
    :return: none
    """
    if not customdict:
        customdict = {}
    try:
        with open(file, encoding="utf-8") as f, open(file + 'new', 'w', encoding="utf-8") as newf:
            lastat = []
            removing = False  # removing is set to 1 until a newkey is found. It is used to remove multiline entries
            for line in f:
                if line[0] == '@':
                    lastat = re.findall("@\w+", line)[0]
                    removing = False

                if line[0] == '}' and not re.findall(",", line):  # do not remove if the line contains just a } and no ,
                    removing = False

                found = re.findall("\w+\s*=", line)  # on trouve la clés
                if found:
                    removing = False
                    cle = found[0].replace(' ', '')[:-1]  # on enleve le = et l'espace
                    # si la cle dans customDict est à 1 et que ce n'est pas pour un type @misc on enlève
                    if cle not in customdict:
                        customdict[cle] = 0
                    if customdict[cle] and not (lastat == '@misc'):
                        print('removed : ' + line)
                        removing = True
                    else:
                        newf.write(line)
                elif not removing:
                    newf.write(line)

        os.remove(file)
        os.renames(file + 'new', file)
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))


class CleanBibUi(QMainWindow):
    def __init__(self, parent=None):
        """ QT ui """
        QMainWindow.__init__(self, parent)
        self.ui = Ui_main()
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('favicon.png'))
        self.ui.setupUi(self)

        # Variables
        self.fname = ''
        self.t = Thread(target=self.clean_timer)
        self.running = True
        self.t.deamon = True
        # ui custom checkbox
        self.ui.cblist = []

        # Charge les checkbox cochés par défaut
        default = self.load_default()
        self.cles = dict()
        for cle in default:
            self.cles[cle] = 1

        # Charge le last open file
        try:
            with open('config', 'r', encoding="utf-8") as f:
                fname = f.read()
            if os.path.isfile(fname):
                self.fname = fname
                self.refresh()
        except IOError:
            print('No recent file')
            pass

        #Connection
        QtCore.QObject.connect(self.ui.pushButton_load, QtCore.SIGNAL("clicked()"), self.file_dialog)
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Apply).clicked.connect(self.apply)
        QtCore.QObject.connect(self.ui.FileEdit, QtCore.SIGNAL("returnPressed()"), self.typed_filename)
        QtCore.QObject.connect(self.ui.pushButto_reload, QtCore.SIGNAL("clicked()"), self.refresh)

    def typed_filename(self):
        """ When changing filename from the textbox update self.fname """
        self.fname = self.ui.FileEdit.text()
        self.refresh()

    def file_dialog(self):
        """Main Gui Program"""
        dia = QtGui.QFileDialog()
        self.fname = QtGui.QFileDialog.getOpenFileName(dia, 'Open file', '~')
        with open('config', 'w+', encoding="utf-8") as f:
            f.write(self.fname)

        if os.path.isfile(self.fname):
            self.refresh()

    def uiclean(self):
        """ Verifies if the file exist and then call the cleandict funtion """
        self.update_checkbox()
        if os.path.isfile(self.fname):
            cleandict(self.fname, self.cles)
            print('Cleaned')
            self.refresh()
        else:
            self.msg_box_missing_file()

    def apply(self):
        self.uiclean()
        self.t.start()

    def clean_timer(self):
        while self.running:
            cleandict(self.fname, self.cles)
            print("Cleaned again " + self.fname)
            time.sleep(1)

    @staticmethod
    def msg_box_missing_file():
        """ Display a message saying that the file is invalid"""
        msgbox = QMessageBox()
        msgbox.setWindowTitle('CleanBib')
        msgbox.setText("Invalid file selected.")
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.exec_()

    def refresh(self):
        """ refresh and load the file and chekboxes """
        newcles = dict()
        if not os.path.isfile(self.fname):
            self.msg_box_missing_file()
            return

        with open(self.fname, 'r', encoding="utf-8") as f:
            self.ui.textEdit_bibtex.setText(f.read())  # on rempli le textbox avec le fichier
            f.seek(0)
            for line in f:
                # on ajoute les clés manquant dans le dictionnaire
                if not line[0] == '@':
                    found = re.findall('\w+ =', line)  # on trouve les clés
                    if found:
                        cle = found[0].replace(' ', '')[:-1]  # on enleve le = et l'espace
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

        self.ui.cblist = []
        i = 0
        # on crée les checkboxes des cles trouvés
        for cle in sorted(self.cles):
            self.ui.cblist.append(QtGui.QCheckBox(cle, self.ui.groupBox_custom))
            self.ui.cblist[i].setObjectName(cle)
            if self.cles[cle]:
                self.ui.cblist[i].setChecked(True)
            self.ui.verticalLayout_3.addWidget(self.ui.cblist[i])
            i += 1

    def update_checkbox(self):
        """ update the dictionary with new checked box"""
        i = 0
        for cb in self.ui.cblist:
            if cb.checkState():
                self.cles[cb.objectName()] = 1
            i += 1

    @staticmethod
    def load_default():
        """ Load the file containing the default checked box """
        try:
            f = open('Default', 'r', encoding="utf-8")
        except IOError:
            f = open('Default', 'w+', encoding="utf-8")
            f.write('url\nfile\nabstract\nurldate\nannote')
            f.seek(0, 0)

        list_default = []
        for line in f:
            if re.findall('\w+', line):
                list_default.append(line.replace('\n', ''))
        f.close()
        return list_default


def main():
    """
    Launch the GUI and the app
    """
    app = QApplication(sys.argv)
    myapp = CleanBibUi()
    myapp.show()
    #sys.exit(app.exec_())
    app.exec_()
    myapp.running = False


if __name__ == '__main__':
    main()
