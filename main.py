import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
import sys
from selectionForm import Ui_MainWindow
from addnewaccForm import Ui_AddNewAccoutWindow
from examineAccountForm import Ui_ExamineAccountWindow
from editaccForm import Ui_EditAccounttWindow
import clipboard

conn = sqlite3.connect("AccStorage.db")
c = conn.cursor()
c.execute("""CREATE TABLE  if not exists acc_storage (
acc_id INTEGER PRIMARY KEY,
acc_platform text, 
username text, 
user_mail text, 
user_password text, 
acc_creation_date text, 
acc_recovery_codes text, 
acc_phone_number text, 
acc_recovery_mail text
)""")

# c.execute("""INSERT INTO acc_storage (acc_platform,
# username,
# user_mail,
# user_password,
# acc_creation_date,
# acc_recovery_codes,
# acc_phone_number,
# acc_recovery_mail) VALUES ('Reddit', 'Fare', 'Tasarruflu@xyz.com', 'abcdefg', '5.5.5', 'xxxxaaaa', '9305010', 'recovery@gmail.com')""")
conn.commit()
conn.close()


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.examineButton.clicked.connect(self.examineAcc)
        self.ui.addnewButton.clicked.connect(self.open_addNewAcc)
        self.ui.acc_Table.setColumnWidth(0, 150)
        self.ui.acc_Table.setColumnWidth(1, 167)
        self.ui.acc_Table.setColumnWidth(2, 167)
        self.ui.acc_Table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        self.ui.acc_Table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        self.ui.acc_Table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        self.ui.acc_Table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.acc_info_read()


#Add New Account Window Functions
    def open_addNewAcc(self):
        self.addNewWindow = QtWidgets.QMainWindow()
        self.add_acc_ui = Ui_AddNewAccoutWindow()
        self.add_acc_ui.setupUi(self.addNewWindow)
        self.addNewWindow.show()

        #Clear Operation Define's
        self.add_acc_ui.clearall_button.clicked.connect(self.clearAll)
        self.add_acc_ui.clearPlatform_button.clicked.connect(self.clearPlatform)
        self.add_acc_ui.clearUsername_button.clicked.connect(self.clearUsername)
        self.add_acc_ui.clearMail_button.clicked.connect(self.clearUsermail)
        self.add_acc_ui.clearPassword_button.clicked.connect(self.clearUserPassword)
        self.add_acc_ui.clearPhone_button.clicked.connect(self.clearPhoneNumber)
        self.add_acc_ui.clearCreationDate_button.clicked.connect(self.clearCreationDate)
        self.add_acc_ui.clearRecoveryCodes_button.clicked.connect(self.clearRecoveryCodes)
        self.add_acc_ui.clearRecoveryMail_button.clicked.connect(self.clearRecoveryMail)
        #End Of Clear Operations Define Section
        self.add_acc_ui.save_button.clicked.connect(self.SaveToDatabase)
    #Clear Operations for add new account window ///////////
    def clearAll(self):
        self.add_acc_ui.platform_lineedit.setText("")
        self.add_acc_ui.username_lineedit.setText("")
        self.add_acc_ui.usermail_lineedit.setText("")
        self.add_acc_ui.userpassword_lineedit.setText("")
        self.add_acc_ui.phonenumber_lineedit.setText("")
        self.add_acc_ui.creationdate_lineedit.setText("")
        self.add_acc_ui.recoverycodes_lineedit.setText("")
        self.add_acc_ui.recoverymail_lineedit.setText("")
    def clearPlatform(self):
        self.add_acc_ui.platform_lineedit.setText("")
    def clearUsername(self):
        self.add_acc_ui.username_lineedit.setText("")
    def clearUsermail(self):
        self.add_acc_ui.usermail_lineedit.setText("")
    def clearUserPassword(self):
        self.add_acc_ui.userpassword_lineedit.setText("")
    def clearPhoneNumber(self):
        self.add_acc_ui.phonenumber_lineedit.setText("")
    def clearCreationDate(self):
        self.add_acc_ui.creationdate_lineedit.setText("")
    def clearRecoveryCodes(self):
        self.add_acc_ui.recoverycodes_lineedit.setText("")
    def clearRecoveryMail(self):
        self.add_acc_ui.recoverymail_lineedit.setText("")
    #End Of Clear Operations //////////////////////////////

    #Saving To Database On Add New Account Section and other actions
    def saved_noti(self):
        msg2 = QMessageBox()
        msg2.setIcon(QMessageBox.Information)
        msg2.setText("Succesfully Saved!")
        msg2.setWindowTitle("Information")
        msg2.setStandardButtons(QMessageBox.Ok)
        msg2.exec_()
    def overwrited_noti(self):
        msg3 = QMessageBox()
        msg3.setIcon(QMessageBox.Information)
        msg3.setText("Succesfully Overwritten!")
        msg3.setWindowTitle("Information")
        msg3.setStandardButtons(QMessageBox.Ok)
        msg3.exec_()
    def cant_add_existing_account(self):
        msg5 = QMessageBox()
        msg5.setIcon(QMessageBox.Information)
        msg5.setText("You attempted to save an existing email address and username on that platform.")
        msg5.setWindowTitle("Information")
        msg5.setStandardButtons(QMessageBox.Ok)
        msg5.exec_()
    def cant_everythink_not_specified(self):
        msg6 = QMessageBox()
        msg6.setIcon(QMessageBox.Information)
        msg6.setText("You did not provide any information. It cannot be saved in this manner!")
        msg6.setWindowTitle("Information")
        msg6.setStandardButtons(QMessageBox.Ok)
        msg6.exec_()
    def do_not_forget_to_select_account(self):
        msg6 = QMessageBox()
        msg6.setIcon(QMessageBox.Information)
        msg6.setText("Please Select An Account or Add New One")
        msg6.setWindowTitle("Information")
        msg6.setStandardButtons(QMessageBox.Ok)
        msg6.exec_()
    def ask_for_delete(self):
        msg4 = QMessageBox()
        msg4.setIcon(QMessageBox.Information)
        msg4.setText("Are you sure you want to delete this save?")
        msg4.setInformativeText("You will not be able to get the changes back.")
        msg4.setWindowTitle("Confirm To Delete")
        msg4.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        return_value = msg4.exec_()
        return return_value
    def NotSpecifeidCalculator(self, given_entries_list):
        index = 0
        for item in given_entries_list:
            if item == '':
                given_entries_list[index] = "Not Specified#(Code: 01)"
            else:
                pass
            index = index + 1
        return given_entries_list
    def isAllNotSpecified(self, given_entries_list):
        allNotSpecified = True
        for item in given_entries_list:
            if not item == "Not Specified#(Code: 01)":
                allNotSpecified = False
        return  allNotSpecified
    def SaveToDatabase(self):
        saved_acc_count = self.ui.acc_Table.rowCount()
        saved_acc_limit = 150
        if saved_acc_count == saved_acc_limit:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"You can only save {saved_acc_limit} accounts at once.")
            msg.setInformativeText("To add a new one, you must first delete one.")
            msg.setWindowTitle("You have reached your save limit!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        else:
            conn3 = sqlite3.connect("AccStorage.db")
            c3 = conn3.cursor()
            c3.execute("SELECT * FROM acc_storage")
            existing_accounts = c3.fetchall()
            general_acc_attr = []
            for item in existing_accounts:
                item_general_attr = (item[1], item[2], item[3])
                general_acc_attr.append(item_general_attr)

            if (self.add_acc_ui.platform_lineedit.text(), self.add_acc_ui.username_lineedit.text(),
                self.add_acc_ui.usermail_lineedit.text()) in general_acc_attr:
                self.cant_add_existing_account()
            else:
                c3.execute("SELECT max(rowid) from acc_storage")
                row_max_count = c3.fetchone()[0]
                if row_max_count == None:
                    row_max_count = 0
                new_id = row_max_count
                #Deleted new id from first index
                UserInputs = [self.add_acc_ui.platform_lineedit.text(),
                              self.add_acc_ui.username_lineedit.text(),
                              self.add_acc_ui.usermail_lineedit.text(), self.add_acc_ui.userpassword_lineedit.text(),
                              self.add_acc_ui.creationdate_lineedit.text(), self.add_acc_ui.recoverycodes_lineedit.text(),
                              self.add_acc_ui.phonenumber_lineedit.text(), self.add_acc_ui.recoverymail_lineedit.text()]

                UserInputs = self.NotSpecifeidCalculator(given_entries_list=UserInputs)
                if self.isAllNotSpecified(given_entries_list=UserInputs):
                    self.cant_everythink_not_specified()
                    conn3.commit()
                    conn3.close()
                else:
                    c3.execute("""INSERT INTO acc_storage (acc_platform, 
                    username, 
                    user_mail, 
                    user_password, 
                    acc_creation_date, 
                    acc_recovery_codes, 
                    acc_phone_number, 
                    acc_recovery_mail) VALUES (?,?,?,?,?,?,?,?)""", UserInputs)
                    conn3.commit()
                    conn3.close()

                    #Update The Table Widget
                    self.acc_info_read()
                    #Saved Information
                    self.saved_noti()
                    self.addNewWindow.close()
    #End of Saving Function
#End Of Add New Account Window Functions

#Examine Account Window Functions
    def bind_acc_data_exm(self, selected_account_given):
        self.exm_acc_ui.platform_lineedit.setText(str(selected_account_given[1]))
        self.exm_acc_ui.username_lineedit.setText(str(selected_account_given[2]))
        self.exm_acc_ui.usermail_lineedit.setText(str(selected_account_given[3]))
        self.exm_acc_ui.userpassword_lineedit.setText(str(selected_account_given[4]))
        self.exm_acc_ui.creationdate_lineedit.setText(str(selected_account_given[5]))
        self.exm_acc_ui.recoverycodes_lineedit.setText(str(selected_account_given[6]))
        self.exm_acc_ui.phonenumber_lineedit.setText(str(selected_account_given[7]))
        self.exm_acc_ui.recoverymail_lineedit.setText(str(selected_account_given[8]))
        self.exm_acc_ui.copyPlatform_button.clicked.connect(self.copy_Platform)
        self.exm_acc_ui.copyUsername_button.clicked.connect(self.copy_Username)
        self.exm_acc_ui.copyMail_button.clicked.connect(self.copy_Mail)
        self.exm_acc_ui.copyPassword_button.clicked.connect(self.copy_Password)
        self.exm_acc_ui.copyCreationDate_button.clicked.connect(self.copy_CreationDate)
        self.exm_acc_ui.copyRecoveryCodes_button.clicked.connect(self.copy_RecoveryCodes)
        self.exm_acc_ui.copyPhone_button.clicked.connect(self.copy_PhoneNumber)
        self.exm_acc_ui.copyRecoveryMail_button.clicked.connect(self.copy_RecoveryMail)
        self.exm_acc_ui.edit_button.clicked.connect(self.open_edit_acc)
    def open_examine_acc(self, selected_account_given, given_row_index):
        self.examineAccWindow = QtWidgets.QMainWindow()
        self.exm_acc_ui = Ui_ExamineAccountWindow()
        self.exm_acc_ui.setupUi(self.examineAccWindow)
        self.examineAccWindow.show()

        #Binding With Choosen Account Data
        self.exm_acc_ui.aditaccLabel.setText(f"Examine Account - Number: {given_row_index + 1}")
        self.bind_acc_data_exm(selected_account_given=selected_account_given)
    def examineAcc(self):
        selected_row_index = int(self.ui.acc_Table.currentRow())
        if not selected_row_index == -1:
            selected_Platform = self.ui.acc_Table.item(selected_row_index, 0).text()
            selected_username = self.ui.acc_Table.item(selected_row_index, 1).text()
            selected_usermail = self.ui.acc_Table.item(selected_row_index, 2).text()
            conn4 = sqlite3.connect("AccStorage.db")
            c4 = conn4.cursor()
            c4.execute(f"""SELECT * FROM acc_storage WHERE acc_platform = '{selected_Platform}' AND
            username = '{selected_username}' AND user_mail = '{selected_usermail}' """)
            selected_account = c4.fetchone()
            self.open_examine_acc(selected_account_given=selected_account, given_row_index=selected_row_index)
        elif selected_row_index == -1:
            self.do_not_forget_to_select_account()

    #Clipboard Functions
    def copy_Platform(self):
        if not self.exm_acc_ui.platform_lineedit.text() == "Not Specified#(Code: 01)":
            clipboard.copy(self.exm_acc_ui.platform_lineedit.text())
    def copy_Username(self):
        if not self.exm_acc_ui.username_lineedit.text() == "Not Specified#(Code: 01)":
            clipboard.copy(self.exm_acc_ui.username_lineedit.text())
    def copy_Mail(self):
        if not self.exm_acc_ui.usermail_lineedit.text() == "Not Specified#(Code: 01)":
            clipboard.copy(self.exm_acc_ui.usermail_lineedit.text())
    def copy_Password(self):
        if not self.exm_acc_ui.userpassword_lineedit.text() == "Not Specified#(Code: 01)":
            clipboard.copy(self.exm_acc_ui.userpassword_lineedit.text())
    def copy_CreationDate(self):
        if not self.exm_acc_ui.creationdate_lineedit.text() == "Not Specified#(Code: 01)":
            clipboard.copy(self.exm_acc_ui.creationdate_lineedit.text())
    def copy_RecoveryCodes(self):
        if not self.exm_acc_ui.recoverycodes_lineedit.text() == "Not Specified#(Code: 01)":
            clipboard.copy(self.exm_acc_ui.recoverycodes_lineedit.text())
    def copy_PhoneNumber(self):
        if not self.exm_acc_ui.phonenumber_lineedit.text() == "Not Specified#(Code: 01)":
            clipboard.copy(self.exm_acc_ui.phonenumber_lineedit.text())
    def copy_RecoveryMail(self):
        if not self.exm_acc_ui.recoverymail_lineedit.text() == "Not Specified#(Code: 01)":
            clipboard.copy(self.exm_acc_ui.recoverymail_lineedit.text())
    #End Of Clipboard Functions

    #This Function Opens Edit Window
    def open_edit_acc(self):
        self.editaccWindow = QtWidgets.QMainWindow()
        self.edit_acc_ui = Ui_EditAccounttWindow()
        self.edit_acc_ui.setupUi(self.editaccWindow)
        self.editaccWindow.show()
        self.edit_acc_ui.platform_lineedit.setText(self.exm_acc_ui.platform_lineedit.text())
        self.edit_acc_ui.username_lineedit.setText(self.exm_acc_ui.username_lineedit.text())
        self.edit_acc_ui.usermail_lineedit.setText(self.exm_acc_ui.usermail_lineedit.text())
        self.edit_acc_ui.userpassword_lineedit.setText(self.exm_acc_ui.userpassword_lineedit.text())
        self.edit_acc_ui.creationdate_lineedit.setText(self.exm_acc_ui.creationdate_lineedit.text())
        self.edit_acc_ui.recoverycodes_lineedit.setText(self.exm_acc_ui.recoverycodes_lineedit.text())
        self.edit_acc_ui.phonenumber_lineedit.setText(self.exm_acc_ui.phonenumber_lineedit.text())
        self.edit_acc_ui.recoverymail_lineedit.setText(self.exm_acc_ui.recoverymail_lineedit.text())
        self.edit_acc_ui.clearall_button.clicked.connect(self.clearall_editing)
        self.edit_acc_ui.clearPlatform_button.clicked.connect(self.clear_Platform_Editing)
        self.edit_acc_ui.clearUsername_button.clicked.connect(self.clear_Username_Editing)
        self.edit_acc_ui.clearMail_button.clicked.connect(self.clear_Mail_Editing)
        self.edit_acc_ui.clearPassword_button.clicked.connect(self.clear_Password_Editing)
        self.edit_acc_ui.clearCreationDate_button.clicked.connect(self.clear_CreationDate_Editing)
        self.edit_acc_ui.clearRecoveryCodes_button.clicked.connect(self.clear_RecoveryCodes_Editing)
        self.edit_acc_ui.clearPhone_button.clicked.connect(self.clear_PhoneNumber_Editing)
        self.edit_acc_ui.clearRecoveryMail_button.clicked.connect(self.clear_RecoveryMail_Editing)
        self.edit_acc_ui.OverwriteAccount_button.clicked.connect(self.OverwriteToDatabase)
        self.edit_acc_ui.delete_acc_button.clicked.connect(self.DeleteFromDatabase)
    #End Of Opening Edit Window

    #Clear Operations For Editing Window
    def clearall_editing(self):
        self.edit_acc_ui.platform_lineedit.setText("")
        self.edit_acc_ui.username_lineedit.setText("")
        self.edit_acc_ui.usermail_lineedit.setText("")
        self.edit_acc_ui.userpassword_lineedit.setText("")
        self.edit_acc_ui.creationdate_lineedit.setText("")
        self.edit_acc_ui.recoverycodes_lineedit.setText("")
        self.edit_acc_ui.phonenumber_lineedit.setText("")
        self.edit_acc_ui.recoverymail_lineedit.setText("")
    def clear_Platform_Editing(self):
        self.edit_acc_ui.platform_lineedit.setText("")
    def clear_Username_Editing(self):
        self.edit_acc_ui.username_lineedit.setText("")
    def clear_Mail_Editing(self):
        self.edit_acc_ui.usermail_lineedit.setText("")
    def clear_Password_Editing(self):
        self.edit_acc_ui.userpassword_lineedit.setText("")
    def clear_CreationDate_Editing(self):
        self.edit_acc_ui.creationdate_lineedit.setText("")
    def clear_RecoveryCodes_Editing(self):
        self.edit_acc_ui.recoverycodes_lineedit.setText("")
    def clear_PhoneNumber_Editing(self):
        self.edit_acc_ui.phonenumber_lineedit.setText("")
    def clear_RecoveryMail_Editing(self):
        self.edit_acc_ui.recoverymail_lineedit.setText("")
    #End Of The Clear Operations

    #Editing Menu Overwrite New Values
    def OverwriteToDatabase(self):
        selected_row_index = int(self.ui.acc_Table.currentRow())
        selected_Platform = self.ui.acc_Table.item(selected_row_index, 0).text()
        selected_username = self.ui.acc_Table.item(selected_row_index, 1).text()
        selected_usermail = self.ui.acc_Table.item(selected_row_index, 2).text()
        conn5 = sqlite3.connect("AccStorage.db")
        c5 = conn5.cursor()
        c5.execute("SELECT * FROM acc_storage")
        existing_accounts = c5.fetchall()
        general_acc_attr = []
        for item in existing_accounts:
            item_general_attr = (item[1], item[2], item[3])
            general_acc_attr.append(item_general_attr)

        if (self.edit_acc_ui.platform_lineedit.text(), self.edit_acc_ui.username_lineedit.text(),
                self.edit_acc_ui.usermail_lineedit.text()) in general_acc_attr:

                self.cant_add_existing_account()

        else:
            edited_datas = [self.edit_acc_ui.platform_lineedit.text(),
                            self.edit_acc_ui.username_lineedit.text(),
                            self.edit_acc_ui.usermail_lineedit.text(),
                            self.edit_acc_ui.userpassword_lineedit.text(),
                            self.edit_acc_ui.creationdate_lineedit.text(),
                            self.edit_acc_ui.recoverycodes_lineedit.text(),
                            self.edit_acc_ui.phonenumber_lineedit.text(),
                            self.edit_acc_ui.recoverymail_lineedit.text()]

            edited_datas = self.NotSpecifeidCalculator(given_entries_list=edited_datas)
            if self.isAllNotSpecified(given_entries_list=edited_datas):
                self.cant_everythink_not_specified()
                conn5.commit()
                conn5.close()
            else:
                c5.execute(f"""UPDATE acc_storage SET acc_platform = '{edited_datas[0]}', 
                username = '{edited_datas[1]}', 
                user_mail = '{edited_datas[2]}', 
                user_password = '{edited_datas[3]}', 
                acc_creation_date = '{edited_datas[4]}', 
                acc_recovery_codes = '{edited_datas[5]}', 
                acc_phone_number = '{edited_datas[6]}', 
                acc_recovery_mail = '{edited_datas[7]}' WHERE acc_platform = '{selected_Platform}' 
                AND username = '{selected_username}' AND user_mail = '{selected_usermail}'
                """)
                conn5.commit()
                conn5.close()
                #Debug for bind_acc_data_exm() func starts to write from 0 and it gives
                #out of bound error when you give edited datas
                new_edited_datas_debug = [None]
                for item in edited_datas:
                    new_edited_datas_debug.append(item)

                self.bind_acc_data_exm(selected_account_given=new_edited_datas_debug)
                self.acc_info_read()
                self.overwrited_noti()
                self.editaccWindow.close()
    def DeleteFromDatabase(self):
        Value_No = 65536
        Value_Yes = 16384
        isconfirm = self.ask_for_delete()
        if isconfirm == Value_Yes:
            selected_row_index = int(self.ui.acc_Table.currentRow())
            selected_Platform = self.ui.acc_Table.item(selected_row_index, 0).text()
            selected_username = self.ui.acc_Table.item(selected_row_index, 1).text()
            selected_usermail = self.ui.acc_Table.item(selected_row_index, 2).text()
            conn6 = sqlite3.connect("AccStorage.db")
            c6 = conn6.cursor()
            c6.execute(f"""DELETE FROM acc_storage WHERE acc_platform = '{selected_Platform}' 
            AND username = '{selected_username}' AND  user_mail='{selected_usermail}'""")
            conn6.commit()
            conn6.close()
            self.editaccWindow.close()
            self.examineAccWindow.close()
            self.acc_info_read()
        elif isconfirm == Value_No:
            pass

#End Of Examine Account Window Functions

    #This Functions Writes Datas To Table
    def acc_info_read(self):
        conn = sqlite3.connect("AccStorage.db")
        c = conn.cursor()
        c.execute("SELECT * FROM acc_storage")
        items = c.fetchall()
        index = 0
        rowcount = len(items)
        self.ui.acc_Table.setColumnCount(3)
        self.ui.acc_Table.setRowCount(rowcount)
        for item in items:
            platform = item[1]
            Username = item[2]
            Usermail = item[3]
            self.ui.acc_Table.setItem(index, 0, QTableWidgetItem(platform))
            self.ui.acc_Table.setItem(index, 1, QTableWidgetItem(Username))
            self.ui.acc_Table.setItem(index, 2, QTableWidgetItem(Usermail))
            index = index + 1
        conn.commit()
        conn.close()


def start_app():
    app = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec_())


start_app()

