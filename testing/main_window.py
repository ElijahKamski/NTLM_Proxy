# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            Qt)
from PySide6.QtWidgets import (QGridLayout, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QSpacerItem,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(529, 381)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 10, 521, 361))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 3, 1, 1)

        self.ConnectButton = QPushButton(self.gridLayoutWidget)
        self.ConnectButton.setObjectName(u"ConnectButton")

        self.gridLayout.addWidget(self.ConnectButton, 6, 3, 1, 1)

        self.PasswordField = QLineEdit(self.gridLayoutWidget)
        self.PasswordField.setObjectName(u"PasswordField")
        self.PasswordField.setInputMethodHints(Qt.ImhHiddenText)

        self.gridLayout.addWidget(self.PasswordField, 4, 3, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 3, 1, 1)

        self.LoginField = QLineEdit(self.gridLayoutWidget)
        self.LoginField.setObjectName(u"LoginField")

        self.gridLayout.addWidget(self.LoginField, 3, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 6, 4, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 6, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 7, 3, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.DomainField = QLineEdit(self.gridLayoutWidget)
        self.DomainField.setObjectName(u"DomainField")

        self.gridLayout.addWidget(self.DomainField, 2, 3, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.ProxyPortField = QLineEdit(self.gridLayoutWidget)
        self.ProxyPortField.setObjectName(u"ProxyPortField")

        self.gridLayout.addWidget(self.ProxyPortField, 1, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.ProxyPortField, self.DomainField)
        QWidget.setTabOrder(self.DomainField, self.LoginField)
        QWidget.setTabOrder(self.LoginField, self.PasswordField)
        QWidget.setTabOrder(self.PasswordField, self.ConnectButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ConnectButton.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043f\u0440\u043e\u043a\u0441\u0438",
                                                              None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u0435\u043d", None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u0418\u043c\u044f \u043f\u0440\u043e\u043a\u0441\u0438:\u043f\u043e\u0440\u0442",
                                                      None))
    # retranslateUi
