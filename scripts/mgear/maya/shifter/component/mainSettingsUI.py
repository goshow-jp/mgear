# MGEAR is under the terms of the MIT License
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Jeremie Passerin, Miquel Campos

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Author:     Jeremie Passerin      geerem@hotmail.com  www.jeremiepasserin.com
# Author:     Miquel Campos         hello@miquel-campos.com  www.miquel-campos.com
# Date:       2016 / 10 / 10

import mgear.maya.pyqt as gqt
try:
    from PySide import QtGui, QtCore
    import PySide.QtGui as QtWidgets
    from PySide.QtGui import QSizePolicy
    from PySide.QtGui import QGroupBox
    from PySide.QtGui import QWidget
    from PySide.QtGui import QVBoxLayout
    from PySide.QtGui import QGridLayout
    from PySide.QtGui import QListWidget
    from PySide.QtGui import QAbstractItemView
    from PySide.QtGui import QListView
    from PySide.QtGui import QPushButton
    from PySide.QtGui import QHBoxLayout
    from PySide.QtGui import QSpacerItem
    from PySide.QtGui import QApplication
    from PySide.QtGui import QMessageBox
    from PySide.QtGui import QInputDialog
    from PySide.QtGui import QLineEdit
    from PySide.QtGui import *
    from shiboken import wrapInstance

except ImportError:
    from PySide2 import QtGui, QtCore, QtWidgets
    from PySide2.QtWidgets import QSizePolicy
    from PySide2.QtWidgets import QGroupBox
    from PySide2.QtWidgets import QWidget

    from PySide2.QtWidgets import QVBoxLayout
    from PySide2.QtWidgets import QGridLayout
    from PySide2.QtWidgets import QListWidget
    from PySide2.QtWidgets import QAbstractItemView
    from PySide2.QtWidgets import QListView
    from PySide2.QtWidgets import QPushButton
    from PySide2.QtWidgets import QHBoxLayout
    from PySide2.QtWidgets import QSpacerItem
    from PySide2.QtWidgets import QApplication
    from PySide2.QtWidgets import QMessageBox
    from PySide2.QtWidgets import QInputDialog
    from PySide2.QtWidgets import QLineEdit
    from PySide2.QtWidgets import *

    QApplication.UnicodeUTF8 = 0

    from shiboken2 import wrapInstance

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(269, 315)
        self.jointConnexionSettings_groupBox = QGroupBox(Form)
        self.jointConnexionSettings_groupBox.setGeometry(QtCore.QRect(11, 156, 249, 81))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jointConnexionSettings_groupBox.sizePolicy().hasHeightForWidth())
        self.jointConnexionSettings_groupBox.setSizePolicy(sizePolicy)
        self.jointConnexionSettings_groupBox.setObjectName("jointConnexionSettings_groupBox")
        self.layoutWidget = QWidget(self.jointConnexionSettings_groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 16, 231, 47))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.useJointIndex_checkBox = QCheckBox(self.layoutWidget)
        self.useJointIndex_checkBox.setObjectName("useJointIndex_checkBox")
        self.verticalLayout.addWidget(self.useJointIndex_checkBox)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.parentJointIndex_label = QLabel(self.layoutWidget)
        self.parentJointIndex_label.setObjectName("parentJointIndex_label")
        self.horizontalLayout.addWidget(self.parentJointIndex_label)
        self.parentJointIndex_spinBox = QSpinBox(self.layoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parentJointIndex_spinBox.sizePolicy().hasHeightForWidth())
        self.parentJointIndex_spinBox.setSizePolicy(sizePolicy)
        self.parentJointIndex_spinBox.setMinimum(-1)
        self.parentJointIndex_spinBox.setMaximum(999999)
        self.parentJointIndex_spinBox.setProperty("value", -1)
        self.parentJointIndex_spinBox.setObjectName("parentJointIndex_spinBox")
        self.horizontalLayout.addWidget(self.parentJointIndex_spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(11, 240, 249, 61))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 19, 231, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.host_label = QLabel(self.layoutWidget1)
        self.host_label.setObjectName("host_label")
        self.horizontalLayout_2.addWidget(self.host_label)
        self.host_lineEdit = QLineEdit(self.layoutWidget1)
        self.host_lineEdit.setObjectName("host_lineEdit")
        self.horizontalLayout_2.addWidget(self.host_lineEdit)
        self.host_pushButton = QPushButton(self.layoutWidget1)
        self.host_pushButton.setObjectName("host_pushButton")
        self.horizontalLayout_2.addWidget(self.host_pushButton)
        self.mainSettings_groupBox = QGroupBox(Form)
        self.mainSettings_groupBox.setGeometry(QtCore.QRect(11, 11, 249, 139))
        self.mainSettings_groupBox.setTitle("")
        self.mainSettings_groupBox.setObjectName("mainSettings_groupBox")
        self.layoutWidget2 = QWidget(self.mainSettings_groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 10, 231, 126))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.formLayout = QFormLayout(self.layoutWidget2)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.name_label = QLabel(self.layoutWidget2)
        self.name_label.setObjectName("name_label")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.name_label)
        self.name_lineEdit = QLineEdit(self.layoutWidget2)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name_lineEdit)
        self.side_label = QLabel(self.layoutWidget2)
        self.side_label.setObjectName("side_label")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.side_label)
        self.side_comboBox = QComboBox(self.layoutWidget2)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_comboBox.sizePolicy().hasHeightForWidth())
        self.side_comboBox.setSizePolicy(sizePolicy)
        self.side_comboBox.setObjectName("side_comboBox")
        self.side_comboBox.addItem("")
        self.side_comboBox.addItem("")
        self.side_comboBox.addItem("")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.side_comboBox)
        self.componentIndex_label = QLabel(self.layoutWidget2)
        self.componentIndex_label.setObjectName("componentIndex_label")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.componentIndex_label)
        self.componentIndex_spinBox = QSpinBox(self.layoutWidget2)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.componentIndex_spinBox.sizePolicy().hasHeightForWidth())
        self.componentIndex_spinBox.setSizePolicy(sizePolicy)
        self.componentIndex_spinBox.setObjectName("componentIndex_spinBox")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.componentIndex_spinBox)
        self.conector_label = QLabel(self.layoutWidget2)
        self.conector_label.setObjectName("conector_label")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.conector_label)
        self.connector_comboBox = QComboBox(self.layoutWidget2)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connector_comboBox.sizePolicy().hasHeightForWidth())
        self.connector_comboBox.setSizePolicy(sizePolicy)
        self.connector_comboBox.setObjectName("connector_comboBox")
        self.connector_comboBox.addItem("")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.connector_comboBox)
        self.size_label = QLabel(self.layoutWidget2)
        self.size_label.setObjectName("size_label")
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.size_label)
        self.size_spinBox = QSpinBox(self.layoutWidget2)
        self.size_spinBox.setMaximum(9999)
        self.size_spinBox.setObjectName("size_spinBox")
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.size_spinBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QApplication.translate("Form", "Form", None, QApplication.UnicodeUTF8))
        self.jointConnexionSettings_groupBox.setTitle(QApplication.translate("Form", "Joint Connexion Settings", None, QApplication.UnicodeUTF8))
        self.useJointIndex_checkBox.setText(QApplication.translate("Form", "Use Joint Index", None, QApplication.UnicodeUTF8))
        self.parentJointIndex_label.setText(QApplication.translate("Form", "Parent Joint Index:", None, QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QApplication.translate("Form", "Channels Host Settings", None, QApplication.UnicodeUTF8))
        self.host_label.setText(QApplication.translate("Form", "Host:", None, QApplication.UnicodeUTF8))
        self.host_pushButton.setText(QApplication.translate("Form", "<<", None, QApplication.UnicodeUTF8))
        self.name_label.setText(QApplication.translate("Form", "Name:", None, QApplication.UnicodeUTF8))
        self.side_label.setText(QApplication.translate("Form", "Side:", None, QApplication.UnicodeUTF8))
        self.side_comboBox.setItemText(0, QApplication.translate("Form", "Center", None, QApplication.UnicodeUTF8))
        self.side_comboBox.setItemText(1, QApplication.translate("Form", "Left", None, QApplication.UnicodeUTF8))
        self.side_comboBox.setItemText(2, QApplication.translate("Form", "Right", None, QApplication.UnicodeUTF8))
        self.componentIndex_label.setText(QApplication.translate("Form", "Component Index:", None, QApplication.UnicodeUTF8))
        self.conector_label.setText(QApplication.translate("Form", "Connector:", None, QApplication.UnicodeUTF8))
        self.connector_comboBox.setItemText(0, QApplication.translate("Form", "standard", None, QApplication.UnicodeUTF8))
        self.size_label.setText(QApplication.translate("Form", "Size", None, QApplication.UnicodeUTF8))

