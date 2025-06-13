# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alarmas-windowCwyaxX.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialogButtonBox,
    QFrame, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_SubVentAlarmas(object):
    def setupUi(self, SubVentAlarmas):
        if not SubVentAlarmas.objectName():
            SubVentAlarmas.setObjectName(u"SubVentAlarmas")
        SubVentAlarmas.resize(981, 630)
        self.frame_2 = QFrame(SubVentAlarmas)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(40, 10, 841, 501))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 20, 311, 41))
        font = QFont()
        font.setFamilies([u"Sylfaen"])
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QFrame.Shape.WinPanel)
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 90, 71, 51))
        font1 = QFont()
        font1.setFamilies([u"Sylfaen"])
        font1.setPointSize(14)
        self.label_10.setFont(font1)
        self.label_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 150, 251, 51))
        self.label_11.setFont(font1)
        self.label_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.checkBox_7 = QCheckBox(self.frame_2)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(90, 100, 111, 31))
        self.checkBox_7.setStyleSheet(u"self.checkBox.setStyleSheet(\"QCheckBox::indicator { width: 20px; height: 20px; border: 1px solid black; }\")\n"
"")
        self.checkBox_5 = QCheckBox(self.frame_2)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(220, 100, 101, 31))
        self.checkBox_8 = QCheckBox(self.frame_2)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setGeometry(QRect(290, 160, 51, 31))
        self.checkBox_8.setStyleSheet(u"self.checkBox.setStyleSheet(\"QCheckBox::indicator { width: 20px; height: 20px; border: 1px solid black; }\")\n"
"")
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 220, 151, 31))
        self.label_12.setFont(font1)
        self.label_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.lineEdit_5 = QLineEdit(self.frame_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(200, 225, 61, 21))
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 280, 171, 31))
        self.label_13.setFont(font1)
        self.label_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.label_13.setFrameShadow(QFrame.Shadow.Plain)
        self.lineEdit_6 = QLineEdit(self.frame_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(200, 285, 61, 21))
        self.lineEdit_6.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_6.setClearButtonEnabled(False)
        self.checkBox_9 = QCheckBox(self.frame_2)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setGeometry(QRect(370, 160, 51, 31))
        self.checkBox_9.setStyleSheet(u"self.checkBox.setStyleSheet(\"QCheckBox::indicator { width: 20px; height: 20px; border: 1px solid black; }\")\n"
"")
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 340, 141, 31))
        self.label_14.setFont(font1)
        self.label_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.checkBox_6 = QCheckBox(self.frame_2)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(180, 340, 111, 31))
        self.checkBox_10 = QCheckBox(self.frame_2)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setGeometry(QRect(300, 340, 121, 31))
        self.buttonBox_3 = QDialogButtonBox(self.frame_2)
        self.buttonBox_3.setObjectName(u"buttonBox_3")
        self.buttonBox_3.setGeometry(QRect(630, 450, 201, 41))
        self.buttonBox_3.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox = QDialogButtonBox(SubVentAlarmas)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(665, 953, 201, 41))
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.retranslateUi(SubVentAlarmas)

        QMetaObject.connectSlotsByName(SubVentAlarmas)
    # setupUi

    def retranslateUi(self, SubVentAlarmas):
        SubVentAlarmas.setWindowTitle(QCoreApplication.translate("SubVentAlarmas", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("SubVentAlarmas", u"Configuraci\u00f3n de Alarmas", None))
        self.label_10.setText(QCoreApplication.translate("SubVentAlarmas", u"Estado", None))
        self.label_11.setText(QCoreApplication.translate("SubVentAlarmas", u"Habilitar Alertas de Escritorio", None))
        self.checkBox_7.setText(QCoreApplication.translate("SubVentAlarmas", u"  Encendido", None))
        self.checkBox_5.setText(QCoreApplication.translate("SubVentAlarmas", u"Sin Conexion", None))
        self.checkBox_8.setText(QCoreApplication.translate("SubVentAlarmas", u" Si", None))
        self.label_12.setText(QCoreApplication.translate("SubVentAlarmas", u"Umbral de Tinta", None))
        self.label_13.setText(QCoreApplication.translate("SubVentAlarmas", u"Paginas Disponibles", None))
        self.checkBox_9.setText(QCoreApplication.translate("SubVentAlarmas", u" No", None))
        self.label_14.setText(QCoreApplication.translate("SubVentAlarmas", u"\u00daltimo Escaneo", None))
        self.checkBox_6.setText(QCoreApplication.translate("SubVentAlarmas", u"Habilitar", None))
        self.checkBox_10.setText(QCoreApplication.translate("SubVentAlarmas", u"Deshabilitar", None))
    # retranslateUi












class AlarmaWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SubVentAlarmas()
        self.ui.setupUi(self)