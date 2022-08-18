# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\editaccForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditAccounttWindow(object):
    def setupUi(self, EditAccounttWindow):
        EditAccounttWindow.setObjectName("EditAccounttWindow")
        EditAccounttWindow.resize(764, 573)
        EditAccounttWindow.setMinimumSize(QtCore.QSize(0, 388))
        EditAccounttWindow.setMaximumSize(QtCore.QSize(1000, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\Resources/icons/edit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditAccounttWindow.setWindowIcon(icon)
        EditAccounttWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(EditAccounttWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.editaccLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Verdana Pro Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.editaccLabel.setFont(font)
        self.editaccLabel.setScaledContents(True)
        self.editaccLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.editaccLabel.setWordWrap(False)
        self.editaccLabel.setObjectName("editaccLabel")
        self.horizontalLayout.addWidget(self.editaccLabel)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(5, 0, 5, 4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.platform_Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(12)
        self.platform_Label.setFont(font)
        self.platform_Label.setObjectName("platform_Label")
        self.verticalLayout.addWidget(self.platform_Label)
        self.username_Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(12)
        self.username_Label.setFont(font)
        self.username_Label.setObjectName("username_Label")
        self.verticalLayout.addWidget(self.username_Label)
        self.usermail_Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(12)
        self.usermail_Label.setFont(font)
        self.usermail_Label.setObjectName("usermail_Label")
        self.verticalLayout.addWidget(self.usermail_Label)
        self.userpassword_Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(12)
        self.userpassword_Label.setFont(font)
        self.userpassword_Label.setObjectName("userpassword_Label")
        self.verticalLayout.addWidget(self.userpassword_Label)
        self.creationdate_Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(12)
        self.creationdate_Label.setFont(font)
        self.creationdate_Label.setObjectName("creationdate_Label")
        self.verticalLayout.addWidget(self.creationdate_Label)
        self.recoverycodes_Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(12)
        self.recoverycodes_Label.setFont(font)
        self.recoverycodes_Label.setObjectName("recoverycodes_Label")
        self.verticalLayout.addWidget(self.recoverycodes_Label)
        self.phonenumber_Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(12)
        self.phonenumber_Label.setFont(font)
        self.phonenumber_Label.setObjectName("phonenumber_Label")
        self.verticalLayout.addWidget(self.phonenumber_Label)
        self.recoverymail_Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(12)
        self.recoverymail_Label.setFont(font)
        self.recoverymail_Label.setObjectName("recoverymail_Label")
        self.verticalLayout.addWidget(self.recoverymail_Label)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.platform_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.platform_lineedit.setObjectName("platform_lineedit")
        self.verticalLayout_4.addWidget(self.platform_lineedit)
        self.username_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_lineedit.setObjectName("username_lineedit")
        self.verticalLayout_4.addWidget(self.username_lineedit)
        self.usermail_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.usermail_lineedit.setObjectName("usermail_lineedit")
        self.verticalLayout_4.addWidget(self.usermail_lineedit)
        self.userpassword_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.userpassword_lineedit.setObjectName("userpassword_lineedit")
        self.verticalLayout_4.addWidget(self.userpassword_lineedit)
        self.creationdate_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.creationdate_lineedit.setObjectName("creationdate_lineedit")
        self.verticalLayout_4.addWidget(self.creationdate_lineedit)
        self.recoverycodes_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.recoverycodes_lineedit.setObjectName("recoverycodes_lineedit")
        self.verticalLayout_4.addWidget(self.recoverycodes_lineedit)
        self.phonenumber_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.phonenumber_lineedit.setObjectName("phonenumber_lineedit")
        self.verticalLayout_4.addWidget(self.phonenumber_lineedit)
        self.recoverymail_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.recoverymail_lineedit.setObjectName("recoverymail_lineedit")
        self.verticalLayout_4.addWidget(self.recoverymail_lineedit)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, 3, 5, 3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.clearPlatform_button = QtWidgets.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\Resources/icons/clear.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearPlatform_button.setIcon(icon1)
        self.clearPlatform_button.setObjectName("clearPlatform_button")
        self.verticalLayout_2.addWidget(self.clearPlatform_button)
        self.clearUsername_button = QtWidgets.QPushButton(self.centralwidget)
        self.clearUsername_button.setIcon(icon1)
        self.clearUsername_button.setObjectName("clearUsername_button")
        self.verticalLayout_2.addWidget(self.clearUsername_button)
        self.clearMail_button = QtWidgets.QPushButton(self.centralwidget)
        self.clearMail_button.setIcon(icon1)
        self.clearMail_button.setObjectName("clearMail_button")
        self.verticalLayout_2.addWidget(self.clearMail_button)
        self.clearPassword_button = QtWidgets.QPushButton(self.centralwidget)
        self.clearPassword_button.setIcon(icon1)
        self.clearPassword_button.setObjectName("clearPassword_button")
        self.verticalLayout_2.addWidget(self.clearPassword_button)
        self.clearCreationDate_button = QtWidgets.QPushButton(self.centralwidget)
        self.clearCreationDate_button.setIcon(icon1)
        self.clearCreationDate_button.setObjectName("clearCreationDate_button")
        self.verticalLayout_2.addWidget(self.clearCreationDate_button)
        self.clearRecoveryCodes_button = QtWidgets.QPushButton(self.centralwidget)
        self.clearRecoveryCodes_button.setIcon(icon1)
        self.clearRecoveryCodes_button.setObjectName("clearRecoveryCodes_button")
        self.verticalLayout_2.addWidget(self.clearRecoveryCodes_button)
        self.clearPhone_button = QtWidgets.QPushButton(self.centralwidget)
        self.clearPhone_button.setIcon(icon1)
        self.clearPhone_button.setObjectName("clearPhone_button")
        self.verticalLayout_2.addWidget(self.clearPhone_button)
        self.clearRecoveryMail_button = QtWidgets.QPushButton(self.centralwidget)
        self.clearRecoveryMail_button.setIcon(icon1)
        self.clearRecoveryMail_button.setObjectName("clearRecoveryMail_button")
        self.verticalLayout_2.addWidget(self.clearRecoveryMail_button)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 2, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.OverwriteAccount_button = QtWidgets.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\Resources/icons/overwrite.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OverwriteAccount_button.setIcon(icon2)
        self.OverwriteAccount_button.setObjectName("OverwriteAccount_button")
        self.verticalLayout_5.addWidget(self.OverwriteAccount_button)
        self.clearall_button = QtWidgets.QPushButton(self.centralwidget)
        self.clearall_button.setIcon(icon1)
        self.clearall_button.setObjectName("clearall_button")
        self.verticalLayout_5.addWidget(self.clearall_button)
        self.delete_acc_button = QtWidgets.QPushButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\Resources/icons/delete.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_acc_button.setIcon(icon3)
        self.delete_acc_button.setObjectName("delete_acc_button")
        self.verticalLayout_5.addWidget(self.delete_acc_button)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 2, 0, 1, 3)
        EditAccounttWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EditAccounttWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 21))
        self.menubar.setObjectName("menubar")
        EditAccounttWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EditAccounttWindow)
        self.statusbar.setObjectName("statusbar")
        EditAccounttWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EditAccounttWindow)
        QtCore.QMetaObject.connectSlotsByName(EditAccounttWindow)

    def retranslateUi(self, EditAccounttWindow):
        _translate = QtCore.QCoreApplication.translate
        EditAccounttWindow.setWindowTitle(_translate("EditAccounttWindow", "Account Editing Menu"))
        self.editaccLabel.setText(_translate("EditAccounttWindow", "EDIT AN EXISTING ACCOUNT"))
        self.platform_Label.setText(_translate("EditAccounttWindow", "Platform:"))
        self.username_Label.setText(_translate("EditAccounttWindow", "Username:"))
        self.usermail_Label.setText(_translate("EditAccounttWindow", "User Mail:"))
        self.userpassword_Label.setText(_translate("EditAccounttWindow", "User Password:"))
        self.creationdate_Label.setText(_translate("EditAccounttWindow", "Creation Date:"))
        self.recoverycodes_Label.setText(_translate("EditAccounttWindow", "Recovery Codes:"))
        self.phonenumber_Label.setText(_translate("EditAccounttWindow", "Phone Number:"))
        self.recoverymail_Label.setText(_translate("EditAccounttWindow", "Recovery Mail:"))
        self.clearPlatform_button.setText(_translate("EditAccounttWindow", "Clear"))
        self.clearUsername_button.setText(_translate("EditAccounttWindow", "Clear"))
        self.clearMail_button.setText(_translate("EditAccounttWindow", "Clear"))
        self.clearPassword_button.setText(_translate("EditAccounttWindow", "Clear"))
        self.clearCreationDate_button.setText(_translate("EditAccounttWindow", "Clear"))
        self.clearRecoveryCodes_button.setText(_translate("EditAccounttWindow", "Clear"))
        self.clearPhone_button.setText(_translate("EditAccounttWindow", "Clear"))
        self.clearRecoveryMail_button.setText(_translate("EditAccounttWindow", "Clear"))
        self.OverwriteAccount_button.setText(_translate("EditAccounttWindow", "Save And Overwrite"))
        self.clearall_button.setText(_translate("EditAccounttWindow", "Clear All"))
        self.delete_acc_button.setText(_translate("EditAccounttWindow", "Delete This Account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditAccounttWindow = QtWidgets.QMainWindow()
    ui = Ui_EditAccounttWindow()
    ui.setupUi(EditAccounttWindow)
    EditAccounttWindow.show()
    sys.exit(app.exec_())