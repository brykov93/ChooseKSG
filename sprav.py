# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sprav.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys,os
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

class MyTableModel(QtCore.QAbstractTableModel): 
    def __init__(self, datain, headerdata, parent=None, *args): 
        """ datain: a list of lists
            headerdata: a list of strings
        """
        QtCore.QAbstractTableModel.__init__(self, parent, *args) 
        self.arraydata = datain
        self.headerdata = headerdata
 
    def rowCount(self, parent): 
        return len(self.arraydata) 
 
    def columnCount(self, parent): 
        return len(self.arraydata[0]) 
 
    def data(self, index, role): 
        if not index.isValid(): 
            return QtCore.QVariant() 
        elif role != QtCore.Qt.DisplayRole: 
            return QtCore.QVariant() 
        return QtCore.QVariant(self.arraydata[index.row()][index.column()]) 

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self.headerdata[col])
        return QtCore.QVariant()

    def sort(self, Ncol, order):
        """Sort table by given column number.
        """
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.arraydata = sorted(self.arraydata, key=operator.itemgetter(Ncol))        
        if order == Qt.DescendingOrder:
            self.arraydata.reverse()
        self.emit(SIGNAL("layoutChanged()"))


class Ui_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.setupUi()    
    def setupUi(self):
        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(1080, 849)
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.LineEdit=QtGui.QLineEdit(self)
        self.LineEdit.setObjectName(_fromUtf8("LineEdit"))
        self.verticalLayout.addWidget(self.LineEdit)
        #self.proxy = QtGui.QSortFilterProxyModel(self)
        #self.proxy.setSourceModel(self.tableWidget.model())
        
        self.tableWidget = QtGui.QTableView(self)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        #self.tableWidget.setColumnCount(3)
        #self.tableWidget.setRowCount(3)
        self.verticalLayout.addWidget(self.tableWidget)
        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        
        header=['1','2','3']
        data=[[0,0,0],[1,1,1],[2,2,2]]
        self.tm = MyTableModel(data, header, self) 
        self.filter_proxy_model = QtGui.QSortFilterProxyModel()
        self.filter_proxy_model.setSourceModel(self.tm)
        self.LineEdit.textChanged.connect(self.filter_proxy_model.setFilterRegExp)
        self.tableWidget.setModel(self.filter_proxy_model)
        self.tableWidget.resizeColumnsToContents()
        
        self.retranslateUi()
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()
    


        return None
    def retranslateUi(self):
        self.setWindowTitle(_translate("Dialog", "Dialog", None))

def main(): 
    app = QtGui.QApplication( sys.argv )  
    QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName("UTF-8"))
    ex = Ui_Dialog()
    sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()