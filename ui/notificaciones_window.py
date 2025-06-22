# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notificaciones-windowgAkDWW.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialogButtonBox,QHBoxLayout,
    QFrame, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1061, 646)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 1039, 619))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.buttonBox = QDialogButtonBox(self.frame_2)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(800, 570, 191, 23))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(370, 10, 281, 41))
        font = QFont()
        font.setFamily(u"Sylfaen")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 60, 951, 491))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(30, 30, 361, 451))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 330, 121, 51))
        self.label_4.setFont(font)
        self.ip_final_7 = QLineEdit(self.frame_4)
        self.ip_final_7.setObjectName(u"ip_final_7")
        self.ip_final_7.setGeometry(QRect(160, 340, 171, 21))
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 250, 111, 41))
        self.label_3.setFont(font)
        self.ip_final_6 = QLineEdit(self.frame_4)
        self.ip_final_6.setObjectName(u"ip_final_6")
        self.ip_final_6.setGeometry(QRect(160, 260, 171, 21))
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 170, 121, 41))
        self.label_5.setFont(font)
        self.ip_final = QLineEdit(self.frame_4)
        self.ip_final.setObjectName(u"ip_final")
        self.ip_final.setGeometry(QRect(160, 180, 51, 21))
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 90, 141, 41))
        self.label_2.setFont(font)
        self.ip_final_4 = QLineEdit(self.frame_4)
        self.ip_final_4.setObjectName(u"ip_final_4")
        self.ip_final_4.setGeometry(QRect(160, 100, 171, 21))
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(560, 30, 361, 451))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 330, 131, 51))
        self.label_6.setFont(font)
        self.ip_final_8 = QLineEdit(self.frame_5)
        self.ip_final_8.setObjectName(u"ip_final_8")
        self.ip_final_8.setGeometry(QRect(160, 340, 171, 21))
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 250, 121, 41))
        self.label_7.setFont(font)
        self.ip_final_9 = QLineEdit(self.frame_5)
        self.ip_final_9.setObjectName(u"ip_final_9")
        self.ip_final_9.setGeometry(QRect(160, 260, 171, 21))
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 170, 121, 41))
        self.label_9.setFont(font)
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 90, 141, 41))
        self.label_10.setFont(font)
        self.ip_final_5 = QLineEdit(self.frame_5)
        self.ip_final_5.setObjectName(u"ip_final_5")
        self.ip_final_5.setGeometry(QRect(160, 100, 171, 21))
        self.ip_final_10 = QLineEdit(self.frame_5)
        self.ip_final_10.setObjectName(u"ip_final_10")
        self.ip_final_10.setGeometry(QRect(160, 180, 171, 21))

        self.horizontalLayout_5.addWidget(self.frame_2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Configuraci\u00f3n de Notificaciones", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Usuario", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Puerto SMTP", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Servidor SMTP", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Destinatario4", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Destinatario 3", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Destinatario 2", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Destinatario 1", None))







class Notificaciones(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form ()
        self.ui.setupUi(self)