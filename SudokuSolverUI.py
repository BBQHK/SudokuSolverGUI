# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SudokuSolverUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(288, 353)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(1)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setMaxLength(1)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setMaxLength(1)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setMaxLength(1)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setMaxLength(1)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(160, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setText("")
        self.lineEdit_6.setMaxLength(1)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(190, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setText("")
        self.lineEdit_7.setMaxLength(1)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(220, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setText("")
        self.lineEdit_8.setMaxLength(1)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(250, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setText("")
        self.lineEdit_9.setMaxLength(1)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(10, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setText("")
        self.lineEdit_10.setMaxLength(1)
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(40, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setText("")
        self.lineEdit_11.setMaxLength(1)
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(70, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setText("")
        self.lineEdit_12.setMaxLength(1)
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(100, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setText("")
        self.lineEdit_13.setMaxLength(1)
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(130, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setText("")
        self.lineEdit_14.setMaxLength(1)
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(160, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setText("")
        self.lineEdit_15.setMaxLength(1)
        self.lineEdit_15.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(190, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setText("")
        self.lineEdit_16.setMaxLength(1)
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setGeometry(QtCore.QRect(220, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setText("")
        self.lineEdit_17.setMaxLength(1)
        self.lineEdit_17.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_18.setGeometry(QtCore.QRect(250, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setText("")
        self.lineEdit_18.setMaxLength(1)
        self.lineEdit_18.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_19.setGeometry(QtCore.QRect(10, 70, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_19.setFont(font)
        self.lineEdit_19.setText("")
        self.lineEdit_19.setMaxLength(1)
        self.lineEdit_19.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_20.setGeometry(QtCore.QRect(40, 70, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_20.setFont(font)
        self.lineEdit_20.setText("")
        self.lineEdit_20.setMaxLength(1)
        self.lineEdit_20.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_21.setGeometry(QtCore.QRect(70, 70, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_21.setFont(font)
        self.lineEdit_21.setText("")
        self.lineEdit_21.setMaxLength(1)
        self.lineEdit_21.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_22.setGeometry(QtCore.QRect(100, 70, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setText("")
        self.lineEdit_22.setMaxLength(1)
        self.lineEdit_22.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_23.setGeometry(QtCore.QRect(130, 70, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_23.setFont(font)
        self.lineEdit_23.setText("")
        self.lineEdit_23.setMaxLength(1)
        self.lineEdit_23.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_24.setGeometry(QtCore.QRect(160, 70, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_24.setFont(font)
        self.lineEdit_24.setText("")
        self.lineEdit_24.setMaxLength(1)
        self.lineEdit_24.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_25.setGeometry(QtCore.QRect(190, 70, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_25.setFont(font)
        self.lineEdit_25.setText("")
        self.lineEdit_25.setMaxLength(1)
        self.lineEdit_25.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_26.setGeometry(QtCore.QRect(220, 70, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_26.setFont(font)
        self.lineEdit_26.setText("")
        self.lineEdit_26.setMaxLength(1)
        self.lineEdit_26.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_27.setGeometry(QtCore.QRect(250, 70, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_27.setFont(font)
        self.lineEdit_27.setText("")
        self.lineEdit_27.setMaxLength(1)
        self.lineEdit_27.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_28.setGeometry(QtCore.QRect(10, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_28.setFont(font)
        self.lineEdit_28.setText("")
        self.lineEdit_28.setMaxLength(1)
        self.lineEdit_28.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_29.setGeometry(QtCore.QRect(40, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_29.setFont(font)
        self.lineEdit_29.setText("")
        self.lineEdit_29.setMaxLength(1)
        self.lineEdit_29.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_30.setGeometry(QtCore.QRect(70, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_30.setFont(font)
        self.lineEdit_30.setText("")
        self.lineEdit_30.setMaxLength(1)
        self.lineEdit_30.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_31.setGeometry(QtCore.QRect(100, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_31.setFont(font)
        self.lineEdit_31.setText("")
        self.lineEdit_31.setMaxLength(1)
        self.lineEdit_31.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_32.setGeometry(QtCore.QRect(130, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_32.setFont(font)
        self.lineEdit_32.setText("")
        self.lineEdit_32.setMaxLength(1)
        self.lineEdit_32.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_33.setGeometry(QtCore.QRect(160, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_33.setFont(font)
        self.lineEdit_33.setText("")
        self.lineEdit_33.setMaxLength(1)
        self.lineEdit_33.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_34.setGeometry(QtCore.QRect(190, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_34.setFont(font)
        self.lineEdit_34.setText("")
        self.lineEdit_34.setMaxLength(1)
        self.lineEdit_34.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.lineEdit_35 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_35.setGeometry(QtCore.QRect(220, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_35.setFont(font)
        self.lineEdit_35.setText("")
        self.lineEdit_35.setMaxLength(1)
        self.lineEdit_35.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.lineEdit_36 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_36.setGeometry(QtCore.QRect(250, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_36.setFont(font)
        self.lineEdit_36.setText("")
        self.lineEdit_36.setMaxLength(1)
        self.lineEdit_36.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.lineEdit_37 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_37.setGeometry(QtCore.QRect(10, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_37.setFont(font)
        self.lineEdit_37.setText("")
        self.lineEdit_37.setMaxLength(1)
        self.lineEdit_37.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_38.setGeometry(QtCore.QRect(40, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_38.setFont(font)
        self.lineEdit_38.setText("")
        self.lineEdit_38.setMaxLength(1)
        self.lineEdit_38.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.lineEdit_39 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_39.setGeometry(QtCore.QRect(70, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_39.setFont(font)
        self.lineEdit_39.setText("")
        self.lineEdit_39.setMaxLength(1)
        self.lineEdit_39.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_40.setGeometry(QtCore.QRect(100, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_40.setFont(font)
        self.lineEdit_40.setText("")
        self.lineEdit_40.setMaxLength(1)
        self.lineEdit_40.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.lineEdit_41 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_41.setGeometry(QtCore.QRect(130, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_41.setFont(font)
        self.lineEdit_41.setText("")
        self.lineEdit_41.setMaxLength(1)
        self.lineEdit_41.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.lineEdit_42 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_42.setGeometry(QtCore.QRect(160, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_42.setFont(font)
        self.lineEdit_42.setText("")
        self.lineEdit_42.setMaxLength(1)
        self.lineEdit_42.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_43.setGeometry(QtCore.QRect(190, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_43.setFont(font)
        self.lineEdit_43.setText("")
        self.lineEdit_43.setMaxLength(1)
        self.lineEdit_43.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.lineEdit_44 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_44.setGeometry(QtCore.QRect(220, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_44.setFont(font)
        self.lineEdit_44.setText("")
        self.lineEdit_44.setMaxLength(1)
        self.lineEdit_44.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.lineEdit_45 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_45.setGeometry(QtCore.QRect(250, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_45.setFont(font)
        self.lineEdit_45.setText("")
        self.lineEdit_45.setMaxLength(1)
        self.lineEdit_45.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.lineEdit_46 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_46.setGeometry(QtCore.QRect(10, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_46.setFont(font)
        self.lineEdit_46.setText("")
        self.lineEdit_46.setMaxLength(1)
        self.lineEdit_46.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.lineEdit_47 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_47.setGeometry(QtCore.QRect(40, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_47.setFont(font)
        self.lineEdit_47.setText("")
        self.lineEdit_47.setMaxLength(1)
        self.lineEdit_47.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.lineEdit_48 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_48.setGeometry(QtCore.QRect(70, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_48.setFont(font)
        self.lineEdit_48.setText("")
        self.lineEdit_48.setMaxLength(1)
        self.lineEdit_48.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_48.setObjectName("lineEdit_48")
        self.lineEdit_49 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_49.setGeometry(QtCore.QRect(100, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_49.setFont(font)
        self.lineEdit_49.setText("")
        self.lineEdit_49.setMaxLength(1)
        self.lineEdit_49.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_49.setObjectName("lineEdit_49")
        self.lineEdit_50 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_50.setGeometry(QtCore.QRect(130, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_50.setFont(font)
        self.lineEdit_50.setText("")
        self.lineEdit_50.setMaxLength(1)
        self.lineEdit_50.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_50.setObjectName("lineEdit_50")
        self.lineEdit_51 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_51.setGeometry(QtCore.QRect(160, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_51.setFont(font)
        self.lineEdit_51.setText("")
        self.lineEdit_51.setMaxLength(1)
        self.lineEdit_51.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_51.setObjectName("lineEdit_51")
        self.lineEdit_52 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_52.setGeometry(QtCore.QRect(190, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_52.setFont(font)
        self.lineEdit_52.setText("")
        self.lineEdit_52.setMaxLength(1)
        self.lineEdit_52.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.lineEdit_53 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_53.setGeometry(QtCore.QRect(220, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_53.setFont(font)
        self.lineEdit_53.setText("")
        self.lineEdit_53.setMaxLength(1)
        self.lineEdit_53.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.lineEdit_54 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_54.setGeometry(QtCore.QRect(250, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_54.setFont(font)
        self.lineEdit_54.setText("")
        self.lineEdit_54.setMaxLength(1)
        self.lineEdit_54.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_54.setObjectName("lineEdit_54")
        self.lineEdit_55 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_55.setGeometry(QtCore.QRect(10, 190, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_55.setFont(font)
        self.lineEdit_55.setText("")
        self.lineEdit_55.setMaxLength(1)
        self.lineEdit_55.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_55.setObjectName("lineEdit_55")
        self.lineEdit_56 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_56.setGeometry(QtCore.QRect(40, 190, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_56.setFont(font)
        self.lineEdit_56.setText("")
        self.lineEdit_56.setMaxLength(1)
        self.lineEdit_56.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_56.setObjectName("lineEdit_56")
        self.lineEdit_57 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_57.setGeometry(QtCore.QRect(70, 190, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_57.setFont(font)
        self.lineEdit_57.setText("")
        self.lineEdit_57.setMaxLength(1)
        self.lineEdit_57.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_57.setObjectName("lineEdit_57")
        self.lineEdit_58 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_58.setGeometry(QtCore.QRect(100, 190, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_58.setFont(font)
        self.lineEdit_58.setText("")
        self.lineEdit_58.setMaxLength(1)
        self.lineEdit_58.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_58.setObjectName("lineEdit_58")
        self.lineEdit_59 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_59.setGeometry(QtCore.QRect(130, 190, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_59.setFont(font)
        self.lineEdit_59.setText("")
        self.lineEdit_59.setMaxLength(1)
        self.lineEdit_59.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_59.setObjectName("lineEdit_59")
        self.lineEdit_60 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_60.setGeometry(QtCore.QRect(160, 190, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_60.setFont(font)
        self.lineEdit_60.setText("")
        self.lineEdit_60.setMaxLength(1)
        self.lineEdit_60.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_60.setObjectName("lineEdit_60")
        self.lineEdit_61 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_61.setGeometry(QtCore.QRect(190, 190, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_61.setFont(font)
        self.lineEdit_61.setText("")
        self.lineEdit_61.setMaxLength(1)
        self.lineEdit_61.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_61.setObjectName("lineEdit_61")
        self.lineEdit_62 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_62.setGeometry(QtCore.QRect(220, 190, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_62.setFont(font)
        self.lineEdit_62.setText("")
        self.lineEdit_62.setMaxLength(1)
        self.lineEdit_62.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_62.setObjectName("lineEdit_62")
        self.lineEdit_63 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_63.setGeometry(QtCore.QRect(250, 190, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_63.setFont(font)
        self.lineEdit_63.setText("")
        self.lineEdit_63.setMaxLength(1)
        self.lineEdit_63.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_63.setObjectName("lineEdit_63")
        self.lineEdit_64 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_64.setGeometry(QtCore.QRect(10, 220, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_64.setFont(font)
        self.lineEdit_64.setText("")
        self.lineEdit_64.setMaxLength(1)
        self.lineEdit_64.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_64.setObjectName("lineEdit_64")
        self.lineEdit_65 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_65.setGeometry(QtCore.QRect(40, 220, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_65.setFont(font)
        self.lineEdit_65.setText("")
        self.lineEdit_65.setMaxLength(1)
        self.lineEdit_65.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_65.setObjectName("lineEdit_65")
        self.lineEdit_66 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_66.setGeometry(QtCore.QRect(70, 220, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_66.setFont(font)
        self.lineEdit_66.setText("")
        self.lineEdit_66.setMaxLength(1)
        self.lineEdit_66.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_66.setObjectName("lineEdit_66")
        self.lineEdit_67 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_67.setGeometry(QtCore.QRect(100, 220, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_67.setFont(font)
        self.lineEdit_67.setText("")
        self.lineEdit_67.setMaxLength(1)
        self.lineEdit_67.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_67.setObjectName("lineEdit_67")
        self.lineEdit_68 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_68.setGeometry(QtCore.QRect(130, 220, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_68.setFont(font)
        self.lineEdit_68.setText("")
        self.lineEdit_68.setMaxLength(1)
        self.lineEdit_68.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_68.setObjectName("lineEdit_68")
        self.lineEdit_69 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_69.setGeometry(QtCore.QRect(160, 220, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_69.setFont(font)
        self.lineEdit_69.setText("")
        self.lineEdit_69.setMaxLength(1)
        self.lineEdit_69.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_69.setObjectName("lineEdit_69")
        self.lineEdit_70 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_70.setGeometry(QtCore.QRect(190, 220, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_70.setFont(font)
        self.lineEdit_70.setText("")
        self.lineEdit_70.setMaxLength(1)
        self.lineEdit_70.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_70.setObjectName("lineEdit_70")
        self.lineEdit_71 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_71.setGeometry(QtCore.QRect(220, 220, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_71.setFont(font)
        self.lineEdit_71.setText("")
        self.lineEdit_71.setMaxLength(1)
        self.lineEdit_71.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_71.setObjectName("lineEdit_71")
        self.lineEdit_72 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_72.setGeometry(QtCore.QRect(250, 220, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_72.setFont(font)
        self.lineEdit_72.setText("")
        self.lineEdit_72.setMaxLength(1)
        self.lineEdit_72.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_72.setObjectName("lineEdit_72")
        self.lineEdit_73 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_73.setGeometry(QtCore.QRect(10, 250, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_73.setFont(font)
        self.lineEdit_73.setText("")
        self.lineEdit_73.setMaxLength(1)
        self.lineEdit_73.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_73.setObjectName("lineEdit_73")
        self.lineEdit_74 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_74.setGeometry(QtCore.QRect(40, 250, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_74.setFont(font)
        self.lineEdit_74.setText("")
        self.lineEdit_74.setMaxLength(1)
        self.lineEdit_74.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_74.setObjectName("lineEdit_74")
        self.lineEdit_75 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_75.setGeometry(QtCore.QRect(70, 250, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_75.setFont(font)
        self.lineEdit_75.setText("")
        self.lineEdit_75.setMaxLength(1)
        self.lineEdit_75.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_75.setObjectName("lineEdit_75")
        self.lineEdit_76 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_76.setGeometry(QtCore.QRect(100, 250, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_76.setFont(font)
        self.lineEdit_76.setText("")
        self.lineEdit_76.setMaxLength(1)
        self.lineEdit_76.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_76.setObjectName("lineEdit_76")
        self.lineEdit_77 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_77.setGeometry(QtCore.QRect(130, 250, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_77.setFont(font)
        self.lineEdit_77.setText("")
        self.lineEdit_77.setMaxLength(1)
        self.lineEdit_77.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_77.setObjectName("lineEdit_77")
        self.lineEdit_78 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_78.setGeometry(QtCore.QRect(160, 250, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_78.setFont(font)
        self.lineEdit_78.setText("")
        self.lineEdit_78.setMaxLength(1)
        self.lineEdit_78.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_78.setObjectName("lineEdit_78")
        self.lineEdit_79 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_79.setGeometry(QtCore.QRect(190, 250, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_79.setFont(font)
        self.lineEdit_79.setText("")
        self.lineEdit_79.setMaxLength(1)
        self.lineEdit_79.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_79.setObjectName("lineEdit_79")
        self.lineEdit_80 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_80.setGeometry(QtCore.QRect(220, 250, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_80.setFont(font)
        self.lineEdit_80.setText("")
        self.lineEdit_80.setMaxLength(1)
        self.lineEdit_80.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_80.setObjectName("lineEdit_80")
        self.lineEdit_81 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_81.setGeometry(QtCore.QRect(250, 250, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_81.setFont(font)
        self.lineEdit_81.setText("")
        self.lineEdit_81.setMaxLength(1)
        self.lineEdit_81.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_81.setObjectName("lineEdit_81")
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(130, 290, 75, 23))
        self.resetButton.setStyleSheet("background-color : #ff9999")
        self.resetButton.setObjectName("resetButton")
        self.solveButton = QtWidgets.QPushButton(self.centralwidget)
        self.solveButton.setGeometry(QtCore.QRect(210, 290, 75, 23))
        self.solveButton.setStyleSheet("background-color : #99ffcc")
        self.solveButton.setObjectName("solveButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 288, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SudokuSolver"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.solveButton.setText(_translate("MainWindow", "Solve"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())