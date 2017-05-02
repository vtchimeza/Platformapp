# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apo.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_number4vernon(object):
    def setupUi(self, number4vernon):
        number4vernon.setObjectName(_fromUtf8("number4vernon"))
        number4vernon.resize(400, 300)
        self.pushButton = QtGui.QPushButton(number4vernon)
        self.pushButton.setGeometry(QtCore.QRect(150, 230, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.label = QtGui.QLabel(number4vernon)
        self.label.setGeometry(QtCore.QRect(30, 0, 351, 201))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(number4vernon)
        QtCore.QMetaObject.connectSlotsByName(number4vernon)

    def retranslateUi(self, number4vernon):
        number4vernon.setWindowTitle(_translate("number4vernon", "vernon", None))
        self.pushButton.setText(_translate("number4vernon", "OK", None))
        self.label.setText(_translate("number4vernon", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">HEY big boy Urisei</span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\"> Greetings from </span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">WATTTAAA!!!</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    number4vernon = QtGui.QWidget()
    ui = Ui_number4vernon()
    ui.setupUi(number4vernon)
    number4vernon.show()
    sys.exit(app.exec_())

