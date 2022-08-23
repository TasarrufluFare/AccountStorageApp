import os
import sqlite3
from Crypto.Cipher import AES
import base64
from cryptography.fernet import Fernet
from Crypto.Random import get_random_bytes

from PyQt5 import QtWidgets
from functools import partial

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QLineEdit
import sys
from selectionForm import Ui_MainWindow
from addnewaccForm import Ui_AddNewAccoutWindow
from examineAccountForm import Ui_ExamineAccountWindow
from editaccForm import Ui_EditAccounttWindow
from createnewaccountForm import Ui_CreateNewAccount
from loginForm import Ui_LoginScreen
import clipboard
from PasswordRandomize import create_list
from PassSet import Ui_PasswordGeneratorSettings
from encrypter import encrypter_method
from Crypto.Random import get_random_bytes
from decrypter import decrypter_method


def login_control():
    if not os.path.exists("LogSvd"):
        os.mkdir("LogSvd")


class App(QtWidgets.QMainWindow):
    database_location = "AccSvd/AccStorage.db"
    database_name = "AccStorage.db"

    def first_controls(self, database_location):
        if not os.path.exists("AccSvd"):
            os.mkdir("AccSvd")
        stored_dbs = os.listdir("AccSvd")
        database_name = database_location.replace("AccSvd/", "")
        database_encryted_name = database_name.split(".")
        database_encryted_name[-1] = "bin"
        self.database_name = database_encryted_name[0]+"."+database_encryted_name[1]
        if self.database_name in stored_dbs:
            decrypter_method(f"AccSvd/{self.database_name}", self.database_name, self.account_db_key)
        conn = sqlite3.connect(database_location)
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


    def open_login_page(self):
        self.loginWindow = QtWidgets.QMainWindow()
        self.login_ui = Ui_LoginScreen()
        self.login_ui.setupUi(self.loginWindow)
        self.login_ui.createnewacc_btn.clicked.connect(self.open_create_account)
        self.login_ui.login_btn.clicked.connect(self.check_and_verify_login)
        self.login_ui.login_password_lineedit.setEchoMode(QLineEdit.Password)
        self.login_ui.saved_label.setVisible(False)
        #self.login_ui.login_btn.clicked.connect(start_app)
        self.loginWindow.show()
    def save_account_properties_crt_new_account(self):
        if not os.path.exists("LogSvd"):
            os.mkdir("LogSvd")
        if not os.path.exists("AccSvd"):
            os.mkdir("AccSvd")
        key = b'Your Key Here'
        key_db = get_random_bytes(32)
        username_crt = self.create_acc_ui.username_crtnewacc_lineedit.text()
        userpassword_crt = self.create_acc_ui.password_crtnewacc_linedit.text()
        usermail_crt = self.create_acc_ui.usermail_crtnewacc_lineedit.text()
        my_seperator = "##tfei##"
        accounts = os.listdir("LogSvd")
        search = f"{username_crt}.bin"
        if not search in accounts:
            user_create_acc_properties = [username_crt.encode("ascii"), usermail_crt.encode("ascii"),
                                          userpassword_crt.encode("ascii"), key_db]
            if not os.path.exists(f"LogSvd/{username_crt}.bin"):
                save_file = open(f"LogSvd/{username_crt}.bin", 'wb')
                string2write = (base64.b64encode(user_create_acc_properties[0])) + (base64.b64encode(my_seperator.encode("ascii"))) + (base64.b64encode(user_create_acc_properties[1])) + (base64.b64encode(my_seperator.encode("ascii"))) + (base64.b64encode(user_create_acc_properties[2]) + (base64.b64encode(my_seperator.encode("ascii"))) + (base64.b64encode(user_create_acc_properties[3])))
                encrypted_str_to_write = self.encrpyterforLogSvd1(string2write, key)
                save_file.write(encrypted_str_to_write)
                save_file.close()
            try:
                with open(f"LogSvd/{username_crt}.bin", 'rb') as save_file_login_update:
                    encrypted_readed_byte = save_file_login_update.read()
                    decrypted_str = self.decrypterforLogSvd(encrypted_readed_byte, key)
                    save_bytes_list = decrypted_str.split(
                        base64.b64encode(my_seperator.encode("ascii")))
                save_file_login_update.close()
                self.login_ui.UserMailOrUsername_linedit.setText(
                    base64.b64decode(save_bytes_list[0]).decode('ascii'))
                self.login_ui.login_password_lineedit.setText(
                     base64.b64decode(save_bytes_list[2]).decode('ascii'))
                self.create_acc_ui.saved_label.setText("Successfully Created")
                self.create_acc_ui.saved_label.setVisible(True)
                self.create_acc_ui.createnewaccconfirm_btn.setDisabled(True)
            except():
                pass
        else:
            self.create_acc_ui.saved_label.setText("Account Already Exists")
            self.create_acc_ui.saved_label.setVisible(True)

    account_db_key = ""
    def check_and_verify_login(self):
        if not os.path.exists("AccSvd"):
            os.mkdir("AccSvd")
        if not os.path.exists("LogSvd"):
            os.mkdir("LogSvd")
        given_username = self.login_ui.UserMailOrUsername_linedit.text()
        given_password = self.login_ui.login_password_lineedit.text()
        my_seperator = "##tfei##"
        accounts = os.listdir("LogSvd")
        search = f"{given_username}.bin"
        if search in accounts:
            with open(f"LogSvd/{search}", 'rb') as save_file_login_update:
                data = save_file_login_update.read()
                key = b'Your Key Here'
                encrypted_data = self.decrypterforLogSvd(data, key)
                save_bytes_list = encrypted_data.split(base64.b64encode(my_seperator.encode("ascii")))
            save_file_login_update.close()
            if base64.b64decode(save_bytes_list[2]).decode('ascii') == given_password:
                self.ui.acc_Table.setEnabled(True)
                self.ui.addnewButton.setEnabled(True)
                self.ui.examineButton.setEnabled(True)
                self.ui.lockTheAccs_btn.setEnabled(True)
                self.database_location = f"AccSvd/AccStorage_{given_username}.db"
                self.account_db_key = base64.b64decode(save_bytes_list[3])
                self.first_controls(database_location=self.database_location)
                self.acc_info_read()
                self.loginWindow.close()
            else:
                self.login_ui.saved_label.setText("Access Denied")
                self.login_ui.saved_label.setVisible(True)
        else:
            self.login_ui.saved_label.setText("Account Not Found.")
            self.login_ui.saved_label.setVisible(True)

    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.examineButton.clicked.connect(self.examineAcc)
        self.ui.addnewButton.clicked.connect(self.open_addNewAcc)
        self.ui.lockTheAccs_btn.clicked.connect(self.safe_exit)
        self.ui.login_logout_btn.clicked.connect(self.open_login_page)
        self.ui.acc_Table.setColumnWidth(0, 150)
        self.ui.acc_Table.setColumnWidth(1, 167)
        self.ui.acc_Table.setColumnWidth(2, 167)
        self.ui.acc_Table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        self.ui.acc_Table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        self.ui.acc_Table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        self.ui.acc_Table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.open_login_page()
        #self.acc_info_read()
    #Encryption and Decryption for Accounts Save
    def encrpyterforLogSvd1(self,data,key):
        print("Data:" + str(data))
        print(type(data))
        f = Fernet(key)
        encrypted = f.encrypt(data)
        return encrypted

    def decrypterforLogSvd(self, data, key):
        f = Fernet(key)
        decrypted = f.decrypt(data)
        return decrypted
#Login screen thing
    def open_create_account(self):
        self.createaccWindow = QtWidgets.QMainWindow()
        self.create_acc_ui = Ui_CreateNewAccount()
        self.create_acc_ui.setupUi(self.createaccWindow)
        self.create_acc_ui.createnewaccconfirm_btn.clicked.connect(self.save_account_properties_crt_new_account)
        self.create_acc_ui.saved_label.setVisible(False)
        self.createaccWindow.show()
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
        self.add_acc_ui.randomizepass_btn.clicked.connect(partial(self.passrandomizer_getsettings, "add_new"))
        self.add_acc_ui.randompasssett_btn.clicked.connect(self.passrandomizer_getsettingsforUI)
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
    def saved_noti_safe_exit(self):
        msg7 = QMessageBox()
        msg7.setIcon(QMessageBox.Information)
        msg7.setText("Succesfully Secured The Accounts, Account Storage App Will Be Closed!")
        msg7.setWindowTitle("Information")
        msg7.setStandardButtons(QMessageBox.Ok)
        msg7.exec_()
    def couldnt_saved_noti_safe_exit(self):
        msg8 = QMessageBox()
        msg8.setIcon(QMessageBox.Information)
        msg8.setText("Could Not Secure The Accounts, Operation Terminated!")
        msg8.setWindowTitle("Information")
        msg8.setDetailedText("Unable To Reach Database. May Be Deleted.")
        msg8.setStandardButtons(QMessageBox.Ok)
        msg8.exec_()
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
            conn3 = sqlite3.connect(self.database_location)
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
                #Deleted new id from first index
                UserInputs = [self.add_acc_ui.platform_lineedit.text(),
                              self.add_acc_ui.username_lineedit.text(),
                              self.add_acc_ui.usermail_lineedit.text(), self.add_acc_ui.userpassword_lineedit.text(),
                              self.add_acc_ui.creationdate_lineedit.text(), self.add_acc_ui.recoverycodes_lineedit.text(),
                              self.add_acc_ui.phonenumber_lineedit.text(), self.add_acc_ui.recoverymail_lineedit.text()]

                UserInputs = self.NotSpecifeidCalculator(given_entries_list=UserInputs)
                #Mail Address And Not Specified Control
                if self.isAllNotSpecified(given_entries_list=UserInputs):
                    self.cant_everythink_not_specified()
                    conn3.commit()
                    conn3.close()
                elif (not len(UserInputs[2].split("@")) == 2) and (not UserInputs[2] == 'Not Specified#(Code: 01)'):
                    self.add_acc_ui.usermail_lineedit.setText("Please provide a valid email address.")
                    if (not len(UserInputs[7].split("@")) == 2) and (not UserInputs[7] == 'Not Specified#(Code: 01)'):
                        self.add_acc_ui.recoverymail_lineedit.setText("Please provide a valid email address.")
                    conn3.commit()
                    conn3.close()
                elif (not len(UserInputs[7].split("@")) == 2) and (not UserInputs[7] == "Not Specified#(Code: 01)"):
                    self.add_acc_ui.recoverymail_lineedit.setText("Please provide a valid email address.")
                    conn3.commit()
                    conn3.close()
                #End Of The Mail Address And Not Specified Control
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

    #Password Randomizing and Password Settings
    def check_to_create_conf_file(self):
        settings_location = "Conf/AS_Pass_Settings.ini"
        default_settings = """/Random Password Properties/
        Pass_Create_Mode_1: 1
        Pass_Create_Mode_2: 1
        Pass_Create_Mode_3: 1
        Pass_Create_Mode_4: 1
        Min_Char_Count: 20
        Max_Char_Count: 25
        /EndOfSetting/"""
        if not os.path.exists(settings_location):
            os.mkdir("Conf")
            with open("Conf/AS_Pass_Settings.ini", 'w') as pass_settings_file:
                pass_settings_file.write(default_settings)
            pass_settings_file.close()

    def passrandomizer_getsettings(self, gui_name):
        self.check_to_create_conf_file()
        pass_mode1 = ""
        pass_mode2 = ""
        pass_mode3 = ""
        pass_mode4 = ""
        pass_max_char = ""
        pass_min_char = ""
        isReadingPassSettings = False
        with open("Conf/AS_Pass_Settings.ini", 'r') as pass_settings_file:
            lines = pass_settings_file.readlines()
            lines = list(map(str.strip, lines))
            for line in lines:
                line.strip()
                if line == "/Random Password Properties/":
                    isReadingPassSettings = True
                elif line.startswith("Pass_Create_Mode_1: "):
                    if line.split(": ")[-1] == "1":
                        pass_mode1 = "1"
                    elif line.split(": ")[-1] == "0":
                        pass_mode1 = "0"
                elif line.startswith("Pass_Create_Mode_2: "):
                    if line.split(": ")[-1] == "1":
                        pass_mode2 = "1"
                    elif line.split(": ")[-1] == "0":
                        pass_mode2 = "0"
                elif line.startswith("Pass_Create_Mode_3: "):
                    if line.split(": ")[-1] == "1":
                        pass_mode3 = "1"
                    elif line.split(": ")[-1] == "0":
                        pass_mode3 = "0"
                elif line.startswith("Pass_Create_Mode_4: "):
                    if line.split(": ")[-1] == "1":
                        pass_mode4 = "1"
                    elif line.split(": ")[-1] == "0":
                        pass_mode4 = "0"
                elif line.startswith("Min_Char_Count: "):
                    if not line.split(": ")[-1] == "":
                        pass_min_char = str(line.split(": ")[-1])
                    else:
                        pass_min_char = 10
                elif line.startswith("Max_Char_Count: "):
                    if not line.split(": ")[-1] == "":
                        pass_max_char = str(line.split(": ")[-1])
                    else:
                        pass_max_char = 15
                elif line == ("/EndOfSetting/") and isReadingPassSettings == True:
                    isReadingPassSettings = False
                    generated_password = create_list(pass_mode1, pass_mode2, pass_mode3, pass_mode4,
                                                     pass_min_char, pass_max_char)
                    if gui_name == "add_new":
                        self.add_acc_ui.userpassword_lineedit.setText(generated_password)
                    elif gui_name == "edit_existing":
                        self.edit_acc_ui.userpassword_lineedit.setText(generated_password)
        pass_settings_file.close()
    #This also opens the Settings interface of Pass randomizer
    def passrandomizer_getsettingsforUI(self):
        self.check_to_create_conf_file()
        self.passSetWindow = QtWidgets.QMainWindow()
        self.pass_set_ui = Ui_PasswordGeneratorSettings()
        self.pass_set_ui.setupUi(self.passSetWindow)
        self.pass_set_ui.minchar_lineedit.textChanged.connect(self.lineedit_txt_changed_min)
        self.pass_set_ui.maxchar_lineedit.textChanged.connect(self.lineedit_txt_changed_max)
        onlyint = QIntValidator()
        onlyint.setRange(0, 30)
        self.pass_set_ui.minchar_lineedit.setValidator(onlyint)
        self.pass_set_ui.maxchar_lineedit.setValidator(onlyint)
        self.pass_set_ui.saved_label.hide()

        self.passSetWindow.show()
        self.pass_set_ui.save_passsett_btn.clicked.connect(self.save_new_settings_for_pass_rnd)

    #Lineedits text changed
    def lineedit_txt_changed_min(self):
        try:
            if self.pass_set_ui.minchar_lineedit.text() == "":
                pass
            elif int(self.pass_set_ui.minchar_lineedit.text()) > 30:
                self.pass_set_ui.minchar_lineedit.setText("30")
            else:
                pass
        except():
            pass

    def lineedit_txt_changed_max(self):
        try:
            if self.pass_set_ui.maxchar_lineedit.text() == "":
                pass
            elif int(self.pass_set_ui.maxchar_lineedit.text()) > 30:
                self.pass_set_ui.maxchar_lineedit.setText("30")
            else:
                pass
        except():
            pass


    #Saving New Settings For Password Randomizer
    def save_new_settings_for_pass_rnd(self):
        pass_mode1 = self.pass_set_ui.passmode1_checkbox.isChecked()
        pass_mode2 = self.pass_set_ui.passmode2_checkbox.isChecked()
        pass_mode3 = self.pass_set_ui.passmode3_checkbox.isChecked()
        pass_mode4 = self.pass_set_ui.passmode4_checkbox.isChecked()
        pass_max_char = self.pass_set_ui.maxchar_lineedit.text()
        pass_min_char = self.pass_set_ui.minchar_lineedit.text()
        settings_begin = "/Random Password Properties/\n"
        settings_end = "/EndOfSetting/"
        if not (pass_mode1 or pass_mode2 or pass_mode3 or pass_mode4):
            pass_mode1 = True
            self.pass_set_ui.passmode1_checkbox.setChecked(True)
            pass_mode2 = True
            self.pass_set_ui.passmode2_checkbox.setChecked(True)
            pass_mode3 = True
            self.pass_set_ui.passmode3_checkbox.setChecked(True)
            pass_mode4 = True
            self.pass_set_ui.passmode4_checkbox.setChecked(True)
        if pass_max_char == "":
            pass_max_char = "25"
            self.pass_set_ui.maxchar_lineedit.setText(pass_max_char)
        if pass_min_char == "":
            pass_min_char = "20"
            self.pass_set_ui.minchar_lineedit.setText(pass_min_char)
        if int(pass_max_char) < int(pass_min_char):
            pass_temp = pass_max_char
            pass_max_char = pass_min_char
            pass_min_char = pass_temp
            self.pass_set_ui.minchar_lineedit.setText(pass_min_char)
            self.pass_set_ui.maxchar_lineedit.setText(pass_max_char)
        with open("Conf/AS_Pass_Settings.ini", 'w') as pass_settings_file:
            pass_settings_file.write(settings_begin)
            if pass_mode1 == True:
                pass_settings_file.write("Pass_Create_Mode_1: 1\n")
            elif pass_mode1 == False:
                pass_settings_file.write("Pass_Create_Mode_1: 0\n")
            if pass_mode2 == True:
                pass_settings_file.write("Pass_Create_Mode_2: 1\n")
            elif pass_mode2 == False:
                pass_settings_file.write("Pass_Create_Mode_2: 0\n")
            if pass_mode3 == True:
                pass_settings_file.write("Pass_Create_Mode_3: 1\n")
            elif pass_mode3 == False:
                pass_settings_file.write("Pass_Create_Mode_3: 0\n")
            if pass_mode4 == True:
                pass_settings_file.write("Pass_Create_Mode_4: 1\n")
            elif pass_mode4 == False:
                pass_settings_file.write("Pass_Create_Mode_4: 0\n")
            pass_settings_file.write(f"Min_Char_Count: {pass_min_char}\n")
            pass_settings_file.write(f"Max_Char_Count: {pass_max_char}\n")
            pass_settings_file.write(settings_end)
        pass_settings_file.close()
        self.pass_set_ui.save_passsett_btn.setDisabled(True)
        self.pass_set_ui.saved_label.show()


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
            conn4 = sqlite3.connect(self.database_location)
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
        self.edit_acc_ui.clearall_button.clicked.connect(self.clearall_Editing)
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
        self.edit_acc_ui.randompasssett_btn.clicked.connect(self.passrandomizer_getsettingsforUI)
        self.edit_acc_ui.randomizepass_btn.clicked.connect(partial(self.passrandomizer_getsettings, "edit_existing"))
    #End Of Opening Edit Window

    #Clear Operations For Editing Window
    def clearall_Editing(self):
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
        conn5 = sqlite3.connect(self.database_location)
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
            #Mail Address And Not Specified Control

            if (not len(edited_datas[2].split("@")) == 2) and (not edited_datas[2] == "Not Specified#(Code: 01)"):
                self.edit_acc_ui.usermail_lineedit.setText("Please provide a valid email address.")
                if (not len(edited_datas[7].split("@")) == 2) and (not edited_datas[7] == "Not Specified#(Code: 01)"):
                    self.edit_acc_ui.recoverymail_lineedit.setText("Please provide a valid email address.")
                conn5.commit()
                conn5.close()
            elif (not len(edited_datas[7].split("@")) == 2) and (not edited_datas[7] == "Not Specified#(Code: 01)"):
                self.edit_acc_ui.recoverymail_lineedit.setText("Please provide a valid email address.")
                conn5.commit()
                conn5.close()
            elif self.isAllNotSpecified(given_entries_list=edited_datas):
                self.cant_everythink_not_specified()
                conn5.commit()
                conn5.close()
            #End Of The Mail Address And Not Specified Control
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
            conn6 = sqlite3.connect(self.database_location)
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
        conn = sqlite3.connect(self.database_location)
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
    #Crypto-Operation for database
    def safe_exit(self):
        if os.path.exists(self.database_location):
            encrypter_method(self.database_location, self.database_name, self.account_db_key)
            self.saved_noti_safe_exit()
            self.close()
        else:
            self.couldnt_saved_noti_safe_exit()

def start_app():
    app = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec_())


start_app()

