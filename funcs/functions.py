def hide_text_from_changes(self):
    self.ui.textEdit_Name.setDisabled(True)
    self.ui.textEdit_Login.setDisabled(True)
    self.ui.textEdit_Password.setDisabled(True)
    self.ui.textEdit_OldPassword.setDisabled(True)
    self.ui.textEdit_Email.setDisabled(True)
    self.ui.textEdit_OldEmail.setDisabled(True)
    self.ui.textEdit_Quation.setDisabled(True)
    self.ui.textEdit_Answer.setDisabled(True)
    self.ui.textEdit_Code.setDisabled(True)
    self.ui.textEdit_Phone.setDisabled(True)
    self.ui.textEdit_Recoverycode.setDisabled(True)
    self.ui.textEdit_Full_name.setDisabled(True)
    self.ui.textEdit_Country.setDisabled(True)
    self.ui.textEdit_State.setDisabled(True)
    self.ui.textEdit_City.setDisabled(True)
    self.ui.textEdit_Address.setDisabled(True)
    self.ui.textEdit_ZipCode.setDisabled(True)


def btns_edit_click(self):
    self.ui.pushButton_Name_Edit.clicked.connect(self.who_btn_clicked)
    self.ui.pushButton_Login_Edit.clicked.connect(self.who_btn_clicked)
    self.ui.pushButton_Password_Edit.clicked.connect(self.who_btn_clicked)
    self.ui.pushButton_OldPassword_Edit.clicked.connect(self.who_btn_clicked)
    self.ui.pushButton_Email_Edit.clicked.connect(self.who_btn_clicked)
    self.ui.pushButton_OldEmail_Edit.clicked.connect(self.who_btn_clicked)
    self.ui.pushButton_Quation_Edit.clicked.connect(self.who_btn_clicked)
    self.ui.pushButton_Answer_Edit.clicked.connect(self.who_btn_clicked)
    self.ui.pushButton_Code_Edit.clicked.connect(self.who_btn_clicked)
    self.ui.pushButton_Phone_Edit.clicked.connect(self.who_btn_clicked)
    self.ui.pushButton_Recoverycode_Edit.clicked.connect(self.who_btn_clicked)
    self.ui.pushButton_Full_name_Edit.clicked.connect(self.who_btn_clicked)
    self.ui.pushButton_Country_Edit.clicked.connect(self.who_btn_clicked)
    self.ui.pushButton_State_Edit.clicked.connect(self.who_btn_clicked)
    self.ui.pushButton_City_Edit.clicked.connect(self.who_btn_clicked)
    self.ui.pushButton_Address_Edit.clicked.connect(self.who_btn_clicked)
    self.ui.pushButton_ZipCode_Edit.clicked.connect(self.who_btn_clicked)


def btns_save_click(self):
    self.ui.pushButton_Name_Save.clicked.connect(
        self.get_text_to_save_table)
    self.ui.pushButton_Login_Save.clicked.connect(
        self.get_text_to_save_table)
    self.ui.pushButton_Password_Save.clicked.connect(
        self.get_text_to_save_table)
    self.ui.pushButton_OldPassword_Save.clicked.connect(
        self.get_text_to_save_table)
    self.ui.pushButton_Email_Save.clicked.connect(
        self.get_text_to_save_table)
    self.ui.pushButton_OldEmail_Save.clicked.connect(
        self.get_text_to_save_table)
    self.ui.pushButton_Quation_Save.clicked.connect(
        self.get_text_to_save_table)
    self.ui.pushButton_Answer_Save.clicked.connect(
        self.get_text_to_save_table)
    self.ui.pushButton_Code_Save.clicked.connect(
        self.get_text_to_save_table)
    self.ui.pushButton_Phone_Save.clicked.connect(
        self.get_text_to_save_table)
    self.ui.pushButton_Recoverycode_Save.clicked.connect(
        self.get_text_to_save_table)
    self.ui.pushButton_Full_name_Save.clicked.connect(
        self.get_text_to_save_table)
    self.ui.pushButton_Country_Save.clicked.connect(
        self.get_text_to_save_table)
    self.ui.pushButton_State_Save.clicked.connect(
        self.get_text_to_save_table)
    self.ui.pushButton_City_Save.clicked.connect(
        self.get_text_to_save_table)
    self.ui.pushButton_Address_Save.clicked.connect(
        self.get_text_to_save_table)
    self.ui.pushButton_ZipCode_Save.clicked.connect(
        self.get_text_to_save_table)


def btns_get_text_click(self):
    self.ui.pushButton_Name_Get.clicked.connect(self.copy_from_text)
    self.ui.pushButton_Login_Get.clicked.connect(self.copy_from_text)
    self.ui.pushButton_Password_Get.clicked.connect(self.copy_from_text)
    self.ui.pushButton_OldPassword_Get.clicked.connect(self.copy_from_text)
    self.ui.pushButton_Email_Get.clicked.connect(self.copy_from_text)
    self.ui.pushButton_OldEmail_Get.clicked.connect(self.copy_from_text)
    self.ui.pushButton_Quation_Get.clicked.connect(self.copy_from_text)
    self.ui.pushButton_Answer_Get.clicked.connect(self.copy_from_text)
    self.ui.pushButton_Code_Get.clicked.connect(self.copy_from_text)
    self.ui.pushButton_Phone_Get.clicked.connect(self.copy_from_text)
    self.ui.pushButton_Recoverycode_Get.clicked.connect(self.copy_from_text)
    self.ui.pushButton_Full_name_Get.clicked.connect(self.copy_from_text)
    self.ui.pushButton_Country_Get.clicked.connect(self.copy_from_text)
    self.ui.pushButton_State_Get.clicked.connect(self.copy_from_text)
    self.ui.pushButton_City_Get.clicked.connect(self.copy_from_text)
    self.ui.pushButton_Address_Get.clicked.connect(self.copy_from_text)
    self.ui.pushButton_ZipCode_Get.clicked.connect(self.copy_from_text)
