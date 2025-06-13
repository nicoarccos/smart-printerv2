# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'escaneo-windowIEEzYD.ui'
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
    QLabel, QLineEdit, QSizePolicy, QSpinBox,
    QWidget)

class Ui_SubVentEscaneo(object):
    def setupUi(self, SubVentEscaneo):
        if not SubVentEscaneo.objectName():
            SubVentEscaneo.setObjectName(u"SubVentEscaneo")
        SubVentEscaneo.resize(638, 378)
        self.buttonBox = QDialogButtonBox(SubVentEscaneo)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(430, 340, 191, 24))
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.ip_inicial = QLineEdit(SubVentEscaneo)
        self.ip_inicial.setObjectName(u"ip_inicial")
        self.ip_inicial.setGeometry(QRect(130, 160, 191, 21))
        self.ip_final = QLineEdit(SubVentEscaneo)
        self.ip_final.setObjectName(u"ip_final")
        self.ip_final.setGeometry(QRect(130, 230, 191, 21))
        self.spinBox = QSpinBox(SubVentEscaneo)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(130, 310, 51, 20))
        self.checkBox = QCheckBox(SubVentEscaneo)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(130, 99, 111, 31))
        self.label = QLabel(SubVentEscaneo)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 10, 301, 51))
        font = QFont()
        font.setFamilies([u"Sylfaen"])
        font.setPointSize(20)
        self.label.setFont(font)
        self.label_2 = QLabel(SubVentEscaneo)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 150, 81, 41))
        font1 = QFont()
        font1.setFamilies([u"Sylfaen"])
        font1.setPointSize(14)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(SubVentEscaneo)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 220, 81, 41))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(SubVentEscaneo)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 305, 81, 31))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(SubVentEscaneo)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 100, 81, 31))
        self.label_5.setFont(font1)

        self.retranslateUi(SubVentEscaneo)

        QMetaObject.connectSlotsByName(SubVentEscaneo)
    # setupUi

    def retranslateUi(self, SubVentEscaneo):
        SubVentEscaneo.setWindowTitle(QCoreApplication.translate("SubVentEscaneo", u"Form", None))
        self.checkBox.setText(QCoreApplication.translate("SubVentEscaneo", u"Solo 1 Impresora", None))
        self.label.setText(QCoreApplication.translate("SubVentEscaneo", u"Configuraci\u00f3n de Escaneo", None))
        self.label_2.setText(QCoreApplication.translate("SubVentEscaneo", u"IP Inicial", None))
        self.label_3.setText(QCoreApplication.translate("SubVentEscaneo", u"IP Final", None))
        self.label_4.setText(QCoreApplication.translate("SubVentEscaneo", u"Hilos", None))
        self.label_5.setText(QCoreApplication.translate("SubVentEscaneo", u"Escaneo", None))
    # retranslateUi




class Escaneo(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SubVentEscaneo()
        self.ui.setupUi(self)