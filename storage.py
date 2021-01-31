#! /usr/bin/python3
from pysqlcipher3 import dbapi2 as sqlite3
import pysqlcipher3
import json
from funcs.myui import Ui_MyWindow
from PyQt5 import QtWidgets, QtCore, QtWidgets
import sys
from funcs.functions import hide_text_from_changes, btns_edit_click, btns_save_click, btns_get_text_click

class MainWindow(QtWidgets.QWidget):

    switch_on_soylewindow = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Авторизация')
        self.setMinimumSize(QtCore.QSize(241, 90))
        self.setMaximumSize(QtCore.QSize(241, 90))
        self.resize(280, 100)
        layout = QtWidgets.QGridLayout()

        self.line_edit_login = QtWidgets.QLineEdit()
        self.line_edit_login.setGeometry(QtCore.QRect(30, 20, 221, 20))
        layout.addWidget(self.line_edit_login)

        self.button_enter = QtWidgets.QPushButton('Войти в программу')
        self.button_enter.setGeometry(QtCore.QRect(30, 50, 221, 23))
        self.button_enter.clicked.connect(self.switch)
        layout.addWidget(self.button_enter)

        self.statusBar = QtWidgets.QStatusBar()
        self.statusBar.setGeometry(QtCore.QRect(30, 80, 221, 26))
        layout.addWidget(self.statusBar)

        self.setLayout(layout)
    
    def open_key_DB(self, secury_key):        
        self.conn = sqlite3.connect('db.sqlite')
        self.cur = self.conn.cursor()
        self.cur.execute(f"PRAGMA key={secury_key}")

    def switch(self):
        global secury_key        
        secury_key = self.line_edit_login.text()
        if secury_key == '' or len(secury_key) > 10:            
            return self.statusBar.showMessage('ERR: EMPTY STRING') 
        try:
            self.open_key_DB(secury_key)
        except pysqlcipher3.dbapi2.OperationalError:
            return self.statusBar.showMessage('ERR: NOT VALID')
        try:            
            self.open_key_DB(secury_key)
            self.cur.execute("SELECT * FROM db;")
            self.cur.close()
        except pysqlcipher3.dbapi2.OperationalError: # table is not create, create table            
            newtable = SoyleWindow()
            newtable.create_table_new()
        except pysqlcipher3.dbapi2.DatabaseError: # key is not valid            
            return self.statusBar.showMessage('ERR: KEY NOT FOUND')
        return self.switch_on_soylewindow.emit(self.line_edit_login.text())

class Controller():
    def __init__(self):
        pass

    def show_main_window(self):
        self.window = MainWindow()
        self.window.switch_on_soylewindow.connect(self.show_soylewindow)
        self.window.show()

    def show_soylewindow(self, text):
        self.window_two = SoyleWindow()
        self.window.close()
        self.window_two.show()

class SoyleWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(SoyleWindow, self).__init__()
        self.ui = Ui_MyWindow()
        self.ui.setupUi(self)
        #global key
        self.open_key_DB(secury_key) # decrypt the table using the key
        # Create table first, second comment this strings in the future, 
        # do not download data from json, but through the GUI form.
        
        self.ui.pushButton_Update_All_Table.clicked.connect(self.create_table_new)
        self.ui.listWidget.setCurrentRow(0)
        self.ui.listWidget.addItems(self.get_items_names())
        hide_text_from_changes(self)
        self.ui.listWidget.currentRowChanged.connect(self.change_list_items)      

        btns_get_text_click(self)
        btns_edit_click(self) # edit from base
        btns_save_click(self) # save in base

        self.cur.close()
    
    def open_key_DB(self, secury_key):        
        self.conn = sqlite3.connect('db.sqlite')
        self.cur = self.conn.cursor()
        self.cur.execute(f"PRAGMA key={secury_key}")

    def copy_from_text(self):
        sender_get_copy = self.sender()  # who send signal
        if sender_get_copy.objectName() == 'pushButton_Name_Get':
            self.ui.textEdit_Name.selectAll()
            self.ui.textEdit_Name.copy()
        elif sender_get_copy.objectName() == 'pushButton_Login_Get':
            self.ui.textEdit_Login.selectAll()
            self.ui.textEdit_Login.copy()
        elif sender_get_copy.objectName() == 'pushButton_Password_Get':
            self.ui.textEdit_Password.selectAll()
            self.ui.textEdit_Password.copy()
        elif sender_get_copy.objectName() == 'pushButton_OldPassword_Get':
            self.ui.textEdit_OldPassword.selectAll()
            self.ui.textEdit_OldPassword.copy()
        elif sender_get_copy.objectName() == 'pushButton_Email_Get':
            self.ui.textEdit_Email.selectAll()
            self.ui.textEdit_Email.copy()
        elif sender_get_copy.objectName() == 'pushButton_OldEmail_Get':
            self.ui.textEdit_OldEmail.selectAll()
            self.ui.textEdit_OldEmail.copy()
        elif sender_get_copy.objectName() == 'pushButton_Quation_Get':
            self.ui.textEdit_Quation.selectAll()
            self.ui.textEdit_Quation.copy()
        elif sender_get_copy.objectName() == 'pushButton_Answer_Get':
            self.ui.textEdit_Answer.selectAll()
            self.ui.textEdit_Answer.copy()
        elif sender_get_copy.objectName() == 'pushButton_Code_Get':
            self.ui.textEdit_Code.selectAll()
            self.ui.textEdit_Code.copy()
        elif sender_get_copy.objectName() == 'pushButton_Phone_Get':
            self.ui.textEdit_Phone.selectAll()
            self.ui.textEdit_Phone.copy()
        elif sender_get_copy.objectName() == 'pushButton_Recoverycode_Get':
            self.ui.textEdit_Recoverycode.selectAll()
            self.ui.textEdit_Recoverycode.copy()
        elif sender_get_copy.objectName() == 'pushButton_FIO_Get':
            self.ui.textEdit_FIO.selectAll()
            self.ui.textEdit_FIO.copy()
        elif sender_get_copy.objectName() == 'pushButton_Country_Get':
            self.ui.textEdit_Country.selectAll()
            self.ui.textEdit_Country.copy()
        elif sender_get_copy.objectName() == 'pushButton_State_Get':
            self.ui.textEdit_State.selectAll()
            self.ui.textEdit_State.copy()
        elif sender_get_copy.objectName() == 'pushButton_City_Get':
            self.ui.textEdit_City.selectAll()
            self.ui.textEdit_City.copy()
        elif sender_get_copy.objectName() == 'pushButton_Addres_Get':
            self.ui.textEdit_Addres.selectAll()
            self.ui.textEdit_Addres.copy()
        elif sender_get_copy.objectName() == 'pushButton_ZipCode_Get':
            self.ui.textEdit_ZipCode.selectAll()
            self.ui.textEdit_ZipCode.copy()

    # decrypt the table using the key
    def open_key_DB(self, secury_key):        
        self.conn = sqlite3.connect('db.sqlite')
        self.cur = self.conn.cursor()
        self.cur.execute(f"PRAGMA key={secury_key}")

    # get name who send signal on press btn
    def who_btn_clicked(self):
        sender = self.sender()  # who send signal
        if sender.objectName() == 'pushButton_Name_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Name.setDisabled(False)
        elif sender.objectName() == 'pushButton_Login_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Login.setDisabled(False)
        elif sender.objectName() == 'pushButton_Password_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Password.setDisabled(False)
        elif sender.objectName() == 'pushButton_OldPassword_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_OldPassword.setDisabled(False)
        elif sender.objectName() == 'pushButton_Email_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Email.setDisabled(False)
        elif sender.objectName() == 'pushButton_OldEmail_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_OldEmail.setDisabled(False)
        elif sender.objectName() == 'pushButton_Quation_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Quation.setDisabled(False)
        elif sender.objectName() == 'pushButton_Answer_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Answer.setDisabled(False)
        elif sender.objectName() == 'pushButton_Code_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Code.setDisabled(False)
        elif sender.objectName() == 'pushButton_Phone_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Phone.setDisabled(False)
        elif sender.objectName() == 'pushButton_Recoverycode_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Recoverycode.setDisabled(False)
        elif sender.objectName() == 'pushButton_FIO_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_FIO.setDisabled(False)
        elif sender.objectName() == 'pushButton_Country_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Country.setDisabled(False)
        elif sender.objectName() == 'pushButton_State_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_State.setDisabled(False)
        elif sender.objectName() == 'pushButton_City_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_City.setDisabled(False)
        elif sender.objectName() == 'pushButton_Addres_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Addres.setDisabled(False)
        elif sender.objectName() == 'pushButton_ZipCode_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_ZipCode.setDisabled(False)

    def update_table(self):
        hide_text_from_changes(self)
        rows = self.ui.listWidget.currentRow()
        texts = self.view_table_by_IDs(str(rows))
        new_names_text = tuple()
        new_names_text += (rows,)
        new_names_text += (self.ui.textEdit_Name.toPlainText(),)
        new_names_text += (self.ui.textEdit_Login.toPlainText(),)
        new_names_text += (self.ui.textEdit_Password.toPlainText(),)
        new_names_text += (self.ui.textEdit_OldPassword.toPlainText(),)
        new_names_text += (self.ui.textEdit_Email.toPlainText(),)
        new_names_text += (self.ui.textEdit_OldEmail.toPlainText(),)
        new_names_text += (self.ui.textEdit_Quation.toPlainText(),)
        new_names_text += (self.ui.textEdit_Answer.toPlainText(),)
        new_names_text += (self.ui.textEdit_Code.toPlainText(),)
        new_names_text += (self.ui.textEdit_Phone.toPlainText(),)
        new_names_text += (self.ui.textEdit_Recoverycode.toPlainText(),)
        new_names_text += (self.ui.textEdit_FIO.toPlainText(),)
        new_names_text += (self.ui.textEdit_Country.toPlainText(),)
        new_names_text += (self.ui.textEdit_State.toPlainText(),)
        new_names_text += (self.ui.textEdit_City.toPlainText(),)
        new_names_text += (self.ui.textEdit_Addres.toPlainText(),)
        new_names_text += (self.ui.textEdit_ZipCode.toPlainText(),)
        if [new_names_text] == texts:
            self.statusBar().showMessage('Изменения не внесены')
        else:
            self.update_to_table(new_names_text)
            sender = self.sender()
            self.statusBar().showMessage('Изменения внесены ' +
                                         str(sender.objectName().split('_')[1]))

    def update_to_table(self, new_names_text):
        self.cur = self.conn.cursor()
        rows = self.ui.listWidget.currentRow()
        update = f'''UPDATE db SET
        id = '{new_names_text[0]}', 
        Name = '{new_names_text[1]}',
        Login = '{new_names_text[2]}',
        Password = '{new_names_text[3]}',
        OldPassword = '{new_names_text[4]}',
        Email = '{new_names_text[5]}',
        OldEmail = '{new_names_text[6]}',
        Quation = '{new_names_text[7]}',
        Answer = "{new_names_text[8]}",
        Code = '{new_names_text[9]}',
        Phone = '{new_names_text[10]}',
        Recoverycode = '{new_names_text[11]}',
        FIO = '{new_names_text[12]}',
        Country = '{new_names_text[13]}',
        State = '{new_names_text[14]}',
        City = '{new_names_text[15]}',
        Addres = '{new_names_text[16]}',
        ZipCode = '{new_names_text[17]}'  
        WHERE 
        ID == {rows};'''
        self.cur.execute(update)
        self.conn.commit()

    # Get items name
    def get_items_names(self):
        try:
            self.cur.execute("SELECT Name, Login FROM db;")
        except pysqlcipher3.dbapi2.OperationalError:
            list_names = ['empty']
            return list_names
        get_name = self.cur.fetchmany(0)
        list_names = []
        for _ in range(len(get_name)):
            list_names.append(get_name[_][0] + " (" + get_name[_][1] + ")")
        return list_names

    def change_list_items(self):
        hide_text_from_changes(self)
        rows = self.ui.listWidget.currentRow()
        texts = self.view_table_by_IDs(str(rows))
        try:
            self.ui.textEdit_Name.setPlainText(texts[0][1])
        except TypeError:
            return
        self.ui.textEdit_Name.setPlainText(texts[0][1])
        self.ui.textEdit_Login.setPlainText(texts[0][2])
        self.ui.textEdit_Password.setPlainText(texts[0][3])
        self.ui.textEdit_OldPassword.setPlainText(texts[0][4])
        self.ui.textEdit_Email.setPlainText(texts[0][5])
        self.ui.textEdit_OldEmail.setPlainText(texts[0][6])
        self.ui.textEdit_Quation.setPlainText(texts[0][7])
        self.ui.textEdit_Answer.setPlainText(texts[0][8])
        self.ui.textEdit_Code.setPlainText(texts[0][9])
        self.ui.textEdit_Phone.setPlainText(texts[0][10])
        self.ui.textEdit_Recoverycode.setPlainText(texts[0][11])
        self.ui.textEdit_FIO.setPlainText(texts[0][12])
        self.ui.textEdit_Country.setPlainText(texts[0][13])
        self.ui.textEdit_State.setPlainText(texts[0][14])
        self.ui.textEdit_City.setPlainText(texts[0][15])
        self.ui.textEdit_Addres.setPlainText(texts[0][16])
        self.ui.textEdit_ZipCode.setPlainText(texts[0][17])

    def view_table_by_IDs(self, name):
        self.cur = self.conn.cursor()
        try:
            self.cur.execute("SELECT * FROM db WHERE ID = '{0}';".format(name))
        except pysqlcipher3.dbapi2.OperationalError:
            return
        return self.cur.fetchmany(0)

    def open_json_file(self, fname):
        self.fname = fname

        try:
            file = open(fname, 'r')
        except FileNotFoundError:
            return self.statusBar().showMessage('ERR: db.json not found')

        with open(self.fname, 'r', encoding='utf-8') as read_json_file:
            data_json = json.load(read_json_file)
            read_json_file.close()
        return data_json

    def create_table_new(self):
        global secury_key
        fname = 'db.json'
        
        try:
            file = open(fname, 'r')
        except FileNotFoundError:
            return self.statusBar().showMessage('ERR: db.json not found')

        self.open_key_DB(secury_key)
        self.cur.execute('DROP TABLE IF EXISTS db')        
        self.cur.execute(
            '''CREATE TABLE db (
            id INT AUTO_INCREMENT NOT NULL, Name VARCHAR(100), Login VARCHAR(100), Password VARCHAR(100), OldPassword VARCHAR(100), Email VARCHAR(300),
            OldEmail VARCHAR(100), Quation VARCHAR(300), Answer VARCHAR(300), Code VARCHAR(300), Phone VARCHAR(20), Recoverycode VARCHAR(300), 
            FIO VARCHAR(300), Country VARCHAR(100), State VARCHAR(100), City VARCHAR(100), Addres VARCHAR(300), ZipCode VARCHAR(50),
            PRIMARY KEY (id)
            );'''
        )
        self.conn.commit()
        fh = self.open_json_file(fname)
        for key, _ in fh.items():
            Name = fh[key][0]['Name']
            Login = fh[key][0]['Login']
            Password = fh[key][0]['Password']
            OldPassword = fh[key][0]["Old Password"]
            Email = fh[key][0]["Email"]
            OldEmail = fh[key][0]["Old Email"]
            Quation = fh[key][0]["Quation"]
            Answer = fh[key][0]["Answer"]
            Code = fh[key][0]["Code"]
            Phone = fh[key][0]["Phone"]
            Recoverycode = fh[key][0]["Recovery code"]
            FIO = fh[key][0]["FIO"]
            Country = fh[key][0]["Country"]
            State = fh[key][0]["State"]
            City = fh[key][0]["City"]
            Addres = fh[key][0]["Addres"]
            ZipCode = fh[key][0]["Zip Code"]
            self.cur.execute(
                '''INSERT INTO db ( id, Name, Login, Password, OldPassword, Email, OldEmail, Quation, Answer, Code, Phone, Recoverycode, FIO, Country, State, City, Addres, ZipCode ) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? );''',
                (int(key), Name, Login, Password, OldPassword, Email, OldEmail, Quation, Answer, Code, Phone, Recoverycode, FIO, Country, State, City, Addres, ZipCode))
        self.conn.commit()
        self.cur.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_main_window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
