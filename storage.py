#! /usr/bin/python3
from pysqlcipher3 import dbapi2 as sqlite3
import pysqlcipher3
import json
from funcs.myui import Ui_MyWindow
from PyQt5 import QtWidgets, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
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
        self.conn = sqlite3.connect('database.db')
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
            newtable.upload_in_table_from_json()
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

    def show_soylewindow(self):
        self.window_two = SoyleWindow()
        self.window.close()
        self.window_two.show()

class SoyleWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(SoyleWindow, self).__init__()
        self.ui = Ui_MyWindow()
        self.ui.setupUi(self)
        self.open_key_DB(secury_key) # decrypt the table using the key      
        self.ui.pushButton_Update_All_Table.clicked.connect(self.upload_in_table_from_json)
        self.ui.listWidget.addItems(self.get_items_names())
        self.ui.listWidget.setCurrentRow(0)
        self.ui.listWidget.itemDoubleClicked.connect(self.delete_account)
        self.ui.listWidget.selectedItems()
        self.ui.pushButton_ADD_ACCOUNT.clicked.connect(self.create_new_account)
        hide_text_from_changes(self)
        self.ui.listWidget.currentRowChanged.connect(self.change_list_items)
        self.ui.pushButton_DELETE_ACCOUNT.clicked.connect(self.delete_account)
        btns_get_text_click(self)
        btns_edit_click(self) # edit from base
        btns_save_click(self) # save in base
        self.cur.close()

    def delete_account(self):
        global secury_key
        self.open_key_DB(secury_key)

        try:
            delete_row = self.get_items_names()[self.ui.listWidget.currentRow()].split(' ')[0]
            okornot = self.get_items_names()[self.ui.listWidget.currentRow()]
        except IndexError:
            return self.statusBar().showMessage('ERR: Empty DB')

        buttonReply = QMessageBox.question(self, 'Allert!', f'Delete "{okornot}?"', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.cur.execute(f'''
            DELETE FROM db
            WHERE id = {delete_row};
            ''')
            self.conn.commit()

            self.cur.execute(f'''
            SELECT id FROM db WHERE id = {delete_row};
            ''')
            get_info = self.cur.fetchmany(0)
            if get_info == []:
                self.ui.listWidget.clear()
                self.ui.listWidget.addItems(self.get_items_names())
                self.cur.close()
                return self.statusBar().showMessage(f'OK: id {delete_row} удален!')
            return self.statusBar().showMessage(f'OK: "{okornot}?" delete!') 
        else:
            return self.statusBar().showMessage(f'OK: id {delete_row} not delete!')           


    def create_new_account(self):
        global secury_key
        self.open_key_DB(secury_key)   
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS db (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            Name VARCHAR(100), 
            Login VARCHAR(100), 
            Password VARCHAR(100), 
            OldPassword VARCHAR(100), 
            Email VARCHAR(300),
            OldEmail VARCHAR(100), 
            Quation VARCHAR(300), 
            Answer VARCHAR(300), 
            Code VARCHAR(300), 
            Phone VARCHAR(20), 
            Recoverycode VARCHAR(300), 
            Full_name VARCHAR(300), 
            Country VARCHAR(100), 
            State VARCHAR(100), 
            City VARCHAR(100), 
            Address VARCHAR(300), 
            ZipCode VARCHAR(50)
            );'''
        )
        Name = '---'
        Login = '---'
        Password = '---'
        OldPassword = '---'
        Email = '---'
        OldEmail = '---'
        Quation = '---'
        Answer = '---'
        Code = '---'
        Phone = '---'
        Recoverycode = '---'
        Full_name = '---'
        Country = '---'
        State = '---'
        City = '---'
        Address = '---'
        ZipCode = '---'
        self.cur.execute(
            '''INSERT INTO db ( Name, Login, Password, OldPassword, Email, OldEmail, Quation, Answer, Code, Phone, Recoverycode, Full_name, Country, State, City, Address, ZipCode )
            VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? );''',
            (Name, Login, Password, OldPassword, Email, OldEmail, Quation, Answer, Code, Phone, Recoverycode, Full_name, Country, State, City, Address, ZipCode))
        self.conn.commit()
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(self.get_items_names())
        self.cur.close()
    
    def open_key_DB(self, secury_key):        
        self.conn = sqlite3.connect('')
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
        elif sender_get_copy.objectName() == 'pushButton_Full_name_Get':
            self.ui.textEdit_Full_name.selectAll()
            self.ui.textEdit_Full_name.copy()
        elif sender_get_copy.objectName() == 'pushButton_Country_Get':
            self.ui.textEdit_Country.selectAll()
            self.ui.textEdit_Country.copy()
        elif sender_get_copy.objectName() == 'pushButton_State_Get':
            self.ui.textEdit_State.selectAll()
            self.ui.textEdit_State.copy()
        elif sender_get_copy.objectName() == 'pushButton_City_Get':
            self.ui.textEdit_City.selectAll()
            self.ui.textEdit_City.copy()
        elif sender_get_copy.objectName() == 'pushButton_Address_Get':
            self.ui.textEdit_Address.selectAll()
            self.ui.textEdit_Address.copy()
        elif sender_get_copy.objectName() == 'pushButton_ZipCode_Get':
            self.ui.textEdit_ZipCode.selectAll()
            self.ui.textEdit_ZipCode.copy()

    # decrypt the table using the key
    def open_key_DB(self, secury_key):        
        self.conn = sqlite3.connect('database.db')
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
        elif sender.objectName() == 'pushButton_Full_name_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Full_name.setDisabled(False)
        elif sender.objectName() == 'pushButton_Country_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Country.setDisabled(False)
        elif sender.objectName() == 'pushButton_State_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_State.setDisabled(False)
        elif sender.objectName() == 'pushButton_City_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_City.setDisabled(False)
        elif sender.objectName() == 'pushButton_Address_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_Address.setDisabled(False)
        elif sender.objectName() == 'pushButton_ZipCode_Edit':
            hide_text_from_changes(self)
            self.ui.textEdit_ZipCode.setDisabled(False)

    def get_text_to_save_table(self):
        hide_text_from_changes(self)
        rows = self.ui.listWidget.currentRow() + 1
        texts = self.view_table_by_IDs(str(rows + self.ui.listWidget.count() + 1))
        update_text_to_table = tuple()
        update_text_to_table += (self.ui.textEdit_Name.toPlainText(),)
        update_text_to_table += (self.ui.textEdit_Login.toPlainText(),)
        update_text_to_table += (self.ui.textEdit_Password.toPlainText(),)
        update_text_to_table += (self.ui.textEdit_OldPassword.toPlainText(),)
        update_text_to_table += (self.ui.textEdit_Email.toPlainText(),)
        update_text_to_table += (self.ui.textEdit_OldEmail.toPlainText(),)
        update_text_to_table += (self.ui.textEdit_Quation.toPlainText(),)
        update_text_to_table += (self.ui.textEdit_Answer.toPlainText(),)
        update_text_to_table += (self.ui.textEdit_Code.toPlainText(),)
        update_text_to_table += (self.ui.textEdit_Phone.toPlainText(),)
        update_text_to_table += (self.ui.textEdit_Recoverycode.toPlainText(),)
        update_text_to_table += (self.ui.textEdit_Full_name.toPlainText(),)
        update_text_to_table += (self.ui.textEdit_Country.toPlainText(),)
        update_text_to_table += (self.ui.textEdit_State.toPlainText(),)
        update_text_to_table += (self.ui.textEdit_City.toPlainText(),)
        update_text_to_table += (self.ui.textEdit_Address.toPlainText(),)
        update_text_to_table += (self.ui.textEdit_ZipCode.toPlainText(),)
        
        if [(rows, ) + update_text_to_table] == texts:
            self.statusBar().showMessage('No changes have been made. No changes.')
        else:                      
            self.update_to_table(update_text_to_table)
            return self.statusBar().showMessage('Saved to the database')

    def update_to_table(self, update_text_to_table):
        self.cur = self.conn.cursor()
        rows = self.ui.listWidget.currentRow() + 1
        update = f'''UPDATE db SET         
        Name = '{update_text_to_table[0]}',
        Login = '{update_text_to_table[1]}',
        Password = '{update_text_to_table[2]}',
        OldPassword = '{update_text_to_table[3]}',
        Email = '{update_text_to_table[4]}',
        OldEmail = '{update_text_to_table[5]}',
        Quation = '{update_text_to_table[6]}',
        Answer = "{update_text_to_table[7]}",
        Code = '{update_text_to_table[8]}',
        Phone = '{update_text_to_table[9]}',
        Recoverycode = '{update_text_to_table[10]}',
        Full_name = '{update_text_to_table[11]}',
        Country = '{update_text_to_table[12]}',
        State = '{update_text_to_table[13]}',
        City = '{update_text_to_table[14]}',
        Address = '{update_text_to_table[15]}',
        ZipCode = '{update_text_to_table[16]}'  
        WHERE 
        ID = "{rows}"'''
        self.cur.execute(update)
        self.conn.commit()
        self.ui.listWidget.clear()            
        self.ui.listWidget.addItems(self.get_items_names())

    # Get items name
    def get_items_names(self):
        try:
            self.cur.execute("SELECT id, Name, Login FROM db;")
        except pysqlcipher3.dbapi2.OperationalError:
            list_names = []
            return list_names
        get_name = self.cur.fetchmany(0)
        list_names = []
        for _ in range(len(get_name)):
            list_names.append(str(get_name[_][0]) + " " + get_name[_][1] + " " + get_name[_][2])
        return list_names

    def change_list_items(self):        
        hide_text_from_changes(self)
        rows = self.ui.listWidget.currentRow() + 1
        texts = self.view_table_by_IDs(str(rows))
        try:
            self.ui.textEdit_Name.setPlainText(texts[0][1])
        except TypeError:
            return self.statusBar().showMessage('TypeError')
        except IndexError:
            #self.ui.listWidget.setCurrentRow(rows + self.ui.listWidget.count() + 1)
            #texts = self.view_table_by_IDs(str(rows + self.ui.listWidget.count() + 1))
            return self.statusBar().showMessage('IndexError')
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
        self.ui.textEdit_Full_name.setPlainText(texts[0][12])
        self.ui.textEdit_Country.setPlainText(texts[0][13])
        self.ui.textEdit_State.setPlainText(texts[0][14])
        self.ui.textEdit_City.setPlainText(texts[0][15])
        self.ui.textEdit_Address.setPlainText(texts[0][16])
        self.ui.textEdit_ZipCode.setPlainText(texts[0][17])
        return

    def view_table_by_IDs(self, name):
        self.cur = self.conn.cursor()
        try:
            self.cur.execute(f"SELECT * FROM db WHERE ID = {name}")
        except pysqlcipher3.dbapi2.OperationalError:
            return
        texts = self.cur.fetchmany(0)
        return texts

    def open_json_file(self, fname):
        self.fname = fname

        try:
            open(fname, 'r')
        except FileNotFoundError:
            return self.statusBar().showMessage('ERR: db.json not found')

        with open(self.fname, 'r', encoding='utf-8') as read_json_file:
            data_json = json.load(read_json_file)
            read_json_file.close()
        return data_json

    def upload_in_table_from_json(self):
        global secury_key
        fname = 'db.json'
        try:
            open(fname, 'r')
        except FileNotFoundError:
            return self.statusBar().showMessage('ERR: db.json not found')

        self.open_key_DB(secury_key)

        self.cur.execute('DROP TABLE IF EXISTS db')
        self.statusBar().showMessage('Database updated from db.json')

        self.cur.execute(
            '''CREATE TABLE db (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            Name VARCHAR(100), 
            Login VARCHAR(100), 
            Password VARCHAR(100), 
            OldPassword VARCHAR(100), 
            Email VARCHAR(300),
            OldEmail VARCHAR(100), 
            Quation VARCHAR(300), 
            Answer VARCHAR(300), 
            Code VARCHAR(300), 
            Phone VARCHAR(20), 
            Recoverycode VARCHAR(300), 
            Full_name VARCHAR(300), 
            Country VARCHAR(100), 
            State VARCHAR(100), 
            City VARCHAR(100), 
            Address VARCHAR(300), 
            ZipCode VARCHAR(50)
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
            Full_name = fh[key][0]["Full_name"]
            Country = fh[key][0]["Country"]
            State = fh[key][0]["State"]
            City = fh[key][0]["City"]
            Address = fh[key][0]["Address"]
            ZipCode = fh[key][0]["Zip Code"]
            self.cur.execute(
                '''INSERT INTO db ( Name, Login, Password, OldPassword, Email, OldEmail, Quation, Answer, Code, Phone, Recoverycode, Full_name, Country, State, City, Address, ZipCode ) 
                VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? );''',
                (Name, Login, Password, OldPassword, Email, OldEmail, Quation, Answer, Code, Phone, Recoverycode, Full_name, Country, State, City, Address, ZipCode))
        self.conn.commit()
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(self.get_items_names())
        self.cur.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_main_window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
